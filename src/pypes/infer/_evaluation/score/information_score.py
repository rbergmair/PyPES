# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "InformationScore" ];

from pypes.utils.mc import object_;

from math import log;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class InformationScore( metaclass=object_ ):

  CSV_HEADER = "h(g),i(s|g),h(g2),i(s2|g2)";


  def _ent_gold( self, contingency_table ):

    ent = 0.0;
    for ref_dec in contingency_table:
      sum = 0;
      for obj_dec in contingency_table[ ref_dec ]:
        sum += contingency_table[ ref_dec ][ obj_dec ];
      prob = sum / self.covered;
      if prob > 0.0:
        ent += prob * log( prob, 2 );
    ent = -ent;
    return ent;


  def _ent_gold_giv_obj( self, contingency_table ):
    
    relent = 0.0;
    for obj_dec in contingency_table:
      sum = 0;
      for ref_dec in contingency_table:
        try:
          sum += contingency_table[ ref_dec ][ obj_dec ];
        except:
          print( contingency_table );
          raise;
      #print( str(obj_dec) + ":" + str(sum) );
      if sum > 0:
        relent_ = 0.0;
        for ref_dec in contingency_table:
          prob = contingency_table[ ref_dec ][ obj_dec ] / sum;
          #print( "  " + str(ref_dec) + ":" + str(prob) );
          if prob > 0.0:
            relent_ += prob * log( prob, 2 );
        relent_ = -relent_;
        #print( " " + str(obj_dec) + ":" + str(relent_) );
        relent += (float(sum)*relent_) / float(self.covered);
      
    return relent;
  
  
  def _mutinf( self, contingency_table ):
    
    eg = self._ent_gold( contingency_table );
    if eg is None:
      return None;
    
    eggo = self._ent_gold_giv_obj( contingency_table );
    if eggo is None:
      return None;
    
    return eg - eggo;


  @property
  def ent_gold( self ):

    if self._lblset != self._lblset_:
      return None;
    
    return self._ent_gold( self._contingency_table );


  @property
  def ent_gold_giv_obj( self ):

    if self._lblset != self._lblset_:
      return None;
    
    return self._ent_gold_giv_obj( self._contingency_table );


  @property
  def mutinf( self ):

    if self._lblset != self._lblset_:
      return None;
    
    return self._mutinf( self._contingency_table );


  @property
  def ent_gold_2w( self ):

    return self._ent_gold( self._collapse( self._contingency_table ) );


  @property
  def ent_gold_giv_obj_2w( self ):

    return self._ent_gold_giv_obj( self._collapse( self._contingency_table ) );


  @property
  def mutinf_2w( self ):
    
    return self._mutinf( self._collapse( self._contingency_table ) );


  def csv_data( self ):
    
    rslt = "";
    if self.ent_gold is not None:
      rslt += str( self.ent_gold );
      
    rslt += ",";
    if self.mutinf is not None:
      rslt += str( self.mutinf );

    rslt += ",";
    if self.ent_gold_2w is not None:
      rslt += str( self.ent_gold_2w );
      
    rslt += ",";
    if self.mutinf_2w is not None:
      rslt += str( self.mutinf_2w );
    
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
