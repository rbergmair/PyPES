# -*-  coding: ascii -*-

__package__ = "pypes.utils";
__all__ = [ "object_", "subject", "singleton", "kls" ];

import atexit;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class object_( type ):


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    
    try:
      cls.__del__;
    except AttributeError:
      cls.__del__ = lambda *args, **kwargs: None;
      
    return cls;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _SubjectCtxMgr( metaclass=object_ ):


  def __init__( self, subj ):

    self._subj = subj;


  def __enter__( self ):

    self._subj._subject__orig_init( self._subj );
    
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


  def __new( cls, obj=None ):

    inst = cls.__orig_new( cls );
    inst.__orig_init = cls.__init__;
    inst.__init__ = lambda *args, **kwargs: None;
    inst._obj_ = obj;
    return _SubjectCtxMgr( inst );


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    
    try:
      cls.__del__;
    except AttributeError:
      cls.__del__ = lambda *args, **kwargs: None;
      
    try:
      cls.__orig_new;
    except AttributeError:
      cls.__orig_new = cls.__new__;
      cls.__new__ = subject.__new;
      
    return cls;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class singleton( type ):


  def __new( cls, *args, **kwargs ):

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
    
    try:
      cls.__del__;
    except AttributeError:
      cls.__del__ = lambda *args, **kwargs: None;
      
    cls.__instance = None;
    try:
      cls.__orig_new;
    except AttributeError:
      cls.__orig_new = cls.__new__;
      cls.__new__ = singleton.__new;
      
    return cls;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class kls( type ):

  
  def __new( cls, **kwargs_outer ):
    
    return \
      lambda **kwargs_inner: cls.__new_2__( cls, kwargs_inner, kwargs_outer );


  def __new_2( cls, kwargs_inner, kwargs_outer ):
    
    kwargs = kwargs_inner;
    kwargs.update( kwargs_outer );
    
    inst = None;

    parent = kwargs_inner.get( cls._superordinate_ );
    
    if parent is None:

      inst = cls.__orig_new( cls );
      inst._init_init_();
      
    else:
      
      try:
        parent._sos_;
      except AttributeError:
        parent._sos_ = {};
      if not cls in parent._sos_:
        parent._sos_[ cls ] = {};
      
      superordinate = parent._sos_[ cls ];
      
      key = kwargs_outer.get( cls._key_ );
      
      if key is None:
        inst = cls.__orig_new( cls );
        inst._init_init_();
        superordinate[ id(inst) ] = inst;
      elif key in superordinate:
        inst = superordinate[ key ];
      else:
        inst = cls.__orig_new( cls );
        inst._init_init_();
        superordinate[ key ] = inst;
    
    inst.__init__( **kwargs );
    return inst;


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );

    try:
      cls.__del__;
    except AttributeError:
      cls.__del__ = lambda *args, **kwargs: None;
    
    try:
      cls.__orig_new;
    except AttributeError:
      cls.__orig_new = cls.__new__;
      cls.__new__ = kls.__new;

    try:
      cls.__new_2__;
    except AttributeError:
      cls.__new_2__ = kls.__new_2;
      
    try:
      cls._init_init_;
    except AttributeError:
      cls._init_init_ = lambda *args, **kwargs: None;

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
