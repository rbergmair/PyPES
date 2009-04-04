# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.tools";
__all__ = [ "extract_smi", "main" ];

import sys;
import re;
import pprint;

import pypes.codecs_._ergsem;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_sign( sign ):
  
  args = {};
  
  sqbrexp = re.compile( r"(\{[^\}]*\}|\,|\s|\.|\[|\])"  );
  
  one = None;
  two = None;
  feats = None;
  
  optional = False;
  
  sqbrexp_ = sqbrexp.split( sign );
  
  # print( sqbrexp_ );
  
  for substr in sqbrexp_:
    
    substr = substr.strip();
    if substr == "":
      continue;
    
    # print( substr );
    
    if substr == "[":
      optional = True;
      continue;

    if substr in { ",", ".", "]" }:
      if not ( one is None and two is None ):
        args[ one ] = ( optional, two, feats );
        one = None;
        two = None;
        feats = None;
      if substr == "]":
        optional = False;
      continue;
      
    if substr[0] == "{" and substr[-1] == "}":
      feats = substr;
      continue;
    
    one = two;
    two = substr;
    
  argnames = set( args.keys() );
  
  for argname in argnames:
    
    if argname is None:
      del args[ argname ];
      continue;
    
    ( optional, sort, feats_ ) = args[ argname ];
    
    if feats_ is None:
      continue;
    
    feats = {};
    
    for val in feats_[1:-1].split( "," ):
      ( featname, featval ) = val.split();
      featname = featname.strip();
      featval = featval.strip();
      feats[ featname ] = featval;
    
    args[ argname ] = ( optional, sort, feats );
  
  return args;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_preds( f ):
  
  poss = {};
  preds = {};

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
    
    predname = predname.strip();
    if predname[0] == '"' or predname[-1] == '"':
      assert predname[0] == '"';
      assert predname[-1] == '"';
      predname = predname[1:-1];
    if predname[0] == "'" or predname[-1] == "'":
      assert predname[0] == "'";
      assert predname[-1] == "'";
      predname = predname[1:-1];
      
    if predname[0] == "_":
      x = predname.split( "_" );
      if len(x) > 2:
        pos = x[2];
        if not len(pos) == 1:
          print( "# " + predname );
        else:
          if not x[2] in poss:
            poss[ x[2] ] = [];
          if not len( poss[ x[2] ] ) > 10:
            poss[ x[2] ].append( predname );
          if pos in { "c", "p", "q", "x" }:
            predname = ascii( predname )[ 1 : -1 ];
            sign = read_sign( sign );
            if predname not in preds:
              preds[ predname ] = [];
            preds[ predname ].append( sign );
          else:
            assert pos in { "n", "v", "a" };
    else:
      predname = ascii( predname )[ 1 : -1 ];
      sign = read_sign( sign );
      if predname not in preds:
        preds[ predname ] = [];
      preds[ predname ].append( sign );
    
  # pprint.pprint( poss );
  
  return preds;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  preds = {};

  with open( "/local/scratch/rb432/delphin/erg/erg.smi" ) as f:
    
    preds.update( read_preds( f ) );
    
  with open( "/local/scratch/rb432/delphin/erg/core.smi" ) as f:
    
    preds.update( read_preds( f ) );
  
  with open( "/local/scratch/rb432/tmp/_smi_erg_auto.py", "w" ) as f:
      
    f.write(
        """# -*-  coding: ascii -*-\n"""
        """__package__ = "pypes.codecs_.mrs";\n"""
        """__all__ = [ "MRSInterpreter" ];\n"""
        """from pypes.utils.mc import subject;\n"""
        """\n"""
        """\n"""
        """\n"""
        """class MRSInterpreter( metaclass=subject ):\n"""
      );

    preds_ = pprint.pformat( preds, width=72 );
    preds_ = preds_[ 1:-1 ];
    preds_ = preds_.replace( "\n", "\n    " );
    preds_ = "  PREDs = {\n" + preds_;
    preds_ = preds_ + "\n    };";
    
    f.write( preds_ );
  
  opqs = {};
  oppms = {};
  opcs = {};
  
  for ( pred, sign ) in preds.items():
    
    if ( "RSTR" in sign ) or ( "BODY" in sign ):
      
      assert sign.keys() == { "ARG0", "RSTR", "BODY" };
      
      assert sign[ "ARG0" ][ 0 ] == False;
      assert sign[ "RSTR" ][ 0 ] == False;
      assert sign[ "BODY" ][ 0 ] == False;
      
      assert sign[ "ARG0" ][ 1 ] == "x";
      assert sign[ "RSTR" ][ 1 ] == "h";
      assert sign[ "BODY" ][ 1 ] == "h";
      
      opqs[ pred ] = sign;
      
      continue;
    
    if ( "L-HNDL" in sign ) or ( "R-HNDL" in sign ):
      
      assert sign.keys() == { "ARG0", "L-INDEX", "L-HNDL", "R-INDEX", "R-HNDL" };

      assert sign[ "ARG0" ][ 0 ] == False;
      assert sign[ "L-INDEX" ][ 0 ] == False;
      assert sign[ "L-HNDL" ][ 0 ] == False;
      assert sign[ "R-INDEX" ][ 0 ] == False;
      assert sign[ "R-HNDL" ][ 0 ] == False;
      
      assert sign[ "ARG0" ][ 1 ] in { "i", "e", "x" };
      assert sign[ "L-INDEX" ][ 1 ] in { "i", "e", "x" };
      assert sign[ "L-HNDL" ][ 1 ] not in { "i", "e", "x" };
      assert sign[ "R-INDEX" ][ 1 ] in { "i", "e", "x" };
      assert sign[ "R-HNDL" ][ 1 ] not in { "i", "e", "x" };
      
      opcs[ pred ] = sign;
      
      continue;
    
    holes = 0;
    for argsig in sign.values():
      if argsig[1] == "h":
        holes += 1;
    assert len( holes ) <= 1;
    
    oppms[ pred ] = sign;
      
      
      
      

  with open( "/local/scratch/rb432/tmp/_ergops_auto.py", "w" ) as f:

    f.write(
        """# -*-  coding: ascii -*-\n"""
        """__package__ = "pypes.proto.lex;\n\n"""
        """__all__ = [ "Operator" ];\n"""
        """from pypes.utils.mc import subject;\n"""
        """\n"""
        """\n"""
        """\n"""
        """class Operator( metaclass=subject ):\n"""
      );
      
      

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
