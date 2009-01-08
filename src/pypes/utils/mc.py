# -*-  coding: ascii -*-

__package__ = "pypes.utils";

import atexit;

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SubjectCtxMgr:

  def __init__( self, subj ):

    self._subj = subj;

  def __enter__( self ):

    self._subj._Subject__orig_init( self._subj );
    enter = None;
    try:
      enter = self._subj._enter_;
    except AttributeError:
      pass;
    if enter is not None:
      enter( self._subj );
    return self._subj;

  def __exit__( self, exc_type, exc_val, exc_tb ):

    rslt = False;
    exit = None;
    try:
      exit = self._subj._exit_;
    except AttributeError:
      pass;
    if exit is not None:
      rslt = exit( self._subj, exc_type, exc_val, exc_tb );
    self._subj._obj_ = None;
    self._subj = None;
    return rslt;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Subject( type ):

  def __subject_new( cls, obj=None ):

    subject = cls.__orig_new( cls );
    subject.__orig_init = cls.__init__;
    subject.__init__ = lambda *args, **kwargs: None;
    subject._obj_ = obj;
    return SubjectCtxMgr( subject );

  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    cls.__orig_new = cls.__new__;
    cls.__new__ = Subject.__subject_new;
    return cls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Singleton( type ):


  def __singleton_new( cls, *args, **kwargs ):

    if cls.__instance is None:

      cls.__instance = cls.__orig_new( cls, *args, **kwargs );
      cls.__orig_init = cls.__init__;
      onexit = None;
      try:
        onexit = cls.__instance._on_exit_;
      except AttributeError:
        pass;
      if not onexit is None:
        atexit.register( onexit );

    elif cls.__init__ == cls.__orig_init:

      cls.__init__ = lambda *xargs, **xkwargs: None; 

    return cls.__instance;


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    cls.__instance = None;
    cls.__orig_new = cls.__new__;
    cls.__new__ = Singleton.__singleton_new;

    return cls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
