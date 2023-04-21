# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";

from os import listdir;

from copy import copy;

from pypes.utils.mc import subject;

import random;

from pypes.infer._evaluation.bowexp import read_concat_results;
from pypes.infer._evaluation.score import Score;



class Mapper( metaclass=subject ):

  def __init__( self ):
    
    ( self._gold, self._bsl ) = self._obj_;

    assert self._gold.keys() == self._bsl.keys();
    
    self.ids_agree = set();
    self.ids_disagree = set();
    
    self.golddec = {};
    self.bsldec = {};
    self.refdec = {};
    
    for id in self._gold:
      
      gdec = self._gold[ id ];
      bdec = self._bsl[ id ];
      
      if gdec == bdec:
        self.ids_agree.add( id );
        self.refdec[ id ] = gdec; 
      else:
        self.ids_disagree.add( id );
        self.bsldec[ id ] = bdec;
        self.golddec[ id ] = gdec;
  
  
  def map( self, obj, subj=None ):
    
    if subj is None:
      subj = self.golddec;
    
    x = 0;
    y = 0;

    for ( id, dec ) in self.refdec.items():
      pdec = obj[ id ];
      if pdec != dec:
        x += 1;
  
    for ( id, dec ) in subj.items():
      pdec = obj[ id ];
      if pdec != dec:
        y += 1;
    
    return (x,y);



class Visualizer( metaclass=subject ):
  
  DISCRETIZATION = 3;
  
  def __init__( self, width, height ):
    
    self._datawidth = width;
    self._dataheight = height;
    
    self._width = ( ( self._datawidth // self.DISCRETIZATION ) + 1 ) * self.DISCRETIZATION;
    self._height = ( ( self._dataheight // self.DISCRETIZATION ) + 1 ) * self.DISCRETIZATION;
  
  def _enter_( self ):
    
    print( '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>', file=self._obj_ ); 
    print( '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"', file=self._obj_ ); 
    print( '  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">', file=self._obj_ ); 
      
    print( '<svg width="{0:d}px" height="{1:d}px" viewBox="0 0 {0:d} {1:d}"'.format(
               self._width, self._height
             ), file=self._obj_ );
    print( '  xmlns="http://www.w3.org/2000/svg" version="1.1" baseProfile="tiny">\n',
           file=self._obj_ );
  
  def draw( self, point, color="black", comment=None ):
    
    (x,y) = point;

    x //= self.DISCRETIZATION;
    y //= self.DISCRETIZATION;
    x *= self.DISCRETIZATION;
    y *= self.DISCRETIZATION;
    
    if comment is not None:
      print( '<!-- {0} -->'.format( comment ), file=self._obj_ );

    print( '<rect x="{0}" y="{1}" width="{2}" height="{2}" fill="{3}"/>\n'.format(
               x, y, self.DISCRETIZATION, color
             ),
           file=self._obj_ );
  
  def draw_raster( self ):
    
    step = ( self._datawidth + self._dataheight ) / 33;
    for i in range( 0, 34 ):
      self.draw( ( (i*step) / 2, (i*step) / 2 ), color="red" );
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
     self.draw( (0,0), color="green", comment="GOLD STANDARD" );
     self.draw( (0,height), color="blue", comment="BASELINE" );
     self.draw( (width,0), color="red" );
     self.draw( (width,height), color="red" );
    
     print( '</svg>', file=self._obj_ );
    


def read_vec_from_files( name ):
  
  ( lblset, data ) = read_concat_results(
                         [ "08-ie", "08-qa", "08-ir", "08-sum" ],
                         name
                       );
  lblset = Score.LBLSETs[ lblset ];
  
  vec = {};
  for ( id, (label,conf,attrs) ) in data.items():
    val = lblset[ label ];
    assert val in [0,1]; 
    vec[ id ] = val;
          
  return vec;



gold = read_vec_from_files( "gold" );
bsl = read_vec_from_files( "BOWAgent" );


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
  
realdata_vecs = {};
for name in names:
  realdata_vecs[ name ] = read_vec_from_files( name ); 
  
realdata_gold_deviation = {};
realdata_bsl_deviation = {};

with Mapper( (gold,bsl) ) as mapper:

  width = len(mapper.ids_agree);
  height = len(mapper.ids_disagree);
  
  with open( "dta/infer/vis/vis-color.svg", "wt", encoding="utf-8" ) as f:
    with open( "dta/infer/vis/vis.svg", "wt", encoding="utf-8" ) as g:
      with Visualizer( f, width=width, height=height ) as viscolor:
        with Visualizer( g, width=width, height=height ) as vis:
          for name in sorted( realdata_vecs.keys() ):
            
            point = realdata_vecs[ name ];
            (x,y) = mapper.map(point);
            
            color = "black";
            if name.startswith( "lcc" ):
              color = "cyan";
            if name.startswith( "uaic" ):
              color = "magenta";
            if name.startswith( "dfki" ):
              color = "yellow";
            if name.startswith( "oaqa" ):
              color = "brown";
            if name.startswith( "quanta" ):
              color = "sandybrown";
            
            viscolor.draw( (x,y), comment=name, color=color );
            vis.draw( (x,y), comment=name );
            
            realdata_gold_deviation[ name ] = x+y;
            
            (x,y) = mapper.map( point, subj=mapper.bsldec );
            realdata_bsl_deviation[ name ] = x+y;
  
  random.seed( 0 );

  with open( "dta/infer/vis/raster.svg", "wt", encoding="utf-8" ) as f:
    with Visualizer( f, width=width, height=height ) as vis:
      vis.draw_raster();

  with open( "dta/infer/vis/ctrl1.svg", "wt", encoding="utf-8" ) as f:
    with Visualizer( f, width=width, height=height ) as vis:
      for name in realdata_vecs:
        devcnt = realdata_gold_deviation[ name ];
        point = copy( gold );
        sample = set( random.sample( point.keys(), devcnt ) );
        for id in sample:
          point[ id ] = int( not point[ id ] );
        (x,y) = mapper.map(point);
        vis.draw( (x,y) );

  random.seed( 0 );

  with open( "dta/infer/vis/ctrl2.svg", "wt", encoding="utf-8" ) as f:
    with Visualizer( f, width=width, height=height ) as vis:
      for name in realdata_vecs:
        devcnt = realdata_bsl_deviation[ name ];
        point = copy( bsl );
        sample = set( random.sample( point.keys(), devcnt ) );
        for id in sample:
          point[ id ] = int( not point[ id ] );
        (x,y) = mapper.map(point);
        vis.draw( (x,y) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
