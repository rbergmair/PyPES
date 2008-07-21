import traceback;
import unittest;


import pyrmrs.globals;
import pyrmrs.ext.wrapper.rasp.splitter;

import pyrmrstest.mytest;


import data;



class TestSplitter( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.splitter = pyrmrs.ext.wrapper.rasp.splitter.Splitter();
    
  def test_splitter( self ):
    
    self.assertSequenceEqual(
      self.globalstate.splitter.split( data.SPLITTER_IN ),
      data.SPLITTER_OUT
    );



def suite():
  return unittest.makeSuite( TestSplitter );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
