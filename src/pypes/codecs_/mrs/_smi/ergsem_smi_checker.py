# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "ERGSemSMIChecker", "ergsem_smi_check" ];

from pypes.utils.mc import subject;
from pypes.codecs_.mrs._mrs import *;
from pypes.codecs_.mrs._smi import _ergsem_smi_checker_auto;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGSemSMIChecker( _ergsem_smi_checker_auto.ERGSemSMIChecker, metaclass=subject ):
  
  def check( self ):
    
    for ep in self._obj_.eps:
      
      for ( arg, var ) in ep.args.items():

        assert isinstance( var, MRSVariable ) or isinstance( var, MRSConstant );
        
        try:
          if arg == "ARG0":
            assert var.sid in { "i", "e", "x" };
          elif arg == "ARG1":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "ARG2":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "ARG3":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "ARG4":
            assert var.sid == "h";
          elif arg == "ARG":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "CARG":
            assert isinstance( var, MRSConstant );
          elif arg == "MARG":
            assert var.sid == "h";
          elif arg == "RSTR":
            assert var.sid == "h";
          elif arg == "BODY":
            assert var.sid == "h";
          elif arg == "L-HNDL":
            assert var.sid == "h";
            # assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "L-INDEX":
            assert var.sid in { "i", "e", "x" };
          elif arg == "R-HNDL":
            assert var.sid == "h";
            # assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "R-INDEX":
            assert var.sid in { "i", "e", "x" };
          elif arg == "PSV":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "TPC":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          else:
            assert False;
        except:
          print( arg );
          print( var );
          raise;
        
        if isinstance( var, MRSConstant ):
          continue;
        
        for ( feat, val ) in var.feats.items():
          
          val = val.lower();
          
          try:
            if feat == "DIV":
              assert val in { "+", "-" };
            elif feat == "IND":
              assert val in { "+", "-" };
            elif feat == "PERF":
              assert val in { "+", "-" };
            elif feat == "PROG":
              assert val in { "+", "-" };
            elif feat == "MOOD":
              assert val in { "subjunctive", "indicative" };
            elif feat == "TENSE":
              assert val in { "past", "pres", "fut", "tensed", "untensed" };
            elif feat == "GEND":
              assert val in { "m", "f", "n", "m-or-f" };
            elif feat == "PERS":
              assert val in { "1", "2", "3" };
            elif feat == "NUM":
              assert val in { "sg", "pl" };
            elif feat == "PRONTYPE":
              assert val in { "refl", "std_pron", "zero_pron" };
            elif feat == "SF":
              assert val in { "prop", "ques", "comm", "prop-or-ques" };
            else:
              assert False;
          except:
            print( feat );
            print( val );
            raise;
      
      if not ep.pred in self.SEMI:
        return;
        
      found = False;
      
      for sign in self.SEMI[ ep.pred ]:

        try:
          
          matched = set();
          
          for ( arg, val ) in sign.items():
  
            ( optional, sort, feats ) = val;
            
            if not arg in ep.args:
              assert optional;
              continue;
              
            var = ep.args[ arg ];
            matched.add( arg );
            
            if sort == "u":
              assert var.sid in { "u", "i", "p", "e", "x", "h" };
            elif sort == "i":
              assert var.sid in { "i", "e", "x" };
            elif sort == "p":
              assert var.sid in { "p", "x", "h" };
            elif sort == "e":
              assert var.sid == "e";
            elif sort == "x":
              assert var.sid == "x";
            elif sort == "h":
              assert var.sid == "h";
            
            if feats is None:
              continue;
            
            for (feat,val) in feats.items():
              
              val = val.lower();
              
              assert feat in var.feats;
              val_ = var.feats[ feat ];
              val_ = val_.lower();

              if feat == "TENSE":
                
                if val == "tensed":
                  assert val_ in { "tensed", "past", "pres", "fut" };
                else:
                  assert val == val_;
                
              elif feat == "GEND":
                
                if val == "m-or-f":
                  assert val_ in { "m-or-f", "m", "f" };
                else:
                  assert val == val_;
                
              elif feat == "SF":
                
                if val == "prop-or-ques":
                  assert val_ in { "prop-or-ques", "prop", "ques" };
                else:
                  assert val == val_;
                
              else:
                
                assert val == val_;
          
          # TODO: check this
          if ep.pred not in { "_and_c_rel", "_and+so_c_rel" }:
            epargs = len( ep.args );
            if "CARG" in ep.args:
              epargs -= 1;
            assert epargs <= len( matched );
          
        except AssertionError:
          pass;
        
        else:
          found = True;
      
      try:
        assert found;
      except:
        print( ep );
        print( self.SEMI[ ep.pred ] );
        raise;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def ergsem_smi_check( mrs ):
  
  rslt = None;
  with ERGSemSMIChecker( mrs ) as checker:
    rslt = checker.check();
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
