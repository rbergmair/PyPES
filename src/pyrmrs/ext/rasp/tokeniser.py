import pyrmrs.config;
import pyrmrs.ext.basicio;

import pyrmrs.smafpkg.token_edge;
import pyrmrs.smafpkg.lattice;

import re;



class Tokeniser( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPTOK + " -w";
  EOB_MARKER_WRITE = "^ \n";
  EOB_MARKER_READ = "^ ";

  WSPAN = re.compile( "(<w s=')([0-9]+)(' e=')([0-9]+)('>)(.*)" );
  NUMBER = re.compile( "(?:[0-9]+)(?:\.[0-9]+(?:e[\+\-]?[0-9]+)?)?" );

  
  def __init__( self ):
    
    pyrmrs.ext.basicio.BasicIO.__init__( self );
    self.invoke( "" );

  
  def tokenise( self, smaf ):
    
    surface = smaf.text;

    #utf8offs = [];
    
    #i = -1;
    #for ch in surface:
    #  i += 1;

    #  utf8offs.append( i );
    #  if ord( ch ) >= 0x80:
    #    utf8offs.append( i );
    #    if ord( ch ) >= 0x800:
    #      utf8offs.append( i );
    #      if ord( ch ) >= 0x10000:
    #        utf8offs.append( i );
    
    sent = smaf.text.replace( "^", "\021" );
    rslt = self.invoke( sent );
    rslt = rslt.replace( "\021", "^" );
    rslt = rslt[ :len(rslt)-1 ];
    
    
    mins = None;
    maxe = None;
    toks = [];
    
    spl = rslt.split( "</w> " );
    
    for token in spl[ :len(spl)-1 ]:
      
      m = self.WSPAN.match( token );
      if m is None:
        print token;
        assert False;
        
      grps = m.groups();
      
      s = int( grps[1] );
      e = int( grps[3] );
      txt = grps[ 5 ];
      
      if mins is None:
        mins = s;
      else:
        mins = min( s, mins );
      
      if maxe is None:
        maxe = e;
      else:
        maxe = max( e, maxe );
      
      toks.append( (s,e,txt) );
      

    lattice = pyrmrs.smafpkg.lattice.Lattice();
    i = -1;
    
    #mins_utf8 = None;
    #maxe_utf8 = None;
    
    
    for (s,e,txt) in toks:
      
      i += 1;
      
      s -= mins;
      e -= mins;

      #s = utf8offs[s];
      #e = utf8offs[e];

      e += 1;
      
      #if mins_utf8 is None:
      #  mins_utf8 = s;
      #else:
      #  mins_utf8 = min( s, mins_utf8 );
      
      #if maxe_utf8 is None:
      #  maxe_utf8 = e;
      #else:
      #  maxe_utf8 = max( e, maxe_utf8 );
      
      try:
        assert surface[s:e] == txt;
      except:
        print s;
        print e;
        print "\"%s\"" % surface[s:e];
        print "\"%s\"" % txt;
        raise;
      
      edge = pyrmrs.smafpkg.token_edge.TokenEdge();
      
      edge.id = "t%d" % i;
      
      edge.source = "v%d" % i;
      edge.target = "v%d" % (i+1);
      edge.cfrom = s;
      edge.cto = e;
      
      edge.text = txt;
  
      lattice.register( edge );
      
    #assert mins_utf8 == 0;

    lattice.init = "v0";
    lattice.final = "v%d" % (i+1);
    lattice.cfrom = 0;
    #lattice.cto = maxe_utf8;
    lattice.cto = maxe - mins + 1;
    smaf.register( lattice );
    
    smaf.cfrom = smaf.lattice.cfrom;
    smaf.cto = smaf.lattice.cto;
    
    return smaf;
