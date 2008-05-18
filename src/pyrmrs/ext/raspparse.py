import os;

import codecs;

import subprocess;

import pyrmrs.config;
import pyrmrs.globals;



class RaspParser:

  raspparsein = None;
  raspparseout = None;
  pipe = None;
  first = None;


  
  def __init__( self ):
    
    cmd = pyrmrs.config.SH_RASPPARSE + " -ot -u -n %d" % pyrmrs.config.RASP_MAX_NO_PARSES;
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    self.pipe = subprocess.Popen( cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT );
    self.raspparsein = self.pipe.stdin;
    self.raspparseout = self.pipe.stdout;
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.raspparsein = codecs.getwriter( "utf-8" )( self.raspparsein );
    self.raspparseout = codecs.getreader( "utf-8" )( self.raspparseout );
    

    stri = "^ ^_^:1\n";
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % stri );
    self.raspparsein.write( stri );
    self.raspparsein.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );



  def str_overlap( self, x, y ):
  
    if x == "":
      return "";
  
    if y == "":
      return "";
  
    z = x[ :len(x)-1 ];
    z = self.str_overlap( z, y );
    
    if len(z) > len(y)-1:
      return z;
    
    if x[ len(x)-1 ] == y[ len(z) ]:
      return z + x[ len(x)-1 ];
    else:
      return "";


    
  def invoke_parser( self, parsestr ):

    parsestr += "^ ^_^:1\n^ ^_^:1\n";
    pyrmrs.globals.logDebugCoarse( self, "parsing |>%s<|;" % parsestr );
    
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % parsestr );
    self.raspparsein.write( parsestr );
    self.raspparsein.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
    eob_marker = "\n\n\n() -1 ; ()\n\n(X)\n\n";
    eom = eob_marker;
    
    buf = "";
    pending = 0;
    while True:
      
      pyrmrs.globals.logDebug( self, "reading %d chars..." % len(eom) );
      block = self.raspparseout.read( len(eom) );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % block );
      
      overl = self.str_overlap( block, eom );
      if len( overl ) == len( block ):
        break;
      else:
        eom = eob_marker;
      eom = eom[ len(overl) : ];

      pending = len(overl);
      buf += block;
    
    buf = buf[ : len(buf) - pending ];
    
    pyrmrs.globals.logDebugCoarse( self, "returning |>%s<|;" % buf );

    return buf;
  

  def __del__( self ):
    
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.raspparsein.close();
    self.raspparseout.close();
    self.pipe.wait();
    pyrmrs.globals.logDebug( self, "finished closing;" );
  