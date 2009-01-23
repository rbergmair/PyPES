# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestProtoForm", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestProtoForm( TestCase, metaclass=object_ ):

  
  def thaw( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, ProtoForm ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, ProtoForm ), msg );
    
    return inst;

  
  def init_pf_1( self ):
    
    inst_ = ProtoForm();
    return inst_;

  def check_pf_1( self, inst, msg=None ):
    
    pass;

  def test_1( self ):
    
    self.check_pf_1( self.thaw( self.init_pf_1() ) );
    

  def init_pf_2( self ):
    
    inst_ = ProtoForm(
                subforms = { Handle( hid=1 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( cspan=(0,4), lemma="Every" ) ),
                                   var = Variable( sidvid=("x",1) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle():
                                                             Predication( predicate = Predicate( referent = Word( cspan=(6,8), lemma="man" ) ),
                                                                          args = { Argument( aid="arg0" ): Variable( sidvid=("x",1) ) } ),
                                                         }
                                            ),
                                   body = Handle( hid=2 )
                                 ),
                             Handle( hid=3 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( cspan=(16,16), lemma="a" ) ),
                                   var = Variable( sidvid=("x",2) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle():
                                                             Predication( predicate = Predicate( referent = Word( cspan=(18,23), lemma="woman" ) ),
                                                                          args = { Argument( aid="arg0" ): Variable( sidvid=("x",2) ) } ),
                                                         }
                                            ),
                                   body = Handle( hid=4 )
                                 ),
                             Handle( hid=5 ):
                               Predication(
                                   predicate = Predicate( referent = Word( cspan=(10,14), lemma="loves" ) ),
                                   args = { Argument( aid="arg1" ): Variable( sidvid=("x",1) ),
                                            Argument( aid="arg2" ): Variable( sidvid=("x",2) )
                                          }
                                 )
                           },
                constraints = { Constraint( harg = Handle( hid=1 ), larg = Handle( hid=5 ) ),
                                Constraint( harg = Handle( hid=3 ), larg = Handle( hid=5 ) )
                              }
              );
    
    return inst_;

      
  def check_pf_2( self, inst, msg=None ):
    
    subforms = {};
    
    for root in inst.subforms:
      
      subform = inst.subforms[ root ];
      
      if isinstance( subform, Quantification ):
        subforms[ subform.quantifier.referent.cfrom ] = ( root, subform );
      elif isinstance( subform, Predication ):
        subforms[ subform.predicate.referent.cfrom ] = ( root, subform );
      else:
        self.fail();
    
    self.assertEquals( len(subforms), 3, msg );
    
    (h1,sf1) = subforms[ 0 ];
    (h3,sf3) = subforms[ 16 ];
    (h5,sf5) = subforms[ 10 ];
    
    self.assert_( isinstance( h1, Handle ), msg );
    
    self.assert_( isinstance( sf1, Quantification ), msg );
    self.assert_( isinstance( sf1.quantifier, Quantifier ), msg );
    self.assert_( isinstance( sf1.quantifier.referent, Word ), msg );
    self.assertEquals( sf1.quantifier.referent.cfrom, 0, msg );
    self.assertEquals( sf1.quantifier.referent.cto, 4, msg );
    self.assertEquals( sf1.quantifier.referent.lemma, "Every", msg );
    
    x1 = sf1.var;

    self.assert_( isinstance( x1, Variable ), msg );
    self.assert_( isinstance( x1.sort, Sort ), msg );
    self.assertEquals( x1.sort.sid, "x", msg );
    self.assert_( isinstance( x1.vid, int ), msg );
    
    self.assert_( isinstance( sf1.rstr, ProtoForm ), msg );
    self.assertEquals( len(sf1.rstr.subforms), 1, msg );
    
    (h_,sf_) = (None,None)
    for (x,y) in sf1.rstr.subforms.items():
      (h_,sf_) = (x,y);
      
    self.assert_( isinstance( h_, Handle ), msg );
    
    self.assert_( isinstance( sf_, Predication ), msg );
    self.assert_( isinstance( sf_.predicate, Predicate ), msg );
    self.assert_( isinstance( sf_.predicate.referent, Word ), msg );
    self.assertEquals( sf_.predicate.referent.cfrom, 6, msg );
    self.assertEquals( sf_.predicate.referent.cto, 8, msg );
    self.assertEquals( sf_.predicate.referent.lemma, "man", msg );
    
    sf_args = {};
    for arg in sf_.args:
      self.assert_( isinstance( arg, Argument ), msg );
      sf_args[ arg.aid ] = sf_.args[ arg ];
    
    self.assertEquals( len( sf_args ), 1, msg );
    self.assert_( sf_args[ "arg0" ] is x1, msg );

    h2 = sf1.body;

    self.assert_( isinstance( h3, Handle ), msg );
    
    self.assert_( isinstance( sf3, Quantification ), msg );
    self.assert_( isinstance( sf3.quantifier, Quantifier ), msg );
    self.assert_( isinstance( sf3.quantifier.referent, Word ), msg );
    self.assertEquals( sf3.quantifier.referent.cfrom, 16, msg );
    self.assertEquals( sf3.quantifier.referent.cto, 16, msg );
    self.assertEquals( sf3.quantifier.referent.lemma, "a", msg );
    
    x2 = sf3.var;

    self.assert_( isinstance( x2, Variable ), msg );
    self.assert_( isinstance( x2.sort, Sort ), msg );
    self.assertEquals( x2.sort.sid, "x", msg );
    self.assert_( isinstance( x2.vid, int ), msg );
    
    self.assert_( isinstance( sf3.rstr, ProtoForm ), msg );
    self.assertEquals( len(sf3.rstr.subforms), 1, msg );

    (h__,sf__) = (None,None)
    for (x,y) in sf3.rstr.subforms.items():
      (h__,sf__) = (x,y);

    self.assert_( isinstance( h__, Handle ), msg );
    
    self.assert_( isinstance( sf__, Predication ), msg );
    self.assert_( isinstance( sf__.predicate, Predicate ), msg );
    self.assert_( isinstance( sf__.predicate.referent, Word ), msg );
    self.assertEquals( sf__.predicate.referent.cfrom, 18, msg );
    self.assertEquals( sf__.predicate.referent.cto, 23, msg );
    self.assertEquals( sf__.predicate.referent.lemma, "woman", msg );

    sf__args = {};
    for arg in sf__.args:
      self.assert_( isinstance( arg, Argument ), msg );
      sf__args[ arg.aid ] = sf__.args[ arg ];
    
    self.assertEquals( len( sf__args ), 1, msg );
    self.assert_( sf__args[ "arg0" ] is x2, msg );

    h4 = sf3.body;
    
    self.assert_( isinstance( h5, Handle ), msg );
    
    self.assert_( isinstance( sf5, Predication ), msg );
    self.assert_( isinstance( sf5.predicate, Predicate ), msg );
    self.assert_( isinstance( sf5.predicate.referent, Word ), msg );
    self.assertEquals( sf5.predicate.referent.cfrom, 10, msg );
    self.assertEquals( sf5.predicate.referent.cto, 14, msg );
    self.assertEquals( sf5.predicate.referent.lemma, "loves", msg );
    
    sf5args = {};
    for arg in sf5.args:
      self.assert_( isinstance( arg, Argument ), msg );
      sf5args[ arg.aid ] = sf5.args[ arg ];
    
    self.assertEquals( len( sf5args ), 2, msg );
    self.assert_( sf5args[ "arg1" ] is x1, msg );
    self.assert_( sf5args[ "arg2" ] is x2, msg );

    self.assertFalse( x1 is x2, msg );
    
    self.assertEquals( len( { h1, h2, h3, h4, h5, h_, h__ } ), 7, msg );
    
    cons = {};
    for constraint in inst.constraints:
      self.assert_( isinstance( constraint, Constraint ), msg );
      cons[ constraint.harg ] = constraint.larg;

    self.assertEquals( len( cons ), 2, msg );
    self.assert_( cons[ h1 ] is h5, msg );
    self.assert_( cons[ h3 ] is h5, msg );
  
  
  def test_2( self ):
    
    self.check_pf_2( self.thaw( self.init_pf_2() ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestProtoForm
    ) );

  return suite;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );

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
