import os;

import codecs;

import subprocess;

import pyrmrs.config;
import pyrmrs.globals;



class RaspMorpher:

  raspmorphin = None;
  raspmorphout = None;
  pipe = None;
  first = None;


  
  def __init__( self ):
    
    cmd = pyrmrs.config.SH_RASPMORPH;
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    self.pipe = subprocess.Popen( cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT );
    self.raspmorphin = self.pipe.stdin;
    self.raspmorphout = self.pipe.stdout;
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.raspmorphin = codecs.getwriter( "utf-8" )( self.raspmorphin );
    self.raspmorphout = codecs.getreader( "utf-8" )( self.raspmorphout );
    
    self.first = True;


    
  def morph_token( self, tokpos ):
    
    pyrmrs.globals.logDebugCoarse( self, "morphing |>%s<|;" % tokpos );
    
    tokpos += "\n";
    
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % tokpos );
    self.raspmorphin.write( tokpos );
    self.raspmorphin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
    morphstr = "";

    while True:
      pyrmrs.globals.logDebug( self, "reading 1 char..." );
      ch = self.raspmorphout.read( 1 );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );
      if ch == "\n":
        break;
      morphstr += ch;
        
    return morphstr;
  

  def morph( self, smaf ):
    
    node = smaf.lattice.init;
    
    mid = 1;
    
    while node != smaf.lattice.final:
  
      trg = None;
      tok = None;
      poss = [];
      
      for edge in smaf.lattice.lattice[ node ]:
    
        if trg is None:
          trg = edge.target;
        assert edge.target == trg;
        
        if isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
          poss.append( edge );
        elif isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
          tok = edge;
      
      for tag in poss:
        
        assert edge.deps == tok.id;
        tagstr = "%s_%s" % ( tok.text, tag.tag );
        morphstr = self.morph_token( tagstr );
        morphstr = morphstr[ : len(morphstr)-len(tag.tag)-1 ];
        if morphstr != tok.text:
          
          morphedge = pyrmrs.smafpkg.morph_edge.MorphologicalEdge();
          
          morphedge.id = "m%d" % mid;
          mid += 1;
          
          morphedge.source = tag.source;
          morphedge.target = tag.target;
          morphedge.cfrom = tag.cfrom;
          morphedge.cto = tag.cto;
          morphedge.deps = tag.id;
          morphedge.text = morphstr;
          
          smaf.lattice.register( morphedge );
      
      node = trg;
  

  def __del__( self ):
    
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.raspmorphin.close();
    self.raspmorphout.close();
    self.pipe.wait();
    pyrmrs.globals.logDebug( self, "finished closing;" );
  