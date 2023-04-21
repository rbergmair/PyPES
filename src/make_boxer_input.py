import testsuite.pairreader;
import codecs;

#testsuites = [ "1-cd", "1-ie", "1-mt", "1-pp", "1-qa", "1-rc",
#  "2-ie", "2-ir", "2-qa", "2-sum", "3-ie", "3-ir", "3-qa",
#  "3-sum" ];

testsuites = [ "1-cd" ];
  
  
for tsname in testsuites:
  for tstdev in [ "tst", "dev" ]:

    tstsuite = tstdev + tsname;

    pfile = open( "testdta/processed/rte/%s.rte.xml" % tstsuite );
    preader = testsuite.pairreader.PairReader( pfile );

    for pair in preader.getAll():
      
      t_ofile = codecs.open( "/local/scratch/rb432/boxer/%s-%s-t.bxinp" % ( tstsuite, pair.id ), "w", encoding="utf-8" );
      #t_mfile = codecs.open( "/local/scratch/rb432/boxer/%s-t.mapping" % tstsuite, "w", encoding="utf-8" );
      h_ofile = codecs.open( "/local/scratch/rb432/boxer/%s-%s-h.bxinp" % ( tstsuite, pair.id ), "w", encoding="utf-8" );
      #h_mfile = codecs.open( "/local/scratch/rb432/boxer/%s-h.mapping" % tstsuite, "w", encoding="utf-8" );
      
      
      i = 0;
      
      i += 1;
      
      t_ofile.write( "<META>'%s-t-%s'\n" % ( tstsuite, pair.id ) );
      for item in pair.t.items:
        t_ofile.write( item.text[ : len(item.text)-1 ] );
        t_ofile.write( " .\n" );
      #t_mfile.write( "%s\n" % pair.id );
    
      h_ofile.write( "<META>'%s-h-%s'\n" % ( tstsuite, pair.id ) );
      for item in pair.h.items:
        h_ofile.write( item.text[ : len(item.text)-1 ] );
        h_ofile.write( " .\n" );
      #h_mfile.write( "%s\n" % pair.id );
    
      #h_mfile.close();
      h_ofile.close();
      
      #t_mfile.close();
      t_ofile.close();
    
    pfile.close();

# cat dev1-cd-h.boxer | $BOXERHOME/bin/candc --models=$BOXERHOME/models/boxer >  dev1-cd-h.ccg
