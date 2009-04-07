# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs._smi";
__all__ = [ "ERGSemSMIExtractor", "ergsem_smi_extract" ];

import re;
from pprint import pformat;

from pypes.utils.mc import subject;

from pypes.codecs_.mrs._ergsem_processor import ERGSemProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGSemSMIExtractor( ERGSemProcessor, metaclass=subject ):
  
  
  @classmethod
  def read_sign( cls, sign ):
    
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
  
  
  @classmethod
  def read_preds( cls, f ):
    
    semi = {};
  
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
        
      ( predstr, sign ) = line.split( ":" );
      predstr = predstr.strip();

      if predstr == "predsort":
        continue;
      
      if predstr[0] == '"' or predstr[-1] == '"':
        assert predstr[0] == '"';
        assert predstr[-1] == '"';
        predstr = predstr[1:-1];
      if predstr[0] == "'" or predstr[-1] == "'":
        assert predstr[0] == "'";
        assert predstr[-1] == "'";
        predstr = predstr[1:-1];
      
      predstr_as_operator = ERGSemProcessor._predstr_as_operator( predstr );
      predstr_as_word = ERGSemProcessor._predstr_as_word( predstr );
      
      if predstr_as_operator is not None:
        assert predstr_as_word is None;
        predstr = predstr.upper();
        predstr = ascii( predstr )[1:-1];
      
      if predstr_as_word is not None:
        assert predstr_as_operator is None;
        ( lemma, pos, sense ) = predstr_as_word;
        assert pos in { "c", "p", "q", "x", "n", "v", "a" };
        if pos in { "c", "p", "q", "x" }:
          predstr = ascii( predstr )[1:-1];
        else:
          predstr = None;
      
      if not predstr is None:
        sign = cls.read_sign( sign );
        if predstr not in semi:
          semi[ predstr ] = [];
        semi[ predstr ].append( sign );
      
    return semi;


  def extract( self, targetdir ):
    
    sourcedir = self._obj_;
    
    semi = {};
  
    with open( sourcedir + "/erg.smi" ) as f:
      
      semi.update( self.read_preds( f ) );
      
    with open( sourcedir + "/core.smi" ) as f:
      
      semi.update( self.read_preds( f ) );
    
    with open( targetdir + "/_ergsem_smi_checker_auto.py", "w" ) as f:
        
      f.write(
          """# -*-  coding: ascii -*-\n"""
          """__package__ = "pypes.codecs_.mrs";\n"""
          """__all__ = [ "ERGSemSMIChecker" ];\n"""
          """from pypes.utils.mc import subject;\n"""
          """from pypes.codecs_.mrs._ergsem_processor import ERGSemProcessor;\n"""
          """class ERGSemSMIChecker( ERGSemProcessor, metaclass=subject ):\n"""
        );
  
      semi_ = pformat( semi, width=72 );
      semi_ = "\n " + semi_[ 1:-1 ];
      semi_ = semi_.replace( "\n", "\n     " );
      semi_ = "  SEMI = {" + semi_;
      semi_ = semi_ + "\n    };";
      
      f.write( semi_ );
        
    with open( targetdir + "/_ergops_auto.py", "w" ) as f:
  
      f.write(
          """# -*-  coding: ascii -*-\n"""
          """__package__ = "pypes.proto.lex";\n"""
          """__all__ = [ "Operator" ];\n"""
          """from pypes.utils.mc import kls;\n"""
          """from pypes.proto.lex import basic;\n"""
          """class Operator( basic.Operator, metaclass=kls ):\n"""
        );
        
      ops = {};
      opqs = set();
      opcs = set();
      opms = set();
      opps = set();
      
      
      for predstr in sorted( semi.keys() ):
        
        otype = ERGSemProcessor._predstr_as_operator( predstr );
        if otype is None:
          continue;
        
        is_quantification = False;
        is_connection = False;
        is_modification = False;
        is_predication = False;
        
        for sign in semi[ predstr ]:
          
          args = {};
          for (arg,(opt,sort,feats)) in sign.items():
            args[ arg ] = sort;
        
          if self._is_quantification( args, strict=False ):
            is_quantification = True;
          if self._is_verbal_coordination( args, strict=False ):
            is_connection = True;
          if self._is_nominal_coordination( args, strict=False ):
            is_predication = True;
          if self._is_connection( args, strict=False ):
            is_connection = True;
          if self._is_modification( args, strict=False ):
            is_modification = True;
          if self._is_predication( args, strict=False ):
            is_predication = True;
        
        ops[ otype ] = otype;
        if is_quantification:
          opqs.add( otype );
        if is_connection:
          opcs.add( otype );
        if is_modification:
          opms.add( otype );
        if is_predication:
          opps.add( otype );
      
      for otype in sorted( ops.keys() ):
        f.write( "  " + otype + " = '" + otype + "';\n" );
      
      f.write( "  OPs = {};\n" );
      f.write( "  OPs.update( basic.Operator.OPs );\n" );
      f.write( "  OPs.update( {" );
      f.write( ( "\n " + pformat( ops, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "} );\n" );
      
      f.write( "  OP_Qs = basic.Operator.OP_Qs | {" );
      f.write( ( "\n " + pformat( opqs, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n" );
      
      f.write( "  OP_Cs = basic.Operator.OP_Cs | {" );
      f.write( ( "\n " + pformat( opcs, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n" );
      
      f.write( "  OP_Ms = basic.Operator.OP_Ms | {" );
      f.write( ( "\n " + pformat( opms, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n" );

      f.write( "  OP_Ps = basic.Operator.OP_Ps | {" );
      f.write( ( "\n " + pformat( opps, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n" );
          
        
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def ergsem_smi_extract( sourcedir, targetdir ):
  
  with ERGSemSMIExtractor( sourcedir ) as extractor:
    extractor.extract( targetdir );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
