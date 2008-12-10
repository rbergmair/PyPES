# -*-  coding: ascii -*-

import sys;

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBObject( object ):

  def __new__( cls, *args, **kargs ):

    inst = object.__new__( cls );
    return inst;

  def __init__( self ):

    pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBSubject( object ):

  def __new__( cls, *args, **kargs ):

    subject = object.__new__( cls );
    return subject.run( *args, **kargs );

  def __init__( self ):

    assert False;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Eat( RBSubject ):


  def run( self, inst ):

    if isinstance( inst, Apple ):
      assert inst.apple;
      assert not inst.banana;

    if isinstance( inst, Banana ):
      assert inst.banana;
      assert not inst.apple;

    inst.eaten = True;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Apple( RBObject ):

  def __init__( self ):

    RBObject.__init__( self );
    self.eaten = False;
    self.apple = True;
    self.banana = False;
    self.eat = lambda: Eat( self );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Banana( RBObject ):

  def __init__( self ):

    RBObject.__init__( self );
    self.eaten = False;
    self.apple = False;
    self.banana = True;
    self.eat = lambda: Eat( self );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=[] ):

  apple = Apple();
  banana = Banana();
  assert not apple.eaten;
  assert not banana.eaten;
  apple.eat();
  banana.eat();
  assert apple.eaten;
  assert banana.eaten;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
  sys.exit( main( sys.argv ) );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
