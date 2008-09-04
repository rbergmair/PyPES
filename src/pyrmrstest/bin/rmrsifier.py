import pyrmrs.globals;

import unittest;

import pyrmrstest.mytest;
import pyrmrstest.ext.data;

import pyrmrs.bin.dispatcher;
import pyrmrs.bin.rmrsifier;



class TestRMRSification( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    pass;

  def test_rmrsification( self ):
    
    for i in range( 0, len(pyrmrstest.ext.data.TEXT) ):

      dat = pyrmrstest.ext.data.TEXT[i];
      
      dispatcher = pyrmrs.bin.rmrsifier.Dispatcher( dat );
      pyrmrs.bin.dispatcher.run( dispatcher );



def suite():
  return unittest.makeSuite( TestRMRSification );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
