import pyrmrs.globals;

import traceback;
import unittest;

import httplib;
import urllib;

import sys;

import pyrmrstest.mytest;

import pyrmrstest.ext.data;

import pyrmrs.smafpkg.smaf;



class TestRMRSificationServer( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    pass;

  def test_rmrsification_server( self ):

    headers = { "Content-type": "text/xml",
                "Accept": "text/xml",
                "Content-Length": None };
    
    for i in range( 0, len(pyrmrstest.ext.data.TEXT) ):
    #for i in [0]:
      
      dat = pyrmrstest.ext.data.TEXT[i];
      smaf = pyrmrs.smafpkg.smaf.SMAF( dat );
      dat = smaf.str_xml().encode( "utf-8" );
      headers[ "Content-Length" ] = "%d" % len(dat);
      conn = httplib.HTTPConnection( "localhost:8081" );
      conn.request( "POST", "/rmrsify?transid=0", dat );
      resp = conn.getresponse();
      self.assertEqual( resp.status, 200 );
      dat = resp.read().decode( "utf-8" );
      conn.close();
      #sys.stdout.write( dat );
      print dat;



def suite():
  return unittest.makeSuite( TestRMRSificationServer );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
