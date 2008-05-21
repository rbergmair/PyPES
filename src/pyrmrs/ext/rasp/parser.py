import pyrmrs.config;
import pyrmrs.ext.basicio;

import pyrmrs.smafpkg.syntree_edge;


class Parser( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPPARSE + " -ot -u";
  CARET = "^ ^_^:1\n";
  EOB_MARKER_WRITE = 2 * CARET;
  EOB_MARKER_READ = "\n\n\n() -1 ; ()\n\n(X)\n\n";
  

  def configure( self ):
    
    pyrmrs.ext.basicio.BasicIO.configure( self );
    self.cmd += " -n %d" % self.no_parses;
    

  def __init__( self, no_parses=5 ):
    
    self.no_parses = no_parses;
    pyrmrs.ext.basicio.BasicIO.__init__( self );
    self.write_block( self.CARET, eob_marker="" );


  def parse( self, smaf ):
    
    node = smaf.lattice.init;
    
    parserinput = "";
    
    for (tok,posmorph) in smaf.getMorphs():
      line = tok.text;
      for (pos,morphs) in posmorph:
        if len( morphs ) == 0:
          line += " %s_%s:%s " % ( tok.text, pos.tag, pos.weight );
        else:
          for morph in morphs:
            line += " %s_%s:%s" % ( morph.text, pos.tag, pos.weight );
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
      newedge.weight = weights[i];
      newedge.tree = tree;
      smaf.lattice.register( newedge );

    return smaf;
