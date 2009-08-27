# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "ProtoProcessor" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ProtoProcessor( metaclass=subject ):


  def process_constant_( self, inst, ident ):
    
    pass;
  
  def process_constant( self, inst ):
    
    return self.process_constant_(
               inst = inst,
               ident = inst.ident
             );


  def process_sort_( self, inst, sid ):
    
    pass;
  
  def process_sort( self, inst ):
    
    return self.process_sort_(
               inst = inst,
               sid = inst.sid
             );


  def process_variable_( self, inst, sort, vid ):
    
    pass;
  
  def process_variable( self, inst ):
    
    sort_ = self.process_sort( inst.sort );
    
    return self.process_variable_(
               inst = inst,
               sort = sort_,
               vid = inst.vid
             );


  def process_argument_( self, inst, aid ):
    
    pass;
  
  def process_argument( self, inst ):
    
    return self.process_argument_(
               inst = inst,
               aid = inst.aid
             );


  def process_word_( self, inst, lemma, pos, sense ):
    
    pass;
  
  def process_word( self, inst ):
    
    return self.process_word_(
               inst = inst,
               lemma = inst.lemma,
               pos = inst.pos,
               sense = inst.sense
             );
  
  
  def process_operator_( self, inst, otype ):
    
    pass;
  
  def process_operator( self, inst ):
    
    return self.process_operator_(
               inst = inst,
               otype = inst.otype
             );


  def process_functor_( self, inst, fid, referent, feats ):
    
    pass;
  
  def process_functor( self, inst ):
    
    if isinstance( inst.referent, Word ):
      referent_ = self.process_word( inst.referent );
    elif isinstance( inst.referent, Operator ):
      referent_ = self.process_operator( inst.referent );
    
    return self.process_functor_(
               inst = inst,
               fid = inst.fid,
               referent = referent_,
               feats = inst.feats
            );


  def process_predication_( self, inst, subform, predicate, args ):
    
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
    
    return self.process_predication_(
               inst = inst,
               subform = subform,
               predicate = predicate_,
               args = args_
             );
  
  
  def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
    
    pass;
  
  def process_quantification( self, inst, subform ):
    
    quantifier_ = self.process_functor( inst.quantifier );
    
    var_ = self.process_variable( inst.var );
    
    rstr_ = self.process_scopebearer( inst.rstr );
    
    body_ = self.process_scopebearer( inst.body );
    
    return self.process_quantification_(
               inst = inst,
               subform = subform,
               quantifier = quantifier_,
               var = var_,
               rstr = rstr_,
               body = body_
             );
  
  
  def process_modification_( self, inst, subform, modality, args, scope ):
    
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
    
    return self.process_modification_(
               inst = inst,
               subform = subform,
               modality = modality_,
               args = args_,
               scope = scope_
             );
  
  
  def process_connection_( self, inst, subform, connective, lscope, rscope ):
    
    pass;
  
  def process_connection( self, inst, subform ):
    
    connective_ = self.process_functor( inst.connective );

    lscope_ = self.process_scopebearer( inst.lscope );
    
    rscope_ = self.process_scopebearer( inst.rscope );
    
    return self.process_connection_(
               inst = inst,
               subform = subform,
               connective = connective_,
               lscope = lscope_,
               rscope = rscope_
             );


  def process_handle_( self, inst, hid ):
    
    pass;
  
  def process_handle( self, inst ):
    
    return self.process_handle_(
               inst = inst,
               hid = inst.hid
             );


  def process_scopebearer( self, inst ):
    
    if isinstance( inst, ProtoForm ):
      return self.process_subform( inst );
    elif isinstance( inst, Handle ):
      return self.process_handle( inst );


  def process_subform_( self, inst, holes, protoforms ):
    
    pass;


  def process_subform( self, subform ):

    subform_ = self.process_subform_( subform, subform.holes, subform.protoforms );

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
  

  def process_constraint_( self, inst, harg, larg ):
    
    pass;
  
  def process_constraint( self, inst ):
    
    assert isinstance( inst.harg, Handle );
    harg_ = self.process_handle( inst.harg );

    assert isinstance( inst.harg, Handle );
    larg_ = self.process_handle( inst.larg );

    return self.process_constraint_(
               inst = inst,
               harg = harg_,
               larg = larg_
             );
  
  
  def process_protoform_( self, inst, subform, subforms, constraints ):
    
    pass;
  
  def process_protoform( self, inst, subform ):
    
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

    constraints_ = [];
    for constraint in inst.constraints:
      constraint_ = self.process_constraint( constraint );
      constraints_.append( constraint_ );
    
    return self.process_protoform_(
               inst = inst,
               subform = subform,
               subforms = subforms_,
               constraints = constraints_
             );


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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
