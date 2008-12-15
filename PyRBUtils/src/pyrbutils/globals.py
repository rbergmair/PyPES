# -*-  coding: ascii -*-

__package__ = "pyrbutils";

from string import digits;
from string import ascii_lowercase;

import random;

from socket import gethostname;

from time import time;
from time import strftime;

from pyrbutils.rbmc import RBSingleton;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBIDController( metaclass=RBSingleton ):


  def get_timestamp( self ):

    return "{0}-{1}".format(
        strftime( "%y%m%d-%H%M%S" ),
        str( int( ( time() % 1.0 ) * 1000.0 ) ).zfill( 3 )
      );


  def __init__( self ):

    self._runningno = 10239;
    self._insttok = "{0}-{1}-{2}{3}".format(
        self.get_timestamp(),
        gethostname(),
        random.choice( digits + ascii_lowercase ),
        random.choice( digits + ascii_lowercase )
      );


  @property
  def insttok( self ):
    return self._insttok;


  def get_guid( self ):

    return "{0}-{1}-{2}{3}".format(
        self.insttok,
        self.get_timestamp(),
        random.choice( digits + ascii_lowercase ),
        random.choice( digits + ascii_lowercase )
      );


  def get_runningno( self ):

    self._runningno += 1;
    return self._runningno;


RBIDController();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
