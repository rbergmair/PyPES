import traceback;
import unittest;


import pyrmrs.globals;
import pyrmrs.ext.rasp.splitter;

import pyrmrstest.mytest;


import data;



class TestSplitter( pyrmrstest.mytest.MyTestCase ):
  
  def my_init( self ):
    
    self.splitter = pyrmrs.ext.rasp.splitter.Splitter();
    
  def test_splitter( self ):
    
    self.assertSequenceEqual(
      self.splitter.split( data.SPLITTER_IN ),
      data.SPLITTER_OUT
    );



def suite():
  return unittest.makeSuite( TestSplitter );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
