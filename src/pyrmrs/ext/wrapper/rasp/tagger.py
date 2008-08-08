import os;
import re;

import pyrmrs.globals;

import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;

import pyrmrs.smafpkg.pos_edge;



class Tagger( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPTAG + " O60";
  EOB_MARKER_WRITE = " ^ \n";
  EOB_MARKER_READ = "\n^ ^:1\n";

  NUMBER = re.compile( "(?:[0-9]+)(?:\.[0-9]+(?:e[\+\-]?[0-9]+)?)?" );
  
  
  def configure( self ):
    
    pyrmrs.ext.wrapper.basicio.BasicIO.configure( self );

    LDLP = "LD_LIBRARY_PATH";
    
    self.env = {};
    if os.environ.has_key( LDLP ):
      self.env[ LDLP ] = os.environ[ LDLP ] + ":";
    else:
      self.env[ LDLP ] = "";
    self.env[ LDLP ] += pyrmrs.config.DIR_RASPTAG_LDLP;
 
  
  def tokstr_to_tagstr( self, tokstr ):
    
    txt = tokstr.replace( "^", "\021" );
    rslt = self.invoke( txt );
    return rslt.replace( "\021", "^" );
  
  
  def tag( self, smaf ):
    
    toks = [];
    toks_str = u"";
    for alt_tokens in smaf.getTokens():
      assert len( alt_tokens ) == 1;
      for token in alt_tokens:
        tok = u"<w s='%d' e='%d'>%s" % ( token.cfrom, token.cto, token.text );
        toks_str += tok + u"</w> ";
        toks.append( tok );
      
    rslt = self.invoke( toks_str );
    
    #print rslt;
    #return smaf;
  
    rslt_toks = rslt.split( "\n" );
    
    assert len( rslt_toks ) == len( toks );

    tok_edges = smaf.getTokens();
    peid = 0;
    
    for i in range( 0, len(rslt_toks) ):

      alt_tok_edges = tok_edges.next();
      assert len( alt_tok_edges ) == 1;
      
      for tok_edge in alt_tok_edges:
        
        tok = toks[i];
        rslt_tok = rslt_toks[i];
        rslt_tok_spl = rslt_toks[i].split( "</w> " );
        rslt_tok_txt = rslt_tok_spl[0];
        rslt_tok_tags = rslt_tok_spl[1];
        rslt_tok_tags_spl = rslt_tok_tags.split( " " );
        
        assert tok == rslt_tok_txt;
        assert "<w s='%d' e='%d'>%s" % ( tok_edge.cfrom, tok_edge.cto, tok_edge.text ) == rslt_tok_txt;
        
        for postag in rslt_tok_tags_spl:
          
          r = postag.rfind( ":" );
          #postagspl = postag.split( ":" );
          tag = postag[:r];
          #tag = postagspl[0];
          probtxt = postag[r+1:];
          #probtxt = postagspl[1];
          
          m = self.NUMBER.search( probtxt );
          try:
            assert not m is None;
          except AssertionError, e:
            pyrmrs.globals.logDebug( self, "failed to find number in |>%s<|" % probtxt );
            raise e;
            
          prob = m.group();
          
          posedge = pyrmrs.smafpkg.pos_edge.PosEdge();
          
          posedge.id = "p%d" % peid;
          peid += 1;
          
          posedge.source = tok_edge.source;
          posedge.target = tok_edge.target;
          posedge.cfrom = tok_edge.cfrom;
          posedge.cto = tok_edge.cto;
          posedge.deps = tok_edge.id;
          
          posedge.weight = prob;
          posedge.tag = tag;
      
          smaf.lattice.register( posedge );
    
    return smaf;
