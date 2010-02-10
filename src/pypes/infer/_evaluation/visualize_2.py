# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
# __all__ = [ "Score", "score_decisions" ];

from subprocess import Popen, PIPE, STDOUT;
from pprint import pprint;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

LONDON = ( (51,30,30,'N'), (0,7,31,'W') );
PARIS = ( (48,51,12,'N'), (2,20,55,'E') );
BOSTON = ( (42,21,30,'N'), (71,3,35,'W') );
NEW_YORK = ( (40,42,51,'N'), (74,0,21,'W') );
SYDNEY = ( (33,52,4,'S'), (151,12,26,'E') );
TOKYO = ( (35,41,22,'N'), (139,41,30,'E') );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def dms_to_float( dms ):
  ( d, m, s, mark ) = dms;
  
  rslt = float( d );
  rslt += float( m ) / 60.0;
  rslt += float( m ) / (60.0*60.0);
  if mark in [ 'W', 'S' ]:
    rslt = -rslt;
  return rslt;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def project( input ):

  inpstr = "";
  for ( lat, long ) in input:
    inpstr += "{0:3.5f}\t{1:2.5f}\n".format( long, lat );
  
  proj = Popen(
             "/usr/local/bin/proj +proj=moll +a=1000.0 +es=0.0 -m 1:1",
             shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE
           );
           
  ( stdoutdata_b, stderrdata_b ) = proj.communicate( inpstr.encode( "ascii" ) );
  
  stderrdata = None;
  if stderrdata_b is not None:
    stderrdata = stderrdata_b.decode( "ascii" );
  if stderrdata is not None:
    print( stderrdata );

  stdoutdata = None;
  if stdoutdata_b is not None:
    stdoutdata = stdoutdata_b.decode( "ascii" );
  
  outp = [];
  for line in stdoutdata.split( "\n" ):
    if line.find( "\t" ) != -1:
      ( long, lat ) = line.split( "\t" );
      long = int( float( long ) );
      lat = int( float( lat ) );
      outp.append( (lat,long) );
  
  return outp;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  
cities = [
    ( dms_to_float( LONDON[0] ), dms_to_float( LONDON[1] ) ),
    ( dms_to_float( PARIS[0] ), dms_to_float( PARIS[1] ) ),
    ( dms_to_float( BOSTON[0] ), dms_to_float( BOSTON[1] ) ),
    ( dms_to_float( NEW_YORK[0] ), dms_to_float( NEW_YORK[1] ) ),
    ( dms_to_float( SYDNEY[0] ), dms_to_float( SYDNEY[1] ) ),
    ( dms_to_float( TOKYO[0] ), dms_to_float( TOKYO[1] ) )
  ];

moll_cities = project( cities );

corners = [
    ( 0.0, 0.0 ),
    ( +45.0, 0.0 ),
    ( +90.0, 0.0 ),
    ( 0.0, +45.0 ),
    ( 0.0, +90.0 ),
    ( 0.0, +135.0 ),
    ( 0.0, +180.0 ),
  ];

moll_corners = project( corners );

( ( lat0, long0 ),
  ( lat45, x1 ),
  ( lat90, x2 ),
  ( x3, long45 ),
  ( x4, long90 ),
  ( x5, long135 ),
  ( x6, long180 ) ) = moll_corners;

assert long0 == x1 == x2;
assert lat0 == x3 == x4 == x5 == x6;

print( lat0 ); print( lat45 ); print( lat90 ); print( "--" );
print( long0 ); print( long45 ); print( long90 ); print( long135 ); print( long180 );


grid = [];

# meridians
for long in [ -180, 0, 180 ]:
  for lat in range( -90, +91 ):
    grid.append( ( float(lat), float(long) ) );

for long in [ -90, 90 ]:
  for lat in range( -90, +91 ):
    grid.append( ( float(lat), float(long) ) );

for long in [ -135, -45, +45, 135 ]:
  for lat in range( -90, +91 ):
    grid.append( ( float(lat), float(long) ) );

# parallels
for lat in [ 0 ]:
  for long in range( -180, 181 ):
    grid.append( ( float(lat), float(long) ) );

for lat in [ -45, 45 ]:
  for long in range( -180, 181 ):
    grid.append( ( float(lat), float(long) ) );

moll_grid = project( grid );

with open( "dta/vis/vis.svg", "wt" ) as f:
  
  print( '<?xml version="1.0"?>', file=f );
  print( '<svg width="1000px" height="500px" viewBox="{0} {1} {2} {3}"'.format(
             -long180, -lat90, 2*long180, 2*lat90
           ), file=f );
  print( '  xmlns="http://www.w3.org/2000/svg" version="1.2" baseProfile="tiny">',
         file=f );
         
  print( '<ellipse cx="{0}" cy="{1}" rx="{2}" ry="{3}" fill="grey" stroke="black" stroke-width="2"/>\n'.format( long0, lat0, long180, lat90 ),
         file=f );

  print( '<ellipse cx="{0}" cy="{1}" rx="{2}" ry="{3}" fill="grey" stroke="black" stroke-width="2"/>\n'.format( long0, lat0, long90, lat90 ),
         file=f );

  print( '<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="black" stroke-width="2"/>\n'.format( long0, lat90, long0, -lat90 ),
         file=f );
  
  #for ( y, x ) in moll_grid:
  #  print( '<circle cx="{0}" cy="{1}" r="3" fill="black" stroke="black" stroke-width="1"/>\n'.format( x, -y ),
  #         file=f );

  for ( y, x ) in moll_cities:
    print( '<circle cx="{0}" cy="{1}" r="30" fill="red" stroke="black" stroke-width="1"/>\n'.format( x, -y ),
           file=f );

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
