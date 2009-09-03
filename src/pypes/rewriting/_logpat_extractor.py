# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "extract_logpats" ];

import sys;
import gzip;
import codecs;
from itertools import chain;

from pypes.utils.mc import subject;

from pypes.proto import *;
import pypes.proto.lex.erg;
from pypes.proto.lex import basic;

from pypes.codecs_ import PFTDecoder, pft_encode;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _LogpatExtractor( ProtoProcessor, metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._decoder_ctx = PFTDecoder( (None,pypes.proto.lex.erg) );
    self._decoder = self._decoder_ctx.__enter__();
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._decoder = None;
    self._decoder_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  
  def extract_from_dir( self, dir ):
    
    self._dir = dir;
    
    for i in range( 1, 108 ):
      self._extract_from_file( "{0}/mrs-{1}1.pft.gz".format( dir, i ) );
    
    for i in range( 1, 641 ):
      self._extract_from_file( "{0}/fracas-{1}.pft.gz".format( dir, i ) );


  def _extract_from_file( self, filename ):
    
    try:
      
      f_ = gzip.open( filename, "rb" );
      
      try:
        
        cdc = codecs.getreader( "utf-8" );
        f = cdc( f_ );
        
        print( filename );
  
        fstr = f.read();
        print( fstr );
        
        pf = self._decoder.decode( fstr )( sig=ProtoSig() );
        
        self._logpats = set();
        self.process( pf );

        k = open( filename.replace( ".pft.gz", ".txt" ) )
        txt = k.read();
        k.close();
        
        for ( logpat_type, logpat_pred ) in self._logpats:
          g = open(
                  self._dir.replace( "/test", "/pat" ) + \
                    "/" + logpat_type + "_" + logpat_pred + ".txt",
                  "a"
                );
          g.write( filename + ": " + txt );
          g.write( "\n\n" );
          g.write( pft_encode(pf) );
          g.write( "\n\n\n\n" );
          g.close();
                    
        
        print( "-------" );
        
      finally:
        f_.close();
        
    except IOError:
      pass;
    
  
  def _register_logpat( self, logpat_type, referent ):
    
    if isinstance( referent, Operator ):
      if not referent.otype in basic.Operator.OPs:
        self._logpats.add( ( logpat_type, referent.otype ) );
      return;
    
    assert isinstance( referent, Word );
    
    if referent.word is not None:
      pred = "";
      for tok in referent.lemma:
        pred += tok + "+";
      pred = pred[ :-1 ];
      if referent.pos is not None:
        pred += "_" + referent.pos;
      if referent.sense is not None:
        pred += "_" + referent.sense;
      self._logpats.add( ( logpat_type, pred ) );
  
  def process_predication_( self, inst, subform, predicate, args ):
    
    self._register_logpat( "p", inst.predicate.referent );
    
  def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):

    self._register_logpat( "q", inst.quantifier.referent );

  def process_modification_( self, inst, subform, modality, args, scope ):

    self._register_logpat( "m", inst.modality.referent );

  def process_connection_( self, inst, subform, connective, lscope, rscope ):

    self._register_logpat( "c", inst.connective.referent );

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def extract_logpats():
  
  with _LogpatExtractor( None ) as extractor:
    extractor.extract_from_dir( "dta/test" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
