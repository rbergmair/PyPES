# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "compare" ];

from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.infer._evaluation.annotation_reader import read_annotation;
from pypes.infer._evaluation.rte_score import RTEScore;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def compare( referencefile, objectfile ):
  
  refdata = None;
  objdata = None;
  
  score = None;

  with open( referencefile ) as f:
    with open( objectfile ) as g:
      refdata_ = read_annotation( f );
      objdata_ = read_annotation( g );
  with open( referencefile ) as f:
    with open( objectfile ) as g:
      score = RTEScore( f, g );

  ( descriptor, labelset, refdata ) = refdata_;
  ( descriptor, labelset, objdata ) = objdata_;
  
  print( "reference file:  " + referencefile );
  print( "object file:     " + objectfile );

  print();
  
  print( "      | {0:23s} | {1:23s}".format( "REFERENCE", "OBJECT" ) )
  
  print( "-" * 59 );
  
  for infid in sorted( refdata.keys() ):
    
    ( ref_decision, ref_conf, ref_vals ) = refdata[ infid ];
    if ref_decision is None:
      continue;

    if ref_decision is None or infid not in objdata:
      print( "{0} {1:3s} | {2:23s} | {3:23s}".format( " ", infid, ref_decision, "-" ) );
      continue;
    
    ( obj_decision, obj_conf, obj_vals ) = objdata[ infid ];
    
    ch = None;
    if ref_decision == obj_decision:
      ch = " ";
    elif score.LBLSETs[ score.lblset_ ][ ref_decision ] != score.LBLSETs[ score.lblset ][ obj_decision ]:
      ch = "+";
    else:
      ch = "-";
    
    print( "{0} {1:3s} | {2:23s} | {3:23s}".format( ch, infid, ref_decision, obj_decision ) );

  print( "-" *59 );

  print();
  if score.coverage is not None:
    print( "COVERAGE:  {0:1.2f}".format( score.coverage ) );
  if score.accuracy is not None:
    print( "ACCURACY:  {0:1.2f}".format( score.accuracy ) );
  if score.accuracy_2w is not None:
    print( "ACCURACY2: {0:1.2f}".format( score.accuracy_2w ) );
  if score.average_precision_2w is not None:
    print( "AVPREC:    {0:1.2f}".format( score.average_precision_2w ) );
  if score.confidence_weighted_score is not None:
    print( "CWS:       {0:1.2f}".format( score.confidence_weighted_score ) );
  if score.confidence_weighted_score_2w is not None:
    print( "CWS2:      {0:1.2f}".format( score.confidence_weighted_score_2w ) );
  if score.ent_gold is not None:
    print( "H(G):    {0:1.4f}".format( score.ent_gold ) );
  if score.mutinf is not None:
    print( "I(S;G):  {0:1.4f}".format( score.mutinf ) );
    
    

  
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
