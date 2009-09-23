# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "Comparer", "pfs_leq", "pfs_eq" ];

from copy import copy;
from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.binary_proto_processor import BinaryProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Comparer( BinaryProtoProcessor, metaclass=subject ):
  

  def process_constant( self, inst1, inst2 ):
    
    if not isinstance( inst2, Constant ):
      return None;
    return super().process_constant( inst1, inst2 );
  
  def process_sort( self, inst1, inst2 ):
    
    return super().process_sort( inst1, inst2 );

  def process_variable( self, inst1, inst2 ):
    
    if not isinstance( inst2, Variable ):
      return None;
    return super().process_variable( inst1, inst2 );
  
  def process_argument_value( self, inst1, inst2 ):
    
    return super().process_argument_value( inst1, inst2 );

  def process_argument( self, inst1, inst2 ):
    
    return super().process_argument( inst1, inst2 );

  def process_word( self, inst1, inst2 ):
    
    if not isinstance( inst2, Word ):
      return None;
    return super().process_word( inst1, inst2 );

  def process_operator( self, inst1, inst2 ):
    
    if not isinstance( inst2, Operator ):
      return None;
    return super().process_operator( inst1, inst2 );

  def process_referent( self, inst1, inst2 ):
    
    return super().process_referent( inst1, inst2 );

  def process_functor( self, inst1, inst2 ):
    
    return super().process_functor( inst1, inst2 );

  def process_predication( self, inst1, inst2, subform ):
    
    if not isinstance( inst2, Predication ):
      return None;
    return super().process_predication( inst1, inst2, subform );

  def process_quantification( self, inst1, inst2, subform ):
    
    if not isinstance( inst2, Quantification ):
      return None;
    return super().process_quantification( inst1, inst2, subform );

  def process_modification( self, inst1, inst2, subform ):
    
    if not isinstance( inst2, Modification ):
      return None;
    return super().process_modification( inst1, inst2, subform );

  def process_connection( self, inst1, inst2, subform ):
    
    if not isinstance( inst2, Connection ):
      return None;
    return super().process_connection( inst1, inst2, subform );

  def process_handle( self, inst1, inst2 ):
    
    return super().process_handle( inst1, inst2 );

  def process_subform( self, inst1, inst2 ):
    
    return super().process_subform( inst1, inst2 );

  def process_constraint( self, inst1, inst2 ):
    
    return super().process_constraint( inst1, inst2 );

  def process_protoform( self, inst1, inst2, subform ):
    
    if not isinstance( inst2, ProtoForm ):
      return None;
    return super().process_protoform( inst1, inst2, subform );

  def process_scopebearer( self, inst1, inst2 ):
    
    if isinstance( inst1, ProtoForm ):
      if not isinstance( inst2, ProtoForm ):
        return None;
    if isinstance( inst1, Handle ):
      if not isinstance( inst2, Handle ):
        return None;
    return super().process_scopebearer( inst1, inst2 );

  def process( self, inst1, inst2 ):
    
    return super().process( inst1, inst2 );
  
  
  def true( self ):
    
    return True;
  
  def false( self ):
    
    return False;

  def meet2( self, arg1, arg2 ):
    
    return arg1 and arg2;
  
  def join2( self, arg1, arg2 ):
    
    return arg1 or arg2;
  
  
  def meet1( self, arg1, arg2 ):
    
    if arg1 is None:
      return None;
    if arg2 is None:
      return None;
    
    return self.meet2( arg1, arg2 );
  
  
  def join1( self, arg1, arg2 ):
    
    if arg1 is None:
      return arg2;
    if arg2 is None:
      return arg1;
    
    return self.join2( arg1, arg2 );
  
  
  def meet( self, *args ):
    
    rslt = self.true();
    for arg in args:
      rslt = self.meet1( rslt, arg );
      
    return rslt;
  
  
  def join( self, *args ):
    
    rslt = self.false();
    for arg in args:
      rslt = self.join1( rslt, arg );
      
    return rslt;


  def process_constant_( self, inst1, inst2, ident1, ident2 ):
    
    if ident1 is not None:
      if ident1 != ident2:
        return False;
    
    return True;


  def process_sort_( self, inst1, inst2, sid1, sid2 ):
    
    if sid1 is not None:
      if sid1 != sid2:
        return False;
      
    return True;


  def process_variable_( self, inst1, inst2, vid1, vid2, sort ):

    assert not inst1.sort is None;
    if sort is None:
      return None;

    if vid1 is not None:
      if vid1 != vid2:
        return False;
    
    return sort;


  def process_argument_( self, inst1, inst2, aid1, aid2 ):
    
    if aid1 is not None:
      if aid1 != aid2:
        return False;
      
    return True;


  def process_word_( self, inst1, inst2, lemma1, lemma2, pos1, pos2, sense1, sense2 ):
    
    if lemma1 is None:
      if lemma2 is not None:
        return False;
      
    if lemma1 is not None:
      if lemma2 is None:
        return False;
      if len( lemma1 ) != len( lemma2 ):
        return False;
      for i in range( 0, len(lemma1) ):
        if lemma1[ i ].upper() != lemma2[ i ].upper():
          return False;
      
    if pos1 != pos2:
      return False;
      
    if sense1 != sense2:
      return False;
      
    return True;
    

  def process_operator_( self, inst1, inst2, otype1, otype2 ):
    
    if otype1 is not None:
      if otype1 != otype2:
        return False;
      
    return True;


  def process_functor_( self, inst1, inst2, fid1, fid2, feats1, feats2, referent ):
    
    assert inst1.referent is not None;
    if referent is None:
      return None;
    
    if fid1 is not None:
      if fid1 != fid2:
        return False;

    if feats1:
      if not feats2:
        return False;
      for feat in feats1:
        if not feat in feats2:
          return False;
        if feats1[ feat ] != feats2[ feat ]:
          return False;
      
    return referent;
  

  # doesn't work
  # _extract_one_to_one_mappings( { (1,5), (1,6), (2,5), (2,7), (2,8), (3,8), (4,8) } );
  # works:
  # _extract_one_to_one_mappings( { (1,5), (1,6), (2,5), (2,7), (3,5), (3,8), (4,8) } );
  # _extract_one_to_one_mappings( { (1,5), (1,6), (1,9), (2,5), (2,7), (3,5), (3,8), (4,8) } );
  
  def _extract_one_to_one_mappings( self, rel ):
    
    if len( rel ) == 0:
      yield set();
      return;
    
    dom = set();
    rng = set();
    for (domitem,rngitem) in rel:
      dom.add( domitem );
      rng.add( rngitem );
    
    # if len( dom ) == 0:
    #   return set();
    
    if len( dom ) > len( rng ):
      return;
    
    for ( domitem, rngitem ) in rel:
      rel_ = set();
      for ( domitem_, rngitem_ ) in rel:
        if ( domitem_ is not domitem ) and ( rngitem_ is not rngitem ):
          rel_.add( (domitem_,rngitem_) );
      for mapping in self._extract_one_to_one_mappings( rel_ ):
        mapping.add( (domitem,rngitem) );
        if len( mapping ) == len( dom ):
          yield mapping;


  def _check_match( self, domlen, rel ):
    
    dom = set();
    for (domitem,rngitem) in rel:
      dom.add( domitem );
    
    if len( dom ) != domlen:
      return;
    
    for mapping in self._extract_one_to_one_mappings( rel ):
      yield mapping;
  
  
  def _process_args( self, inst1, args ):

    subresults = {};
    rel = set();
    
    for ( (arg1,arg2,arg_), (val1,val2,val_) ) in args:
      subrslt = self.meet( arg_, val_ );
      if subrslt:
        subresults[ (arg1,arg2) ] = subrslt;
        rel.add( (arg1,arg2) );
    
    rslt = self.join();
    for mapping in self._check_match( len(inst1.args), rel ):
      rslt_ = self.meet();
      for (arg1,arg2) in mapping:
        rslt_ = self.meet( rslt_, subresults[ (arg1,arg2) ] );
      rslt = self.join( rslt, rslt_ );
    
    return rslt;

  
  def process_predication_( self, inst1, inst2, subform, predicate, args ):

    if subform is None:
      return None;
    
    assert inst1.predicate is not None;
    if predicate is None:
      return None;
    
    if inst1.args and not inst2.args:
      return None;
    
    return self.meet( subform, predicate, self._process_args( inst1, args ) ); 


  def process_quantification_( self, inst1, inst2, subform, quantifier, var, rstr, body ):
    
    if subform is None:
      return None;

    assert inst1.quantifier is not None;
    if quantifier is None:
      return None;
    
    assert inst1.var is not None;
    if var is None:
      return None;
    
    assert inst1.rstr is not None;
    if rstr is None:
      return None;

    assert inst1.body is not None;
    if body is None:
      return None;
    
    return self.meet( subform, quantifier, var, rstr, body );


  def process_modification_( self, inst1, inst2, subform, modality, args, scope ):
    
    if subform is None:
      return None;
    
    assert inst1.modality is not None;
    if modality is None:
      return None;
      
    assert inst1.scope is not None;
    if scope is None:
      return None;

    if inst1.args and not inst2.args:
      return None;

    return self.meet( subform, modality, self._process_args( inst1, args ), scope ); 

  
  def process_connection_( self, inst1, inst2, subform, connective, lscope, rscope ):
    
    if subform is None:
      return None;
    
    assert inst1.connective is not None;
    if connective is None:
      return None;
      
    assert inst1.lscope is not None;
    if lscope is None:
      return None;
    
    assert inst1.rscope is not None;
    if rscope is None:
      return None;
    
    return self.meet( subform, connective, lscope, rscope );
  
  
  def process_handle_( self, inst1, inst2, hid1, hid2 ):
    
    if hid1 is not None:
      if hid1 != hid2:
        return False;
    return True;


  def process_subform_( self, inst1, inst2, holes, protoforms ):
    
    if inst1.holes and not inst2.holes:
      return None;
    
    subresults = {};
    rel = set();
    
    for ( hole1, hole2, hole_ ) in holes:
      if hole_:
        subresults[ (hole1,hole2) ] = hole_;
        rel.add( (hole1,hole2) );
    
    rslt = self.join();
    for mapping in self._check_match( len(inst1.holes), rel ):
      rslt_ = self.meet();
      for ( hole1, hole2 ) in mapping:
        rslt_ = self.meet( rslt_, subresults[ (hole1,hole2) ] ); 
      rslt = self.join( rslt, rslt_ );
    
    return rslt;
  

  def process_constraint_( self, inst1, inst2, harg, larg ):
    
    assert inst1.harg is not None;
    if harg is None:
      return None;
    
    assert inst1.larg is not None;
    if larg is None:
      return None;
    
    return self.meet( harg, larg );
  
  
  def process_protoform_( self, inst1, inst2, subform, subforms, constraints ):
    
    if subform is None:
      return None;
    
    if inst1.subforms and not inst2.subforms:
      return None;
    
    subresults = {};
    rel = set();
    
    for ( (root1,root2,root_), (subform1,subform2,subform_) ) in subforms:
      subrslt = self.meet( root_, subform_ );
      if subrslt:
        subresults[ (root1,root2) ] = subrslt;
        rel.add( (root1,root2) );
    
    rslt1 = self.join();
    for mapping in self._check_match( len(inst1.subforms), rel ):
      rslt_ = self.meet();
      for ( root1, root2 ) in mapping:
        rslt_ = self.meet( rslt_, subresults[ (root1,root2) ] );
      rslt1 = self.join( rslt1, rslt_ );
    
    if inst1.constraints and not inst2.constraints:
      return None;

    subresults = {};
    rel = set();
    
    for ( constraint1, constraint2, constraint_ ) in constraints:
      if constraint_:
        subresults[ (constraint1,constraint2) ] = constraint_;
        rel.add( (constraint1,constraint2) );
        
    rslt2 = self.join();
    for mapping in self._check_match( len(inst1.constraints), rel ):
      rslt_ = self.meet();
      for ( constraint1, constraint2 ) in mapping:
        rslt_ = self.meet( rslt_, subresults[ (constraint1,constraint2) ] );
      rslt2 = self.join( rslt2, rslt_ );
    
    rslt = self.meet( subform, rslt1, rslt2 );
    
    return rslt;
  
  
  def pfs_leq( self, pf1, pf2 ):
    
    return self.process( pf1, pf2 ) and self.process( pf2, pf1 );


  def pfs_eq( self, pf1, pf2 ):
    
    return self.process( pf1, pf2 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pfs_leq( pf1, pf2 ):
  
  rslt = False;  
  with Comparer() as comparer:
    rslt = comparer.pfs_leq( inst1, inst2 );
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pfs_eq( pf1, pf2 ):
  
  rslt = False;  
  with Comparer() as comparer:
    rslt = comparer.pfs_eq( inst1, inst2 ):
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
