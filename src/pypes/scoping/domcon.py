# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "DomCon", "DomConSolution" ];

from pypes.utils.mc import object_;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DomConSolution( metaclass=object_ ):
  
  def __init__( self ):
    
    self.domcon = None;
    self.chart_index = [];
    self.chart = [];
    self.cur_component = None;
    self.cur_root = None;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DomCon( metaclass=object_ ):
  
  def __init__( self ):
    
    self.pf = None;
    self.cons = None;
    self.cons_inv = None;
    self.fragments = None;
    self.fragments_inv = None;
    
  def _get_root( self, rt ):
    
    if rt in self.fragments:
      return rt;
    if rt in self.fragments_inv:
      return self.fragments_inv[ rt ];
    try:
      return None;
    except:
      print( rt );
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
