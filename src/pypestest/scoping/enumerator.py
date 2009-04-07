# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.scoping";
__all__ = [ "TestEnumerator", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;
import codecs;
import re;
from pprint import pprint;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;

from pypes.codecs_ import PFTDecoder, tree_encode, pft_encode;

from pypes.scoping.solver import Solver;
from pypes.scoping.enumerator import Enumerator;
from pypes.scoping.recursivizer import Recursivizer;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestEnumerator( TestCase, metaclass=object_ ):

  
  _TESTDTADIR = "dta/native";


  _number = re.compile( "[0-9]+" );
  _lkb_variable = re.compile( "[uipexh]?[0-9]+(, )?" );

  
  @classmethod
  def _format_utool_record( cls, line ):
  
    while True:
      
      m = cls._number.search( line );
      if m is None:
        break;
      line = line[ : m.start() ] + line[ m.end() : ];
      
    line = line.replace( "'", "" );
    line = line.lower();
    line = line.replace( "_rel", "" );
    line = line.replace( "-", "" );
    line = line.replace( "_", "" );
    line = line.replace( "&", " /\ " );
    line = line.replace( ",", ", " );
    line = line.replace( "(", "( " );
    line = line.replace( ")", " )" );
    
    if line[0] == "[":
      line = line[1:];
    if line[-1] == "\n":
      line = line[:-1];
    line = line.strip();
    if line[-1] == "]":
      line = line[:-1];
    if line[-1] == ",":
      line = line[:-1];
    
    return line;


  @classmethod
  def _format_my_record( cls, line ):
    
    while True:
      
      m = cls._number.search( line );
      if m is None:
        break;
      line = line[ : m.start() ] + line[ m.end() : ];
  
    line = line.replace( "-", "" );
    line = line.replace( "_", "" );
    line = line.lower();
    
    return line;


  @classmethod
  def _format_lkb_record( cls, line ):
    
    while True:
      
      m = cls._lkb_variable.search( line );
      if m is None:
        break;
      line = line[ : m.start() ] + line[ m.end() : ];
  
    # line = line.replace( "*TOP*", "" );
      
    line = line.replace( "-", "" );
    line = line.replace( "_", "" );
      
    line = line.replace( "  ", " " );
    #line = line.replace( " /\ ", " & " );
    line = line.replace( ", )", ")" );
    line = line.replace( "()", "" );
    line = line.replace( "( ", "(" );
    line = line.replace( "(", "( " );
    line = line.replace( ")", " )" );
    line = line.lower();
    
    return line;
  
  
  def write_testfile( self, filename, decoder ):

    try:

      f_ = gzip.open( filename );
      
      try:
        
        cdc = codecs.getreader( "utf-8" );
        f = cdc( f_ );
        
        try:
          
          try:
            
            h_ = gzip.open( filename.replace( ".pft.gz", ".pl.gz" ) );
            
            try:
              
              cdc = codecs.getreader( "utf-8" );
              h = cdc( h_ );
              
              try:
                
                try:
                  
                  i_ = gzip.open( filename.replace( ".pft.gz", ".scmrs.txt.gz" ) );
                  
                  try:
                    
                    cdc = codecs.getreader( "utf-8" );
                    i = cdc( i_ );
                    
                    try:
          
                      r = None;
                      gstr = None;
        
                      mylines_orig = [];
                      mylines_utool = set();
                      mylines_lkb = set();
                      
                      fstr = f.read();
                      pstr = None;
                      
                      pf1 = decoder.decode( fstr )( sig=ProtoSig() );
                      
                      print( filename );
                      
                      #pf2 = minrec_to_dsf_rewrite( pf1 )( sig=ProtoSig() );
                      #pstr = pft_encode( pf2 );
                      #print( pstr );
                      #g.write( pstr );
                      #g.write( "\n" );
                      
                      # print( fstr );
                      
                      with Solver( pf1 ) as solver:
                        solution = solver.solve_all();
                        # pprint( solution.solution.chart_index );
                        # pprint( solution.solution.chart );
                        with Enumerator( solution ) as enumerator:
                          for solution in enumerator.enumerate():
                            # pprint( solution.solution.chart_index );
                            # pprint( solution.solution.chart );
                            with Recursivizer( solution ) as recursivizer:
                              
                              pf = recursivizer.recursivize();
                              
                              # print( pft_encode( pf ) );
                              
                              myline_orig = tree_encode( pf );
                              if myline_orig is None:
                                mylines_orig = [];
                                mylines_lkb = [];
                                mylines_utool = [];
                                break;
                              mylines_orig.append( myline_orig );
                              mylines_lkb.add( self._format_my_record( myline_orig ) );
                              
                              myline_utool = tree_encode( pf, utool_style=True );
                              mylines_utool.add( self._format_my_record( myline_utool ) );
                      
                      utoollines = set();
                      
                      for line in h:
                        line = self._format_utool_record( line );
                        utoollines.add( line );
                      
                      lkblines = set();
                      lkb_warning = False;
                      lkboutput = i.read();
                      
                      if lkboutput.find( "Maximum scoping calls exceeded" ) != -1:
                        lkb_warning = True;
                        
                      else:
                        
                        logical_record = "";
                        real_line = "";
                        
                        for ch in lkboutput[1:] + "\n\n":
                          
                          if ch == "\n":
                            logical_record += " ";
                          else:
                            logical_record += ch;
                            
                          real_line += ch;
                          
                          if ch == "\n":
                            if real_line == "\n":
                              if logical_record.startswith( "WARNING:" ):
                                warning = True;
                                break;
                              logical_record = logical_record[ : len(logical_record)-2 ];
                              if not logical_record == "":
                                lkblines.add( self._format_lkb_record( logical_record ) );
                                logical_record = "";
                              
                          if ch == "\n":
                            real_line = "";
                      
                      utoolerr = False;
                      lkberr = False;
                      pypeserr = False;
                      
                      if len( utoollines ) == 0:
                        print( "  utool found no scopings" );
                        utoolerr = True;
                      if len( lkblines ) == 0:
                        print( "  lkb found no scopings" );
                        lkberr = True;
                      if lkb_warning:
                        print( "  lkb warning" );
                        lkberr = True;
                      if len( mylines_orig ) == 0:
                        print( "  pypes found no scopings" );
                        pypeserr = True;
                      
                      if utoolerr:
                        return;
                      
                      succ = not pypeserr;
                      if succ:
                        succ = succ and ( mylines_utool == utoollines );
                        if not lkberr:
                          succ = succ and ( mylines_lkb == lkblines );
                        
                      if not succ:
                        print( fstr );
                        pprint( mylines_lkb );
                        pprint( utoollines );
                        pprint( lkblines );
                        print( "------" );
                        assert False;
                      
                      if not pypeserr:
                        g = open( filename.replace( ".pft.gz", ".trees.txt" ), "w" );
                        try:
                          for line in mylines_orig:
                            g.write( line );
                            g.write( "\n" );
                        finally:
                          g.close();
                      
                    finally:
                      i.close();
                      
                  finally:
                    i_.close();
                
                except IOError:
                  pass;
                
              finally:
                h.close();
            
            finally:
              h_.close();
          
          except IOError:
            pass;
          
        finally:
          f.close();
        
      finally:
        f_.close();
        
    except IOError:
      pass;


  def check_testfile( self, filename, decoder ):
    
    try:
      
      f_ = gzip.open( filename );
      try:
        
        try:
          
          g_ = gzip.open( filename.replace( ".pft.gz", ".trees.txt.gz" ) );
          try:

            r = None;
            gstr = None;
            
            try:

              cdc = codecs.getreader( "utf-8" );
              f = cdc( f_ );
              cdc = codecs.getreader( "utf-8" );
              g = cdc( g_ );

              fstr = f.read();
              
              pf1 = decoder.decode( fstr )( sig=ProtoSig() );
              
              print( filename );
              
              with Solver( pf1 ) as solver:
                solution = solver.solve_all();
                with Enumerator( solution ) as enumerator:
                  
                  i = 0;
                  for solution in enumerator.enumerate():
                    i += 1;
                    if i > 100:
                      break;
                    
                    with Recursivizer( solution ) as recursivizer:
                      
                      pf = recursivizer.recursivize();
                      tree = tree_encode( pf );
                      assert tree is not None;
                      
                      gstr = g.readline();
                      gstr = gstr[ :-1 ];
                      
                      try:
                        self.assertEquals( tree, gstr, filename );
                      except:
                        print( tree );
                        print( gstr );
                        raise;

              g.close();
              f.close();
            
            except:

              print( fstr );
              raise;
    
          finally:
            g_.close();
          
        except IOError:
          pass;
      
      finally:
        f_.close();
    
    except IOError:
      pass;



  def quicktest( self, filename, decoder ):
    
    try:
      
      f_ = gzip.open( filename );
      try:
        
        cdc = codecs.getreader( "utf-8" );
        f = cdc( f_ );
  
        fstr = f.read();
        
        pf1 = decoder.decode( fstr )( sig=ProtoSig() );
        
        print( filename );
        
        with Solver( pf1 ) as solver:
          solution = solver.solve_all();
          with Enumerator( solution ) as enumerator:
            for solution in enumerator.enumerate():
              with Recursivizer( solution ) as recursivizer:
                
                pf = recursivizer.recursivize();
                print( pft_encode( pf ) );
  
        f.close();
      
      finally:
        f_.close();
    
    except IOError:
      pass;
    

  def x_test_quick( self ):
    
    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
      
      i = 102;
      self.quicktest( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );
  
  def test_enumerator( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
  
      for i in range( 1, 108 ):
        self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );

      for i in range( 1, 641 ):
        self.write_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestEnumerator
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
