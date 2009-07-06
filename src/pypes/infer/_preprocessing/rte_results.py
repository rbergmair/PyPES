# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "RTEResultsProcessor" ];

import tarfile;
import tempfile;
import os;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEResultsProcessor( metaclass=subject ):


  def __init__( self, dataset, datasubset ):
    
    self._dataset = dataset;
    self._datasubset = datasubset;

  
  def _enter_( self ):
    
    self._tempdir = tempfile.mkdtemp( "-pypes" );
    self._tarfile = tarfile.open(
                        "dta/infer/orig/rte-{0}-{1}-results.tar.gz".format(
                            self._dataset, self._datasubset
                          ),
                        "r"
                      );
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
  
  
  def process_file( self, f, filename ):
    
    with open(
             "dta/infer/rte/rte-{0}/{1}-{2}.tsa.xml".format(
                 self._dataset,
                 filename.lower(),
                 self._datasubset
               ),
             "wt",
             encoding="utf-8"
           ) as g:
      
      g.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
      
      lines = iter( f );
      ranked = next( lines );
      
      g.write( '<annotations descriptor="{0}" labelset="'.format( filename ) );
      
      assert self._directoryname == "two-way" or self._directoryname == "three-way";
      g.write( self._directoryname );
  
      assert ( ranked == "ranked: YES\n" ) or ( ranked == "ranked: NO\n" );
      g.write( '" confidence_ranked="{0}">\n'.format( ranked == "ranked: YES\n" ) );
      
      line = next( lines, False );
      while line:
        
        assert line[ len(line)-1 ] == "\n";
        line = line[ : len(line)-1 ];
        i = line.find( " " );
        
        infid = line[ :i ];
        decision_ = line[ i+1: ];
        
        # print( "{0}: {1}".format( infid, decision_ ) );
        
        assert decision_ in { "ENTAILMENT", "NO_ENTAILMENT",
                              "UNKNOWN", "CONTRADICTION" };
        
        decision = decision_.replace( "_", " " ).lower();
        
        g.write(
            '  <annotation infid="{0}" decision="{1}"/>\n'.format(
                infid,
                decision
          ) ); 
        
        line = next( lines, False );
      
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
        self.process_file( f, filename );
      
      name = next( names, False );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
