# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTEncoder", "pft_encode", "argseq", "sortseq" ];

import re;
import string;

from itertools import chain;

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.rewriting.renaming_rewriter import renaming_rewrite, sortseq;

from pypes.codecs_.pft import _pft_parser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def argseq( int_ ):
  
  return "arg" + str(int_);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTEncoder( ProtoProcessor, metaclass=subject ):


  def _initialize( self ):

    self._assigned_sortvids = set();
    self._assigned_sids = set();
    
    if not self._fast_initialize:
      
      sig = ProtoSig();
      obj_ = renaming_rewrite(
                 self._obj_,
                 force_rename_handles_p = self._pretty
               );
      self._obj_ = obj_( sig=sig );
      
      if hasattr( sig, "_sos_" ) and Variable in sig._sos_:
        for vid in sig._sos_[ Variable ]:
          var = sig._sos_[ Variable ][ vid ];
          self._assigned_sortvids.add( (var.sort,var.vid) );
  
      if hasattr( sig, "_sos_" ) and Sort in sig._sos_:
        self._assigned_sids = set( sig._sos_[ Sort ].keys() );


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


  re_alphanum = re.compile( _pft_parser.PFTParser.RE_ALPHANUMs );
  
  @classmethod
  def _fmt_alphanum( cls, stri ):
    
    r = cls.re_alphanum.match( stri );
    assert r is not None;
    
    return stri;
  
  
  @classmethod
  def _fmt_quoted( cls, stri ):
    
    r = repr( stri );
    if r[0] != "'" and r[0] != '"':
      r = "'" + r + "'";
    return r;
  
  
  @classmethod
  def _fmt_lemma( cls, stri, sensitive=None ):
    
    if not isinstance( stri, str ):
      stri = str( stri );
    
    r = cls.re_alphanum.match( stri )
    if r is not None and r.start() == 0 and r.end() == len( stri ):
      return stri;
    else:
      return cls._fmt_quoted( stri );
  
  
  re_identifier = re.compile( _pft_parser.PFTParser.RE_IDENTIFIER );
  
  @classmethod
  def _fmt_identifier( cls, stri, sensitive=None ):

    if not isinstance( stri, str ):
      stri = str( stri );
    
    r = cls.re_identifier.match( stri );
    if r is not None and r.start() == 0 and r.end() == len( stri ):
      return stri;
    
    print( stri );
    assert False;


  re_word = re.compile( _pft_parser.PFTParser.RE_WORD );

  @classmethod
  def _fmt_word( cls, stri ):
    
    r = cls.re_word.match( stri );
    try:
      assert r is not None;
    except:
      print( stri );
      raise;
    
    return stri;
  
  
  def _process_handle( self, inst, hid ):
    
    if hid is None:
      return "__";
    return str( hid );


  def _process_freezer( self, content, freezelevel ):
    
    if freezelevel <= 0:
      return content;
    else:
      return "<" + content + ">";


  def _process_variable( self, inst, sid, vid ):
    
    if sid is None:
      sid = self._next_sid();
      
    if vid is None:
      vid = self._next_vid( inst.sort );

    return str(sid) + str(vid);


  def _process_constant( self, inst, ident ):
    
    return self._fmt_quoted( ident );
  
  
  def _process_feats( self, feats ):

    if self._pretty:
      return "";
    
    rslt = "";

    if feats:
      rslt += "["
      for feat in feats:
        rslt += " " + self._fmt_identifier( feat ) + "=" + \
                self._fmt_quoted( feats[feat] ) + ",";
      rslt = rslt[ :-1 ];
      rslt += " ]";
    
    return rslt;
  
  
  def _process_operator( self, inst, otype, feats ):
    
    rslt = otype;
    if feats is not None:
      rslt += self._process_feats( feats );
    return rslt;
  
  
  def _process_word( self, inst, wid, lemma, pos, sense, feats ):
    
    rslt = "|";
    if lemma is not None:
      for lemtok in lemma:
        rslt += self._fmt_lemma( lemtok ) + "+";
      rslt = rslt[ :-1 ];
    if pos is not None or sense is not None:
      rslt += "_";
      if pos is not None:
        rslt += self._fmt_alphanum( pos );
      if sense is not None:
        rslt += "_" + self._fmt_alphanum( sense );
    if wid is not None:
      rslt += ":" + str(wid);
    rslt += "|";
    rslt = self._fmt_word( rslt );
    if feats is not None:
      rslt += self._process_feats( feats );
    
    return rslt;


  def _process_argument( self, inst, aid ):
    
    return inst;
  
  
  def _process_argslist( self, predmod, args_ ):
    
    if hasattr( predmod, "_sos_" ) and Argument in predmod._sos_:
      assigned_aids = predmod._sos_[ Argument ].keys();
    else:
      assigned_aids = set();
    
    args = [];
    aid = 0;
    
    for (arg,var) in args_.items():
      if arg.aid is None:
        while argseq(aid) in assigned_aids:
          aid += 1;
        args.append( ( argseq(aid), arg, var ) );
        aid += 1;
      else:
        args.append( ( arg.aid, arg, var ) );

    rslt = "(";
    
    if args:
      rslt += " ";
      for (aid,arg,var) in sorted( args ):
        rslt += self._fmt_identifier( aid );
        rslt += "=" + var;
        rslt += ", ";
      rslt = rslt[ :-2 ];
      rslt += " ";
      
    rslt += ")";
    
    return rslt;
      

  def _process_predicate( self, inst, referent ):
    
    return referent;
  
  def _process_predication( self, inst, predicate, args ):
    
    rslt = "\ue100 ";
    rslt += predicate;
    rslt += self._process_argslist( inst.predicate, args );
    
    return rslt;
      

  def _process_quantifier( self, inst, referent ):
    
    return referent;
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    rslt = "\ue101 ";
    rslt += quantifier;
    rslt += " " + var;
    rslt += " " + rstr;
    rslt += " " + body;
    
    return rslt;


  def _process_modality( self, inst, referent ):
    
    return referent;

  def _process_modification( self, inst, modality, args, scope ):
    
    rslt = "\ue102 ";
    rslt += modality;
    rslt += self._process_argslist( inst.modality, args );
    rslt += " " + scope;
    
    return rslt;


  def _process_connective( self, inst, referent ):
    
    return referent;

  def _process_connection( self, inst, connective, lscope, rscope ):
    
    rslt = "\ue103 ";
    rslt += lscope + " ";
    rslt += connective;
    rslt += " " + rscope;
    
    return rslt;


  def _process_constraint( self, inst, harg, larg ):
    
    rslt = "\ue104 ";
    rslt += harg;
    rslt += " ^ ";
    rslt += larg;
    
    return rslt;


  def _process_protoform( self, inst, subforms, constraints ):
    
    rslt = "{";
    
    labeled = False;
    for ( root, subform ) in subforms:
      if root != "__":
        labeled = True;
        break;
    
    if inst.subforms or inst.constraints:
      rslt += " ";
      
      for ( root, subform ) in subforms:
        if root != "__":
          rslt += root.rjust(2) + ": ";
        elif labeled:
          rslt += "    ";
          pass;
        rslt += subform + "; ";
      for constraint in constraints:
        rslt += "    " + constraint + "; ";
      rslt = rslt[ :-2 ];
      rslt += " ";
    
    rslt += "}";
    
    return rslt;
  
  
  def _format( self, stri ):
    
    if not self._pretty and not self._linebreaks:
      return stri;
    
    rslt = "";
    indents = [];
    curindent = -1;
    
    skip = False;
    
    for idx in range( 0, len(stri) ):
      
      ch = stri[idx];
      
      if self._pretty:
        if ch in { "\ue100", "\ue101", "\ue102", "\ue103", "\ue104" }:
          skip = True;
          continue;
      
      if skip:
        skip = False;
        continue;
      
      rslt += ch;
      curindent += 1;
      
      if ch == "{":
        indents.append( curindent );
      elif ch == "}":
        if indents:
          indents.pop();
      elif ch == ";":
        rslt += "\n";
        curindent = 0;
        if indents:
          rslt += ( " " * (indents[-1]+1) ); 
          curindent += indents[-1];
    
    return rslt;

  
  def encode( self, pretty=True, fast_initialize=False, linebreaks=True ):
    
    if pretty:
      self._pretty = True;
      self._fast_initialize = False;
      self._linebreaks = True;
    else:
      self._pretty = False;
      self._fast_initialize = fast_initialize;
      self._linebreaks = linebreaks;
    
    self._initialize();
    r = self.process( self._obj_ );
    return self._format( r );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_encode( pfobj, pretty=True, fast_initialize=False, linebreaks=True ):
  
  rslt = None;
  with PFTEncoder( pfobj ) as encoder:
    rslt = encoder.encode(
               pretty = pretty,
               fast_initialize = fast_initialize,
               linebreaks = linebreaks
             );
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
