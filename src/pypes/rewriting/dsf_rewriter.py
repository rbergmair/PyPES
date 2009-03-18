# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "DSFRewriter", "dsf_rewrite" ];

from pypes.utils.mc import subject, Object;
from pypes.proto import *;
from pypes.scoping import *;
from pypes.rewriting.null_rewriter import NullRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _MySolver( Solver, metaclass=subject ):
  
  def _apply_cuts( self ):
    
    contains_connections = False;
    contains_quantifications = False;
    
    idx = self._domcon.solution.cur_component;
    splits = self._domcon.solution.chart[ idx ];
    
    roots = set( splits.keys() );
    
    for root in roots:
      subform = self._obj_.subforms[ root ];
      if isinstance( subform, Connection ):
        contains_connections = True;
        break;
      elif isinstance( subform, Quantification ):
        contains_quantifications = True;
    
    for root in roots:
      subform = self._obj_.subforms[ root ];
      # print( subform );
      if contains_connections and not isinstance( subform, Connection ):
        # print( "!" );
        del splits[ root ];
      elif contains_quantifications and not isinstance( subform, Quantification ):
        # print( "!!" );
        del splits[ root ];



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DSFRewriter( NullRewriter, metaclass=subject ):

  def _enter_( self ):
    
    self._orig = self._obj_;
    with _MySolver( self._orig ) as solver:
      solution = solver.solve_all();
      self._obj_ = recursivize( solution );



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
