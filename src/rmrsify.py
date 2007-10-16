import globals;

import sys;
import time;
import string;
import codecs;

import xml.sax;
import xml.sax.handler;

import delphin.pet;
import delphin.raspsent;

import common.reader_element;



STDINDENT = "  ";
CHBREAK = 78;

LINELEN = CHBREAK - len( STDINDENT );

VERBOSE = False;



class RMRSifier( xml.sax.handler.ContentHandler ):

  tags = {};
  parser = None;
  copythrough = True;
  out = None;
  chbuf = [];
  
  preprocsurface = "";
  realsurface = "";
  
  petctrl = None;
  raspsentctrl = None;
  
  active_tags = None;
  atindent = "";
  
  indent = "";
  
  succ = 0;
  total = 0;
  cnts = [];
  
  def __init__( self, ifile, ofile, active_tags = [ 't', 'h', 'proposition' ] ):

    self.succ = 0;
    self.total = 0;
    self.cnts = [];
    
    self.tags = {};
    self.copythrough = True;
    self.out = ofile;
    
    self.chbuf = [];
    
    self.parser = xml.sax.make_parser( \
      [ "xml.sax.xmlreader.IncrementalParser" ] );
    self.parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    self.parser.setContentHandler( self );

    self.preprocsurface = "";
    self.realsurface = "";
    
    self.active_tags = active_tags;
    self.active_tags.append( "pp" );
    
    self.petctrl = delphin.pet.PET( 5, 5 );
    self.raspsentctrl = delphin.raspsent.RaspSentenceSplitter();
    
    reading_indent = True;
    self.indent = "";

    while True:
      data = ifile.read( 1 );
      if data == "":
        break;
      data = data.replace( "\t", STDINDENT );
      if self.copythrough:
        ofile.write( data );
      if reading_indent:
        if data.find( " " ) != -1:
          self.indent += data;
        else:
          reading_indent = False;
      if data == "\n":
        reading_indent = True;
        self.indent = "";
      self.parser.feed( data );

  def startElement( self, name, attrs ):
    
    if not self.tags.has_key( name ):
      self.tags[ name ] = 1;
    else:
      self.tags[ name ] += 1;
      
    if name in self.active_tags:
      self.copythrough = False;
      self.atindent = self.indent;
      self.preprocsurface = None;
      self.surface = None;
      self.chbuf.append( "" );
    
  def characters( self, content ):
    
    if not self.copythrough:
      self.chbuf[ len( self.chbuf )-1 ] += content;

  def decode_str( self, block ):
    
    if block.find( "\\\n" ) != -1:
      st = "";
      if block[ 0 ] == "\n":
        block = block[ 1: ];
      for ch in block:
        if ch == " ":
          st += " ";
        else:
          break;
      block = block.replace( "\\\n"+st, "" );
    return block.strip();
  
  def rmrsify( self, surface ):

    self.out.write( "\n" + self.atindent + "<analysis>" );
    self.out.write( "\n" + self.atindent );
    
    for sent in self.raspsentctrl.sentsplit( surface ):
      
      self.out.write( "\n" + self.atindent + "<sentence>" );
      self.out.write( "\n" + self.atindent );
      
      err = None;
      cnt = 0;
      
      try:
        
        for rmrs in self.petctrl.analyze( sent ):
          
          cnt += 1;

          self.out.write( "\n" + self.atindent + "<!--\n" );
          self.out.write( rmrs.str_pretty() );
          self.out.write( "\n" + self.atindent + "-->\n" + self.atindent );
          self.out.write( \
            string.replace( rmrs.str_xml(), "\n", "\n" + self.atindent ) );
          self.out.write( "\n" );
      
      except delphin.pet.PETError, e:
        self.out.write( "<error>\n" + self.atindent + STDINDENT );
        self.out.write( e.errmsg );
        self.out.write( "\n" + self.atindent + "</error>" );
        
        err = e;
        
      self.cnts.append( cnt );
      
      self.total += 1;
      if err == None:
        print "   --> %s" % sent;
        self.succ += 1;
      else:
        print "%2d --> %s" % ( err.errno, sent );
        if err.errno != 1:
          print "       " + err.errmsg;

      self.out.write( "\n" + self.atindent + "</sentence>" );
      
    self.out.write( "\n" + self.atindent + "</analysis>" );
    self.out.write( "\n" );
    
  def endElement( self, name ):
    
    if name in self.active_tags:
    
      text = self.chbuf.pop();
      text = self.decode_str( text );

      if name == "pp":
        self.preprocsurface = text;
      else:
        self.surface = text;

      if self.preprocsurface == None:
        self.preprocsurface = self.surface;
        
      self.out.write( "\n" + self.atindent );
      self.out.write( "<surface>" );
      self.out.write( "\n" + self.atindent + STDINDENT );
      
      i = 0;
      while True:
        self.out.write( self.surface[ i : i + LINELEN - 1 ] );
        i += LINELEN - 1;
        if i >= len( self.surface ):
          break;
        self.out.write( "\\\n" + self.atindent + STDINDENT );
        
      self.out.write( "\n" + self.atindent + "</surface>" );

      self.preprocsurface = self.preprocsurface.replace( "\\ ", "" );

      self.rmrsify( self.preprocsurface );
      
      self.copythrough = True;
      self.out.write( self.atindent + "</%s>" % name );



globals.init_main();

ifile = open( sys.argv[ 1 ], "r" );
ofile = codecs.open( sys.argv[ 2 ], "w", encoding="utf-8" );

before_time = time.time();
before_cpu = time.clock();
rte3rd = RMRSifier( ifile, ofile );
after_cpu = time.clock();
after_time = time.time();

ofile.flush();
ofile.close();
ifile.close();

print;
print "%3.5f secs ( %s units of processor time )" % \
  ( after_time - before_time, after_cpu - before_cpu );
print "%d/%d successful ( %2.2f%% )" % \
  ( rte3rd.succ, rte3rd.total, (100.0*float(rte3rd.succ))/float(rte3rd.total) );

cnts = rte3rd.cnts;
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

globals.destruct_main();
