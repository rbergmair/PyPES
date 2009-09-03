# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "CopulaResolver", "resolve_copula" ];

from pprint import pprint;

from pypes.utils.mc import subject, object_;

from pypes.proto import ProtoProcessor, Operator;

from pypes.rewriting.renamer import rename;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class CopulaResolver( metaclass=subject ):
  
  
  class _IndexCollector( ProtoProcessor, metaclass=subject ):


    def __init__( self ):

      self._quants = set();

  
    def process_predication_( self, inst, subform, predicate, args ):
      
      if not isinstance( inst.predicate.referent, Operator ):
        return;
      
      if inst.predicate.referent.otype != Operator.OP_P_COPULA:
        return;
      
      var1 = None;
      var2 = None;
      
      for (arg,var) in inst.args.items():
        if ( arg.aid == "arg1" ) or ( arg.aid == "ARG1" ):
          assert var.sort.sid == "x";
          var1 = var;
        if ( arg.aid == "arg2" ) or ( arg.aid == "ARG2" ):
          assert var.sort.sid == "x";
          var2 = var;

      self._obj_._vars_by_copula[ inst ] = (var1,var2);

      
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
  
      if not isinstance( inst.quantifier.referent, Operator ):
        return;
      
      self._obj_._quant_by_var[ inst.var ] = inst;
      self._quants.add( inst );
    
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      for (root,subform) in inst.subforms.items():
          self._obj_._subform_by_root[ root ] = subform;
      
      for cons in inst.constraints:
        self._obj_._lo_by_hi[ cons.harg ] = cons.larg;
  
  
  class _Substituter( ProtoProcessor, metaclass=subject ):

    
    def _process_args( self, args ):
      
      for arg in args:
        var = args[ arg ];
        if var in self._obj_._newvar_by_oldvar:
          args[ arg ] = self._obj_._newvar_by_oldvar[ var ];

    
    def process_predication_( self, inst, subform, predicate, args ):
      
      self._process_args( inst.args );
    
    
    def process_modification_( self, inst, subform, modality, args, scope ):
      
      self._process_args( inst.args );
    
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      for root in set( inst.subforms.keys() ):
        
        subform = inst.subforms[ root ];
        
        if subform in self._obj_._newsubform_by_oldsubform:
          inst.subforms[ root ] = self._obj_._newsubform_by_oldsubform[ subform ];
          continue;
        
        if subform in self._obj_._removable_subforms:
          inst.roots.remove( root );
          del inst.subforms[ root ];
      
      for cons in set( inst.constraints ):
        if cons.harg in self._obj_._removable_holes:
          inst.constraints.remove( cons );
          continue;
  
  
  def resolve( self, pf ):
    
    pf = rename( pf, force_rename_handles_p=True );

    self._vars_by_copula = {};
    self._quant_by_var = {};
    self._subform_by_root = {};
    self._lo_by_hi = {};
    
    with self._IndexCollector( self ) as idxcol:
      idxcol.process( pf );
    
    self._newvar_by_oldvar = {};
    self._newsubform_by_oldsubform = {};
    self._removable_subforms = set();
    self._removable_holes = set();
    
    vars = set();
    
    for ( cpsf, (var1,var2) ) in self._vars_by_copula.items():
      
      if var1 not in self._quant_by_var:
        continue;
      if var2 not in self._quant_by_var:
        continue;
      
      quant1 = self._quant_by_var[ var1 ];
      quant2 = self._quant_by_var[ var2 ];
      
      assert var1 not in vars;
      assert var2 not in vars;
      vars.add( var1 );
      vars.add( var2 );

      assert isinstance( quant1.quantifier.referent, Operator );
      q1 = quant1.quantifier.referent.otype;

      assert isinstance( quant2.quantifier.referent, Operator );
      q2 = quant2.quantifier.referent.otype;
      
      qhi = None;
      qlo = None;
      
      if q1 == Operator.OP_Q_EXIST:
        
        if q2 == Operator.OP_Q_EXIST:
          qhi = quant1;
          qlo = quant2;
          
        elif q2 == Operator.OP_Q_DESCR:
          qhi = quant2;
          qlo = quant1;
          
      elif q1 == Operator.OP_Q_DESCR:
        
        if q2 == Operator.OP_Q_EXIST:
          qhi = quant1;
          qlo = quant2;
          
        elif q2 == Operator.OP_Q_DESCR:
          qhi = quant2;
          qlo = quant1;

      elif q1 == Operator.OP_Q_UNIV:

        if q2 == Operator.OP_Q_EXIST:
          qhi = quant1;
          qlo = quant2;

        elif q2 == Operator.OP_Q_DESCR:
          qhi = quant2;
          qlo = quant1;
      
      if qhi is None or qlo is None:
        continue;
      
      if qhi.rstr.hid is None or qhi.body.hid is not None:
        continue;
      
      if qlo.rstr.hid is None or qlo.body.hid is not None:
        continue;
        
      rstrsubf = self._subform_by_root[ self._lo_by_hi[ qlo.rstr ] ];
      self._newvar_by_oldvar[ qlo.var ] = qhi.var;
      self._newsubform_by_oldsubform[ cpsf ] = rstrsubf;
      self._removable_subforms.add( qlo );
      self._removable_subforms.add( rstrsubf );
      self._removable_holes.add( qlo.rstr );
      
    with self._Substituter( self ) as subst: 
      subst.process( pf );
    
    return pf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def resolve_copula( obj ):
  
  rslt = None;
  with CopulaResolver() as cpres:
    rslt = cpres.resolve( obj );
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
