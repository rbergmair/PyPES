# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.tools";
__all__ = [ "extract_ergops" ];

import sys;
import pprint;

from pyparsing import Literal, LineStart;
from pyparsing import Word as Word_;
from pyparsing import ZeroOrMore, OneOrMore;
from pyparsing import printables;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


_nonspecial = "";
for ch in printables:
  if not ch in ".:<=&,#[]$()>!^}/+;":
    if not ch.isspace():
      _nonspecial += ch;


typename = Word_( _nonspecial, _nonspecial );

typedef = LineStart() + \
          typename + \
          ( Literal( ":=" ) | Literal( ":<" ) ) + \
          typename + \
          ZeroOrMore( Literal( "&" ) + typename ) + \
          ( ( Literal( "&" ) + Literal( "[" ) ) | Literal( "." ) );
#typedef = LineStart() + OneOrMore( typename ) + Literal( "." );
#typedef = OneOrMore( typename ) + Literal( "." );

def _decode_typedef( str_, loc, toks ):
  
  subtype = None;
  suptypes = set();
  
  i = 0;
  subtype = toks[i];
  
  i += 1;
  
  assert toks[i] in { ":=", ":<" };
  
  i += 1;
  
  while True:

    if toks[i] == "[":
      break;
    
    suptypes.add( toks[i] );
    i += 1;

    if toks[i] == ".":
      break;
    
    assert toks[i] == "&";
    i += 1;
  
  return ( subtype, suptypes );

typedef.setParseAction( _decode_typedef );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def extract_erg_pred_types( f ):
  
  types = {};
  
  r = typedef.scanString( f.read() );
  for (result, cfrom, cto) in r:
    ( subtype, suptypes ) = result[0];
    for suptype in suptypes:
      if not suptype in types:
        types[ suptype ] = set();
      types[ suptype ].add( subtype );
  
  nonpred_types = set();
  pred_types = {};
  
  x = [ "predsort" ];
  i = 0;
  
  while True:
    
    if i >= len(x):
      break;
    
    suptype = x[i];
    
    if not suptype in types:
      
      if suptype[ -4: ] == "_rel":
        pred_types[ suptype ] = None;
      else:
        nonpred_types.add( suptype );
      
      print( "leaf: " + str(suptype) );
      print();
      
    else:
      subtypes = types[ suptype ];
      
      for subtype in subtypes:
        x.append( subtype );
      
      if suptype[ -4: ] == "_rel":
        subtypes_ = set();
        for subtype in subtypes:
          if subtype[ -4: ] == "_rel":
            subtypes_.add( subtype );
          else:
            nonpred_types.add( subtype );
        pred_types[ suptype ] = subtypes_;
      else:
        nonpred_types.add( suptype );
        
      print( suptype );
      print( subtypes );
      print();
    
    i += 1;
  
  pprint.pprint( pred_types );
  pprint.pprint( nonpred_types );
  print( len( pred_types ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  f = open( "/local/scratch/rb432/delphin/erg/fundamentals.tdl" );
  extract_erg_pred_types( f );
  f.close();
  return 0;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
