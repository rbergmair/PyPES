# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "ProtoProcessor" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ProtoProcessor( metaclass=subject ):
  
  
  def __init__( self ):
    
    self.global_holes = {};
  
  
  def process( self, inst ):
    
    if isinstance( inst, SubForm ):
      return self.process_subform( inst );
    if isinstance( inst, Constraint ):
      return self.process_constraint( inst );
    if isinstance( inst, Functor ):
      return self.process_functor( inst );
    if isinstance( inst, Variable ):
      return self.process_variable( inst );
    if isinstance( inst, Constant ):
      return self.process_constant( inst );
    if isinstance( inst, Sort ):
      return self.process_sort( inst );
    if isinstance( inst, Argument ):
      return self.process_argument( inst );
    if isinstance( inst, Word ):
      return self.process_word( inst );
    if isinstance( inst, Operator ):
      return self.process_operator( inst );
    if isinstance( inst, Handle ):
      return self.process_handle( inst );
    try:
      assert False;
    except:
      print( inst );
      raise;


  def _process_subform( self, inst, holes, protoforms ):
    
    pass;


  def process_subform( self, subform ):

    for hole in subform.holes:
      self.global_holes[ hole ] = 0;
      
    subform_ = self._process_subform( subform, subform.holes, subform.protoforms );

    if isinstance( subform, Predication ):
      return self.process_predication( subform, subform_ );
    if isinstance( subform, Quantification ):
      return self.process_quantification( subform, subform_ );
    if isinstance( subform, Modification ):
      return self.process_modification( subform, subform_ );
    if isinstance( subform, Connection ):
      return self.process_connection( subform, subform_ );
    if isinstance( subform, ProtoForm ):
      return self.process_protoform( subform, subform_ );
    assert False;
  
  
  def _process_freezer( self, content, freezelevel ):
    
    pass;
  
  def process_freezer( self, handle, freezelevel=None ):
    
    if freezelevel is None:
      freezelevel = self.global_holes[ handle ];
    
    if freezelevel == -1:
      return self.process_handle( handle );
    else:
      return self._process_freezer(
                 self.process_freezer( handle, freezelevel-1 ),
                 freezelevel
               );
  
  
  def process_scopebearer( self, inst ):
    
    if isinstance( inst, ProtoForm ):
      return self.process_subform( inst );
    elif isinstance( inst, Handle ):
      return self.process_freezer( inst );


  def _process_predication( self, inst, subform, predicate, args ):
    
    pass;
  
  def process_predication( self, inst, subform ):
    
    predicate_ = self.process_functor( inst.predicate );
    
    args_ = {};
    for ( arg, val ) in inst.args.items():
      arg_ = self.process_argument( arg );
      if isinstance( val, Variable ):
        val_ = self.process_variable( val );
      elif isinstance( val, Constant ):
        val_ = self.process_constant( val );
      else:
        assert False;
      args_[ arg_ ] = val_;
    
    return self._process_predication(
               inst = inst,
               subform = subform,
               predicate = predicate_,
               args = args_
             );
  
  
  def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
    
    pass;
  
  def process_quantification( self, inst, subform ):
    
    quantifier_ = self.process_functor( inst.quantifier );
    
    var_ = self.process_variable( inst.var );
    
    rstr_ = self.process_scopebearer( inst.rstr );
    
    body_ = self.process_scopebearer( inst.body );
    
    return self._process_quantification(
               inst = inst,
               subform = subform,
               quantifier = quantifier_,
               var = var_,
               rstr = rstr_,
               body = body_
             );
  
  
  def _process_modification( self, inst, subform, modality, args, scope ):
    
    pass;
  
  def process_modification( self, inst, subform ):
    
    modality_ = self.process_functor( inst.modality );
    
    args_ = {};
    for ( arg, val ) in inst.args.items():
      arg_ = self.process_argument( arg );
      if isinstance( val, Variable ):
        val_ = self.process_variable( val );
      elif isinstance( val, Constant ):
        val_ = self.process_constant( val );
      else:
        assert False;
      args_[ arg_ ] = val_;

    scope_ = self.process_scopebearer( inst.scope );
    
    return self._process_modification(
               inst = inst,
               subform = subform,
               modality = modality_,
               args = args_,
               scope = scope_
             );
  
  
  def _process_connection( self, inst, subform, connective, lscope, rscope ):
    
    pass;
  
  def process_connection( self, inst, subform ):
    
    connective_ = self.process_functor( inst.connective );

    lscope_ = self.process_scopebearer( inst.lscope );
    
    rscope_ = self.process_scopebearer( inst.rscope );
    
    return self._process_connection(
               inst = inst,
               subform = subform,
               connective = connective_,
               lscope = lscope_,
               rscope = rscope_
             );


  def _process_handle( self, inst, hid ):
    
    pass;
  
  def process_handle( self, inst ):
    
    return self._process_handle(
               inst = inst,
               hid = inst.hid
             );
  
  
  def _process_constraint( self, inst, harg, larg ):
    
    pass;
  
  def process_constraint( self, inst ):
    
    assert isinstance( inst.harg, Handle );
    harg_ = self.process_handle( inst.harg );

    assert isinstance( inst.harg, Handle );
    larg_ = self.process_handle( inst.larg );

    return self._process_constraint(
               inst = inst,
               harg = harg_,
               larg = larg_
             );
  
  
  def _process_protoform( self, inst, subform, subforms, constraints ):
    
    pass;
  
  def process_protoform( self, inst, subform ):
    
    for hole in self.global_holes:
      self.global_holes[ hole ] += 1;
    
    subforms_ = [];
    
    for root in inst.roots:
      
      subform__ = inst.subforms[ root ];
      root_ = self.process_handle( root );
      
      if isinstance( subform__, SubForm ):
        subform_ = self.process_subform( subform__ );
      else:
        try:
          assert False;
        except:
          print( root );
          print( subform__ );
          raise;
        
      subforms_.append( (root_,subform_) );

    holes = set( self.global_holes );
    for hole in holes:
      self.global_holes[ hole ] -= 1;
      if self.global_holes[ hole ] < 0:
        del self.global_holes[ hole ];
    
    constraints_ = [];
    for constraint in inst.constraints:
      constraint_ = self.process_constraint( constraint );
      constraints_.append( constraint_ );
    
    return self._process_protoform(
               inst = inst,
               subform = subform,
               subforms = subforms_,
               constraints = constraints_
             );
  
  
  def _process_functor( self, inst, fid, referent, feats ):
    
    pass;
  
  def process_functor( self, inst ):
    
    if isinstance( inst.referent, Word ):
      referent_ = self.process_word( inst.referent );
    elif isinstance( inst.referent, Operator ):
      referent_ = self.process_operator( inst.referent );
    
    return self._process_functor(
               inst = inst,
               fid = inst.fid,
               referent = referent_,
               feats = inst.feats
            );
            
            
  def _process_argument( self, inst, aid ):
    
    pass;
  
  def process_argument( self, inst ):
    
    return self._process_argument(
               inst = inst,
               aid = inst.aid
             );

  
  def _process_variable( self, inst, sid, vid ):
    
    pass;
  
  def process_variable( self, inst ):
    
    self.process_sort( inst.sort );
    
    return self._process_variable(
               inst = inst,
               sid = inst.sort.sid,
               vid = inst.vid
             );

  
  def _process_constant( self, inst, ident ):
    
    pass;
  
  def process_constant( self, inst ):
    
    return self._process_constant(
               inst = inst,
               ident = inst.ident
             );
  
  
  def _process_sort( self, inst, sid ):
    
    pass;
  
  def process_sort( self, inst ):
    
    return self._process_sort(
               inst = inst,
               sid = inst.sid
             );
  
  
  def _process_word( self, inst, lemma, pos, sense ):
    
    pass;
  
  def process_word( self, inst ):
    
    return self._process_word(
               inst = inst,
               lemma = inst.lemma,
               pos = inst.pos,
               sense = inst.sense
             );
  
  
  def _process_operator( self, inst, otype ):
    
    pass;
  
  def process_operator( self, inst ):
    
    return self._process_operator(
               inst = inst,
               otype = inst.otype
             );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
