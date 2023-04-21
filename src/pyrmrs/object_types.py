class GenericObject( object ):
  
  def _init_1( self ):
    
    pass;
  
  def _init_2( self ):
    
    pass;

  def _init_3( self ):
    
    pass;

  def _init( self ):
    
    pass;

  def __init__( self ):
    
    self._init_1();
    self._init_2();
    self._init();



class SingletonObject( GenericObject ):
  
  _instances = {};
  
  def __new__( cls, *args, **kargs ):
    
    if not SingletonObject._instances.has_key( cls ):
      SingletonObject._instances[ cls ] = GenericObject.__new__( cls, *args, **kargs );
      SingletonObject._instances[ cls ]._init_1();
      SingletonObject._instances[ cls ]._init_2();
      SingletonObject._instances[ cls ]._init_3();
      SingletonObject._instances[ cls ]._init();
      
    return SingletonObject._instances[ cls ];
  
  def __init__( self ):
    
    pass;
  

  
class Borg( SingletonObject ):
  
  UNIMATRIX_ONE = 1;
  UNIMATRIX_TWO = 2;
  UNIMATRIX_THREE = 3;
  UNIMATRIX_FOUR = 4;
  UNIMATRIX_FIVE = 5;
  UNIMATRIX_SIX = 6;
  
  _consciousness = {};

  def __init( self ):
    
    self._consciousness = {};
    
  def _assimilate( self, drone, unimatrix=None ):
    
    if unimatrix is None:
      unimatrix = self.__class__;

    # your technological and cultural distinctiveness
    # will be added to our own!
    if not self._consciousness.has_key( id ):
      self._consciousness[ id ] = {};
    for key in drone.__dict__:
      if not self._consciousness[ id ].has_key( key ):
        self._consciousness[ id ][ key ] = drone.__dict__[ key ];
    
    # resistance is futile!
    drone.__dict__ = self._consciousness[ id ];
    
    

class BorgDrone( GenericObject ):
  
  def __init__( self, unimatrix=1 ):
    
    self._init_1();
    Borg()._assimilate( self, unimatrix );
    self._init_2();
    self._init_3();
    self._init();
