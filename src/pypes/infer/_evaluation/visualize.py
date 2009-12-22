# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";

from os import listdir;

from pypes.infer._evaluation.bowexp import read_concat_results;
from pypes.infer._evaluation.score_decisions import Score;

( lblset, gold ) = read_concat_results(
                       [ "08-ie", "08-qa", "08-ir", "08-sum" ],
                       "gold"
                     );

( lblset_, bow ) = read_concat_results(
                       [ "08-ie", "08-qa", "08-ir", "08-sum" ],
                       "BOWAgent"
                     );

assert gold.keys() == bow.keys();

lblset = Score.LBLSETs[ lblset ];

ids_agree = set();
ids_disagree = set();

golddec = {};
bowdec = {};
refdec = {};

for id in gold:
  
  (gdec,gconf,gattrs) = gold[ id ];
  (bdec,bconf,battrs) = bow[ id ];
  gdec = lblset[gdec];
  bdec = lblset[bdec];
  
  if gdec == bdec:
    ids_agree.add( id );
    refdec[ id ] = gdec; 
  else:
    ids_disagree.add( id );
    bowdec[ id ] = bdec;
    golddec[ id ] = gdec;

files = set( listdir( "dta/infer/rte/rte-08-qa" ) );
files_ = set( listdir( "dta/infer/rte/rte-08-ir" ) );
assert files == files_;
files_ = set( listdir( "dta/infer/rte/rte-08-ie" ) );
assert files == files_;
files_ = set( listdir( "dta/infer/rte/rte-08-sum" ) );
assert files == files_;

names = set();
for filename in files_:
  if not filename.endswith( ".tsa.xml" ):
    continue;
  if filename.startswith( "gold" ):
    continue;
  if filename.startswith( "BOWAgent" ):
    continue;
  filename = filename[ :-len(".tsa.xml") ];
  names.add( filename );


discretization = 3;

width = ( ( len(ids_agree) // discretization ) + 1 ) * discretization;
height = ( ( len(ids_disagree) // discretization ) + 1 ) * discretization;

with open( "dta/infer/vis/vis.svg", "wt" ) as f:
  
  print( '<?xml version="1.0"?>', file=f );
  print( '<svg width="{0:d}px" height="{1:d}px" viewBox="0 0 {0:d} {1:d}"'.format(
             width, height
           ), file=f );
  print( '  xmlns="http://www.w3.org/2000/svg" version="1.2" baseProfile="tiny">',
         file=f );

  for name in names:
  
    ( lblset, point ) = read_concat_results(
                           [ "08-ie", "08-qa", "08-ir", "08-sum" ],
                           name
                         );
                         
    lblset = Score.LBLSETs[ lblset ];
    
    x = 0;
    y = 0;
    
    for ( id, dec ) in refdec.items():
      ( pdec, conf, attrs ) = point[ id ];
      if lblset[ pdec ] != dec:
        x += 1;
  
    for ( id, dec ) in golddec.items():
      ( pdec, conf, attrs ) = point[ id ];
      if lblset[ pdec ] != dec:
        y += 1;
    
    print( "{0:15s} {1:3d} {2:3d}".format( name, x, y ) );

    x //= discretization;
    y //= discretization;
    x *= discretization;
    y *= discretization;

    print( '<rect x="{0}" y="{1}" width="{2}" height="{2}" fill="black"/>\n'.format(
               x, y, discretization
             ),
           file=f );

  print( '<rect x="0" y="0" width="3" height="3" fill="green"/>\n', file=f );
  print( '<rect x="0" y="{0:d}" width="3" height="3" fill="blue"/>\n'.format( height-3 ), file=f );
  print( '<rect x="{0:d}" y="0" width="3" height="3" fill="red"/>\n'.format( width-3 ), file=f );
  print( '<rect x="{0:d}" y="{1:d}" width="3" height="3" fill="red"/>\n'.format( width-3, height-3 ), file=f );

  print( '</svg>', file=f );
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
