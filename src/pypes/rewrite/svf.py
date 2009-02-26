# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewrite";
__all__ = [ "SVFRewriter" ];

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SVFRewriter( metaclass=subject ):


  def _enter_( self ):

    self._sig = ProtoSig();
    self._pf = self._obj_( sig=self._sig );
    self._quantified_vars = set();
    self._collect_quantified_vars( self._pf );


  def _collect_quantified_vars( self, form ):

    if isinstance( form, Modification ):

      self._collect_quantified_vars( form.scope );

    elif isinstance( form, Quantification ):
      
      self._quantified_vars.add( form.var );

      self._collect_quantified_vars( form.rstr );
      self._collect_quantified_vars( form.body );

    elif isinstance( form, Connection ):

      self._collect_quantified_vars( form.lscope );
      self._collect_quantified_vars( form.rscope );
    
    elif isinstance( form, ProtoForm ):
      
      for ( root, subf ) in form.subforms:
        self._collect_quantified_vars( subf );
  
  
  def _rewrite( self, form ):
    
    


  def rewrite( self ):

    return self._rewrite( self._pf );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
