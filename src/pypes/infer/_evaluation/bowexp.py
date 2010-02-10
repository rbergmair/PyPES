# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";

from pypes.infer._evaluation.annotation_reader import read_annotation;
from pypes.infer._evaluation.score_decisions import Score;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_concat_results( datasetnames, filename ):

  lblset = None;
  data = None;
  
  for dataset in datasetnames:
  
    with open( "dta/infer/rte/rte-{0}/{1}.tsa.xml".format(dataset,filename), "rb" ) as f:
      
      ( descriptor_, lblset_, data_ ) = read_annotation( f );
      
      if lblset is None:
        lblset = lblset_;
      else:
        assert lblset == lblset_;
      
      if data is None:
        data = data_;
      else:
        assert not data.keys() & data_.keys();
        data.update( data_ );
    
  return (lblset,data);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():
  
  ( lblset, gold ) = read_concat_results(
                         [ "08-ie", "08-qa", "08-ir", "08-sum" ],
                         "gold"
                       );

  ( lblset_, bow ) = read_concat_results(
                         [ "08-ie", "08-qa", "08-ir", "08-sum" ],
                         "BOWAgent"
                       );
                       
  assert lblset == lblset_;

  for cutoff in range( 0, 101 ):

    cutoff = cutoff / 100;
    
    for ( id, (dec,conf,attrs) ) in bow.items():
      conf = float( conf );
      if conf >= cutoff:
        bow[ id ] = ("entailment",conf,attrs);
      else:
        bow[ id ] = ("unknown",conf,attrs);
        
    sc = Score();
    sc._run_statistics( ("",lblset,gold), ("",lblset,bow) );
    
    print( "{0:5f}   {1:3f}".format( cutoff, sc.accuracy_2w ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
  import sys;
  main();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
