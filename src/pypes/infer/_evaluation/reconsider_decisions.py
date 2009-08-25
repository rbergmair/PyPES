# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "reconsider_decisions" ];

from pprint import pprint;

from pypes.utils.os_ import listsubdirs;
from pypes.utils.mc import subject;
from pypes.infer._evaluation.annotation_reader import read_annotation;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def reconsider_decisions(
        tsdirnameprefix,
        infile = "McPIETAgent.tsa.xml",
        outfile = "McPIETAgent-reconsidered.tsa.xml"
      ):

  for subdir in listsubdirs( tsdirnameprefix ):
      
    data = None;
    
    with open( subdir + "/" + infile ) as f:
      
      ( descriptor, labelset, annotation ) = read_annotation( f );
      
      with open( subdir + "/" + outfile, "wt" ) as f:
    
        f.write( """<?xml version="1.0" encoding="UTF-8"?>\n\n""" );
        f.write(
            """<annotations descriptor="{0}" labelset="two-way">\n\n\n""".format( descriptor )
          );
        
        for ( infid, ( dec, conf, vals ) ) in annotation.items():
          
          r1 = float( vals[ "r1" ] );
          r2 = float( vals[ "r2" ] );
          
          if r1 > r2:
            decision = "entailment";
          else:
            decision = "no entailment";
    
          confidence = "";
          if conf is not None:
            confidence = ' confidence="{0}"'.format( conf )
    
          f.write(
              ( """<annotation infid="{0:s}"{4} decision="{1:s}">\n"""
                """  <value attribute="r1">{2:0.5f}</value>\n"""
                """  <value attribute="r2">{3:0.5f}</value>\n"""
                """</annotation>\n\n""" ).format( infid, decision, r1, r2, confidence )
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
