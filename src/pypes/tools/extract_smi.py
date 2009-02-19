# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.tools";
__all__ = [ "extract_smi", "main" ];

import sys;
import re;
import pprint;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_sign( sign ):
  
  args = {};
  
  sqbrexp = re.compile( r"(\{[^\}]*\}|\,|\s|\.)"  );
  
  one = None;
  two = None;
  three = None;
  
  read_feats = False;
  
  for substr in sqbrexp.split( sign ):
    
    substr = substr.strip();
    if substr == "":
      continue;
    
    one = two;
    two = three;
    three = substr;

    if substr in { ",", "." }:
      if not read_feats:
        args[ one ] = ( two, None );
        one = None;
        two = None;
        three = None;
        read_feats = False;
      
    elif three[0] == "{" and substr[-1] == "}":
      args[ one ] = ( two, three );
      one = None;
      two = None;
      three = None;
      read_feats = True;

  if not read_feats:
    args[ two ] = ( three, None );
    one = None;
    two = None;
    three = None;
    read_feats = False;
    
  argnames = set( args.keys() );
  
  for argname in argnames:
    
    if argname is None:
      del args[ argname ];
      continue;
    
    ( sort, feats_ ) = args[ argname ];
    
    if feats_ is None:
      continue;
    
    feats = {};
    
    for val in feats_[1:-1].split( "," ):
      ( featname, featval ) = val.split();
      featname = featname.strip();
      featval = featval.strip();
      feats[ featname ] = featval;
    
    args[ argname ] = ( sort, feats );
  
  return args;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_ops( f ):
  
  ops = {};

  active = True;
  
  i = 0;
  
  for line in f:
    
    line = line[ :-1 ];
    line = line.strip();
    
    if not line:
      continue;
    
    if line[0] == ";":
      continue;
    
    if line[-1] == ":":
      active = False;
      
    if line == "predicates:":
      active = True;
      continue;
    
    if line.startswith( "include:" ):
      continue;
    
    if not active:
      continue;
      
    ( predname, sign ) = line.split( ":" );
    
    predname = predname.replace( "+", "_" );
    predname = predname.replace( "-", "_" );
    
    predname = predname.strip();
    if predname[0] == '"' or predname[-1] == '"':
      assert predname[0] == '"';
      assert predname[-1] == '"';
      predname = predname[1:-1];
    if predname[0] == "_":
      continue;
    assert predname[ -4: ] == "_rel";
    predname = predname[ :-4 ];
    predname = predname.upper();
    
    sign = read_sign( sign );
    
    ops[ predname ] = sign;
  
  return ops;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  ops = {};
  
  with open( "/local/scratch/rb432/delphin/erg/erg.smi" ) as f:
    ops.update( read_ops( f ) );
  with open( "/local/scratch/rb432/delphin/erg/core.smi" ) as f:
    ops.update( read_ops( f ) );
    
  # print( len(ops) );
  pprint.pprint( ops, width=72 );



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
