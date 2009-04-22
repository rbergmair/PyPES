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

  
  def logify( self, inst_, msg=None ):

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
    
    self.check_pf_1( self.logify( self.init_pf_1() ) );
    

  def init_pf_2( self ):
    
    inst_ = ProtoForm(
                subforms = [ ( Handle( hid=1 ),
                                 Quantification(
                                     quantifier = Functor( fid=0, referent = Word( lemma = ["Every"] ) ),
                                     var = Variable( sidvid=("x",1) ),
                                     rstr = ProtoForm(
                                                subforms = [ ( Handle(),
                                                                 Predication( predicate = Functor( fid=6, referent = Word( lemma = ["man"] ) ),
                                                                              args = { Argument( aid="arg0" ): Variable( sidvid=("x",1) ) } ) ),
                                                           ]
                                              ),
                                     body = Freezer( content = Handle( hid=2 ) )
                                   ) ),
                             ( Handle( hid=3 ),
                                 Quantification(
                                     quantifier = Functor( fid=16, referent = Word( lemma = ["a"] ) ),
                                     var = Variable( sidvid=("x",2) ),
                                     rstr = ProtoForm(
                                                subforms = [ ( Handle(),
                                                                 Predication( predicate = Functor( fid=18, referent = Word( lemma = ["woman"] ) ),
                                                                              args = { Argument( aid="arg0" ): Variable( sidvid=("x",2) ) } ) )
                                                           ]
                                              ),
                                     body = Freezer( content = Handle( hid=4 ) )
                                   ) ),
                             ( Handle( hid=5 ),
                                 Predication(
                                     predicate = Functor( fid=10, referent = Word( lemma = ["loves"] ) ),
                                     args = { Argument( aid="arg1" ): Variable( sidvid=("x",1) ),
                                              Argument( aid="arg2" ): Variable( sidvid=("x",2) )
                                            }
                                   ) )
                           ],
                constraints = [ Constraint( harg = Handle( hid=1 ), larg = Handle( hid=5 ) ),
                                Constraint( harg = Handle( hid=3 ), larg = Handle( hid=5 ) )
                              ]
              );
    
    return inst_;
      
  def check_pf_2( self, inst, msg=None ):
    
    self.assertEquals( len( inst.subforms ), 3, msg );
    
    h1 = inst.roots[0];
    sf1 = inst.subforms[ h1 ];
    h3 = inst.roots[1];
    sf3 = inst.subforms[ h3 ];
    h5 = inst.roots[2];
    sf5 = inst.subforms[ h5 ];
    
    self.assert_( isinstance( h1, Handle ), msg );
    
    self.assert_( isinstance( sf1, Quantification ), msg );
    self.assert_( isinstance( sf1.quantifier, Functor ), msg );
    self.assertEquals( sf1.quantifier.fid, 0, msg );
    self.assert_( isinstance( sf1.quantifier.referent, Word ), msg );
    self.assertEquals( sf1.quantifier.referent.lemma, ["Every"], msg );
    
    x1 = sf1.var;

    self.assert_( isinstance( x1, Variable ), msg );
    self.assert_( isinstance( x1.sort, Sort ), msg );
    self.assertEquals( x1.sort.sid, "x", msg );
    self.assert_( isinstance( x1.vid, int ), msg );
    
    self.assert_( isinstance( sf1.rstr, ProtoForm ), msg );
    self.assertEquals( len(sf1.rstr.subforms), 1, msg );
    
    h_ = sf1.rstr.roots[0];
    sf_ = sf1.rstr.subforms[ h_ ];
      
    self.assert_( isinstance( h_, Handle ), msg );
    
    self.assert_( isinstance( sf_, Predication ), msg );
    self.assert_( isinstance( sf_.predicate, Functor ), msg );
    self.assertEquals( sf_.predicate.fid, 6, msg );
    self.assert_( isinstance( sf_.predicate.referent, Word ), msg );
    self.assertEquals( sf_.predicate.referent.lemma, ["man"], msg );
    
    sf_args = {};
    for arg in sf_.args:
      self.assert_( isinstance( arg, Argument ), msg );
      sf_args[ arg.aid ] = sf_.args[ arg ];
    
    self.assertEquals( len( sf_args ), 1, msg );
    self.assert_( sf_args[ "arg0" ] is x1, msg );

    h2 = sf1.body;

    self.assert_( isinstance( h3, Handle ), msg );
    
    self.assert_( isinstance( sf3, Quantification ), msg );
    self.assert_( isinstance( sf3.quantifier, Functor ), msg );
    self.assertEquals( sf3.quantifier.fid, 16, msg );
    self.assert_( isinstance( sf3.quantifier.referent, Word ), msg );
    self.assertEquals( sf3.quantifier.referent.lemma, ["a"], msg );
    
    x2 = sf3.var;

    self.assert_( isinstance( x2, Variable ), msg );
    self.assert_( isinstance( x2.sort, Sort ), msg );
    self.assertEquals( x2.sort.sid, "x", msg );
    self.assert_( isinstance( x2.vid, int ), msg );
    
    self.assert_( isinstance( sf3.rstr, ProtoForm ), msg );
    self.assertEquals( len(sf3.rstr.subforms), 1, msg );

    h__ = sf3.rstr.roots[0];
    sf__ = sf3.rstr.subforms[ h__ ];

    self.assert_( isinstance( h__, Handle ), msg );
    
    self.assert_( isinstance( sf__, Predication ), msg );
    self.assert_( isinstance( sf__.predicate, Functor ), msg );
    self.assertEquals( sf__.predicate.fid, 18, msg );
    self.assert_( isinstance( sf__.predicate.referent, Word ), msg );
    self.assertEquals( sf__.predicate.referent.lemma, ["woman"], msg );

    sf__args = {};
    for arg in sf__.args:
      self.assert_( isinstance( arg, Argument ), msg );
      sf__args[ arg.aid ] = sf__.args[ arg ];
    
    self.assertEquals( len( sf__args ), 1, msg );
    self.assert_( sf__args[ "arg0" ] is x2, msg );

    h4 = sf3.body;
    
    self.assert_( isinstance( h5, Handle ), msg );
    
    self.assert_( isinstance( sf5, Predication ), msg );
    self.assert_( isinstance( sf5.predicate, Functor ), msg );
    self.assertEquals( sf5.predicate.fid, 10, msg );
    self.assert_( isinstance( sf5.predicate.referent, Word ), msg );
    self.assertEquals( sf5.predicate.referent.lemma, ["loves"], msg );
    
    sf5args = {};
    for arg in sf5.args:
      self.assert_( isinstance( arg, Argument ), msg );
      sf5args[ arg.aid ] = sf5.args[ arg ];
    
    self.assertEquals( len( sf5args ), 2, msg );
    self.assert_( sf5args[ "arg1" ] is x1, msg );
    self.assert_( sf5args[ "arg2" ] is x2, msg );

    self.assertFalse( x1 is x2, msg );
    
    self.assertEquals( len( { id(h1), id(h2), id(h3), id(h4), id(h5),
                              id(h_), id(h__) } ), 7, msg );
    
    self.assertEquals( len( inst.constraints ), 2, msg );
    
    self.assert_( inst.constraints[0].harg is h1 );
    self.assert_( inst.constraints[0].larg is h5 );
    self.assert_( inst.constraints[1].harg is h3 );
    self.assert_( inst.constraints[1].larg is h5 );
  
  def test_2( self ):
    
    self.check_pf_2( self.logify( self.init_pf_2() ) );


  def init_pf_3( self ):
    
    inst_ = ProtoForm(
                subforms = [ ( Handle(),
                                 Quantification(
                                     quantifier = Functor( fid=0, referent = Word( lemma = ["every"] ) ),
                                     var = Variable( sidvid=("x",1) ),
                                     rstr = Freezer( content = Handle( hid=1 ) ),
                                     body = ProtoForm(
                                                subforms = [ ( Handle(),
                                                                 Predication(
                                                                     predicate = Functor( fid=32, referent = Word( lemma = ["lie"] ) ),
                                                                     args = { Argument( aid="arg1" ): Variable( sidvid=("x",1) ) }
                                                                   ) )
                                                           ]
                                              )
                                   ) ),
                             ( Handle( hid=2 ),
                                 ProtoForm(
                                     subforms = [ ( Handle( hid=5 ),
                                                      Connection(
                                                          connective = Functor( referent = Operator( otype=Operator.OP_C_WEACON ) ),
                                                          lscope = Freezer( content = Handle() ),
                                                          rscope = Freezer( content = Handle() )
                                                        ) ),
                                                  ( Handle( hid=6 ),
                                                      Predication(
                                                          predicate = Functor( fid=6, referent = Word( lemma = ["witness"] ) ),
                                                          args = { Argument( aid="arg0" ): Variable( sidvid=("x",1) ) }
                                                        ) ),
                                                  ( Handle( hid=7 ),
                                                      Modification(
                                                          modality = Functor( fid=18, referent = Word( lemma = ["say"] ) ),
                                                          args = { Argument( aid="arg1" ): Variable( sidvid=("x",1) ) },
                                                          scope = Freezer( content = Freezer( content = Handle( hid=3 ) ) )
                                                        ) )
                                                ]
                                   ) ),
                             ( Handle( hid=4 ),
                                 Quantification(
                                     quantifier = Functor( fid=23, referent = Word( lemma = ["she"] ) ),
                                     var = Variable( sidvid=("x",2) ),
                                     rstr = ProtoForm(
                                                subforms = [ ( Handle(),
                                                                 Predication(
                                                                     predicate = Functor( fid=23, referent = Word( lemma = ["she"] ) ),
                                                                     args = { Argument( aid="arg0" ): Variable( sidvid=("x",2) ) }
                                                                   ) )
                                                           ]
                                              ),
                                     body = ProtoForm(
                                                subforms = [ ( Handle(),
                                                                 Predication(
                                                                     predicate = Functor( fid=27, referent = Word( lemma = ["lie"] ) ),
                                                                     args = { Argument( aid="arg1" ): Variable( sidvid=("x",2) ) }
                                                                   ) )
                                                           ]
                                              )
                                   ) )
                           ],
                constraints = [ Constraint( harg = Handle( hid=1 ), larg = Handle( hid=2 ) ),
                                Constraint( harg = Handle( hid=3 ), larg = Handle( hid=4 ) ) ]
              );
    
    return inst_;

  def check_pf_3( self, inst, msg=None ):
    
    sf2 = inst.subforms[ inst.roots[1] ];
    sf7 = sf2.subforms[ sf2.roots[2] ];
    self.assertEquals( sf2.holes, {sf7.scope} );

  def test_3( self ):
    
    self.check_pf_3( self.logify( self.init_pf_3() ) );
  
  
  def init_logified_pf_4( self ):
    
    pf2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    pf3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    pf4 = ProtoForm( subforms = [
                         ( Handle(),
                             Connection(
                                 connective = Functor( referent = Operator( otype=Operator.OP_C_WEACON ) ),
                                 lscope = ProtoForm(),
                                 rscope = ProtoForm()
                               ) )
                       ] )( sig=ProtoSig() );
    
    subf = pf4.subforms[ pf4.roots[0] ];
    subf.lscope = pf2;
    subf.rscope = pf3;
    
    return pf4;
  
  
  def test_cmp( self ):
    
    pf1 = self.logify( self.init_pf_1() );
    pf2 = self.logify( self.init_pf_2() );
    pf3 = self.logify( self.init_pf_3() );

    pf1_ = self.logify( self.init_pf_1() );
    pf2_ = self.logify( self.init_pf_2() );
    pf3_ = self.logify( self.init_pf_3() );
    
    self.assertEquals_( pf1, pf1_ );
    self.assertEquals_( pf2, pf2_ );
    self.assertEquals_( pf3, pf3_ );
    
    self.assertNotEquals_( pf1, pf2_ );
    self.assertNotEquals_( pf2, pf3_ );
    self.assertNotEquals_( pf3, pf1_ );
    


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
