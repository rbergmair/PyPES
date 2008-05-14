import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.lattice;
import pyrmrs.smafpkg.token_edge;
import pyrmrs.smafpkg.pos_edge;

import re;

MAP = {
#  "&FO" : "UNC",
#  "$" : "POS"
};

wspan = re.compile( "(<w s=')([0-9]+)(' e=')([0-9]+)('>)(.*)(</w>)" );
number = re.compile( "([0-9]+)(\.[0-9]+(e[+-]?[0-9]+)?)?" );


def rasptagstr_to_smaf( surface, raspstr ):
  
  smaf = pyrmrs.smafpkg.smaf.SMAF();
  lattice = pyrmrs.smafpkg.lattice.Lattice();
  
  # print surface;
  
  min = None;
  max = None;
  
  utf8offs = [];
  i = 0;
  for ch in surface:
    utf8offs.append( i );
    if ord( ch ) >= 0x80:
      utf8offs.append( i );
      if ord( ch ) >= 0x800:
        utf8offs.append( i );
        if ord( ch ) >= 0x10000:
          utf8offs.append( i );
    i += 1;

  i = 1;
  peid = 1;
  
  for token in raspstr.split( "\n" ):
    
    m = wspan.search( token );
    if m is None:
      assert False;
    
    grps = m.groups();
      
#     print token;
#     print m.groups();
#     print len( m.groups() );
    
    s = int( grps[1] );
    e = int( grps[3] );
    tx2 = grps[ 5 ];
    
    pos_txt = token[ m.end( len(grps) ): ];
    pos_txt = pos_txt.strip();
    
#    print pos_txt;

    if min is None:
      min = s;
    max = e;

    s -= min;
    e -= min;
    
    s = utf8offs[s];
    e = utf8offs[e];

    e += 1;
      
    txt = surface[ s : e ];
    
    assert txt == tx2;
    
    edge = pyrmrs.smafpkg.token_edge.TokenEdge();
    
    edge.id = "t%d" % i;
    
    edge.source = "v%d" % (i-1);
    edge.target = "v%d" % i;
    edge.cfrom = s;
    edge.cto = e;
    
    edge.text = txt;

    lattice.register( edge );
    
    for postag in pos_txt.split(" "):
      
      postagspl = postag.split( ":" );
#      print postagspl;
      
      tag = postagspl[0];
      probtxt = postagspl[1];
      
      m = number.search( probtxt );
      prob = probtxt[ m.start(0) : m.end( len( m.groups() ) ) ];
      
      posedge = pyrmrs.smafpkg.pos_edge.PosEdge();
      
      posedge.id = "p%d" % peid;
      peid += 1;
      
      posedge.source = edge.source;
      posedge.target = edge.target;
      posedge.cfrom = edge.cfrom;
      posedge.cto = edge.cto;
      posedge.deps = edge.id;
      
      posedge.weight = prob;
      
      if MAP.has_key( tag ):
        posedge.tag = MAP[ tag ];
      else:
        posedge.tag = tag;
  
      lattice.register( posedge );

    i += 1;
  
  lattice.init = "v0";
  lattice.final = "v%d" % (i-1);
  lattice.cfrom = 0;
  lattice.cto = max-1;
  
  smaf.register( lattice );
  
  return smaf;
