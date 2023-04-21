import pyrmrs.globals;
import pyrmrs.rmrsifier;

import cPickle;

import sys;
import time;
import codecs;

import pyrmrs.ext.rasp;
import pyrmrs.ext.raspsent;
import pyrmrs.ext.fspp;
import pyrmrs.ext.pet;

import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.merge_pos_into_smaf;
import pyrmrs.tools.fix_fspp_smaf;



class MyRMRSifier( pyrmrs.rmrsifier.RMRSifier ):
  
  raspctrl = None;
  raspsentctrl = None;
  fsppctrl = None;
  petctrl = None;
  
  outfile = None;
  
  def __init__( self, ifile, ofile, active_tags = [ "t", "h" ] ):
    
    self.raspctrl = pyrmrs.ext.rasp.Rasp();
    self.raspsentctrl = pyrmrs.ext.raspsent.RaspSentenceSplitter();
    self.fsppctrl = pyrmrs.ext.fspp.FSPP();
    self.petctrl = pyrmrs.ext.pet.PET( 5, 5 );
    
    self.outfile = open( "testdta/rtesmafs.pickle", "w" );

    pyrmrs.rmrsifier.RMRSifier.__init__( self, ifile, ofile, active_tags );
    
  def rmrsify( self, surface ):
    
    surface = surface.strip();
    
    pyrmrs.globals.logDebug( self, "|>%s<|" % surface );

    self.out.write( "\n" + self.atindent + "<analysis>" );
    self.out.write( "\n" + self.atindent );
    
    for sent in self.raspsentctrl.txtstr_to_sentstrs( surface ):
      
      pyrmrs.globals.logDebug( self, "|>%s<|" % sent );
        
      self.out.write( "\n" + self.atindent + "<sentence>" );
      self.out.write( "\n" + self.atindent );
      
      err = None;
      cnt = 0;
      
      try:

        fsppsmaf = None;
        for smaf_ in self.fsppctrl.sentstr_to_smafs( sent ):
          fsppsmaf = smaf_;
        if fsppsmaf is None:
          assert False;
        fsppsmaf = pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( fsppsmaf );
        pyrmrs.globals.logDebug( self, "|>%s<|" % fsppsmaf.str_xml() );
        
        raspstr = self.raspctrl.sentstr_to_raspstr( sent );
        pyrmrs.globals.logDebug( self, "|>%s<|" % raspstr );
        raspsmaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( sent, raspstr );
        pyrmrs.globals.logDebug( self, "|>%s<|" % raspsmaf.str_xml() );
        
        cPickle.dump( fsppsmaf, self.outfile, 2 );
        cPickle.dump( raspsmaf, self.outfile, 2 );
        
        smaf = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( fsppsmaf, raspsmaf );
        pyrmrs.globals.logDebug( self, "|>%s<|" % smaf.str_xml() );
        
        # smaf = fsppsmaf;
          
        for rmrs in self.petctrl.smaf_to_rmrss( smaf ):
          
          cnt += 1;
           
          self.out.write( "\n" + self.atindent + "<!--\n" );
          self.out.write( rmrs.str_pretty() );
          self.out.write( "\n" + self.atindent + "-->\n" + self.atindent );
          self.out.write( \
            rmrs.str_xml().replace( "\n", "\n" + self.atindent ) );
          self.out.write( "\n" );
      
      except pyrmrs.ext.pet.PETError, e:
        self.out.write( "<error>\n" );
        self.out.write( self.atindent + self.atindent );
        self.out.write( e.errmsg.replace( "\n", "\n"+self.atindent+self.STDINDENT ) );
        self.out.write( "\n" + self.atindent + "</error>" );
        
        err = e;
        
      self.cnts.append( cnt );
      
      self.total += 1;
      if err == None:
        print "   --> %s" % sent;
        self.succ += 1;
      else:
        print "%2d --> %s" % ( err.errno, sent );
        #if err.errno != 1:
        #  print "       " + err.errmsg;

      self.out.write( "\n" + self.atindent + "</sentence>" );
      
    self.out.write( "\n" + self.atindent + "</analysis>" );
    self.out.write( "\n" );
  
  def __del__( self ):
    
    self.outfile.close();
  


def rmrsify( ifile, ofile ):

  before_time = time.time();
  before_cpu = time.clock();
  rmrsifier = MyRMRSifier( ifile, ofile );
  after_cpu = time.clock();
  after_time = time.time();
  
  print;
  print "%3.5f secs ( %s units of processor time )" % \
    ( after_time - before_time, after_cpu - before_cpu );
  print "%d/%d successful ( %2.2f%% )" % \
    ( rmrsifier.succ, rmrsifier.total, (100.0*float(rmrsifier.succ))/float(rmrsifier.total) );
  
  cnts = rmrsifier.cnts;
  cnts.sort();
  
  sum = 0;
  for cnt in cnts:
    sum += cnt;
  avg = float( sum ) / float( len( cnts ) );
  q0 = cnts[ 0 ];
  q1 = cnts[ int( (len(cnts)-1) * 0.25 ) ];
  q2 = cnts[ int( (len(cnts)-1) * 0.5 ) ];
  q3 = cnts[ int( (len(cnts)-1) * 0.75 ) ];
  q4 = cnts[ len(cnts)-1 ];
  
  print "readings per sentence: avg=%2.2f min=%d q1=%d med=%d q3=%d max=%d" % \
    ( avg, q0, q1, q2, q3, q4 );

def main(argv=None):
  
  if argv == None:
    argv = sys.argv;
  
  pyrmrs.globals.initMain();
  ifile = open( argv[1], "r" );
  ofile = codecs.open( argv[2], "w", encoding="utf-8" );
  rmrsify( ifile, ofile );
  ofile.flush();
  ofile.close();
  ifile.close();
  pyrmrs.globals.destructMain();
  
  return 0;

if __name__ == "__main__":
    sys.exit( main() );

#
# 61.94369 secs ( 12.17 units of processor time )
# 62/248 successful ( 25.00% )
# readings per sentence: avg=1.16 min=0 q1=0 med=0 q3=0 max=5
#
    
#    
# 101.49628 secs ( 30.98 units of processor time )
# 61/248 successful ( 24.60% )
# readings per sentence: avg=1.14 min=0 q1=0 med=0 q3=0 max=5
#

#
# 220.12133 secs ( 42.79 units of processor time )
# 149/248 successful ( 60.08% )
# readings per sentence: avg=2.73 min=0 q1=0 med=4 q3=5 max=5
#
