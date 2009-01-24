# -*-  coding: ascii -*-

__package__ = "pypes.codecs";
__all__ = [ "PFTEncoder" ];

import re;
import string;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTEncoder( metaclass=subject ):


  ANONYMOUS_CHARS = "cdfghklmnorstuvwCDFGHKLMNORSTUVW";
  ALPHANUMS = string.ascii_lowercase + string.ascii_uppercase + string.digits;
  
  
  def _enter_( self ):
    
    self._vid = 0;
    self._sid = 0;
    self._aid = 0;
  
  
  def _next_vid( self ):
    
    self._vid += 1;
    return self._vid;
  
  
  @classmethod
  def _anonymous_string( cls, int_ ):
    
    rslt = "";
    while int_ > 0:
      rest = int_ & 0x1F;
      int_ = int_ >> 5;
      rslt += cls.ANONYMOUS_CHARS[ rest ];
    return rslt;


  def _next_sid( self ):
    
    self._sid += 1;
    return self._anonymous_string( self._sid );
  
  
  def _next_aid( self ):
    
    self._aid += 1;
    return self._anonymous_string( self._aid );
  

  re_regstr = re.compile( "["+ALPHANUMS+"]+" );
  
  @classmethod
  def _fmt_str( cls, stri, sensitive=None ):
    
    if cls.re_regstr.match( stri ):
      return stri;
    else:
      return repr( stri );


  def _encode_handle( self, inst ):
    
    if inst.hid is None:
      return "__";
    return str( inst.hid );


  def _encode_variable( self, inst ):
    
    sid = None;
    if inst.sort.sid is None:
      sid = self._next_sid();
    else:
      sid = inst.sort.sid;
      
    vid = None;
    if inst.vid is None:
      vid = self._next_vid();
    else:
      vid = inst.vid;

    return str(sid) + str(vid);
  
  
  def _encode_word( self, inst ):
    
    rslt = "[";
    if inst.lemma is not None:
      rslt += self._fmt_str( inst.lemma );
    if inst.scf is not None:
      rslt += "+" + self._fmt_str( inst.scf );
    if inst.pos is not None or inst.sense is not None:
      rslt += "_";
      if inst.pos is not None:
        rslt += self._fmt_str( inst.pos );
      if inst.sense is not None:
        rslt += "_" + self._fmt_str( inst.sense );
    if inst.cfrom is not None or inst.cto is not None:
      rslt += ":";
      if inst.cfrom is not None:
        rslt += str(inst.cfrom);
      if inst.cto is not None:
        rslt += ":" + str(inst.cto);
    rslt += "]";
    
    return rslt;
  
  
  def _encode_argslist( self, inst ):
    
    rslt = "(";
    
    if inst:
      rslt += " ";
      for arg in inst:
        var = inst[ arg ];
        if arg.aid is None:
          rslt += self._next_aid();
        else:
          rslt += str( arg.aid );
        rslt += "=" + self._encode( var );
        rslt += ", ";
      rslt = rslt[ :-2 ];
      rslt += " ";
      
    rslt += ")";
    
    return rslt;
      
  
  def _encode_predication( self, inst ):
    
    rslt = "";
    if isinstance( inst.predicate.referent, Word ):
      rslt += self._encode( inst.predicate.referent );
    elif isinstance( inst.predicate.referent, Operator ):
      assert inst.predicate.referent.otype == Operator.OP_R_EQUALITY;
      rslt += "EQUALS";
    else:
      assert False;
    
    rslt += self._encode_argslist( inst.args );
    
    return rslt;
      
  
  def _encode_quantification( self, inst ):
    
    rslt = "";
    if isinstance( inst.quantifier.referent, Word ):
      rslt += self._encode( inst.quantifier.referent );
    elif isinstance( inst.quantifier.referent, Operator ):
      if inst.quantifier.referent.otype == Operator.OP_Q_UNIV:
        rslt += "ALL";
      elif inst.quantifier.referent.otype == Operator.OP_Q_EXIST:
        rslt += "SOME";
      elif inst.quantifier.referent.otype == Operator.OP_Q_DESCR:
        rslt += "THE";
      else:
        assert False;
    else:
      assert False;
    
    rslt += " " + self._encode( inst.var );
    rslt += " " + self._encode( inst.rstr );
    rslt += " " + self._encode( inst.body );
    
    return rslt;


  def _encode_modification( self, inst ):
    
    rslt = "";
    if isinstance( inst.modality.referent, Word ):
      rslt += self._encode( inst.modality.referent );
    elif isinstance( inst.modality.referent, Operator ):
      if inst.modality.referent.otype == Operator.OP_M_NECESSITY:
        rslt += "NECESSARILY";
      elif inst.modality.referent.otype == Operator.OP_M_POSSIBILITY:
        rslt += "POSSIBLY";
      else:
        assert False;
    else:
      assert False;
      
    rslt += self._encode_argslist( inst.args );
    rslt += " " + self._encode( inst.scope );
    
    return rslt;


  def _encode_connection( self, inst ):
    
    rslt = self._encode( inst.lscope ) + " ";
    
    if isinstance( inst.connective.referent, Word ):
      rslt += self._encode( inst.connective.referent );
    elif isinstance( inst.connective.referent, Operator ):
      if inst.connective.referent.otype == Operator.OP_C_WEACON:
        rslt += "/\\";
      elif inst.connective.referent.otype == Operator.OP_C_STRCON:
        rslt += "&&";
      elif inst.connective.referent.otype == Operator.OP_C_WEADIS:
        rslt += "\\/";
      elif inst.connective.referent.otype == Operator.OP_C_STRDIS:
        rslt += "||";
      elif inst.connective.referent.otype == Operator.OP_C_IMPL:
        rslt += "->";
      else:
        assert False;
    else:
      assert False;

    rslt += " " + self._encode( inst.rscope );
    
    return rslt;


  def _encode_constraint( self, inst ):
    
    return self._encode( inst.harg ) + " >> " + self._encode( inst.larg )


  def _encode_protoform( self, inst ):
    
    rslt = "{";
    
    if inst.subforms or inst.constraints:
      rslt += " ";
      for root in inst.subforms:
        subform = inst.subforms[ root ];
        if root.hid is not None:
          rslt += self._encode( root ) + ": ";
        rslt += self._encode( subform ) + "; ";
      for constraint in inst.constraints:
        rslt += self._encode( constraint ) + "; ";
      rslt = rslt[ :-2 ];
      rslt += " ";
    
    rslt += "}";
    
    return rslt;


  def _encode( self, inst ):
    
    return self._item_encoders[ inst.__class__ ]( self, inst );
  
  
  def _indent( self, stri ):
    
    rslt = "";
    indents = [];
    
    for idx in range( 0, len(stri) ):
      
      rslt += stri[idx];
      
      if stri[idx] == "{":
        indents.append( idx+1 );
      elif stri[idx] == "}":
        if indents:
          indents.pop();
      elif stri[idx] == ";":
        rslt += "\n";
        if indents:
          rslt += ( " " * indents[-1] );     
    
    return rslt;

  
  def encode( self ):
    
    return self._indent( self._encode( self._obj_ ) );
    


PFTEncoder._item_encoders = {
    Handle : PFTEncoder._encode_handle,
    Variable : PFTEncoder._encode_variable,
    Word : PFTEncoder._encode_word,
    Predication : PFTEncoder._encode_predication,
    Quantification : PFTEncoder._encode_quantification,
    Modification : PFTEncoder._encode_modification,
    Connection : PFTEncoder._encode_connection,
    Constraint : PFTEncoder._encode_constraint,
    ProtoForm : PFTEncoder._encode_protoform
  };
