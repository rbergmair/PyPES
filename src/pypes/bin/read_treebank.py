# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import gzip;
import sys;
import codecs;

from pypes.utils.itembank import *;

from pypes.codecs_ import mrs_decode, MRSDecoder, pft_encode;
from pypes.scoping.solver import Solver;
from pypes.scoping.enumerator import Enumerator;
from pypes.scoping.recursivizer import Recursivizer;

from pypes.rewriting.erg_to_dsf_rewriter import erg_to_dsf_rewrite;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  with TableManager( ( "dta/items/fracas", "sentence" ) ) as tbl:
    
    converrs = set();
    scoerrs = set();
    rewerrs = set();
    succ = set();

    f_ = gzip.open( "/local/scratch/rb432/delphin/erg/gold/fracas/result.gz" );
    
    try:
      
      cdc = codecs.getreader( "utf-8" );
      f = cdc( f_ );
      
      try:
        
        while True:
          
          line = f.readline();
          if line == "":
            break;
          
          idr = line.find( "@" );
          id = int( line[ :idr ] );
          mrsr = line.rfind( "@" );
          mrsl = line[ :mrsr ].rfind( "@" ) + 1;
          mrs = line[ mrsl : mrsr ];
          
          assert tbl.has_id( id );
          with tbl.record_by_id( id ) as rec:
            
            print( "{0:3d}: {1:s}".format( id, rec.get_ctx_str() ) );

            pf = None;
            try:
              pf = mrs_decode( mrs, MRSDecoder.SEM_ERG )( sig=ProtoSig() );
            except:
              print( "   can't convert." );
              rec.set( "status", "converr" );
              converrs.add( id );
              continue;
            
            pfrec = None;
            with Solver( pf ) as solver:
              solution = solver.solve_all( branching_factor=1 );
              #solution = solver.solve_all();
              if solution is not None:
                with Enumerator( solution ) as enumerator:
                  for solution in enumerator.enumerate():
                    with Recursivizer( solution ) as recursivizer:
                      assert pfrec is None;
                      pfrec = recursivizer.recursivize();
            
            if pfrec is None:
              print( "   can't scope." );
              rec.set( "status", "scoerr" );
              scoerrs.add( id );
              continue;
            
            pfrw = None;
            try:
              pfrw = erg_to_dsf_rewrite( pf );
            except:
              print( "   can't rewrite." );
              rec.set( "status", "rewerr" );
              rewerrs.add( id );
              raise;
              continue;

            succ.add( id );
            
            pft = pft_encode( pfrw, pretty=False, fast_initialize=True, linebreaks=False )
            rec.append_to( "sem", pft );

      finally:
        f.close();
        
    finally:
      f_.close();


    gramerrs = set( range( 1, tbl.max_id+1 ) ) - succ;
    
    for id in gramerrs:
      with tbl.record_by_id( id ) as rec:
        rec.set( "status", "gramerr" );
    
    n_total = tbl.max_id;
    
    n_gramerrs = len( gramerrs );
    n_gram = tbl.max_id - len( gramerrs );
    p_gram = int( n_gram*100 / n_total );
    
    n_scoerrs = len( scoerrs );
    n_sco = n_gram - n_scoerrs;
    p_sco = int( n_sco*100 / n_gram );
    
    n_rewerrs = len( rewerrs );
    n_rew = n_sco - n_rewerrs;
    p_rew = int( n_rew*100 / n_sco );
    
    n_succ = len( succ );
    p_succ = int( n_succ*100 / n_total )
    
    with open( "dta/items/fracas/summary.txt", "wt" ) as f:
      
      print( "\n--- SUMMARY ---" );
      
      print( "total number of items: {0:d}".format( tbl.max_id ) );
      print( "total number of items: {0:d}".format( tbl.max_id ), file=f );
      
      print( "syntax errors: {0:d} ({1:d}% good)".format( n_gramerrs, p_gram ) );
      print( "syntax errors: {0:d} ({1:d}% good)".format( n_gramerrs, p_gram ), file=f );
      if gramerrs:
        print( "  " + repr( gramerrs ) );
        print( "  " + repr( gramerrs ), file=f );
      
      print( "scoping errors: {0:d} ({1:d}% good)".format( n_scoerrs, p_sco ) );
      print( "scoping errors: {0:d} ({1:d}% good)".format( n_scoerrs, p_sco ), file=f );
      if scoerrs:
        print( "  " + repr( scoerrs ) );
        print( "  " + repr( scoerrs ), file=f );
        
      print( "rewriting errors: {0:d} ({1:d}% good)".format( n_rewerrs, p_rew ) );
      print( "rewriting errors: {0:d} ({1:d}% good)".format( n_rewerrs, p_rew ), file=f );
      if rewerrs:
        print( "  " + repr( rewerrs ) );
        print( "  " + repr( rewerrs ), file=f );
        
      print( "total number of processed items: {0:d} ({1:d}% good)".format( n_succ, p_succ ) );
      print( "total number of processed items: {0:d} ({1:d}% good)".format( n_succ, p_succ ), file=f );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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