# -*-  coding: ascii -*-

__package__ = "pyrbutils";

from string import digits;
from string import ascii_lowercase;

import random;

from socket import gethostname;

from time import time;
from time import strftime;

from pyrbutils.mc import RBSingleton;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBIDController( metaclass=RBSingleton ):

  def get_current_timestamp( self ):

    return "{0}-{1}-{2}-{3}{4}".format(
        strftime( "%y%m%d-%H%M%S" ),
        str( int( ( time() % 1.0 ) * 1000.0 ) ).zfill( 3 ),
        gethostname(),
        random.choice( digits + ascii_lowercase ),
        random.choice( digits + ascii_lowercase )
      );

  def __init__( self ):

    self._insttok = self.get_current_timestamp();
    self._runningno = 10239;

  @property
  def insttok( self ):
    return self._insttok;

  def get_guid( self ):

    self._runningno += 1;
    return "{0}-{1}".format( self.insttok, self.get_current_timestamp() );

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
