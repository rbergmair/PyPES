# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "TreeEncoder", "tree_encode" ];

import re;
import string;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TreeEncoder( ProtoProcessor, metaclass=subject ):

  def _process_operator( self, inst, otype, feats ):
    
    return otype;
  
  def _process_word( self, inst, wid, lemma, pos, sense, feats ):
    
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
  
  def _process_argslist( self, inst, args ):
    
    if self._utool_style:
      return "";
    
    for arg in inst.values():
      if isinstance( arg, Constant ):
        try:
          int( arg.ident );
        except:
          return "( " + arg.ident + " )";
    
    return "";

  def _process_predicate( self, inst, referent ):
    
    return referent;
  
  def _process_predication( self, inst, predicate, args ):
    
    if predicate is not None:
      return predicate + self._process_argslist( inst.args, args );

  def _process_quantifier( self, inst, referent ):
    
    return referent;
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    return quantifier + "( " + rstr + ", " + body + " )";

  def _process_modality( self, inst, referent ):
    
    return referent;

  def _process_modification( self, inst, modality, args, scope ):
    
    if scope is None:
      return;
    return modality + "( " + scope + " )";

  def _process_connective( self, inst, referent ):
    
    return referent;

  def _process_connection( self, inst, connective, lscope, rscope ):
    
    if lscope is None:
      return;
    if rscope is None:
      return;
    return connective + "( " + lscope + ", " + rscope + " )";

  def _process_protoform( self, inst, subforms, constraints ):
    
    arg = "";
    rslt = "";
    used_refs = set();
    for ( root_, subform_ ), ( root, subform ) in zip( subforms, inst.subforms ):
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

    for ( root_, subform_ ), ( root, subform ) in zip( subforms, inst.subforms ):
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
