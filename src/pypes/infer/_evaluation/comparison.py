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
  
  with open( referencefile ) as f:
    refdata_ = read_annotation( f );
  
  with open( objectfile ) as f:
    objdata_ = read_annotation( f );
  
  ( descriptor, labelset, refdata ) = refdata_;
  ( descriptor, labelset, objdata ) = objdata_;
  
  print( "reference file:  " + referencefile );
  print( "object file:     " + objectfile );
  
  print();
  
  print( "      | {0:23s} | {1:23s}".format( "REFERENCE", "OBJECT" ) )
  
  print( "-" * 59 );
  
  entailment_entailment = 0;
  entailment_unknown = 0;
  entailment_contradiction = 0;
  unknown_entailment = 0;
  unknown_unknown = 0;
  unknown_contradiction = 0;
  contradiction_entailment = 0;
  contradiction_unknown = 0;
  contradiction_contradiction = 0;
  
  total = 0;
  error = 0;
  
  for infid in sorted( refdata.keys() ):
    
    ( ref_decision, ref_conf, ref_vals ) = refdata[ infid ];
    
    total += 1;
    
    if ref_decision is None or infid not in objdata:
      error += 1;
      print( "{0} {1:3s} | {2:23s} | {3:23s}".format( " ", infid, ref_decision, "-" ) );
      continue;
    
    ( obj_decision, obj_conf, obj_vals ) = objdata[ infid ];
    
    if ref_decision == "entailment":
      if obj_decision == "entailment":
        entailment_entailment += 1;
      elif obj_decision == "unknown":
        entailment_unknown += 1;
      elif obj_decision == "contradiction":
        entailment_contradiction += 1;
      else:
        assert False;
    elif ref_decision == "unknown":
      if obj_decision == "entailment":
        unknown_entailment += 1;
      elif obj_decision == "unknown":
        unknown_unknown += 1;
      elif obj_decision == "contradiction":
        unknown_contradiction += 1;
      else:
        assert False;
    elif ref_decision == "contradiction":
      if obj_decision == "entailment":
        contradiction_entailment += 1;
      elif obj_decision == "unknown":
        contradiction_unknown += 1;
      elif obj_decision == "contradiction":
        contradiction_contradiction += 1;
      else:
        assert False;
    else:
      assert False;
    
    ch = None;
    if ref_decision != obj_decision:
      ch = "*";
    else:
      ch = " ";
    
    print( "{0} {1:3s} | {2:23s} | {3:23s}".format( ch, infid, ref_decision, obj_decision ) );

  print( "-" *59 );
  
  print();
  print( "error:                                    {0:2d}".format( error ) );
  print( "coverage:                               {0:3d}%".format( int( ((total-error) * 100) / total ) ) );

  print( "acc( sys; gold ):                       {0:3d}%".format( int( ((entailment_entailment+unknown_unknown+contradiction_contradiction ) * 100) / (total-error) ) ) );
  print( "2w-acc( sys; gold ):                    {0:3d}%".format( int( ((entailment_entailment+unknown_unknown+contradiction_contradiction+unknown_contradiction+contradiction_unknown ) * 100) / (total-error) ) ) );
  print( "2w'-acc( sys; gold ):                   {0:3d}%".format( int( ((entailment_entailment+unknown_unknown+contradiction_contradiction+unknown_entailment+entailment_unknown ) * 100) / (total-error) ) ) );

  if (entailment_entailment+unknown_entailment+contradiction_entailment) == 0:
    print( "acc( gold | sys = entailment ):         undef." );
  else:
    print( "acc( gold | sys = entailment ):         {0:3d}%".format( int( ( entailment_entailment*100) / (entailment_entailment+unknown_entailment+contradiction_entailment) ) ) );
    
  if (entailment_unknown+unknown_unknown+contradiction_unknown) == 0:
    print( "acc( gold | sys = unknown ):            undef." );
  else:
    print( "acc( gold | sys = unknown ):            {0:3d}%".format( int( ( unknown_unknown*100) / (entailment_unknown+unknown_unknown+contradiction_unknown) ) ) );
  
  if (entailment_contradiction+unknown_contradiction+contradiction_contradiction) == 0:
    print( "acc( gold | sys = contradiction ):      undef." );
  else:
    print( "acc( gold | sys = contradiction ):      {0:3d}%".format( int( ( contradiction_contradiction*100) / (entailment_contradiction+unknown_contradiction+contradiction_contradiction) ) ) );
  
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
