# -*-  coding: ascii -*-

__package__ = "pypes.utils";

import atexit;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _SubjectCtxMgr:

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
    
    pname = None;
    pval = None;
    for argname in kwargs_inner:
      if "_p_"+argname+"_" in cls.__dict__:
        pname = argname;
        pval = kwargs_inner[ argname ];

    kwargs = kwargs_inner;
    kwargs.update( kwargs_outer );
    
    inst = None;
    
    if pname is None or pval is None:

      inst = cls.__orig_new( cls );
      
    else:
      
      try:
        pval._sos_;
      except AttributeError:
        pval._sos_ = {};
      if not cls in pval._sos_:
        pval._sos_[ cls ] = {};
      
      superordinate = pval._sos_[ cls ];
      
      keyname = None;
      keyval = None;
      for kwargname in kwargs_outer:
        if "_k_"+kwargname+"_" in cls.__dict__:
          keyname = kwargname;
          keyval = kwargs_outer[ keyname ];
      
      if keyval is None:
        inst = cls.__orig_new( cls );
        superordinate[ id(inst) ] = inst;
      elif keyval in superordinate:
        inst = superordinate[ keyval ];
      else:
        inst = cls.__orig_new( cls );
        superordinate[ keyval ] = inst;
    
    inst.__init__( **kwargs );
    return inst;


  def __init( self, **kwargs ):
    
    self.__orig_init( **kwargs );
    

  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    
    try:
      cls.__orig_new;
    except AttributeError:
      cls.__orig_new = cls.__new__;
      cls.__new__ = kls.__new;
      
    try:
      cls.__orig_init;
    except AttributeError:
      cls.__orig_init = cls.__init__;
      cls.__init__ = kls.__init;

    try:
      cls.__new_2__;
    except AttributeError:
      cls.__new_2__ = kls.__new_2;

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
