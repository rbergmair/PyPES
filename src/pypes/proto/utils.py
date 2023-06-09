# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "sanity_check",
            "recursion_check",
            "analyze_as_conjunction_pf",
            "sortseq" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.proto_processor import ProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def sanity_check( obj ):

  class SanityChecker( ProtoProcessor, metaclass=subject ):
    
    def __init__( self ):
      
      self._insane = False;
      super().__init__();
    
    def check( self ):
      
      self.process( self._obj_ );
      return not self._insane;
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      holes = set();
      for root in inst.roots:
        subform = inst.subforms[ root ];
        holes_ = set( subform.holes );
        assert len( holes_ ) == len( subform.holes );
        assert not holes_ & holes;
        holes |= holes_;
      
      if len( holes ) + 1 != len( inst.roots ):
        self._insane = True;
  
  rslt = None;
  with SanityChecker( obj ) as checker:
    rslt = checker.check();
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def analyze_as_conjunction_pf( pf ):
  
  conns = [];
  nonconns = [];
  for root in pf.roots:
    subform = pf.subforms[ root ];
    if not isinstance( subform, Connection ):
      nonconns.append( subform );
      continue;
    if not isinstance( subform.connective.referent, Operator ):
      nonconns.append( subform );
      continue;
    if not subform.connective.referent.otype == Operator.OP_C_WEACON:
      nonconns.append( subform );
      continue;
    if not ( isinstance( subform.lscope, Handle ) and isinstance( subform.rscope, Handle ) ):
      nonconns.append( subform );
      continue;
    if not ( subform.lscope.hid is None and subform.rscope.hid is None ):
      nonconns.append( subform );
      continue;
    conns.append( subform );
  
  if len( conns ) < 1:
    return None;
  
  if len( pf.constraints ) > 0:
    return None;
  
  if not len(conns) + 1 == len(nonconns):
    return None;
  
  return ( conns, nonconns );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def recursion_check( obj ):

  class RecursionChecker( ProtoProcessor, metaclass=subject ):
    
    def __init__( self ):
      
      self._insane = False;
      super().__init__();
    
    def check( self ):
      
      self.process( self._obj_ );
      return not self._insane;
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      if len( subforms ) == 1:
        return;
      
      if analyze_as_conjunction_pf( inst ) is None:
        self._insane = True;
  
  rslt = None;
  with RecursionChecker( obj ) as checker:
    rslt = checker.check();
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def sortseq( int_ ):

  SORT_CHARS = "cdfghklmnorstuvw";
  
  rslt = "";
  while int_ > 0:
    rest = int_ & 0xF;
    int_ = int_ >> 4;
    rslt += SORT_CHARS[ rest ];
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
