import cPickle;

from infeng.logic import Logic;

import testsuite.pairreader;



#tasks = [ "cd", "ie", "mt", "pp", "qa", "rc", "ir", "sum" ];
tasks = [ "sum" ];



#for tsname in [ "dev1", "tst1", "dev2", "tst2", "dev3", "tst3" ]:
for tsname in [ "dev2", "tst2", "dev3", "tst3" ]:
#for tsname in [ "dev1", "dev2", "dev3" ]:
#for tsname in [ "dev1", "dev2" ]:

  dat_x = "";
  dat_y = "";
  dat_c = "";
  
  for task in tasks:
    
    try:
    
      rfile = open( "testdta/results/rte/%s-%s.pickle" % ( tsname, task ) );
      
      unpickler = cPickle.Unpickler( rfile );
      results = unpickler.load();
      del unpickler;
      
      rfile.close();
    
    except:
      continue;

    try:
      pfile = open( "testdta/processed/rte/%s-%s.rte.xml" % ( tsname, task ) );
    except:
      continue;

    preader = testsuite.pairreader.PairReader( pfile );

    for pair in preader.getAll():
      
      id = pair.id;
      
      if results.has_key( id ):
        pass;
      elif results.has_key( int(id) ):
        id = int(id);
      else:
        continue;
      
      ( r1, r2, duration, cnt ) = results[ id ];
      
      #try:
      #  assert cnt in [16, 17];
      #except:
      #  print cnt;
      #  raise;
      
      try:
        r1 /= cnt;
        r2 /= cnt;
      except:
        print "!! %s" % pair.id;
        continue;
      
      dat_x += Logic.to_str( r1 );
      dat_x += ", ";
      dat_y += Logic.to_str( r2 );
      dat_y += ", ";
  
      if pair.value:
        dat_c += "0, 1, 0; ";
      else:
        dat_c += "1, 0, 0; ";
  
  dat_c = dat_c[ : len(dat_c)-2 ];
  dat_x = dat_x[ : len(dat_x)-2 ];
  dat_y = dat_y[ : len(dat_y)-2 ];
  
  #print """C = [ %s ];""" % dat_c;
  #print """X = [ %s ];""" % dat_x;
  #print """Y = [ %s ];""" % dat_y;
  print """scatter( Y, X, [], C );""";

  print """set( gca, 'XLim', [ 0.95 1 ] );""";
  print """set( gca, 'YLim', [ 0.95 1 ] );""";

  print """title( '%s' );""" % tsname;
  
  print """orient portrait;""";
  print """print -depsc '~/figs/%s-scatter.eps';""" % tsname;
  print """orient landscape;""";
  print """print -dpsc '~/figs/%s-scatter.ps';""" % tsname;
  
  print;
