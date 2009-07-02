# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "compare" ];

from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.infer._evaluation.annotation_reader import read_annotation;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def compare( referencefile, objectfile ):
  
  refdata = None;
  objdata = None;
  
  with open( referencefile, "rb" ) as f:
    refdata = read_annotation( f );
  
  with open( objectfile, "rb" ) as f:
    objdata = read_annotation( f );
  
  ( refdata_ranked, refdata ) = refdata;
  ( objdata_ranked, objdata ) = objdata;
  
  objdata = dict( objdata );
  
  print( "reference file:  " + referencefile );
  print( "object file:     " + objectfile );
  
  print();
  
  print( "      | {0:23s} | {1:23s}".format( "REFERENCE", "OBJECT" ) )
  
  print( "-" * 59 );
  
  right = 0;
  wrong = 0;
  error = 0;
  
  for ( infid, ( ref_decision, ref_vals ) ) in refdata:
    
    if ref_decision is None:
      continue;
    
    if infid not in objdata:
      error += 1;
      print( "{0} {1:3s} | {2:23s} | {3:23s}".format( " ", infid, ref_decision, "-" ) );
      continue;
    
    ( obj_decision, obj_vals ) = objdata[ infid ];
    
    ch = None;
    if ref_decision != obj_decision:
      ch = "*";
      wrong += 1;
    else:
      ch = " ";
      right += 1;
    
    print( "{0} {1:3s} | {2:23s} | {3:23s}".format( ch, infid, ref_decision, obj_decision ) );

  print( "-" *59 );
  
  total = right + wrong;

  print();
  print( "right:           {0:2d}".format( right ) );
  print( "wrong:           {0:2d}".format( wrong ) );
  print( "total:           {0:2d}".format( total ) );
  print( "accuracy:      {0:3d}%".format( int( (right*100) / total ) ) );
  print( "error:           {0:2d}".format( error ) );
  print( "coverage:      {0:3d}%".format( int( (total*100) / (total+error) ) ) );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
