import random;
import copy;

import rmrsutils;
import matrixutils;

import basic_modchecker;



class ModChecker1( basic_modchecker.BasicModChecker ):
  
  max_search_iterations = None;
  update_threshold = None;
  max_update_cycles = None;
  randomization = None;
  
  _map = None;
  _rmrs = None;
  _allvars = None;
  
  def __init__( self ):
    
    self._BasicModChecker_init();
    
    self.max_search_iterations = 10**5;
    self.update_threshold = 0.0;
    self.max_update_cycles = 10;
    self.randomization = 0.3;
  
  def _initialize_map( self ):

    self._map = {};
    for var in self._allvars:
      self._map[ var ] = random.randrange( 0, self.domain_size );
      
  def _randomize_map( self ):
    
    if self.randomization == 0.0:
      return;
    
    samp = None;
    
    keys = self._map.keys();
    sampsize = int( len(keys)*self.randomization + 1.0 );
    if sampsize >= len( keys ):
      samp = keys;
    else:
      samp = random.sample( keys, sampsize );
      
    for key in samp:
      self._map[ key ] = random.randrange( 0, self.domain_size );
  
  def _update_map( self ):

    rslt = None;

    i = 0;
    curvar = 0;
    
    pendingvars = copy.copy( self._allvars );
      
    while len(pendingvars) > 0 and i < self.max_search_iterations:
      
      curvar %= len( pendingvars );
      var = pendingvars[ curvar ];
      
      i += 1;
      
      prevref = self._map[ var ];
      
      maxref = None;
      maxval = None;
      for ref in range( 0, self.domain_size ):
        self._map[ var ] = ref;
        val = self._check_rmrs_map( self._rmrs, self._map );
        if maxval is None or maxval < val:
          maxval = val;
          maxref = ref;
      self._map[ var ] = maxref;
          
      if maxref == prevref or len( pendingvars ) == 1:
        del pendingvars[ curvar ];
      else:
        curvar += 1;
        
      rslt = maxval;
    
    return rslt;    
    

  
  def check_rmrs_proposition( self, rmrs ):
    
    self._rmrs = rmrs;
    self._allvars = rmrsutils.get_vars( rmrs );
    self._initialize_map();
    
    val = None;
    dval = None;
    oldval = 0.0;
    i = 0;
    
    maxmap = self._map;
    maxval = None;
    
    while True:
      
      self._randomize_map();
      val = self._update_map();
      
      if val > maxval:
        maxval = val;
        maxmap = self._map;
        
      if val == 1.0:
        break;
      
      if val - oldval < self.update_threshold:
        break;
      oldval = val;

      i += 1;
      if i >= self.max_update_cycles:
        break;
      
    self._map = maxmap;
    return maxval;