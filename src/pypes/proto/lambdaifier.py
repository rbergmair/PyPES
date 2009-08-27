# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "Lambdaifier", "lambdaify" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.proto_processor import ProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class LambdaifyingProcessor( ProtoProcessor, metaclass=subject ):
  
  
  def __init__( self ):
    
    self.global_holes = {};
  
  
  def process_subform( self, subform ):

    for hole in subform.holes:
      self.global_holes[ hole ] = 0;
    
    return super().process_subform( subform );
  
  
  def process_freezer_( self, content, freezelevel ):
    
    pass;
  
  def process_freezer( self, handle, freezelevel=None ):
    
    if freezelevel is None:
      freezelevel = self.global_holes[ handle ];
    
    if freezelevel == -1:
      return self.process_handle( handle );
    else:
      return self.process_freezer_(
                 self.process_freezer( handle, freezelevel-1 ),
                 freezelevel
               );
  
  
  def process_scopebearer( self, inst ):
    
    if isinstance( inst, ProtoForm ):
      return self.process_subform( inst );
    elif isinstance( inst, Handle ):
      return self.process_freezer( inst );

    
  def process_protoform( self, inst, subform ):
    
    for hole in self.global_holes:
      self.global_holes[ hole ] += 1;
    
    rslt = super().process_protoform( inst, subform );
    
    holes = set( self.global_holes );
    for hole in holes:
      self.global_holes[ hole ] -= 1;
      if self.global_holes[ hole ] < 0:
        del self.global_holes[ hole ];
    
    return rslt;
  
  
  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Lambdaifier( LambdaifyingProcessor, metaclass=subject ):
  
  
  def lambdaify( self, pf ):
    
    return self.process( pf );
  
  
  def process_freezer_( self, content, freezelevel ):
    
    return Freezer( content=content );

  def process_predication_( self, inst, subform, predicate, args ):
    
    return inst.__class__(
               predicate = predicate,
               args = args
             );
    
  def process_quantification_(
          self, inst, subform, quantifier, var, rstr, body
        ):
    
    return inst.__class__(
               quantifier = quantifier,
               var = var,
               rstr = rstr,
               body = body
             );
             
  def process_modification_( self, inst, subform, modality, args, scope ):
    
    return inst.__class__(
               modality = modality,
               args = args,
               scope = scope
             );
    
  def process_connection_( self, inst, subform, connective, lscope, rscope ):
    
    return inst.__class__(
               connective = connective,
               lscope = lscope,
               rscope = rscope
             );
    
  def process_handle_( self, inst, hid ):
    
    return inst.__class__(
               hid = hid
             );
    
  def process_constraint_( self, inst, harg, larg ):
    
    return inst.__class__(
               harg = harg,
               larg = larg
             );
    
  def process_protoform_( self, inst, subform, subforms, constraints ):
    
    return inst.__class__(
               subforms = subforms,
               constraints = constraints
            );
    
  def process_functor_( self, inst, fid, referent, feats ):
    
    return inst.__class__(
               fid = fid,
               referent = referent,
               feats = feats
             );
             
  def process_argument_( self, inst, aid ):
    
    return inst.__class__(
               aid = aid
             );
    
  def process_variable_( self, inst, sort, vid ):
    
    return inst.__class__(
               sidvid = (inst.sort.sid,vid)
             );
    
  def process_constant_( self, inst, ident ):
    
    return inst.__class__(
               ident = ident
             );
    
  def process_sort_( self, inst, sid ):
    
    return inst.__class__(
               sid = sid
             );
    
  def process_word_( self, inst, lemma, pos, sense ):
    
    return inst.__class__(
               lemma = lemma,
               pos = pos,
               sense = sense
             );
    
  def process_operator_( self, inst, otype ):
    
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
