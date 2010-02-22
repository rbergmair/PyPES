# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "InformationScore" ];

from pypes.utils.mc import object_;

from math import log;

from pypes.infer._evaluation.score.information_score import InformationScore;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class InformationScoreValVSRel( InformationScore, metaclass=object_ ):

  CSV_HEADER = InformationScore.CSV_HEADER + \
                 ",h(g2_1),h(s2_1),i(s2_1;g2_1)" + \
                 ",h(g2_2),h(s2_2),i(s2_2;g2_2)" + \
                 ",h(g2_3),h(s2_3),i(s2_3;g2_3)";
  
  LBLSET1 = {
      "entailment":0,
      "unknown":1,
      "contradiction":1
    };

  LBLSET2 = {
      "entailment":1,
      "unknown":1,
      "contradiction":0
    };

  LBLSET3 = {
      "entailment":1,
      "unknown":0,
      "contradiction":1
    };
  
  
  def info( self, lblset ):
    
    conttbl = self._collapse( self.contingency_table, lblset, lblset );

    ( refm, objm ) = self._marginals( conttbl );
    
    def compute( ref, obj ):
        
      cnt = conttbl[ ref ][ obj ];
      freq = None;
      if cnt == 0:
        return 0;
      div = None;
      marg = refm[ ref ];
      if marg == 0:
        div = 0;
      elif self.covered != 0:
        div = marg / self.covered;
      if div != 0 and div is not None:
        freq = cnt / div;
      return freq;

    conttbl_rb = { ref: { obj : compute( ref, obj )
                          for obj in conttbl[ ref ]
                        }
                   for ref in conttbl };

    ( rb_refm, rb_objm ) = self._marginals( conttbl_rb );
    
    prent_rb_ref = self._entropy( rb_refm.values() );
    prent_rb_obj = self._entropy( rb_objm.values() );
    
    # weighting = { 0:1, 1:1 };
    
    mi_rb = prent_rb_obj - self._entropy_cond( conttbl_rb, rb_refm );
    
    return ( prent_rb_ref, prent_rb_obj, mi_rb );


  def csv_data( self ):
    
    rslt = InformationScore.csv_data( self );
    
    if self.obj_lblset is not self.LBLSET_3W:
      return rslt + ",,,,,,,,,";

    if self.ref_lblset is not self.LBLSET_3W:
      return rslt + ",,,,,,,,,";
    
    (hg,hs,isg) = self.info( self.LBLSET1 );
    rslt += "," + str(hg) + "," + str(hs) + "," + str(isg);

    (hg,hs,isg) = self.info( self.LBLSET2 );
    rslt += "," + str(hg) + "," + str(hs) + "," + str(isg);

    (hg,hs,isg) = self.info( self.LBLSET3 );
    rslt += "," + str(hg) + "," + str(hs) + "," + str(isg);
    
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
