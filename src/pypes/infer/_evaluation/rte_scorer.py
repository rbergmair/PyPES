# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "RTEScorer", "score" ];

from pypes.utils.mc import subject;
from pypes.utils.os_ import listsubdirs;
from os import listdir;

from pypes.infer._evaluation.rte_score import RTEScore;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEScorer( metaclass=subject ):
  
  def __init__( self, prefix ):
    
    self._prefix = prefix;
  
  def read_datastructure_( self ):
    
    subdirs = set();
    self._refs = None;
    self._gold = None;
    
    for subdirname in listsubdirs( self._prefix ):
      
      subdirs.add( subdirname );
      
      refs_ = set();
      gold_ = None;
      
      for filename in listdir( subdirname ):
        
        if not filename.endswith( ".tsa.xml" ):
          continue;
        
        filename = filename[ : - len(".tsa.xml") ];
        
        if filename.startswith( "gold" ):
          assert gold_ is None;
          gold_ = filename;
          continue;
        
        refs_.add( filename );
      
      if self._refs is None:
        self._refs = refs_;
      else:
        assert self._refs == refs_;
      
      if self._gold is None:
        self._gold = gold_;
      else:
        assert self._gold == gold_;
    
    self._prefixes = set();
    
    self._subdir_subdir = None;
    self._subdir_names = set();
    
    for subdir_ in subdirs:
      
      r = subdir_.rfind( "/" );
      
      subdir_subdir = subdir_[ :r ];
      subdir_name = subdir_[ r+1: ];
      
      self._subdir_names.add( subdir_name );
      
      if self._subdir_subdir is None:
        self._subdir_subdir = subdir_subdir;
      else:
        assert self._subdir_subdir == subdir_subdir;
      
      name = subdir_name.split( "-" );
      
      prefixes_ = [];
      while name:
        name_ = "";
        for x in name:
          name_ += x + "-";
        name_ = name_[ :-1 ];
        name = name[ :-1 ];
        prefixes_.insert( 0, name_ );
        
      for prefix in prefixes_:
        if not prefix in self._prefixes:
          self._prefixes.add( prefix );
  
  
  def score( self ):
    
    self.read_datastructure_();

    #print( self._gold );
    #print( self._refs );
    #print( self._subdir_subdir );
    #print( self._subdir_names );
    #print( self._prefixes );
    
    scores = {};
    for prefix in self._prefixes:
      scores_ = {};
      for ref in self._refs:
        scores_[ ref ] = RTEScore();
      scores[ prefix ] = scores_;
    
    for subdir_name in self._subdir_names:
      
      subdir = self._subdir_subdir + "/" + subdir_name;
      
      for ref in self._refs:
        
        score = None;
        with open( subdir + "/gold.tsa.xml", "rb" ) as r:
          with open( subdir + "/" + ref + ".tsa.xml", "rb" ) as o:
            score = RTEScore( r, o );
        assert score is not None;
            
        for prefix in scores:
          if subdir_name.startswith( prefix ):
            scores[ prefix ][ ref ].concatenate( score );
    
    for prefix in sorted( self._prefixes ):
      with open( "dta/infer/scores/" + prefix + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "system," + RTEScore.CSV_HEADER + "\n" );
        for ref in sorted( self._refs ):
          score = scores[ prefix ][ ref ];
          f.write( ref + "," );
          f.write( score.csv_data + "\n" );
    
    for ref in sorted( self._refs ):
      with open( "dta/infer/scores/" + ref + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "dataset," + RTEScore.CSV_HEADER + "\n" );
        for prefix in sorted( self._prefixes ):
          score = scores[ prefix ][ ref ];
          f.write( prefix + "," )
          f.write( score.csv_data + "\n" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def score( prefix ):
  
  with RTEScorer( prefix=prefix ) as sc:
    sc.score();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
