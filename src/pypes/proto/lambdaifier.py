# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "Lambdaifier", "lambdaify" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.proto_processor import ProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Lambdaifier( ProtoProcessor, metaclass=subject ):
  
  
  def lambdaify( self, pf ):
    
    return self.process( pf );
  
  
  def _process_freezer( self, content, freezelevel ):
    
    return Freezer( content=content );

  def _process_predication( self, inst, subform, predicate, args ):
    
    return inst.__class__(
               predicate = predicate,
               args = args
             );
    
  def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
    
    return inst.__class__(
               quantifier = quantifier,
               var = var,
               rstr = rstr,
               body = body
             );
             
  def _process_modification( self, inst, subform, modality, args, scope ):
    
    return inst.__class__(
               modality = modality,
               args = args,
               scope = scope
             );
    
  def _process_connection( self, inst, subform, connective, lscope, rscope ):
    
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
    
  def _process_protoform( self, inst, subform, subforms, constraints ):
    
    return inst.__class__(
               subforms = subforms,
               constraints = constraints
            );
    
  def _process_functor( self, inst, fid, referent, feats ):
    
    return inst.__class__(
               fid = fid,
               referent = referent,
               feats = feats
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
    
  def _process_word( self, inst, lemma, pos, sense ):
    
    return inst.__class__(
               lemma = lemma,
               pos = pos,
               sense = sense
             );
    
  def _process_operator( self, inst, otype ):
    
    return inst.__class__(
               otype = otype
             );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def lambdaify( pf ):
  
  rslt = None;
  with Lambdaifier() as lambdaifier:
    rslt = lambdaifier.lambdaify( pf );
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
