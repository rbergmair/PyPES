# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "RTEResultsPreprocessor", "preprocess_rte_results" ];

import tarfile;
import tempfile;
import os;
import re;

from pypes.utils.mc import subject;
from pypes.utils.os_ import listsubdirs;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEResultsPreprocessor( metaclass=subject ):


  def __init__( self, f, dataset, datasubset ):
    
    self._tarfile = f;
    self._dataset = dataset;
    self._datasubset = datasubset;

  
  def _enter_( self ):
    
    self._tempdir = tempfile.mkdtemp( "-pypes" );
    self._tarfile.extractall( path = self._tempdir );
    names = iter( self._tarfile.getnames() );
    self._directoryname = next( names );

  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    names = iter( self._tarfile.getnames() );
    assert self._directoryname == next( names );
    
    name = next( names, False ); 
    while name:
      
      os.remove( self._tempdir + "/" + name );
      name = next( names, False );
    
    os.rmdir( self._tempdir + "/" + self._directoryname );
    os.rmdir( self._tempdir );
  
  
  def _process_file( self, f, filename ):
    
    lines = iter( f );
    ranked_ = next( lines );
    
    assert ( ranked_ == "ranked: YES\n" ) or ( ranked_ == "ranked: NO\n" );
    ranked = ranked_ == "ranked: YES\n";
    
    decision = {};

    line = next( lines, False );
    rank = 1;
    while line:
      
      assert line[ len(line)-1 ] == "\n";
      line = line[ : len(line)-1 ];
      i = line.find( " " );
      
      infid = line[ :i ];
      decision_ = line[ i+1: ];
      
      assert decision_ in { "ENTAILMENT", "NO_ENTAILMENT",
                            "UNKNOWN", "CONTRADICTION" };
      
      decision[ infid ] = ( decision_.replace( "_", " " ).lower(), rank );
      
      line = next( lines, False );
      rank += 1;
    
    infidre = re.compile( r'(?:<annotation infid=")([0-9]+)[^>]*>\n' );
    
    for subdir in listsubdirs( "dta/infer/rte/rte-" + self._dataset ):
      
      gold = "";
      with open( subdir + "/gold.tsa.xml", "rt", encoding="utf-8" ) as g:
        gold = g.read();
        
      with open( subdir + "/" + filename.lower() + "-" + self._datasubset + ".tsa.xml", "wt", encoding="utf-8" ) as g:
      
        g.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
        g.write( '<annotations descriptor="{0}" labelset="'.format( filename ) );
        
        assert self._directoryname == "two-way" or self._directoryname == "three-way";
        g.write( self._directoryname );
        g.write( '">\n' );
  
        for infid in infidre.findall( gold ):
      
          ( decision_, confidence ) = decision[ infid ];
          
          if ranked:
            g.write(
                '  <annotation infid="{0}" decision="{1}" confidence="-{2}"/>\n'.format(
                    infid,
                    decision_,
                    confidence
              ) ); 
          else:
            g.write(
                '  <annotation infid="{0}" decision="{1}"/>\n'.format(
                    infid,
                    decision_
              ) ); 
      
        g.write( "</annotations>\n" );


  def process( self ):
    
    names = iter( self._tarfile.getnames() );
    assert self._directoryname == next( names );
    
    name = next( names, False ); 
    while name:
      
      assert name.startswith( self._directoryname + "/" );
      filename = name[ len( self._directoryname ) + 1 : ];
      # print( "==" + filename + "==" );
      
      with open( self._tempdir + "/" + name, "rt", encoding="utf-8" ) as f:
        self._process_file( f, filename );
      
      name = next( names, False );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def preprocess_rte_results( argv=None ):

  f = tarfile.open( "dta/infer/orig/rte-08-3w-results.tar.gz", "r" );
  try:
    with RTEResultsPreprocessor( f=f, dataset="08", datasubset="3w" ) as proc:
      proc.process();
  finally:
    f.close();

  f = tarfile.open( "dta/infer/orig/rte-08-2w-results.tar.gz", "r" );
  try:
    with RTEResultsPreprocessor( f=f, dataset="08", datasubset="2w" ) as proc:
      proc.process();
  finally:
    f.close();
  
  return 0; 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
