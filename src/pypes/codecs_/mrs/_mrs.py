# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRSVariable", "MRSConstant", "MRSElementaryPredication",
            "MRSConstraint", "MRS" ];

import string;

from pypes.utils.mc import subject, object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSVariable( metaclass=object_ ):
  
  def __init__( self ):
    
    self.sid = None;
    self.vid = None;
    self.feats = {};
  
  def __repr__( self ):
    
    return str(self.sid) + str(self.vid) + str(self.feats);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSConstant( metaclass=object_ ):
  
  def __init__( self ):
    
    self.constant = None;
  
  def __repr__( self ):
    
    return self.constant;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSElementaryPredication( metaclass=object_ ):

  def __init__( self ):
    
    self.lid = None;
    self.pred = None;
    self.args = {};
    self.cfrom = None;
    self.cto = None;
  
  def __repr__( self ):
    
    return \
        str(self.lid) + "\n" + \
        str(self.pred) + "\n" + \
        str(self.cfrom) + "\n" + \
        str(self.cto) + "\n" + \
        str(self.args).replace( ",", ",\n  " ) + "\n";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSConstraint( metaclass=object_ ):

  def __init__( self ):
    
    self.hi = None;
    self.lo = None;
    
  def __repr__( self ):
    
    return str(self.hi) + " qeq " + str(self.lo);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRS( metaclass=object_ ):
  
  def __init__( self ):
    
    self.eps = [];
    self.cons = [];
  
  def __str__( self ):
    
    return str( self.eps ) + str( self.cons );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
