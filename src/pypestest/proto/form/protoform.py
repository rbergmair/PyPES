# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestProtoForm", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestProtoForm( TestCase, metaclass=object_ ):

  
  def init_pf1( self ):
    
    inst_ = ProtoForm();

    self.assertFalse( isinstance( inst_, ProtoForm ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, ProtoForm ) );
    
    return inst;
    

  def init_pf2( self ):
    
    ( hid1, hid2, hid3, hid4, hid5 ) = random.sample( range(0,0x7FFFFFFF), 5 );
    ( vid1, vid2 ) = random.sample( range(0,0x7FFFFFFF), 2 );
    hid_ = random.randint( 0, 0x7FFFFFFF );
    hid__ = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = ProtoForm(
                subforms = { Handle( hid=hid1 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( cspan=(0,4), lemma="Every" ) ),
                                   var = Variable( sortvid=("x",vid1) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle( hid=hid_ ):
                                                             Predication( predicate = Predicate( referent = Word( cspan=(6,8), lemma="man" ) ),
                                                                          args = { Argument( arglabel="arg0" ): Variable( sortvid=("x",vid1) ) } ),
                                                         }
                                            ),
                                   body = Handle( hid=hid2 )
                                 ),
                             Handle( hid=hid3 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( cspan=(16,16), lemma="a" ) ),
                                   var = Variable( sortvid=("x",vid2) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle( hid=hid__ ):
                                                             Predication( predicate = Predicate( referent = Word( cspan=(18,23), lemma="woman" ) ),
                                                                          args = { Argument( arglabel="arg0" ): Variable( sortvid=("x",vid2) ) } ),
                                                         }
                                            ),
                                   body = Handle( hid=hid4 )
                                 ),
                             Handle( hid=hid5 ):
                               Predication(
                                   predicate = Predicate( referent = Word( cspan=(10,14), lemma="loves" ) ),
                                   args = { Argument( arglabel="arg1" ): Variable( sortvid=("x",vid1) ),
                                            Argument( arglabel="arg2" ): Variable( sortvid=("x",vid2) )
                                          }
                                 )
                           },
                constraints = { Constraint( harg = Handle( hid=hid1 ), larg = Handle( hid=hid5 ) ),
                                Constraint( harg = Handle( hid=hid3 ), larg = Handle( hid=hid5 ) )
                              }
              );

    self.assertFalse( isinstance( inst_, ProtoForm ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, ProtoForm ) );
    
    return inst;
  
  
  def check_pf1( self, inst ):
    
    pass;

      
  def check_pf2( self, inst ):
    
    subforms = {};
    
    for root in inst.subforms:
      
      subform = inst.subforms[ root ];
      
      if isinstance( subform, Quantification ):
        subforms[ subform.quantifier.referent.cspan ] = ( root, subform );
      elif isinstance( subform, Predication ):
        subforms[ subform.predicate.referent.cspan ] = ( root, subform );
      else:
        self.fail();
    
    self.assertEquals( len(subforms), 3 );
    
    (h1,sf1) = subforms[ (0,4) ];
    (h3,sf3) = subforms[ (16,16) ];
    (h5,sf5) = subforms[ (10,14) ];
    
    self.assert_( isinstance( h1, Handle ) );
    self.assert_( isinstance( h1.hid, int ) );
    
    self.assert_( isinstance( sf1, Quantification ) );
    self.assert_( isinstance( sf1.quantifier, Quantifier ) );
    self.assert_( isinstance( sf1.quantifier.referent, Word ) );
    self.assertEquals( sf1.quantifier.referent.cspan, (0,4) );
    self.assertEquals( sf1.quantifier.referent.lemma, "Every" );
    
    x1 = sf1.var;

    self.assert_( isinstance( x1, Variable ) );
    self.assert_( isinstance( x1.sort, Sort ) );
    self.assertEquals( x1.sort.sortdsc, "x" );
    self.assert_( isinstance( x1.vid, int ) );
    
    self.assert_( isinstance( sf1.rstr, ProtoForm ) );
    self.assertEquals( len(sf1.rstr.subforms), 1 );
    
    (h_,sf_) = (None,None)
    for (x,y) in sf1.rstr.subforms.items():
      (h_,sf_) = (x,y);
      
    self.assert_( isinstance( h_, Handle ) );
    self.assert_( isinstance( h_.hid, int ) );
    
    self.assert_( isinstance( sf_, Predication ) );
    self.assert_( isinstance( sf_.predicate, Predicate ) );
    self.assert_( isinstance( sf_.predicate.referent, Word ) );
    self.assertEquals( sf_.predicate.referent.cspan, (6,8) );
    self.assertEquals( sf_.predicate.referent.lemma, "man" );
    
    sf_args = {};
    for arg in sf_.args:
      self.assert_( isinstance( arg, Argument ) );
      sf_args[ arg.arglabel ] = sf_.args[ arg ];
    
    self.assertEquals( len( sf_args ), 1 );
    self.assert_( sf_args[ "arg0" ] is x1 );

    h2 = sf1.body;

    self.assert_( isinstance( h3, Handle ) );
    self.assert_( isinstance( h3.hid, int ) );
    
    self.assert_( isinstance( sf3, Quantification ) );
    self.assert_( isinstance( sf3.quantifier, Quantifier ) );
    self.assert_( isinstance( sf3.quantifier.referent, Word ) );
    self.assertEquals( sf3.quantifier.referent.cspan, (16,16) );
    self.assertEquals( sf3.quantifier.referent.lemma, "a" );
    
    x2 = sf3.var;

    self.assert_( isinstance( x2, Variable ) );
    self.assert_( isinstance( x2.sort, Sort ) );
    self.assertEquals( x2.sort.sortdsc, "x" );
    self.assert_( isinstance( x2.vid, int ) );
    
    self.assert_( isinstance( sf3.rstr, ProtoForm ) );
    self.assertEquals( len(sf3.rstr.subforms), 1 );

    (h__,sf__) = (None,None)
    for (x,y) in sf3.rstr.subforms.items():
      (h__,sf__) = (x,y);

    self.assert_( isinstance( h__, Handle ) );
    self.assert_( isinstance( h__.hid, int ) );
    
    self.assert_( isinstance( sf__, Predication ) );
    self.assert_( isinstance( sf__.predicate, Predicate ) );
    self.assert_( isinstance( sf__.predicate.referent, Word ) );
    self.assertEquals( sf__.predicate.referent.cspan, (18,23) );
    self.assertEquals( sf__.predicate.referent.lemma, "woman" );

    sf__args = {};
    for arg in sf__.args:
      self.assert_( isinstance( arg, Argument ) );
      sf__args[ arg.arglabel ] = sf__.args[ arg ];
    
    self.assertEquals( len( sf__args ), 1 );
    self.assert_( sf__args[ "arg0" ] is x2 );

    h4 = sf3.body;
    
    self.assert_( isinstance( h5, Handle ) );
    self.assert_( isinstance( h5.hid, int ) );
    
    self.assert_( isinstance( sf5, Predication ) );
    self.assert_( isinstance( sf5.predicate, Predicate ) );
    self.assert_( isinstance( sf5.predicate.referent, Word ) );
    self.assertEquals( sf5.predicate.referent.cspan, (10,14) );
    self.assertEquals( sf5.predicate.referent.lemma, "loves" );
    
    sf5args = {};
    for arg in sf5.args:
      self.assert_( isinstance( arg, Argument ) );
      sf5args[ arg.arglabel ] = sf5.args[ arg ];
    
    self.assertEquals( len( sf5args ), 2 );
    self.assert_( sf5args[ "arg1" ] is x1 );
    self.assert_( sf5args[ "arg2" ] is x2 );

    self.assertFalse( x1 is x2 );
    
    self.assertEquals( len( { h1, h2, h3, h4, h5, h_, h__ } ), 7 );
    
    cons = {};
    for constraint in inst.constraints:
      self.assert_( isinstance( constraint, Constraint ) );
      cons[ constraint.harg ] = constraint.larg;

    self.assertEquals( len( cons ), 2 );
    self.assert_( cons[ h1 ] is h5 );
    self.assert_( cons[ h3 ] is h5 );
  
  
  def test_pf1( self ):
    
    self.check_pf1( self.init_pf1() );
  
  
  def test_pf2( self ):
    
    self.check_pf2( self.init_pf2() );



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
