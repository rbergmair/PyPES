# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "TestsuiteRunner", "run_testsuite" ];

import sys;

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import *;

from pypes.infer.biet import YesInferenceAgent, NoInferenceAgent;
from pypes.infer.mcpiet.mcpiet import McPIETAgent;

from pypes.utils.itembank import *;

from pypes.codecs_ import pft_encode;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestsuiteRunner( XMLHandler, metaclass=subject ):


  class _SentenceHandler( XMLPCharElementHandler, metaclass=subject ):
    
    XMLELEM = "sentence";
    
    def startElement( self, name, attrs ):
      
      self._sentid = int( attrs["sentid"] );
      self._obj_._sents.append( self._sentid );
      super().startElement( name, attrs );
    
    def endElement( self, name ):
      
      super().endElement( name );
      self._obj_._process_sentence( self._sentid, self._text );

    
  class _DiscourseHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "discourse";
    
    def startElement( self, name, attrs ):
      
      self._discid = int( attrs["discid"] );
      self._obj_._sents = [];
    
    def endElement( self, name ):
      
      self._obj_._process_discourse( self._discid, self._obj_._sents );


  class _AntecedentHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "antecedent";
    
    def startElement( self, name, attrs ):

      self._obj_._antecedent = int( attrs["discid"] );


  class _ConsequentHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "consequent";
    
    def startElement( self, name, attrs ):

      self._obj_._consequent = int( attrs["discid"] );
  

  class _InferenceHandler( XMLElementHandler, metaclass=subject ):

    XMLELEM = "inference";
  
    def startElement( self, name, attrs ):
      
      self._infid = attrs[ "infid" ];
      self._discid = int( attrs["discid"] );
      self._obj_._antecedent = None;
      self._obj_._consequent = None;
      
    def endElement( self, name ):
      
      self._obj_._infer(
          self._infid,
          self._discid,
          self._obj_._antecedent,
          self._obj_._consequent
        );
      
      #sys.exit( 0 );


  class _GroupHandler( XMLElementHandler, metaclass=subject ):

    XMLELEM = "group";

    def endElement( self, name ):
      
      self._obj_._reset();
  
  
  class _TestsuiteHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "testsuite";


  CLIENT_BYNAME = {
      _SentenceHandler.XMLELEM: ( _SentenceHandler, lambda: None ),
      _DiscourseHandler.XMLELEM: ( _DiscourseHandler, lambda: None ),
      _AntecedentHandler.XMLELEM: ( _AntecedentHandler, lambda: None ),
      _ConsequentHandler.XMLELEM: ( _ConsequentHandler, lambda: None ),
      _InferenceHandler.XMLELEM: ( _InferenceHandler, lambda: None ),
      _GroupHandler.XMLELEM: ( _GroupHandler, None ),
    };
  
  IGNORE = [ "testsuite" ];
  
  
  def _enter_( self ):
    
    super()._enter_();
    self._agent = [];
    self._agent_ctx = [];
    
    ( self._tsdir, self._itemsdir ) = self._obj_;
    
    self._sents_tbl_ctx = TableManager( ( self._itemsdir, "sentence" ) );
    self._sents_tbl = self._sents_tbl_ctx.__enter__();

    self._discs_tbl_ctx = TableManager( ( self._itemsdir, "discourse" ) );
    self._discs_tbl = self._discs_tbl_ctx.__enter__();
    
    self._ofile = {};
    
  def add_agent( self, agent ):
    
    inst_ctx = agent();
    inst = inst_ctx.__enter__();
    self._agent_ctx.append( inst_ctx );
    self._agent.append( inst );
    
    filename = self._tsdir + "/" + inst.__class__.__name__;
    if inst.paramid is not None:
      filename += "-" + inst.paramid;
    filename += ".tsa.xml";
    
    f = open( filename, "wt", encoding="utf-8" );
    self._ofile[ inst ] = f;
    
    f.write(
         """<?xml version="1.0" encoding="UTF-8"?>\n\n"""
         """<annotations>\n\n\n"""
      );
    f.flush();
    
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    for ctx in self._agent_ctx:
      ctx.__exit__( exc_type, exc_val, exc_tb );
    
    for f in self._ofile.values():
      f.write( "\n</annotations>\n" );
      f.close();
    
    self._agent = None;
    self._agent_ctx = None;

    self._discs_tbl_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._discs_tbl = None;
    
    self._sents_tbl_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._sents_tbl = None;

    super()._exit_( exc_type, exc_val, exc_tb );
    
    
  def _reset( self ):
    
    for agent in self._agent:
      agent.reset();
    self._discs = {};
    self._processed = set();
    self._error = False;
    
  
  def _process_sentence( self, sentid, text ):
    
    with self._sents_tbl.record_by_id( sentid ) as rec:
      if rec.get( "status" ) != "succ":
        self._error = True;
      else:
        for agent in self._agent:
          assert rec.get_ctx_str() == text;
          agent.process_sentence( sentid, rec, text );
  
  
  def _process_discourse( self, discid, sents, inf=False ):

    self._discs[ discid ] = sents;
    with self._discs_tbl.record_by_id( discid ) as rec:
      if rec.get( "status" ) != "succ":
        self._error = True;
      else:
        for agent in self._agent:
          agent.process_discourse( discid, rec, sents, inf=inf );
  
  
  def _infer( self, infid, discid, antecedent, consequent ):
    
    sents = self._discs[ antecedent ] + self._discs[ consequent ];
    self._process_discourse( discid, sents, inf=True );
    
    if self._error:
      return;
    
    sys.stdout.write( "   {0:3s}    ".format(infid) );

    for agent in self._agent:

      f = self._ofile[ agent ];
      
      if not agent in self._processed:
        self._processed.add( agent );
        rslt = agent.preprocess();
        f.write( "<!--\n" );
        for key in sorted( rslt.keys() ):
          pf = rslt[ key ];
          key_ = str( key ) + ": ";
          outp = pft_encode( pf );
          outp = outp.replace( "\n", "\n" + len(key_) * " " );
          outp = key_ + outp + "\n";
          f.write( outp );
        f.write( "-->\n" );
      
      (r1, r2) = agent.infer( discid, antecedent, consequent );
      decision = "unknown";
      
      if r1 >= 1.0:
        decision = "entailment";
      if r2 >= 1.0:
        decision = "contradiction";
      if r1 >= 1.0 and r2 >= 1.0:
        decision = "unknown";
      
      f.write(
          ( """<annotation infid="{0:s}" decision="{1:s}">\n"""
            """  <value attribute="r1">{2:0.5f}</value>\n"""
            """  <value attribute="r2">{3:0.5f}</value>\n"""
            """</annotation>\n\n""" ).format( infid, decision, r1, r2 )
        );
      
      f.flush();

    sys.stdout.write( "\n" );
  
  
  
  def run( self ):
    
    self._reset();
    
    with open( self._tsdir + "/data.ts.xml", "rb" ) as f:
      
      x = f.read( self.CHUNK_SIZE );
      while x:
        self.feed( x );
        x = f.read( self.CHUNK_SIZE );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def run_testsuite( tsdir, itemsdir ):
  
  with TestsuiteRunner( (tsdir,itemsdir) ) as runner:
    
    #runner.add_agent( lambda: YesInferenceAgent( paramid="ASDF" ) );
    runner.add_agent( YesInferenceAgent );
    runner.add_agent( NoInferenceAgent );
    runner.add_agent( McPIETAgent );
    runner.run();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
