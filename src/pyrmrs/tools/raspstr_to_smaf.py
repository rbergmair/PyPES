import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.lattice;
import pyrmrs.smafpkg.token_edge;
import pyrmrs.smafpkg.pos_edge;

import re;

MAP = {
  "&FO" : "UNC",
  "$" : "POS"
};

def raspstr_to_smaf( surface, raspstr ):
  
  smaf = pyrmrs.smafpkg.smaf.SMAF();
  lattice = pyrmrs.smafpkg.lattice.Lattice();
  
  raspstr = raspstr[ : raspstr.find( "\n" ) ];
  
  print surface;
  
  min = None;
  max = None;
  
  utf8offs = [];
  i = 0;
  for ch in surface:
    utf8offs.append( i );
    if ord( ch ) > 127:
      utf8offs.append( i );
    i += 1;

  i = 1;
  
  for token in raspstr.split( "|" ):
    
    if not ( token.find( "<w s='" ) == 0 and token.endswith( "</w>" ) ):
      continue;
    
    r = re.compile( "(<w s=')([0-9]+)(' e=')([0-9]+)('>.*_)(.*)(</w>)" );
    m = r.match( token );
    if m is None:
      assert False;
    else:
      
      s = int( m.groups()[ 1 ] );
      e = int( m.groups()[ 3 ] );
      pos = m.groups()[ 5 ];

      if min is None:
        min = s;
      max = e;

      s -= min;
      e -= min;

      s = utf8offs[s];
      e = utf8offs[e];

      e += 1;
        
      txt = surface[ s : e ];
      
      edge = pyrmrs.smafpkg.token_edge.TokenEdge();
      edge.id = "t%d" % i;
      edge.source = "v%d" % (i-1);
      edge.target = "v%d" % i;
      edge.cfrom = s;
      edge.cto = e;
      edge.text = txt;

      lattice.register( edge );
      
      posedge = pyrmrs.smafpkg.pos_edge.PosEdge();
      posedge.id = "p%d" % i;
      posedge.source = edge.source;
      posedge.target = edge.target;
      posedge.cfrom = edge.cfrom;
      posedge.cto = edge.cto;
      posedge.deps = edge.id;
      if MAP.has_key( pos ):
        posedge.tag = MAP[ pos ];
      else:
        posedge.tag = pos;

      lattice.register( posedge );

      i += 1;
  
  lattice.init = "v0";
  lattice.final = "v%d" % (i-1);
  lattice.cfrom = 0;
  lattice.cto = max;
  
  smaf.register( lattice );
  
  return smaf;