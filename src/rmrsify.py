import pyrmrs.globals;
import pyrmrs.rmrsifier;

import sys;
import time;
import codecs;

import pyrmrs.delphin.pet;
import pyrmrs.delphin.raspsent;
import pyrmrs.delphin.fspp;



class MyRMRSifier( pyrmrs.rmrsifier.RMRSifier ):
  
  petctrl = None;
  raspsentctrl = None;
  fsppctrl = None;
  
  def __init__( self, ifile, ofile, active_tags = [ "t", "h" ] ):
    
    self.petctrl = pyrmrs.delphin.pet.PET( 5, 5 );
    self.raspsentctrl = pyrmrs.delphin.raspsent.RaspSentenceSplitter();
    self.fsppctrl = pyrmrs.delphin.fspp.FSPP();
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
        
        for smaf in self.fsppctrl.sentstr_to_smafs( sent ):
          for rmrs in self.petctrl.smaf_to_rmrss( smaf ):
            
            cnt += 1;
            
            self.out.write( "\n" + self.atindent + "<!--\n" );
            self.out.write( rmrs.str_pretty() );
            self.out.write( "\n" + self.atindent + "-->\n" + self.atindent );
            self.out.write( \
              rmrs.str_xml().replace( "\n", "\n" + self.atindent ) );
            self.out.write( "\n" );
      
      except pyrmrs.delphin.pet.PETError, e:
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
  
  #
  #   35.67179 secs ( 3.65 units of processor time )
  #   44/237 successful (18.57%)
  #   readings per sentence: avg=0.84 min=0 q1=0 med=0 q3=0 max=5
  #
  
  #
  #   185.28623 secs ( 10.47 units of processor time )
  #   126/237 successful (53.16%)
  #   readings per sentence: avg=2.32 min=0 q1=0 med=1 q3=5 max=5
  #

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