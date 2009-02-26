# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewrite";
__all__ = [ "DSFRewriter" ];

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DSFRewriter( metaclass=subject ):


  def _enter_( self ):

    self._sig = ProtoSig();
    self._pf = self._obj_( sig=self._sig );


  def _collect_subforms_by_var( self, pf ):

    for subf in pf.subforms.values():

      if isinstance( subf, Predication ):

        for arg in subf.args.values():
          if isinstance( arg, Variable ):
            if not arg in self._subforms_by_var:
              self._subforms_by_var[ arg ] = set();
            self._subforms_by_var[ arg ].add( subf );

      elif isinstance( subf, Modification ):

        for arg in subf.args.values():
          if isinstance( arg, Variable ):
            if not arg in self._subforms_by_var:
              self._subforms_by_var[ arg ] = set();
            self._subforms_by_var[ arg ].add( subf );

        self._collect_subforms_by_var( subf.scope );

      elif isinstance( subf, Quantification ):

        self._collect_subforms_by_var( subf.rstr );
        self._collect_subforms_by_var( subf.body );

      elif isinstance( subf, Connection ):

        self._collect_subforms_by_var( subf.lscope );
        self._collect_subforms_by_var( subf.rscope );


  def rewrite( self ):

    self._subforms_by_var = {};
    self._collect_subforms_by_var( self._pf );
    self._subform_quant = [];

    for var in self._sig._sos_[ Variable ].values():

      quant = [];

      for subf in self._subforms_by_var[ var ]:
        if isinstance( subf, Quantification ):
          pass;

      assert len( quant ) == 1;

      for subf in self._subforms_by_var

      

    
  



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
