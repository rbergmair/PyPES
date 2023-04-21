# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "TreeEncoder", "tree_encode" ];

import re;
import string;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TreeEncoder( ProtoProcessor, metaclass=subject ):

  def process_operator_( self, inst, otype ):
    
    return otype;
  
  def process_word_( self, inst, lemma, pos, sense ):
    
    rslt = "_";
    if lemma is not None:
      for lemtok in lemma:
        rslt += lemtok + "+";
      rslt = rslt[ :-1 ];
    if pos is not None or sense is not None:
      rslt += "_";
      if pos is not None:
        rslt += pos;
      if sense is not None:
        rslt += "_" + sense;
    
    return rslt;
  
  def process_argslist_( self, inst, args ):
    
    if self._utool_style:
      return "";
    
    for arg in inst.values():
      if isinstance( arg, Constant ):
        try:
          int( arg.ident );
        except:
          return "( " + arg.ident + " )";
    
    return "";

  def process_functor_( self, inst, fid, referent, feats ):
    
    rslt = referent;
    if fid is not None:
      rslt += ":" + str(fid);
    return rslt;
  
  def process_predication_( self, inst, subform, predicate, args ):
    
    if predicate is not None:
      return predicate + self.process_argslist_( inst.args, args );
  
  def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
    
    if rstr is None:
      return None;
    if body is None:
      return None;
    return quantifier + "( " + rstr + ", " + body + " )";

  def process_modification_( self, inst, subform, modality, args, scope ):
    
    if scope is None:
      return None;
    return modality + "( " + scope + " )";

  def process_connection_( self, inst, subform, connective, lscope, rscope ):
    
    if lscope is None:
      return None;
    if rscope is None:
      return None;
    return connective + "( " + lscope + ", " + rscope + " )";

  def process_protoform_( self, inst, subform, subforms, constraints ):
    
    try:
      arg = "";
      rslt = "";
      used_refs = set();
      for ( root, ( root_, subform_ ) ) in zip( inst.roots, subforms ):
        subform = inst.subforms[ root ];
        if isinstance( subform, Connection ):
          if     isinstance( subform.connective.referent, Operator ) \
             and ( subform.connective.referent.otype is Operator.OP_C_WEACON ):
            continue;
          pref = subform_.split( "(" )[ 0 ];
          if not self._utool_style:
            rslt += subform_ + " /\ ";
          else:
            rslt += pref + " /\ ";
            r = subform_.find( "(" );
            if r != -1:
              arg += subform_[ r: ];
          used_refs.add( pref );
      
      # print( used_refs );
  
      for ( root, ( root_, subform_ ) ) in zip( inst.roots, subforms ):
        subform = inst.subforms[ root ];
        if isinstance( subform, Connection ):
          continue;
        pref = subform_.split( "(" )[ 0 ];
        if pref not in used_refs:
          if not self._utool_style:
            rslt += subform_ + " /\ ";
          else:
            rslt += pref + " /\ ";
            r = subform_.find( "(" );
            if r != -1:
              arg += subform_[ r: ];
      
      rslt = rslt[ :-4 ];
      rslt += arg;
      
      return rslt;  
      
    except:
      return None;
  
  def encode( self, utool_style=False ):
    
    self._utool_style = utool_style;
    
    return self.process( self._obj_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def tree_encode( pfobj, utool_style=False ):
  
  rslt = None;
  with TreeEncoder( pfobj ) as encoder:
    rslt = encoder.encode( utool_style=utool_style );
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
