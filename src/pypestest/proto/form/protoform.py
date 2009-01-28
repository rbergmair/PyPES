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
                subforms = { Handle( hid=1 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( wid=0, lemma="Every" ) ),
                                   var = Variable( sidvid=("x",1) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle():
                                                             Predication( predicate = Predicate( referent = Word( wid=6, lemma="man" ) ),
                                                                          args = { Argument( aid="arg0" ): Variable( sidvid=("x",1) ) } ),
                                                         }
                                            ),
                                   body = Handle( hid=2 )
                                 ),
                             Handle( hid=3 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( wid=16, lemma="a" ) ),
                                   var = Variable( sidvid=("x",2) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle():
                                                             Predication( predicate = Predicate( referent = Word( wid=18, lemma="woman" ) ),
                                                                          args = { Argument( aid="arg0" ): Variable( sidvid=("x",2) ) } ),
                                                         }
                                            ),
                                   body = Handle( hid=4 )
                                 ),
                             Handle( hid=5 ):
                               Predication(
                                   predicate = Predicate( referent = Word( wid=10, lemma="loves" ) ),
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
        subforms[ subform.quantifier.referent.wid ] = ( root, subform );
      elif isinstance( subform, Predication ):
        subforms[ subform.predicate.referent.wid ] = ( root, subform );
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
    self.assertEquals( sf1.quantifier.referent.wid, 0, msg );
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
    self.assertEquals( sf_.predicate.referent.wid, 6, msg );
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
    self.assertEquals( sf3.quantifier.referent.wid, 16, msg );
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
    self.assertEquals( sf__.predicate.referent.wid, 18, msg );
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
    self.assertEquals( sf5.predicate.referent.wid, 10, msg );
    self.assertEquals( sf5.predicate.referent.lemma, "loves", msg );
    
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
    
    cons = {};
    for constraint in inst.constraints:
      self.assert_( isinstance( constraint, Constraint ), msg );
      cons[ constraint.harg ] = constraint.larg;

    self.assertEquals( len( cons ), 2, msg );
    self.assert_( cons[ h1 ] is h5, msg );
    self.assert_( cons[ h3 ] is h5, msg );
  
  def test_2( self ):
    
    self.check_pf_2( self.logify( self.init_pf_2() ) );


  def init_pf_3( self ):
    
    inst_ = ProtoForm(
                subforms = { Handle():
                               Quantification(
                                   quantifier = Quantifier( referent = Word( wid=0, lemma="every" ) ),
                                   var = Variable( sidvid=("x",1) ),
                                   rstr = Handle( hid=1 ),
                                   body = ProtoForm(
                                              subforms = { Handle():
                                                             Predication(
                                                                 predicate = Predicate( referent = Word( wid=32, lemma="lie" ) ),
                                                                 args = { Argument( aid="arg1" ): Variable( sidvid=("x",1) ) }
                                                               )
                                                         }
                                            )
                                 ),
                             Handle( hid=2 ):
                               ProtoForm(
                                   subforms = { Handle():
                                                  Connection(
                                                      connective = Connective( referent = Operator( otype=Operator.OP_C_WEACON ) ),
                                                      lscope = Handle(),
                                                      rscope = Handle()
                                                    ),
                                                Handle():
                                                  Predication(
                                                      predicate = Predicate( referent = Word( wid=6, lemma="witness" ) ),
                                                      args = { Argument( aid="arg0" ): Variable( sidvid=("x",1) ) }
                                                    ),
                                                Handle():
                                                  Modification(
                                                      modality = Modality( referent = Word( wid=18, lemma="say" ) ),
                                                      args = { Argument( aid="arg1" ): Variable( sidvid=("x",1) ) },
                                                      scope = Freezer( content = Handle( hid=3 ) )
                                                    )
                                              }
                                 ),
                             Handle( hid=4 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( wid=23, lemma="she" ) ),
                                   var = Variable( sidvid=("x",2) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle():
                                                             Predication(
                                                                 predicate = Predicate( referent = Word( wid=23, lemma="she" ) ),
                                                                 args = { Argument( aid="arg0" ): Variable( sidvid=("x",2) ) }
                                                               )
                                                         }
                                            ),
                                   body = ProtoForm(
                                              subforms = { Handle():
                                                             Predication(
                                                                 predicate = Predicate( referent = Word( wid=27, lemma="lie" ) ),
                                                                 args = { Argument( aid="arg1" ): Variable( sidvid=("x",2) ) }
                                                               )
                                                         }
                                            )
                                 )
                           },
                constraints = { Constraint( harg = Handle( hid=1 ), larg = Handle( hid=2 ) ),
                                Constraint( harg = Handle( hid=3 ), larg = Handle( hid=4 ) ) }
              );
    
    return inst_;

  def check_pf_3( self, inst, msg=None ):
    
    pass;

  def test_3( self ):
    
    self.check_pf_3( self.logify( self.init_pf_3() ) );
  
  
  def init_logified_pf_4( self ):
    
    pf2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    pf3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    pf4 = ProtoForm( subforms = {
                         Handle():
                           Connection(
                               connective = Connective( referent = Operator( otype=Operator.OP_C_WEACON ) ),
                               lscope = ProtoForm(),
                               rscope = ProtoForm()
                             )
                       } )( sig=ProtoSig() );
    
    subform = set( pf4.subforms.values() ).pop();
    subform.lscope = pf2;
    subform.rscope = pf3;
    
    return pf4;
  
  
  def test_cmp( self ):
    
    pf1 = self.logify( self.init_pf_1() );
    pf2 = self.logify( self.init_pf_2() );
    pf3 = self.logify( self.init_pf_3() );

    pf1_ = self.logify( self.init_pf_1() );
    pf2_ = self.logify( self.init_pf_2() );
    pf3_ = self.logify( self.init_pf_3() );
    
    self.assertEquals( pf1, pf1_ );
    self.assertEquals( pf2, pf2_ );
    self.assertEquals( pf3, pf3_ );
    
    self.assertNotEquals( pf1, pf2_ );
    self.assertNotEquals( pf2, pf3_ );
    self.assertNotEquals( pf3, pf1_ );
    


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
