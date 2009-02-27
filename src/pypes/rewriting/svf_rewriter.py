# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "SVFRewriter", "svf_rewrite" ];

from pypes.utils.mc import subject, Object;

from pypes.proto import *;

from pypes.rewriting.null_rewriter import NullRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _IndexCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_._quantified_vars = set();
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    self._obj_._quantified_vars.add( inst.var );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SVFRewriter( NullRewriter, metaclass=subject ):


  def _enter_( self ):

    self._index = Object();
    with _IndexCollector( self._index ) as coll:
      coll.process( self._obj_ );
    
    print( self._index._quantified_vars );
  
  
  def _process_predication( self, inst, predicate, args ):
    
    const_args = {};
    var_args = {};
    
    for (arg,val) in inst.args.items():
      arg_ = self.process_argument( arg );
      if isinstance( val, Constant ):
        const_args[ arg_ ] = self.process_constant( val );
        continue;
      if val not in self._index._quantified_vars:
        #ident = str(val.sort.sid) + str(val.vid);
        #const_args[ arg_ ] = Constant( ident = ident );
        continue;
      var_args[ arg_ ] = self.process_variable( val );
    
    args_ = const_args;
    args_.update( var_args );
    return Predication(
               predicate = predicate,
               args = args_
             );


  def rewrite( self ):
    
    return self.process( self._obj_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def svf_rewrite( obj ):
  
  rslt = None;
  with SVFRewriter( obj ) as rewriter:
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
