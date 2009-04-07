# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs._smi";
__all__ = [ "ERGSemSMIExtractor", "ergsem_smi_extract" ];

import re;
from pprint import pformat;

from pypes.utils.mc import subject;

from pypes.codecs_.mrs._ergsem_processor import ERGSemProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGSemSMIExtractor( ERGSemProcessor, metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._semi = {};
    
    self._ops = {};
    self._opqs = set();
    self._opcs = set();
    self._opms = set();
    self._opps = set();
    
    self._wqs = [];
    self._wcs = [];
    self._wps = [];
  
  
  @classmethod
  def _read_sign( cls, sign ):
    
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
  
  
  def _read_preds( self, f ):
    
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
      
      assert predstr_as_operator is not None or predstr_as_word is not None;
      
      if predstr_as_operator is not None:
        assert predstr_as_word is None;
        predstr = predstr.upper();
      
      if predstr_as_word is not None:
        assert predstr_as_operator is None;

      predstr = ascii( predstr )[1:-1];
      
      sign = self._read_sign( sign );
      
      interesting = False;

      args = {};
      for (arg,(opt,sort,feats)) in sign.items():
        args[ arg ] = sort;

      if predstr_as_word is not None:
        ( lemma, pos, sense ) = predstr_as_word;
        try:
          assert pos in { "c", "p", "q", "x", "n", "v", "a" };
        except:
          # TODO: activate;
          return;
          
        if pos in { "c", "p", "q", "x" }:
          interesting = True;
        lemma_ = [];
        for tok in lemma:
          lemma_.append( ascii( tok )[1:-1] );
        lemma = lemma_;
        sense = ascii( sense )[1:-1];
        predstr_as_word = ( lemma, pos, sense );

      if predstr_as_operator is not None:
        self._ops[ predstr_as_operator ] = predstr_as_operator;

      if self._is_quantification( args, strict=False ):
        interesting = True;
        if predstr_as_operator is not None:
          self._opqs.add( predstr_as_operator );
        if predstr_as_word is not None:
          assert pos in { "q" };
          if not predstr_as_word in self._wqs:
            self._wqs.append( predstr_as_word );
          
      if self._is_verbal_coordination( args, strict=False ):
        interesting = True;
        if predstr_as_operator is not None:
          self._opcs.add( predstr_as_operator );
        if predstr_as_word is not None:
          assert pos in { "c" };
          if not predstr_as_word in self._wcs:
            self._wcs.append( predstr_as_word );
          
      if self._is_nominal_coordination( args, strict=False ):
        interesting = True;
        if predstr_as_operator is not None:
          self._opps.add( predstr_as_operator );
        if predstr_as_word is not None:
          assert pos in { "c" };
          if not predstr_as_word in self._wps:
            self._wps.append( predstr_as_word );

      if self._is_connection( args, strict=False ):
        interesting = True;
        if predstr_as_operator is not None:
          self._opcs.add( predstr_as_operator );
        if predstr_as_word is not None:
          assert pos in { "v", "p", "a", "x" };
          if pos in { "p", "x" }:
            if not predstr_as_word in self._wcs:
              self._wcs.append( predstr_as_word );
        
      if self._is_modification( args, strict=False ):
        if predstr_as_operator is not None:
          interesting = True;
          self._opms.add( predstr_as_operator );
        if predstr_as_word is not None:
          assert pos in { "a", "c", "v", "p", "x", "n" };
        
      if self._is_predication( args, strict=False ):
        if predstr_as_operator is not None:
          interesting = True;
          self._opps.add( predstr_as_operator );
        if predstr_as_word is not None:
          assert pos != "q";

      if interesting:
        if predstr not in self._semi:
          self._semi[ predstr ] = [];
        self._semi[ predstr ].append( sign );


  def extract( self, targetdir ):
    
    sourcedir = self._obj_;
    
    with open( sourcedir + "/erg.smi" ) as f:
      
      self._read_preds( f );
      
    with open( sourcedir + "/core.smi" ) as f:
      
      self._read_preds( f );
    
    with open( targetdir + "/_ergsem_smi_checker_auto.py", "w" ) as f:
        
      f.write(
          """# -*-  coding: ascii -*-\n"""
          """__package__ = "pypes.codecs_.mrs";\n"""
          """__all__ = [ "ERGSemSMIChecker" ];\n"""
          """from pypes.utils.mc import subject;\n"""
          """from pypes.codecs_.mrs._ergsem_processor import ERGSemProcessor;\n"""
          """class ERGSemSMIChecker( ERGSemProcessor, metaclass=subject ):\n"""
        );
  
      semi = pformat( self._semi, width=72 );
      semi = "\n " + semi[ 1:-1 ];
      semi = semi.replace( "\n", "\n     " );
      semi = "  SEMI = {" + semi;
      semi = semi + "\n    };";
      
      f.write( semi );
        
    with open( targetdir + "/_erg_auto.py", "w" ) as f:
  
      f.write(
          """# -*-  coding: ascii -*-\n\n"""
          """__package__ = "pypes.proto.lex";\n"""
          """__all__ = [ "Operator" ];\n\n"""
          """from pypes.utils.mc import kls;\n"""
          """from pypes.proto.lex import basic;\n\n"""
          """class Operator( basic.Operator, metaclass=kls ):\n\n"""
        );
        
      for otype in sorted( self._ops.keys() ):
        f.write( "  " + otype + " = '" + otype + "';\n" );

      f.write( "\n" );
      
      f.write( "  OPs = {};\n" );
      f.write( "  OPs.update( basic.Operator.OPs );\n" );
      f.write( "  OPs.update( {" );
      f.write( ( "\n " + pformat( self._ops, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "} );\n\n" );
      
      f.write( "  OP_Qs = basic.Operator.OP_Qs | {" );
      f.write( ( "\n " + pformat( self._opqs, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n\n" );
      
      f.write( "  OP_Cs = basic.Operator.OP_Cs | {" );
      f.write( ( "\n " + pformat( self._opcs, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n\n" );
      
      f.write( "  OP_Ms = basic.Operator.OP_Ms | {" );
      f.write( ( "\n " + pformat( self._opms, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n\n" );

      f.write( "  OP_Ps = basic.Operator.OP_Ps | {" );
      f.write( ( "\n " + pformat( self._opps, width=74 )[1:-1] ).replace( "\n", "\n   " ).replace( "'", "" ) );
      f.write( "};\n\n" );

      f.write( "\n" );
      f.write( "class Word( basic.Word, metaclass=kls ):\n\n" );

      f.write( "  WRD_Qs = basic.Word.WRD_Qs + [" );
      f.write( ( "\n " + pformat( self._wqs, width=74 )[1:-1] ).replace( "\n", "\n   " ) );
      f.write( "];\n\n" );

      f.write( "  WRD_Cs = basic.Word.WRD_Cs + [" );
      f.write( ( "\n " + pformat( self._wcs, width=74 )[1:-1] ).replace( "\n", "\n   " ) );
      f.write( "];\n\n" );

      f.write( "  WRD_Ps = basic.Word.WRD_Ps + [" );
      f.write( ( "\n " + pformat( self._wps, width=74 )[1:-1] ).replace( "\n", "\n   " ) );
      f.write( "];\n\n" );
          
        
        
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
