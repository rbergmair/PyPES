# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "BinaryProtoProcessor" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class BinaryProtoProcessor( metaclass=subject ):


  def process_constant_( self, inst1, inst2, ident1, ident2 ):
    
    pass;
  
  def process_constant( self, inst1, inst2 ):
    
    return self.process_constant_(
               inst1 = inst1,
               inst2 = inst2,
               ident1 = inst1.ident,
               ident2 = inst2.ident
             );


  def process_sort_( self, inst1, isnt2, sid1, sid2 ):
    
    pass;
  
  def process_sort( self, inst1, inst2 ):
    
    return self.process_sort_(
               inst1 = inst1,
               inst2 = inst2,
               sid1 = inst1.sid,
               sid2 = inst2.sid
             );


  def process_variable_( self, inst1, inst2, sid1, sid2, vid1, vid2 ):
    
    pass;
  
  def process_variable( self, inst1, inst2 ):
    
    self.process_sort( inst1.sort, inst2.sort );
    
    return self.process_variable_(
               inst1 = inst1,
               inst2 = inst2,
               sid1 = inst1.sort.sid,
               sid2 = inst2.sort.sid,
               vid1 = inst1.vid,
               vid2 = inst2.vid
             );
  
  
  def process_argument_value( self, inst1, inst2 ):
    
    if isinstance( inst1, Variable ):
      assert isinstance( inst2, Variable );
      return process_variable( inst1, inst2 );
    
    if isinstance( inst1, Constant ):
      assert isinstance( inst2, Constant );
      return process_constant( inst1, inst2 );
    
    try:
      assert False;
    except:
      print( inst1 );
      print( inst2 );
      raise;
    

  def process_argument_( self, inst1, inst2, aid1, aid2 ):
    
    pass;
  
  def process_argument( self, inst1, inst2 ):
    
    return self.process_argument_(
               inst1 = inst1,
               inst2 = inst2,
               aid1 = inst1.aid,
               aid2 = inst2.aid
             );


  def process_word_( self, inst1, inst2, lemma1, lemma2, pos1, pos2, sense1, sense2 ):
    
    pass;
  
  def process_word( self, inst1, inst2 ):
    
    return self.process_word_(
               inst1 = inst1,
               inst2 = inst2,
               lemma1 = inst1.lemma,
               lemma2 = inst2.lemma,
               pos1 = inst1.pos,
               pos2 = inst2.pos,
               sense = inst.sense
             );
  
  
  def process_operator_( self, inst1, inst2, otype1, otype2 ):
    
    pass;
  
  def process_operator( self, inst1, inst2 ):
    
    return self.process_operator_(
               inst1 = inst1,
               inst2 = inst2,
               otype1 = inst1.otype,
               otype2 = inst2.otype
             );
  
  
  def process_referent( self, inst1, inst2 ):
    
    if isinstance( inst1, Word ):
      assert isinstance( inst2, Word );
      return process_word( inst1, inst2 );
    
    if isinstance( inst1, Operator ):
      assert isinstance( inst2, Word );
      return process_operator( inst1, inst2 );

    try:
      assert False;
    except:
      print( inst1 );
      print( inst2 );
      raise;
    

  def process_functor_( self, inst1, inst2, fid1, fid2, feats1, feats2, referent ):
    
    pass;
  
  def process_functor( self, inst1, inst2 ):
    
    referent_ = self.process_referent( inst1.referent, inst2.referent );
    
    return self.process_functor_(
               inst1 = inst1,
               inst2 = inst2,
               fid1 = inst1.fid,
               fid2 = inst2.fid,
               feats1 = inst1.feats,
               feats2 = inst2.feats,
               referent = referent_
             );
  
  
  def process_predication_( self, inst1, inst2, subform, predicate, args ):
    
    pass;
  
  def process_predication( self, inst1, inst2, subform ):
    
    predicate_ = self.process_functor( inst1.predicate, inst2.predicate );
    
    args_ = [];
    for ( arg1, val1 ) in inst1.args.items():
      args__ = [];
      for ( arg2, val2 ) in inst2.args.items():
        arg_ = self.process_argument( arg1, arg2 );
        val_ = self.process_argument_value( val1, val2 );
        args__.append( (arg_,val_) );
      args_.append( args__ );
    
    return self.process_predication_(
               inst1 = inst1,
               inst2 = inst2,
               subform = subform,
               predicate = predicate_,
               args = args_
             );
  
  
  def process_quantification_( self, inst1, inst2, subform, quantifier, var, rstr, body ):
    
    pass;
  
  def process_quantification( self, inst1, inst2, subform ):
    
    quantifier_ = self.process_functor( inst1.quantifier, inst2.quantifier );
    
    var_ = self.process_variable( inst1.var, inst2.var );
    
    rstr_ = self.process_scopebearer( inst1.rstr, inst2.rstr );
    
    body_ = self.process_scopebearer( inst1.body, inst2.body );
    
    return self.process_quantification_(
               inst1 = inst1,
               inst2 = inst2,
               subform = subform,
               quantifier = quantifier_,
               var = var_,
               rstr = rstr_,
               body = body_
             );
  
  
  def process_modification_( self, inst1, inst2, subform, modality, args, scope ):
    
    pass;
  
  def process_modification( self, inst1, inst2, subform ):
    
    modality_ = self.process_functor( inst1.modality, inst2.modality );
    
    args_ = [];
    for ( arg1, val1 ) in inst1.args.items():
      args__ = [];
      for ( arg2, val2 ) in inst2.args.items():
        arg_ = self.process_argument( arg1, arg2 );
        val_ = self.process_argument_value( val1, val2 );
        args__.append( (arg_,val_) );
      args_.append( args__ );

    scope_ = self.process_scopebearer( inst.scope );
    
    return self.process_modification_(
               inst1 = inst1,
               inst2 = inst2,
               subform = subform,
               modality = modality_,
               args = args_,
               scope = scope_
             );
  
  
  def process_connection_( self, inst1, inst2, subform, connective, lscope, rscope ):
    
    pass;
  
  def process_connection( self, inst1, inst2, subform ):
    
    connective_ = self.process_functor( inst1.connective, inst2.connective );

    lscope_ = self.process_scopebearer( inst1.lscope, inst2.lscope );
    
    rscope_ = self.process_scopebearer( inst1.rscope, inst2.rscope );
    
    return self.process_connection_(
               inst1 = inst1,
               inst2 = inst2,
               subform = subform,
               connective = connective_,
               lscope = lscope_,
               rscope = rscope_
             );


  def process_handle_( self, inst1, inst2, hid1, hid2 ):
    
    pass;
  
  def process_handle( self, inst1, inst2 ):
    
    return self.process_handle_(
               inst1 = inst1,
               inst2 = inst2,
               hid1 = inst1.hid,
               hid2 = inst2.hid
             );


  def process_subform_( self, inst1, inst2, holes, protoforms ):
    
    pass;

  def process_subform( self, inst1, inst2 ):
    
    holes_ = [];
    for hole1 in inst1.holes:
      holes__ = [];
      for hole2 in inst2.holes:
        hole_ = self.process_handle( hole1, hole2 );
        holes__.append( hole_ );
      holes_.append( holes__ );

    protoforms_ = [];
    for protoform1 in subform1.protoforms:
      protoforms__ = [];
      for protoform2 in subform2.protoforms:
        protoform_ = self.process_subform( protoform1, protoform2 );
        protoforms__.append( protoform_ );
      protoforms_.append( protoforms__ );

    subform_ = self.process_subform_(
                   inst1 = inst1,
                   inst2 = inst2,
                   holes = holes_,
                   protoforms = protoforms_
                 );

    if isinstance( inst1, Predication ):
      assert isinstance( inst2, Predication );
      return self.process_predication( inst1, inst2, subform_ );
    
    if isinstance( inst1, Quantification ):
      assert isinstance( inst2, Quantification );
      return self.process_quantification( inst1, inst2, subform_ );
    
    if isinstance( inst1, Modification ):
      assert isinstance( inst2, Modification );
      return self.process_modification( inst1, inst2, subform_ );
    
    if isinstance( inst1, Connection ):
      assert isinstance( inst2, Connection );
      return self.process_connection( inst1, inst2, subform_ );
    
    if isinstance( inst1, ProtoForm ):
      assert isinstance( inst2, ProtoForm );
      return self.process_protoform( inst1, inst2, subform_ );
    
    try:
      assert False;
    except:
      print( inst1 );
      print( inst2 );
      raise;
  

  def process_constraint_( self, inst1, inst2, harg, larg ):
    
    pass;
  
  def process_constraint( self, inst1, inst2 ):
    
    harg_ = self.process_handle( inst1.harg, inst2.harg );
    larg_ = self.process_handle( inst1.larg, inst2.larg  );

    return self.process_constraint_(
               inst1 = inst1,
               inst2 = inst2,
               harg = harg_,
               larg = larg_
             );
  
  
  def process_protoform_( self, inst1, inst2, subform, subforms, constraints ):
    
    pass;
  
  def process_protoform( self, inst1, inst2, subform ):
    
    subforms_ = [];
    
    for root1 in inst1.roots:
      
      subform1 = inst1.subforms[ root ];
      
      subforms__ = [];
      
      for root2 in inst2.roots:
        
        subform2 = inst2.subforms[ root ];
        
        root_ = self.process_handle( root1, root2 );
        subform_ = self.process_subform( subform1, subform2 );
        
        subforms__.append( (root_, subform_) );
      
      subforms_.append( subforms__ );
    
    constraints_ = [];
    
    for constraint1 in inst1.constraints:
      
      constraints__ = [];
       
      for constraint2 in inst1.constraints:
        
        constraint_ = self.process_constraint( constraint1, constraint2 );
        constraints__.append( constraint_ );
      
      constraints_.append( constraints__ );
    
    return self.process_protoform_(
               inst1 = inst1,
               inst2 = inst2,
               subform = subform,
               subforms = subforms_,
               constraints = constraints_
             );


  def process_scopebearer( self, inst1, inst2 ):
    
    if isinstance( inst1, ProtoForm ):
      assert isinstance( inst2, ProtoForm );
      return self.process_subform( inst1, inst2 );
    
    if isinstance( inst1, Handle ):
      assert isinstance( inst2, Handle );
      return self.process_handle( inst1, inst2 );

    try:
      assert False;
    except:
      print( inst1 );
      print( inst2 );
      raise;


  def compare( self, inst1, inst2 ):
    
    if isinstance( inst1, SubForm ):
      assert isinstance( inst2, SubForm );
      return self.process_subform( inst1, inst2 );
    
    if isinstance( inst1, Constraint ):
      assert isinstance( inst2, Constraint );
      return self.process_constraint( inst1, inst2 );
    
    if isinstance( inst1, Functor ):
      assert isinstance( inst2, Functor );
      return self.process_functor( inst1, inst2 );
    
    if isinstance( inst1, Variable ):
      assert isinstance( inst2, Variable );
      return self.process_variable( inst1 );
    
    if isinstance( inst1, Constant ):
      assert isinstance( inst2, Constant );
      return self.process_constant( inst1, inst2 );
    
    if isinstance( inst1, Sort ):
      assert isinstance( inst2, Sort );
      return self.process_sort( inst1, inst2 );
    
    if isinstance( inst1, Argument ):
      assert isinstance( inst2, Argument );
      return self.process_argument( inst1, inst2 );
    
    if isinstance( inst1, Word ):
      assert isinstance( inst2, Word );
      return self.process_word( inst1, inst2 );
    
    if isinstance( inst1, Operator ):
      assert isinstance( inst2, Operator );
      return self.process_operator( inst1, inst2 );
    
    if isinstance( inst1, Handle ):
      assert isinstance( inst2, Handle );
      return self.process_handle( inst1, inst2 );
    
    try:
      assert False;
    except:
      print( inst1 );
      print( inst2 );
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
