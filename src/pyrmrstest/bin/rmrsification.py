import pyrmrs.globals;

import unittest;

import pyrmrstest.mytest;

import pyrmrstest.ext.data;

import pyrmrs.bin.rmrsification_dispatcher;



class TestRMRSification( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    pass;

  def test_rmrsification( self ):
    
    for i in range( 0, len(pyrmrstest.ext.data.TEXT) ):
      
      dat = pyrmrstest.ext.data.TEXT[i];
      
      pyrmrs.bin.rmrsification_dispatcher.main( [ None, dat ] );



def suite():
  return unittest.makeSuite( TestRMRSification );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
