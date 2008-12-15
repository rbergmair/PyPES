# -*-  coding: ascii -*-

__package__ = "pyrbutils";


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBSubject( type ):

  def __subject_new( cls, *args, **kwargs ):

    subject = object.__new__( cls );
    return subject.run( *args, **kwargs );

  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    cls.__new__ = RBSubject.__subject_new;
    return cls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBSingleton( type ):


  def __singleton_new( cls, *args, **kwargs ):

    if cls.__instance is None:

      cls.__instance = cls.__orig_new( cls, *args, **kwargs );
      cls.__orig_init = cls.__init__;

    elif cls.__init__ == cls.__orig_init:

      #def __nothing( *args, **kwargs ):
      #  pass;

      cls.__init__ = lambda *args, **kwargs: None; 

    return cls.__instance;


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    cls.__instance = None;
    cls.__orig_new = cls.__new__;
    cls.__new__ = RBSingleton.__singleton_new;

    return cls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
