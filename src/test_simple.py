import pyrmrs.mrs.robust.rmrsreader;
import infeng.logintrmrs.loginterg;


ofile = open( "/local/scratch/rb432/scopetest/folapprox.txt", "w" );


#for id in range( 1, 326 ):  # 326
#for id in [ 66, 144, 199, 200 ]:
for id in [ 117 ]:

  
  f = open( "/local/scratch/rb432/scopetest/%d.txt" % id );
  item = f.read();
  f.close();
  
  f = open( "/local/scratch/rb432/scopetest/%d.rmrs.xml" % id );
  rmrsrd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( f, True, 1 );
  rmrs = rmrsrd.getFirst();
  f.close();

  ofile.write( "%d: %s" % ( id, item ) );
  ofile.write( "\n\n" );
  
  try:
    formula = infeng.logintrmrs.loginterg.Interpret( rmrs );
    print formula.str_pretty_indent();
    if not formula is None:
      ofile.write( formula.str_pretty_indent() );
      assert len( formula.signature.unbound_vars ) == 0;
    else:
      ofile.write( "empty formula" );
  except:
    print id;
    print rmrs.str_pretty();
    raise;
  
  ofile.write( "\n\n\n" );


ofile.close();
