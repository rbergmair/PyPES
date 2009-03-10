# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "DSFRewriter", "dsf_rewrite" ];

from pypes.utils.mc import subject, Object;

from pypes.proto import *;

from pypes.rewriting.null_rewriter import NullRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _IndexCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_._quantified_vars = [];
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    if not inst.var in self._obj_._quantified_vars:
      self._obj_._quantified_vars.append( inst.var );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DSFRewriter( NullRewriter, metaclass=subject ):


  def _enter_( self ):

    self._index = Object();
    with _IndexCollector( self._index ) as coll:
      coll.process( self._obj_ );

    # print( self._index._quantified_vars );
  
  
  def _filter_args( self, args ):

    args_ = {};
    var_arg = None;
    var_var = None;
    
    for (arg,val) in args.items():
      arg_ = self.process_argument( arg );
      if isinstance( val, Constant ):
        args_[ arg_ ] = self.process_constant( val );
      elif val is self._active_variable:
        var_arg = arg_;
        var_var = self.process_variable( val );
    
    return ( args_, var_arg, var_var  );
  
  
  def _process_predication( self, inst, predicate, args ):
    
    ( args_, var_arg, var_var ) = self._filter_args( inst.args );
    
    if var_var is None:
      return None;
    
    args_[ var_arg ] = var_var;

    return inst.__class__(
               predicate = predicate,
               args = args_
             );
  
  
  def _visit_hole( self, hndl, lvl ):
    
    if isinstance( hndl, Handle ):
      self._visited_holes[ lvl-1 ].add( hndl );
    
    elif isinstance( hndl, Freezer ):
      self._visit_hole( hndl.content, lvl-1 );
  
  
  def _process_modification( self, inst, modality, args, scope ):
    
    ( args_, var_arg, var_var ) = self._filter_args( inst.args );
    
    if var_var is None:
      return None;
    
    self._visit_hole( inst.scope, 0 );
    
    args_[ var_arg ] = var_var;

    return inst.__class__(
               modality = modality,
               args = args_,
               scope = scope
             );
  
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    if inst.var is not self._active_variable:
      return None;
    
    self._visit_hole( inst.rstr, 0 );
    self._visit_hole( inst.body, 0 );

    return inst.__class__(
              quantifier = quantifier,
              var = var,
              rstr = rstr,
              body = body
            );
  
  
  def _is_filler_conjunction( self, conn ):
    
    if not isinstance( conn, Connection ):
      return False;
    if not isinstance( conn.connective.referent, Operator ):
      return False;
    if not conn.connective.referent.otype is Operator.OP_C_WEACON:
      return False;
    if not isinstance( conn.lscope, Handle ):
      return False;
    if conn.lscope.hid is not None:
      return False;
    if not isinstance( conn.rscope, Handle ):
      return False;
    if conn.rscope.hid is not None:
      return False;
    return True;
  
  
  def _process_connection( self, inst, connective, lscope, rscope ):
    
    if self._is_filler_conjunction( inst ):
      return None;
    
    self._visit_hole( inst.lscope, 0 );
    self._visit_hole( inst.rscope, 0 );
    
    return inst.__class__(
               connective = connective,
               lscope = lscope,
               rscope = rscope
             );
            
            
  def _process_protoform( self, inst, subforms, constraints ):
    
    subforms_ = [];
    
    holes = self._visited_holes.pop();
    roots = set();
    
    for ( (root,subform), (root_,subform_) ) in zip( inst.subforms, subforms ):
      if subform_ is not None:
        roots.add( root );
        subforms_.append( (root_,subform_) );
    
    if len( subforms_ ) == 0:
      return None;
    
    i = 0;
    added = 0;
    while True:
      if i >= len( subforms_ ):
        break;
      if len(holes) + added + 1 < len(roots):
        subforms_.insert( i+1,
            ( Handle(),
                Connection(
                    connective = Connective(
                                     referent = Operator(
                                                    otype = Operator.OP_C_WEACON
                                                  )
                                   ),
                    lscope = Handle(),
                    rscope = Handle(),
                  ) )
          );
        added += 1;
        i += 1;
      i += 1;
    
    #for hole in holes:
    #  print( hole.hid );
    #print( "--" );
    
    constraints_ = [];
    
    for ( constraint, constraint_ ) in zip( inst.constraints, constraints ):
      if constraint.harg in holes and constraint.larg in roots:
        constraints_.append( constraint_ );
    
    return inst.__class__(
               subforms = subforms_,
               constraints = constraints_
            );


  def process_protoform( self, inst ):
    
    self._visited_holes.append( set() );
    return super().process_protoform( inst );
    
      
  def rewrite( self ):
    
    for var in self._index._quantified_vars:
      self._visited_holes = [];
      self._active_variable = var;
      return self.process( self._obj_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def dsf_rewrite( obj ):
  
  rslt = None;
  with DSFRewriter( obj ) as rewriter:
    rslt = rewriter.rewrite();
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
