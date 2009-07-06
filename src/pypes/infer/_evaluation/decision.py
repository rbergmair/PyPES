# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "decide" ];

from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.infer._evaluation.annotation_reader import read_annotation;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def decide( infile, outfile ):
  
  data = None;
  with open( infile ) as f:
    data = read_annotation( f );
    
  ( ranked, data ) = data;
  
  with open( outfile, "wt" ) as f:

    f.write( """<?xml version="1.0" encoding="UTF-8"?>\n\n""" );
    f.write(
        """<annotations confidence_ranked="{0}">\n\n\n""".format( ranked )
      );
    
    for ( infid, ( dec, vals ) ) in data:
      
      r1 = float( vals[ "r1" ] );
      r2 = float( vals[ "r2" ] );
      
      if r1 > r2:
        decision = "entailment";
      elif r2 > r1:
        decision = "contradiction";
      else:
        decision = "unknown";
        
      f.write(
          ( """<annotation infid="{0:s}" decision="{1:s}">\n"""
            """  <value attribute="r1">{2:0.5f}</value>\n"""
            """  <value attribute="r2">{3:0.5f}</value>\n"""
            """</annotation>\n\n""" ).format( infid, dec, r1, r2 )
        );
    
    f.write( "\n</annotations>\n" );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
