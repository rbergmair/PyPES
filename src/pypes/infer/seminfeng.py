# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "SemanticInferenceAgent" ];

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.codecs_ import pft_decode, pft_encode;

from pypes.rewriting.renamer import Renamer;
from pypes.rewriting.reifier import Reifier;

from pypes.infer.infeng import InferenceAgent;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SemanticInferenceAgent( InferenceAgent, metaclass=subject ):
  
  SEMFIELD = None;
  
  
  class _PreProcessor( ProtoProcessor, metaclass=subject ):
    
    def process_sort_( self, inst, sid ):
      
      if inst.sid != "x":
        inst.sid = "e";

    def process_functor_( self, inst, fid, referent, feats ):
      
      inst.feats = {};
  
  
  class _PostProcessor( ProtoProcessor, metaclass=subject ):
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      def wrap( subform ):
        
        pf = ProtoForm()( sig = ProtoSig() );
        root = Handle()( sig = ProtoSig() );
        pf.append_fragment( root, subform );
        return pf;
      
      r = analyze_as_conjunction_pf( inst );
      if r is None:
        return;
      
      ( conns, nonconns ) = r;
      
      cur = conns[0];
      
      conns = conns[1:];

      cur.lscope = wrap( nonconns[0] );
      cur.rscope = wrap( nonconns[1] );

      nonconns = nonconns[2:];
      
      for ( nonconn, conn ) in zip( nonconns, conns ):
        
        conn.lscope = wrap( cur );
        conn.rscope = wrap( nonconn );
        cur = conn;
      
      newroot = Handle()( sig = ProtoSig() );
      inst.roots = [ newroot ];
      inst.subforms = { newroot: cur };
      
      return inst;


  def _enter_( self ):
    
    self._pp_ctx = self._PreProcessor( self );
    self._pp = self._pp_ctx.__enter__();
    self._renamer_ctx = Renamer();
    self._renamer = self._renamer_ctx.__enter__();
    self._reifier_ctx = Reifier();
    self._reifier = self._reifier_ctx.__enter__();
    self._postp_ctx = self._PostProcessor( self );
    self._postp = self._postp_ctx.__enter__();

  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._postp = None;
    self._postp_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._reifier = None;
    self._reifier_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._renamer = None;
    self._renamer_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._pp = None;
    self._pp_ctx.__exit__( exc_type, exc_val, exc_tb );
    

  def reset( self ):
    
    self.pfs = {};
    self.discs = {};
    
  
  def process_sentence( self, sentid, rec, text ):
    
    assert rec.get_ctx_str() == text;
    pf = pft_decode( rec.fetch_first( self.SEMFIELD ) )( sig = ProtoSig() );
    self.pfs[ sentid ] = pf;


  def process_discourse( self, discid, rec, sents, inf=False ):
    
    if not inf:
      self.discs[ discid ] = sents;


  def preprocess( self ):
    
    for ( sentid, pf ) in self.pfs.items():
      
      self._pp.process( pf );
      self._renamer.process_pf( pf );

    self._renamer.invert();

    self._sig = ProtoSig();

    for ( sentid, pf ) in self.pfs.items():
      
      pf = self._renamer.rename( pf );
      pf_ = lambdaify( pf );
      pf = pf_( sig = self._sig );
      self.pfs[ sentid ] = pf;
      
      self._reifier.process_pf( pf );

    self._reifier.invert();

    self._sig = ProtoSig();

    for ( sentid, pf ) in self.pfs.items():
      
      pf = self._reifier.reify( pf );
      pf_ = lambdaify( pf );
      pf = pf_( sig = self._sig );
      self.pfs[ sentid ] = pf;

    for pf in self.pfs.values():
      self._postp.process( pf );
    
    return self.pfs;

  
  def infer( self, disc, antecedent, consequent ):
    
    pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
