import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;

import pyrmrs.smafpkg.syntree_edge;


class Parser( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPPARSE + " -ot -u";
  CARET = "^ ^_^:1\n";
  EOB_MARKER_WRITE = 2 * CARET;
  EOB_MARKER_READ = "\n\n\n() -1 ; ()\n\n(X)\n\n";
  

  def configure( self ):
    
    pyrmrs.ext.wrapper.basicio.BasicIO.configure( self );
    self.cmd += " -n %d" % self.no_parses;
    

  def __init__( self, no_parses=5 ):
    
    self.no_parses = no_parses;
    pyrmrs.ext.wrapper.basicio.BasicIO.__init__( self );
    self.write_block( self.CARET, eob_marker="" );


  def parse( self, smaf ):
    
    node = smaf.lattice.init;
    
    parserinput = "";
    
    for alt_toks in smaf.getTokens():
      assert len( alt_toks ) == 1;
      for tok in alt_toks:
        line = tok.text;
        for tag in smaf.getTags( tok ):
          morphs = smaf.getMorphs( tag );
          if len( morphs ) == 0:
            line += " <w s='%d' e='%d'>%s_%s:%s</w>" % ( tok.cfrom, tok.cto, tok.text, tag.tag, tag.weight );
          else:
            for morph in morphs:
              line += " <w s='%d' e='%d'>%s_%s:%s</w>" % ( tok.cfrom, tok.cto, morph.text, tag.tag, tag.weight );
        parserinput += line+"\n";
    
    #parserinput = parserinput[ : len(parserinput) - 1 ];
    #print parserinput;
    rslt = self.invoke( parserinput );
    if rslt[0] == "\n":
      rslt = rslt[1:];
      
    r = rslt.find("\n");
    firstline = rslt[ :r ];
    rest = rslt[ r+1: ];
    r = firstline.find(" ; ");
    weights = firstline[ r+3: ];
    assert weights[0] == "(";
    assert weights[len(weights)-1] == ")";
    weights = weights[ 1 : len(weights)-1 ];
    weights = weights.split( " " );
      
    #print "|>%s<|" % weights;
    
    sid = 0;
    
    for i in range( 0, len(weights) ):
      
      start_indicator = "tree-rasp: %d\n" % (i+1);
      startidx = rest.find( start_indicator );
      startidx += len( start_indicator );
      endidx = len( rest );
      if i+1 < len(weights):
        endidx = rest.find( "\ntree-rasp: %d" % (i+2) );
        
      tree = rest[ startidx : endidx ];
      assert tree[0] == "(";
      assert tree[len(tree)-1] == ")";
      
      newedge = pyrmrs.smafpkg.syntree_edge.SyntaxTreeEdge();
      
      newedge.id = "s%d" % sid;
      sid += 1;

      newedge.source = smaf.lattice.init;
      newedge.target = smaf.lattice.final;
      newedge.cfrom = smaf.lattice.cfrom;
      newedge.cto = smaf.lattice.cto;
      
      newedge.weight = weights[i];
      newedge.tree = tree;
      
      smaf.lattice.register( newedge );

    return smaf;
