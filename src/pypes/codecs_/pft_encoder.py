# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTEncoder", "pft_encode",
            "argseq", "sortseq",
            "ALPHAS", "NUMS", "ALPHANUMS", "PRINTABLES" ];

import re;
import string;

from itertools import chain;

from pypes.utils.mc import subject;

from pypes.proto import *;
from pypes.proto.lambdaifier import sortseq;

from pypes.codecs_.pft_decoder import ALPHAS, NUMS, ALPHANUMS, PRINTABLES;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def argseq( int_ ):
  
  return "arg" + str(int_);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTEncoder( metaclass=subject ):


  def _enter_( self ):
    
    sig = ProtoSig();
    self.obj = lambdaify( self._obj_ )( sig=sig );

    self._assigned_sortvids = set();
    
    if hasattr( sig, "_sos_" ) and Variable in sig._sos_:
      for vid in sig._sos_[ Variable ]:
        var = sig._sos_[ Variable ][ vid ];
        self._assigned_sortvids.add( (var.sort,var.vid) );

    if hasattr( sig, "_sos_" ) and Sort in sig._sos_:
      self._assigned_sids = set( sig._sos_[ Sort ].keys() );
    else:
      self._assigned_sids = set();


  def _next_sid( self ):
    
    sid = 1;
    while sortseq( sid ) in self._assigned_sids:
      sid += 1;
    sid_ = sortseq( sid );
    self._assigned_sids.add( sid_ );
    return sid_;
  
  
  def _next_vid( self, sort ):
    
    vid = 1;
    while (sort,vid) in self._assigned_sortvids:
      vid += 1;
    self._assigned_sortvids.add( (sort,vid) );
    return vid;
  
  
  re_string = re.compile( "["+ALPHANUMS+"]+" );
  
  @classmethod
  def _fmt_string( cls, stri, sensitive=None ):
    
    if not isinstance( stri, str ):
      stri = str( stri );
    
    r = cls.re_string.match( stri )
    if r is not None and r.start() == 0 and r.end() == len( stri ):
      return stri;
    else:
      return repr( stri );
  
  
  re_identifier = re.compile( "["+ALPHAS+"]["+ALPHANUMS+"\.]*" );
  
  @classmethod
  def _fmt_identifier( cls, stri, sensitive=None ):

    if not isinstance( stri, str ):
      stri = str( stri );
    
    r = cls.re_identifier.match( stri );
    if r is not None and r.start() == 0 and r.end() == len( stri ):
      return stri;
    else:
      print( stri );
      assert False;


  def _encode_handle( self, inst ):
    
    if inst.hid is None:
      return "__";
    return str( inst.hid );


  def _encode_freezer( self, inst ):
    
    return "<" + self._encode( inst.content ) + ">";


  def _encode_variable( self, inst ):
    
    sid = None;
    if inst.sort.sid is None:
      sid = self._next_sid();
    else:
      sid = inst.sort.sid;
      
    vid = None;
    if inst.vid is None:
      vid = self._next_vid( inst.sort );
    else:
      vid = inst.vid;

    return str(sid) + str(vid);
  
  
  def _encode_feats( self, feats ):
    
    rslt = "";

    if feats:
      rslt += "["
      for feat in feats:
        rslt += " " + self._fmt_identifier( feat ) + "=" + \
                self._fmt_string( feats[feat] ) + ",";
      rslt = rslt[ :-1 ];
      rslt += " ]";
    
    return rslt;
  
  
  def _encode_operator( self, inst ):
    
    rslt = inst.otype;
    if inst.feats is not None:
      rslt += self._encode_feats( inst.feats );
    return rslt;
  
  
  def _encode_word( self, inst ):
    
    rslt = "|";
    if inst.lemma is not None:
      for lemtok in inst.lemma:
        rslt += self._fmt_string( lemtok ) + "+";
      rslt = rslt[ :-1 ];
    if inst.pos is not None or inst.sense is not None:
      rslt += "_";
      if inst.pos is not None:
        rslt += self._fmt_string( inst.pos );
      if inst.sense is not None:
        rslt += "_" + self._fmt_string( inst.sense );
    if inst.wid is not None:
      rslt += ":"+str(inst.wid);
    if inst.feats is not None:
      rslt += self._encode_feats( inst.feats );
    
    rslt += "|";
    
    return rslt;
  
  
  def _encode_argslist( self, predmod, args ):
    
    if hasattr( predmod, "_sos_" ) and Argument in predmod._sos_:
      assigned_aids = predmod._sos_[ Argument ].keys();
    else:
      assigned_aids = set();
    
    aid = 0;
    
    rslt = "(";
    
    if args:
      rslt += " ";
      for arg in args:
        var = args[ arg ];
        if arg.aid is None:
          while argseq(aid) in assigned_aids:
            aid += 1;
          rslt += self._fmt_identifier( argseq(aid) );
          aid += 1;
        else:
          rslt += self._fmt_identifier( arg.aid );
        rslt += "=" + self._encode( var );
        rslt += ", ";
      rslt = rslt[ :-2 ];
      rslt += " ";
      
    rslt += ")";
    
    return rslt;
      
  
  def _encode_predication( self, inst ):
    
    rslt = self._encode( inst.predicate.referent );
    rslt += self._encode_argslist( inst.predicate, inst.args );
    
    return rslt;
      
  
  def _encode_quantification( self, inst ):
    
    rslt = self._encode( inst.quantifier.referent );
    rslt += " " + self._encode( inst.var );
    rslt += " " + self._encode( inst.rstr );
    rslt += " " + self._encode( inst.body );
    
    return rslt;


  def _encode_modification( self, inst ):
    
    rslt = self._encode( inst.modality.referent );
    rslt += self._encode_argslist( inst.modality, inst.args );
    rslt += " " + self._encode( inst.scope );
    
    return rslt;


  def _encode_connection( self, inst ):
    
    rslt = self._encode( inst.lscope ) + " ";
    rslt += self._encode( inst.connective.referent );
    rslt += " " + self._encode( inst.rscope );
    
    return rslt;


  def _encode_constraint( self, inst ):
    
    return self._encode( inst.harg ) + " >> " + self._encode( inst.larg )


  def _encode_protoform( self, inst ):
    
    rslt = "{";
    
    if inst.subforms or inst.constraints:
      rslt += " ";
      
      roots = set();
      for key in inst.subforms:
        if key.hid is not None:
          roots.add( ( int(key.hid), key ) );
        else:
          roots.add( ( 0, key ) );
      
      for ( hid_, root ) in sorted( roots ):
        subform = inst.subforms[ root ];
        if root.hid is not None:
          rslt += self._encode( root ).rjust(3) + ": ";
        else:
          rslt += "     ";
        rslt += self._encode( subform ) + "; ";
      for constraint in inst.constraints:
        rslt += "     " + self._encode( constraint ) + "; ";
      rslt = rslt[ :-2 ];
      rslt += " ";
    
    rslt += "}";
    
    return rslt;


  def _encode( self, inst ):
    
    if isinstance( inst, Handle ):
      return self._encode_handle( inst );
    elif isinstance( inst, Freezer ):
      return self._encode_freezer( inst );
    elif isinstance( inst, Variable ):
      return self._encode_variable( inst );
    elif isinstance( inst, Word ):
      return self._encode_word( inst );
    elif isinstance( inst, Operator ):
      return self._encode_operator( inst );
    elif isinstance( inst, Predication ):
      return self._encode_predication( inst );
    elif isinstance( inst, Quantification ):
      return self._encode_quantification( inst );
    elif isinstance( inst, Modification ):
      return self._encode_modification( inst );
    elif isinstance( inst, Connection ):
      return self._encode_connection( inst );
    elif isinstance( inst, Constraint ):
      return self._encode_constraint( inst );
    elif isinstance( inst, ProtoForm ):
      return self._encode_protoform( inst );
    else:
      assert False;
  
  
  def _indent( self, stri ):
    
    rslt = "";
    indents = [];
    curindent = -1;
    
    for idx in range( 0, len(stri) ):
      
      rslt += stri[idx];
      curindent += 1;
      
      if stri[idx] == "{":
        indents.append( curindent );
      elif stri[idx] == "}":
        if indents:
          indents.pop();
      elif stri[idx] == ";":
        rslt += "\n";
        curindent = 0;
        if indents:
          rslt += ( " " * (indents[-1]+1) ); 
          curindent += indents[-1];
    
    return rslt;

  
  def encode( self ):
    
    return self._indent( self._encode( self._obj_ ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_encode( pfobj ):
  
  rslt = None;
  with PFTEncoder( pfobj ) as encoder:
    rslt = encoder.encode();
  return rslt;

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
