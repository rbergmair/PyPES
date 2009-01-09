# -*-  coding: ascii -*-

__package__ = "pypes.utils";

import atexit;

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _SubjectCtxMgr:

  def __init__( self, subj ):

    self._subj = subj;

  def __enter__( self ):

    self._subj._subject__orig_init();
    enter = None;
    try:
      enter = self._subj._enter_;
    except AttributeError:
      pass;
    if enter is not None:
      enter();
    return self._subj;

  def __exit__( self, exc_type, exc_val, exc_tb ):

    rslt = False;
    exit = None;
    try:
      exit = self._subj._exit_;
    except AttributeError:
      pass;
    if exit is not None:
      rslt = exit( exc_type, exc_val, exc_tb );
    self._subj._obj_ = None;
    self._subj = None;
    return rslt;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class subject( type ):

  def __subject_new( cls, obj=None ):

    subject = cls._subject__orig_new( cls );
    subject._subject__orig_init = subject.__init__;
    subject.__init__ = lambda *args, **kwargs: None;
    subject._obj_ = obj;
    return _SubjectCtxMgr( subject );

  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    try:
      cls._subject__orig_new;
    except AttributeError:
      cls._subject__orig_new = cls.__new__;
      cls.__new__ = subject.__subject_new;
    return cls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class singleton( type ):


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
    cls.__new__ = singleton.__singleton_new;

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
