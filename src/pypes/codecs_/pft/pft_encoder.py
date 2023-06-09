# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTEncoder", "pft_encode", "argseq" ];

import re;
import string;

from itertools import chain;

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.rewriting.renamer import rename;

from pypes.codecs_.pft import _pft_parser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def argseq( int_ ):
  
  return "arg" + str(int_);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTEncoder( LambdaifyingProcessor, metaclass=subject ):


  def _initialize( self ):

    self._assigned_sortvids = set();
    self._assigned_sids = set();
    
    if not self._fast_initialize:
      
      sig = ProtoSig();
      self._obj_ = rename(
                 self._obj_,
                 force_rename_handles_p = self._pretty
               );
      
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


  re_alphanum = re.compile( _pft_parser.PFTDecoder._RE_ALPHANUMs );
  
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
  
  
  re_identifier = re.compile( _pft_parser.PFTDecoder._RE_IDENTIFIER );
  
  @classmethod
  def _fmt_identifier( cls, stri, sensitive=None ):

    if not isinstance( stri, str ):
      stri = str( stri );
    
    r = cls.re_identifier.match( stri );
    if r is not None and r.start() == 0 and r.end() == len( stri ):
      return stri;
    
    print( stri );
    assert False;


  re_word = re.compile( _pft_parser.PFTDecoder._RE_WORD );

  @classmethod
  def _fmt_word( cls, stri ):
    
    r = cls.re_word.match( stri );
    try:
      assert r is not None;
    except:
      print( stri );
      raise;
    
    return stri;
  
  
  def process_handle_( self, inst, hid ):
    
    if hid is None:
      return "__";
    return str( hid );


  def process_freezer_( self, content, freezelevel ):
    
    if freezelevel <= 0:
      return content;
    else:
      return "<" + content + ">";


  def process_variable_( self, inst, sort, vid ):
    
    sid = inst.sort.sid;
    if sid is None:
      sid = self._next_sid();
      
    if vid is None:
      vid = self._next_vid( sort );

    return str(sid) + str(vid);


  def process_constant_( self, inst, ident ):
    
    return self._fmt_quoted( ident );
  
  
  def process_feats_( self, feats ):

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
  
  
  def process_operator_( self, inst, otype ):
    
    rslt = otype;
    return rslt;
  
  
  def process_word_( self, inst, lemma, pos, sense ):
    
    # TODO: check this
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
    rslt += "|";
    rslt = self._fmt_word( rslt );
    
    return rslt;


  def process_argument_( self, inst, aid ):
    
    return inst;
  
  
  def process_argslist_( self, predmod, args_ ):
    
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
      
      args.sort();
      
      idx = None;
      val = None;
      
      for i in range( 0, len(args) ):
        (aid,arg,var) = args[i];
        if aid == "KEY":
          idx = i;
          val = (aid,arg,var);
          
      if idx is not None:
        del args[ idx ];
        args.insert( 0, val );
      
      rslt += " ";
      for (aid,arg,var) in args:
        rslt += self._fmt_identifier( aid );
        rslt += "=" + var;
        rslt += ", ";
      rslt = rslt[ :-2 ];
      rslt += " ";
      
    rslt += ")";
    
    return rslt;
      

  def process_functor_( self, inst, fid, referent, feats ):
    
    rslt = referent;
    if inst.fid is not None:
      rslt += ":" + str(inst.fid);
    if feats is not None:
      rslt += self.process_feats_( feats );
    return rslt;

  
  def process_predication_( self, inst, subform, predicate, args ):
    
    rslt = "\ue100 ";
    rslt += predicate;
    rslt += self.process_argslist_( predicate, args );
    
    return rslt;

  
  def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
    
    rslt = "\ue101 ";
    rslt += quantifier;
    rslt += " " + var;
    rslt += " " + rstr;
    rslt += " " + body;
    
    return rslt;


  def process_modification_( self, inst, subform, modality, args, scope ):
    
    rslt = "\ue102 ";
    rslt += modality;
    rslt += self.process_argslist_( modality, args );
    rslt += " " + scope;
    
    return rslt;


  def process_connection_( self, inst, subform, connective, lscope, rscope ):
    
    rslt = "\ue103 ";
    rslt += lscope + " ";
    rslt += connective;
    rslt += " " + rscope;
    
    return rslt;


  def process_constraint_( self, inst, harg, larg ):
    
    rslt = "\ue104 ";
    rslt += harg;
    rslt += " ^ ";
    rslt += larg;
    
    return rslt;


  def process_protoform_( self, inst, subform, subforms, constraints ):
    
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
    
    def _lookahead( idx ):
      
      i = idx+1;
      while True:
        if i >= len(stri):
          return None;
        ch = stri[i];
        if ch.isspace():
          i += 1;
          continue;
        return ch;
    
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
      if ch == "}":
        if indents:
          indents.pop();
      la = _lookahead( idx );
      if ch == ";" or ( ch == "}" and la not in { ";", "}", "_" } ):
        rslt += "\n";
        curindent = 0;
        if indents:
          rslt += ( " " * (indents[-1]+1) ); 
          curindent += indents[-1];
          if ch == "}" and la == "{":
            rslt += "  ";
            curindent += 2;
    
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
