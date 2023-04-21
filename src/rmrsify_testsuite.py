import os;
import codecs;
import string;
import sys;

import pyrmrs.globals;
import pyrmrs.rmrsifier;

import pyrmrs.ext.mrsread;



PREFIX="syllogism";

pyrmrs.globals.initMain();

os.chdir( "testdta" );

ifile = codecs.open( "source/%s/%s.items" % ( PREFIX, PREFIX ), "r", encoding="utf-8" );
jfile = codecs.open( "source/%s/%s.out" % ( PREFIX, PREFIX ), "r", encoding="utf-8" );

mrss = {};
mrsr = pyrmrs.ext.mrsread.MRSRead();

i = 0;

while True:

  i += 1; 
  
  surface = ifile.readline();
  tsdb = jfile.readline();
  if surface == "" and tsdb == "":
    break;
  if tsdb == "\n":
    continue;
  surface = surface.replace("\n","");
  mrs = tsdb[ tsdb.find("@@@") + 3 : tsdb.rfind("@") ];
  
  rmrs = None;
  try:
    for xrmrs in mrsr.mrsread( mrs ):
      rmrs = xrmrs;
  except Exception, e:
    print str( e );
    rmrs = None;
    del mrsr;
    mrsr = pyrmrs.ext.mrsread.MRSRead();
    sys.exit( -1 );
      
  st = "! ";
  if not rmrs is None:
    st = "  ";
  print "%s--> %s" % ( st, surface );
  
  mrss[ surface ] = rmrs;

jfile.close();  
ifile.close();



class MyRMRSifier( pyrmrs.rmrsifier.RMRSifier ):
  
  def __init__( self, ifile, ofile, active_tags = [ "proposition" ] ):
    
    pyrmrs.rmrsifier.RMRSifier.__init__( self, ifile, ofile, active_tags );
  
  def rmrsify( self, surface ):
    
    global mrss;
    
    tx = surface;
    txt = "";
    active = True;
    for ch in tx:
      if ch == "\n":
        active = False;
      if ch != "\n" and string.whitespace.find( ch ) == -1:
        if active == False:
          txt += " ";
        active = True;
      if active:
        txt += ch;
    surface = txt;
    
    self.out.write( "\n" + self.atindent + "<analysis>" );
    self.out.write( "\n" + self.atindent + "<sentence>" );
    
    rmrs = None;
    if mrss.has_key( surface ):
      rmrs = mrss[ surface ];
    
    if not rmrs is None:
      self.out.write( "\n" + self.atindent + "<!--\n" );
      self.out.write( rmrs.str_pretty() );
      self.out.write( "\n" + self.atindent + "-->\n" + self.atindent );
      self.out.write( \
        rmrs.str_xml().replace( "\n", "\n" + self.atindent ) );
    else:
      self.out.write( "\n" + self.atindent + "<rmrs/>" );
    
    self.out.write( "\n" + self.atindent + "</sentence>" );
    self.out.write( "\n" + self.atindent + "</analysis>" );
    self.out.write( "\n" );



for filename in os.listdir( "source/" + PREFIX ):
  if filename.endswith( ".ts.xml" ):
    print filename;
    ifile = open( "source/" + PREFIX + "/" + filename );
    ofile = codecs.open( "processed/" + PREFIX + "/" + filename.replace( ".ts.xml", ".rmrs.ts.xml"), \
                         "w", encoding="utf-8" );
    rmrsifier = MyRMRSifier( ifile, ofile );
    ofile.close();
    ifile.close();

pyrmrs.globals.destructMain();
