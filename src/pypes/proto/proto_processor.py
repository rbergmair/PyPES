# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "ProtoProcessor" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ProtoProcessor( metaclass=subject ):
  
  
  def process( self, proto ):
    
    if isinstance( proto, SubForm ):
      return self.process_subform( proto );
    if isinstance( proto, Constraint ):
      return self.process_constraint( proto );
    if isinstance( proto, Predicate ):
      return self.process_predicate( proto );
    if isinstance( proto, Quantifier ):
      return self.process_quantifier( proto );
    if isinstance( proto, Modality ):
      return self.process_modality( proto );
    if isinstance( proto, Connective ):
      return self.process_connective( proto );
    if isinstance( proto, Variable ):
      return self.process_variable( proto );
    if isinstance( proto, Constant ):
      return self.process_constant( proto );
    if isinstance( proto, Sort ):
      return self.process_sort( proto );
    if isinstance( proto, Argument ):
      return self.process_argument( proto );
    if isinstance( proto, Word ):
      return self.process_word( proto );
    if isinstance( proto, Operator ):
      return self.process_operator( proto );
    if isinstance( proto, Handle ):
      return self.process_handle( proto );
    try:
      assert False;
    except:
      print( proto );
      raise;


  def _process_subform( self, inst, holes ):
    
    pass;


  def process_subform( self, subform, global_holes=None ):

    if global_holes is None:
      global_holes = {};
    for hole in subform.holes:
      global_holes[ hole ] = 0;
      
    subform_ = self._process_subform( subform, subform.holes );

    if isinstance( subform, Predication ):
      return self.process_predication( subform, subform_, global_holes );
    if isinstance( subform, Quantification ):
      return self.process_quantification( subform, subform_, global_holes );
    if isinstance( subform, Modification ):
      return self.process_modification( subform, subform_, global_holes );
    if isinstance( subform, Connection ):
      return self.process_connection( subform, subform_, global_holes );
    if isinstance( subform, ProtoForm ):
      return self.process_protoform( subform, subform_, global_holes );
    assert False;
  
  
  def _process_freezer( self, content, freezelevel ):
    
    pass;
  
  def process_freezer( self, handle, freezelevel ):
    
    if freezelevel == -1:
      return self._process_handle( handle, handle.hid );
    else:
      return self._process_freezer(
                 self.process_freezer( handle, freezelevel-1 ),
                 freezelevel
               );
  
  
  def process_scopebearer( self, inst, global_holes ):
    
    if isinstance( inst, ProtoForm ):
      return self.process_subform( inst, global_holes );
    elif isinstance( inst, Handle ):
      return self.process_freezer( inst, global_holes[ inst ] );


  def _process_predication( self, inst, subform, predicate, args ):
    
    pass;
  
  def process_predication( self, inst, subform, global_holes=None ):
    
    predicate_ = self.process_predicate( inst.predicate );
    
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
  
  def process_quantification( self, inst, subform, global_holes=None ):
    
    quantifier_ = self.process_quantifier( inst.quantifier );
    
    var_ = self.process_variable( inst.var );
    
    rstr_ = self.process_scopebearer( inst.rstr, global_holes );
    
    body_ = self.process_scopebearer( inst.body, global_holes );
    
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
  
  def process_modification( self, inst, subform, global_holes=None ):
    
    modality_ = self.process_modality( inst.modality );
    
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

    scope_ = self.process_scopebearer( inst.scope, global_holes );
    
    return self._process_modification(
               inst = inst,
               subform = subform,
               modality = modality_,
               args = args_,
               scope = scope_
             );
  
  
  def _process_connection( self, inst, subform, connective, lscope, rscope ):
    
    pass;
  
  def process_connection( self, inst, subform, global_holes=None ):
    
    connective_ = self.process_connective( inst.connective );

    lscope_ = self.process_scopebearer( inst.lscope, global_holes );
    
    rscope_ = self.process_scopebearer( inst.rscope, global_holes );
    
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
  
  def process_protoform( self, inst, subform, global_holes=None ):
    
    global_holes_ = {};
    if global_holes is not None:
      for ( hole, freezelevel ) in global_holes.items():
        global_holes_[ hole ] = freezelevel+1;
    for hole in inst.holes:
      global_holes_[ hole ] = 1;
    
    subforms_ = [];
    
    for root in inst.roots:
      
      subform__ = inst.subforms[ root ];
      root_ = self.process_handle( root );
      
      if isinstance( subform__, SubForm ):
        subform_ = self.process_subform( subform__, global_holes_ );
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
    
    return self._process_protoform(
               inst = inst,
               subform = subform,
               subforms = subforms_,
               constraints = constraints_
             );
  
  
  def _process_predicate( self, inst, referent ):
    
    pass;
  
  def process_predicate( self, inst ):
    
    if isinstance( inst.referent, Word ):
      referent_ = self.process_word( inst.referent );
    elif isinstance( inst.referent, Operator ):
      referent_ = self.process_operator( inst.referent );
    
    return self._process_predicate(
               inst = inst,
               referent = referent_
            );
  
  
  def _process_quantifier( self, inst, referent ):
    
    pass;
  
  def process_quantifier( self, inst ):
    
    if isinstance( inst.referent, Word ):
      referent_ = self.process_word( inst.referent );
    elif isinstance( inst.referent, Operator ):
      referent_ = self.process_operator( inst.referent );
    
    return self._process_quantifier(
               inst = inst,
               referent = referent_
            );
  
  
  def _process_modality( self, inst, referent ):
    
    pass;
  
  def process_modality( self, inst ):
    
    if isinstance( inst.referent, Word ):
      referent_ = self.process_word( inst.referent );
    elif isinstance( inst.referent, Operator ):
      referent_ = self.process_operator( inst.referent );
    
    return self._process_modality(
               inst = inst,
               referent = referent_
            );
  
  
  def _process_connective( self, inst, referent ):
    
    pass;
  
  def process_connective( self, inst ):
    
    if isinstance( inst.referent, Word ):
      referent_ = self.process_word( inst.referent );
    elif isinstance( inst.referent, Operator ):
      referent_ = self.process_operator( inst.referent );
    
    return self._process_connective(
               inst = inst,
               referent = referent_
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
  
  
  def _process_word( self, inst, wid, lemma, pos, sense, feats ):
    
    pass;
  
  def process_word( self, inst ):
    
    return self._process_word(
               inst = inst,
               wid = inst.wid,
               lemma = inst.lemma,
               pos = inst.pos,
               sense = inst.sense,
               feats = inst.feats
             );
  
  
  def _process_operator( self, inst, otype, feats ):
    
    pass;
  
  def process_operator( self, inst ):
    
    return self._process_operator(
               inst = inst,
               otype = inst.otype,
               feats = inst.feats
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
