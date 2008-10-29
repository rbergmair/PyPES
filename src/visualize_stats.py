import random;



# comparisons

stats = {

  "tst1" : {
      "Bos & Markert" : {
          "all" : ( 56.25, 59.31 )
        },
      "Tatu et al." : {
          "ir" : ( 47.8, 38.6 ),
          "cd" : ( 78.0, 82.2 ),
          "rc" : ( 51.4, 53.4 ),
          "qa" : ( 48.5, 43.4 ),
          "ie" : ( 48.3, 58.0 ),
          "mt" : ( 54.2, 44.0 ),
          "pp" : ( 45.0, 45.0 ),
          "all" : ( 55.1, 56.0 )
        },
      "Median" : {
          "all" : ( 55.2, 56.9 )
        }
    },
  
  "tst2" : {
      "Bos & Markert" : {
          "ie" : ( 55.0, 55.0 ),
          "ir" : ( 64.0, 72.3 ),
          "qa" : ( 53.0, 59.8 ),
          "sum" : ( 70.5, 74.6 ),
          "all" : ( 60.6, 60.4 )
        },
      "Stanford" : {
          "ie" : ( 52.5, 50.46 ),
          "ir" : ( 61.0, 60.37 ),
          "qa" : ( 58.5, 53.21 ),
          "sum" : ( 70.0, 76.27 ),
          "all" : ( 60.5, 60.07 )
        },
      "Tatu et al." : {
          "ie" : ( 71.5, 62.99 ),
          "ir" : ( 74.0, 74.3 ),
          "qa" : ( 70.5, 75.1 ),
          "sum" : ( 79.0, 80.33 ),
          "all" : ( 73.75, 71.33 )
        },
      "Hickl et al." : {
          "ie" : ( 69.5, 82.37 ),
          "ir" : ( 74.5, 77.74 ),
          "qa" : ( 69.5, 82.37 ),
          "sum" : ( 84.5, 83.43 ),
          "all" : ( 75.38, 80.82 )
        },
      "Nicholson et al." : {
          "ie" : ( 52.9, 54.6 ),
          "ir" : ( 49.0, 55.6 ),
          "qa" : ( 56.5, 57.0 ),
          "sum" : ( 58.0, 60.8 ),
          "all" : ( 52.9, 54.6 )
        },
      "Median" : {
          "all" : ( 58.25, 58.0 )
        },
      
    },
  
  "tst3" : {
      "Wang" : {
          "ie" : ( 58.5, 58.5 ),
          "ir" : ( 70.5, 70.5 ),
          "qa" : ( 79.5, 79.5 ),
          "sum" : ( 59.0, 59.0 ),
          "all" : ( 66.9, 66.9 )
        },
      "MacCartney & Manning" : {
          "all" : ( 57.38, None )
        },
      "Stanford" : {
          "all" : ( 63.62, 65.27 )
        },
      "Tatu et al." : {
          "ie" : ( 63.5, 61.44 ),
          "ir" : ( 78.0, 78.83 ),
          "qa" : ( 87.5, 87.81 ),
          "sum" : ( 60.0, 61.54 ),
          "all" : ( 72.25, 69.42 )
        },
      "Hickl et al." : {
          "ie" : ( 69.5, 82.37 ),
          "ir" : ( 74.5, 77.74 ),
          "qa" : ( 90.0, 93.08 ),
          "sum" : ( 84.0, 89.74 ),
          "all" : ( 80.38, 88.15 )
        },
      "Median" : {
          "all" : ( 61.75, 60.96 )
        }
    }
         
};


f = open( "testdta/results/rte/summary.csv" );

mygroups = [];

firstline = f.readline();
firstline = firstline.replace( "\n", "" );

for item in firstline.split( ";" )[ 2: ]:
  
  mygroups.append( item );

for line in f:
  
  s = line.split( ";" );
  
  dataset = s[ 0 ];
  subset = s[ 1 ];
  
  # dataset = dataset.replace( "dev", "rte" );
  if not stats.has_key( dataset ):
    stats[ dataset ] = {};
    
  for i in range( 2, len(s) ):
    group = mygroups[ i-2 ];
    if not stats[ dataset ].has_key( group ):
      stats[ dataset ][ group ] = {};
    stats[ dataset ][ group ][ subset ] = eval( s[i] );
  
f.close();

for dataset in stats:
  for group in mygroups:
    if stats[ dataset ].has_key( group ):
      sum0 = 0.0;
      sum1 = 0.0;
      n0 = 0;
      n1 = 0;
      for subset in stats[ dataset ][ group ]:
        r0 = stats[ dataset ][ group ][ subset ][ 0 ];
        if not r0 is None:
          sum0 += r0;
          n0 += 1;
        r1 = stats[ dataset ][ group ][ subset ][ 1 ];
        if not r1 is None:
          sum1 += r1;
          n1 += 1;
      sum0 /= float( n0 );
      sum1 /= float( n1 );
      stats[ dataset ][ group ][ "all" ] = ( sum0, sum1, None );

def printall( dataset, fn, title, xlim ):
  
  subsets = [];
  groups = [];
  maxgrouplen = None;
  
  for group in stats[ dataset ]:
    
    groupscore = random.random();
    if stats[ dataset ][ group ].has_key( "all" ):
      r = None;
      try:
        r = fn( stats[ dataset ][ group ][ "all" ] );
      except:
        pass;
      if not r is None:
        groupscore = r;
    
    found = False;
    for subset in stats[ dataset ][ group ]:
      r = None;
      try:
        r = fn( stats[ dataset ][ group ][ subset ] );
      except:
        pass;
      if not r is None:
        found = True;
        break;
    
    if not found:
      continue;
    
    groups.append( ( groupscore, group ) );
    maxgrouplen = max( maxgrouplen, len(group) );
    
    for subset in stats[ dataset ][ group ]:
      if not subset in subsets:
        r = None;
        try:
          r = fn( stats[ dataset ][ group ][ subset ] );
        except:
          pass;
        if not r is None:
          subsets.append( subset );

  if len( groups ) == 0:
    return;
    
  subsets.sort();
  groups.sort( reverse=True );
  
  dat_x = "[ ";
  dat_y = "[ ";
  lbl = "[ ";
  tick = "[ ";
  
  j = 1;
  
  l = len( subsets );
  
  for ( groupscore, group ) in groups:

    tick += "%d; " % j;
    
    fmtstr = "'%%%ds'; " % maxgrouplen;
    lbl += fmtstr % group;

    for subset in subsets:
      
      
      #dat_x += "%d, " % ( ((j-1)/l)*l + l-((j-1)%l) );
      dat_x += "%d, " % j;
      j += 1;
      if stats[ dataset ][ group ].has_key( subset ):
        r = None;
        try:
          r = fn( stats[ dataset ][ group ][ subset ] );
        except:
          pass;
        if not r is None:
          dat_y += "%2.2f, " % r;
        else:
          dat_y += "0.0, ";
      else:
        dat_y += "0.0, ";
        
    dat_x = dat_x[ : len(dat_x)-2 ];
    dat_y = dat_y[ : len(dat_y)-2 ];
    
    dat_x += "; ";
    dat_y += "; ";
    
  dat_x = dat_x[ : len(dat_x)-2 ];
  dat_y = dat_y[ : len(dat_y)-2 ]; 
  lbl = lbl[ : len(lbl)-2 ];
  tick = tick[ : len(lbl)-2 ];
  dat_x += " ]";
  dat_y += " ]";
  lbl += " ]";
  tick += " ]";
  
  legend = "";
  #for i in range( len(subsets)-1,-1,-1 ):
  #  legend += "'%s', " % subsets[ i ];
  for subset in subsets:
    legend += "'%s', " % subset;
  legend = legend[ : len(legend)-2 ];
  
  print "X = %s;" % dat_x;
  print "Y = %s;" % dat_y;
  print """barh( X, Y, 'grouped');""";
  print """grid on;""";
  print """set( gca, 'XLim', %s );""" % xlim;
  # print """set( gca, 'YTick', %s );""" % tick;
  print """set( gca, 'YTickLabel', %s );""" % lbl;
  print """legend( %s );""" % legend;
  print """ylabel( '%s' )""" % title;
  print """title( '%s' );""" % dataset;
  print """orient portrait;""";
  print """print -depsc '~/figs/%s-%s.eps';""" % ( dataset, title );
  print """orient landscape;""";
  print """print -dpsc '~/figs/%s-%s.ps';""" % ( dataset, title );
  print;
  
    
  
for dataset in stats:
  printall( dataset, lambda x: x[0], "acc", "[30 90]" );
  printall( dataset, lambda x: x[1], "ap", "[30 90]" );
  printall( dataset, lambda x: x[2], "cov", "[0 100]" );
  