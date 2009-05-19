# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.utils";
__all__ = [ "object_", "subject", "singleton", "kls", "Object" ];

import atexit;
from copy import copy;



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

class Object( metaclass=object_ ):
  
  pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _SubjectCtxMgr( metaclass=object_ ):


  def __init__( self, subj, kwargs ):

    self._subj = subj;
    self._kwargs = kwargs;


  def __enter__( self ):

    self._subj._subject__orig_init( self._subj, **self._kwargs );
    
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


  def __new( cls, obj=None, **kwargs ):

    inst = cls.__orig_new( cls );
    inst.__orig_init = cls.__init__;
    inst.__init__ = lambda *args, **kwargs: None;
    inst._obj_ = obj;
    return _SubjectCtxMgr( inst, kwargs );


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

  
  def __new_outer( cls, **kwargs_outer ):
    
    return \
      lambda **kwargs_inner: cls.__new_inner( kwargs_inner, kwargs_outer );


  def __new_inner( cls, kwargs_inner, kwargs_outer ):
    
    kwargs = {};
    kwargs.update( kwargs_inner );
    kwargs.update( kwargs_outer );
    
    inst = None;

    parent = kwargs_inner.get( cls._superordinate_ );
    
    if parent is None:

      inst = cls.__new_orig( cls );
      inst._init_init_();
      inst.__init__( **kwargs );
      return inst;
      
    if not hasattr( parent, "_sos_" ):
      parent._sos_ = {};
    if not cls in parent._sos_:
      parent._sos_[ cls ] = {};
    
    superordinate = parent._sos_[ cls ];
    
    if cls._key_ is None:

      inst = cls.__new_orig( cls );
      inst._init_init_();
      inst.__init__( **kwargs );
      foundinst = None;
      for inst_ in superordinate.values():
        if inst_ <= inst or inst <= inst_:
          assert foundinst is None;
          foundinst = inst_;
      if foundinst is None:
        superordinate[ id(inst) ] = inst;
      else:
        inst = foundinst;
        inst.__init__( **kwargs );
    
    else:
    
      key = kwargs_outer.get( cls._key_ );
      
      if key is None:
        inst = cls.__new_orig( cls );
        inst._init_init_();
        superordinate[ id(inst) ] = inst;
      elif key in superordinate:
        inst = superordinate[ key ];
      else:
        inst = cls.__new_orig( cls );
        inst._init_init_();
        superordinate[ key ] = inst;
  
      inst.__init__( **kwargs );
      
    return inst;
  
  
  def __getnewargs( self ):
    
    if self._key_ is not None:
      return { self._key_: eval( "self." + self._key_ ) };
    return {};
  
  
  def __getstate( self ):
    
    return copy( self.__dict__ );
  
  
  def __setstate( self, state ):
    
    self.__dict__ = copy( state );
  
  
  def __copy_outer( self ):
    
    state = self.__getstate__();
    kwargs_outer = self.__getnewargs__();
    cls = self.__class__;
    return lambda **kwargs_inner: cls.__copy_inner( state, kwargs_inner, kwargs_outer );
  
  
  def __copy_inner( cls, state, kwargs_inner, kwargs_outer ):
    
    inst_ = cls.__new__( cls, **kwargs_outer );
    inst = inst_( **kwargs_inner );
    inst.__setstate__( state );
    return inst;


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    
    try:
      cls.__del__;
    except AttributeError:
      cls.__del__ = lambda *args, **kwargs: None;
    
    try:
      cls.__new_orig;
    except AttributeError:
      cls.__new_orig = cls.__new__;
      cls.__new__ = kls.__new_outer;
    
    try:
      cls.__new_inner;
    except AttributeError:
      cls.__new_inner = kls.__new_inner;
    
    try:
      cls._init_init_;
    except AttributeError:
      cls._init_init_ = lambda *args, **kwargs: None;
      
    try:
      cls.__getnewargs__;
    except AttributeError:
      cls.__getnewargs__ = kls.__getnewargs;

    try:
      cls.__getstate__;
    except AttributeError:
      cls.__getstate__ = kls.__getstate;

    try:
      cls.__setstate__;
    except AttributeError:
      cls.__setstate__ = kls.__setstate;

    try:
      cls.__copy__;
    except AttributeError:
      cls.__copy__ = kls.__copy_outer;

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
