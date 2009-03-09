# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "NullRewriter", "null_rewrite" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.proto_processor import ProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class NullRewriter( ProtoProcessor, metaclass=subject ):
  
  
  def rewrite( self ):
    
    return self.process( self._obj_ );


  def _process_predication( self, inst, predicate, args ):
    
    return inst.__class__(
               predicate = predicate,
               args = args
             );
    
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    return inst.__class__(
               quantifier = quantifier,
               var = var,
               rstr = rstr,
               body = body
             );
             
  def _process_modification( self, inst, modality, args, scope ):
    
    return inst.__class__(
               modality = modality,
               args = args,
               scope = scope
             );
    
  def _process_connection( self, inst, connective, lscope, rscope ):
    
    return inst.__class__(
               connective = connective,
               lscope = lscope,
               rscope = rscope
             );
    
  def _process_handle( self, inst, hid ):
    
    return inst.__class__(
               hid = hid
             );
    
  def _process_constraint( self, inst, harg, larg ):
    
    return inst.__class__(
               harg = harg,
               larg = larg
             );
    
  def _process_protoform( self, inst, subforms, constraints ):
    
    return inst.__class__(
               subforms = subforms,
               constraints = constraints
            );
    
  def _process_predicate( self, inst, referent ):
    
    return inst.__class__(
                referent = referent
             );
    
  def _process_quantifier( self, inst, referent ):
    
    return inst.__class__(
               referent = referent
             );
    
  def _process_modality( self, inst, referent ):
    
    return inst.__class__(
               referent = referent
            );
    
  def _process_connective( self, inst, referent ):
    
    return inst.__class__(
               referent = referent
             );
    
  def _process_argument( self, inst, aid ):
    
    return inst.__class__(
               aid = aid
             );
    
  def _process_variable( self, inst, sid, vid ):
    
    return inst.__class__(
               sidvid = (sid,vid)
             );
    
  def _process_constant( self, inst, ident ):
    
    return inst.__class__(
               ident = ident
             );
    
  def _process_sort( self, inst, sid ):
    
    return inst.__class__(
               sid = sid
             );
    
  def _process_word( self, inst, wid, lemma, pos, sense, feats ):
    
    return inst.__class__(
               wid = wid,
               lemma = lemma,
               pos = pos,
               sense = sense,
               feats = feats
             );
    
  def _process_operator( self, inst, otype, feats ):
    
    return inst.__class__(
               otype = otype,
               feats = feats
             );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def null_rewrite( obj ):
  
  rslt = None;
  with NullRewriter( obj ) as rewriter:
    rslt = rewriter.rewrite();
  return rslt;
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
