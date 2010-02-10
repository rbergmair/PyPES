# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "AccuracyScore" ];

from pypes.utils.mc import object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class AccuracyScore( metaclass=object_ ):

  CSV_HEADER = "acc,acc2";


  def _accuracy( self, comp ):

    if self.covered == 0:
      return None;
    
    total = 0;
    correct = 0;
    
    for ref_dec in self.contingency_table:
      for obj_dec in self.contingency_table[ ref_dec ]:
        total += self.contingency_table[ ref_dec ][ obj_dec ];
        if comp( ref_dec, obj_dec ):
          correct += self.contingency_table[ ref_dec ][ obj_dec ];
    
    assert total == self.covered;
    return correct/total;


  @property
  def accuracy( self ):
    
    if self.lblset != self.lblset_:
      return None;
    
    return self._accuracy( lambda ref, obj: ref == obj );


  @property
  def accuracy_2w( self ):
    
    return self._accuracy(
               lambda ref, obj:
                 self.LBLSETs[ self._lblset_ ][ ref ] == \
                 self.LBLSETs[ self._lblset ][ obj ]
             );


  def csv_data( self ):
    
    rslt = "";
    if self.accuracy is not None:
      rslt += str( self.accuracy );
    
    rslt += ",";
    if self.accuracy_2w is not None:
      rslt += str( self.accuracy_2w );
    
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
