# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "compare_decisions" ];

from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.utils.os_ import listsubdirs;

from pypes.infer._evaluation.annotation_reader import read_annotation;
from pypes.infer._evaluation.score_decisions import Score;

from pypes.infer.infeng import InferenceAgent;
from pypes.infer.testsuite_runner import TestsuiteRunner;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DecisionComparer( metaclass=subject ):

  
  class _Agent( InferenceAgent, metaclass=subject ):
    

    def reset( self ):
      
      self.txts = {};
      self.discs = {};
      

    def process_discourse( self, discid, rec, sents, inf=False ):
      
      self.discs[ discid ] = sents;
      return False;
      
    
    def process_sentence( self, sentid, rec, text ):
      
      self.txts[ sentid ] = text;
      return False;
  

    def infer( self, infid, disc, antecedent, consequent, error=False ):
      
      err = False;

      ( ref_decision, ref_conf, ref_vals ) = self._obj_._refdata[ infid ];
      if ref_decision is None:
        return (None,None);
      
      if infid not in self._obj_._objdata:
        print( "{0} {1:3s} | {2:23s} | {3:23s}".format( " ", infid, ref_decision, "-" ) );
        
      else:
        ( obj_decision, obj_conf, obj_vals ) = self._obj_._objdata[ infid ];
        
        if obj_conf == 0.0:
          print( "{0} {1:3s} | {2:23s} | {3:23s}".format( "?", infid, ref_decision, obj_decision ) );
          
        else:
          ch = None;
          if ref_decision == obj_decision:
            ch = " ";
          elif self.lblset_[ ref_decision ] != self.lblset[ obj_decision ]:
            ch = "+";
          else:
            ch = "-";
          print( "{0} {1:3s} | {2:23s} | {3:23s}".format( ch, infid, ref_decision, obj_decision ) );
      
      if ref_decision == "entailment":
        self.tracefile.write( "BEGIN_INFERENCE_ENT(" + str(int(infid)) + ")\n" );
      elif ref_decision == "unknown":
        self.tracefile.write( "BEGIN_INFERENCE_UNK(" + str(int(infid)) + ")\n" );
      elif ref_decision == "contradiction":
        self.tracefile.write( "BEGIN_INFERENCE_CON(" + str(int(infid)) + ")\n" );
      else:
        assert False;
      
      self.tracefile.write( "BEGIN_ANTECEDENT\n" );
      for sent in self.discs[ antecedent ]:
        senttxt = self.txts[ sent ];
        self.tracefile.write( "SENTENCE(" + senttxt +")\n" );
      self.tracefile.write( "END_ANTECEDENT\n" );
      self.tracefile.write( "BEGIN_CONSEQUENT\n" );
        
      assert len( self.discs[consequent] ) == 1;
      
      senttxt = self.txts[ self.discs[consequent][0] ];
      self.tracefile.write(
          "SENTENCE(" + senttxt +")\n"
        );

      self.tracefile.write( "END_CONSEQUENT\n" );
      self.tracefile.write( "END_INFERENCE\n\n" );
      
      return ( None, None );
    
    
  def _enter_( self ):
    
    self._agent_ctx = self._Agent( self );
    self._agent = self._agent_ctx.__enter__();


  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._agent = None;
    self._agent_ctx.__exit__( exc_type, exc_val, exc_tb );
    
    
  def compare_decisions(
          self,
          tsdirnameprefix,
          tsitemsdbdirname,
          objectfilename = "McPIETAgent.tsa.xml",
          referencefilename = "gold.tsa.xml",
          tracefilename = "trace.txt"
        ):
  
    for subdir in listsubdirs( tsdirnameprefix ):
    
      self._refdata = None;
      self._objdata = None;
      
      score = None;
    
      with open( subdir + "/" + referencefilename ) as f:
        with open( subdir + "/" + objectfilename ) as g:
          refdata_ = read_annotation( f );
          objdata_ = read_annotation( g );
          
      with open( subdir + "/" + referencefilename ) as f:
        with open( subdir + "/" + objectfilename ) as g:
          score = Score( f, g );
          
      with open( subdir + "/" + tracefilename, "wt", encoding="utf-8" ) as f:
        
        ( descriptor, labelset, self._refdata ) = refdata_;
        ( descriptor, labelset, self._objdata ) = objdata_;

        print( "subdir:          " + subdir );
        print( "reference file:  " + referencefilename );
        print( "object file:     " + objectfilename );
        
        print();
        
        print( "      | {0:23s} | {1:23s}".format( "REFERENCE", "OBJECT" ) )
        
        print( "-" * 59 );

        self._tracefile = f;
        
        with TestsuiteRunner( (subdir,tsitemsdbdirname,None) ) as runner:
        
          runner.add_agent( self._agent, passive=True );
          self._agent.lblset_ = score.LBLSETs[ score.lblset_ ];
          self._agent.lblset = score.LBLSETs[ score.lblset ];
          self._agent.tracefile = f;
          runner.run();
        
        print( "-" * 59 );
        print();
        
        if score.coverage is not None:
          print( "COVERAGE:  {0:1.2f}".format( score.coverage ) );
        if score.accuracy is not None:
          print( "ACCURACY:  {0:1.2f}".format( score.accuracy ) );
        if score.accuracy_2w is not None:
          print( "ACCURACY2: {0:1.2f}".format( score.accuracy_2w ) );
        if score.average_precision_2w is not None:
          print( "AVPREC:    {0:1.2f}".format( score.average_precision_2w ) );
        if score.confidence_weighted_score is not None:
          print( "CWS:       {0:1.2f}".format( score.confidence_weighted_score ) );
        if score.confidence_weighted_score_2w is not None:
          print( "CWS2:      {0:1.2f}".format( score.confidence_weighted_score_2w ) );
        if score.ent_gold is not None:
          print( "H(G):    {0:1.4f}".format( score.ent_gold ) );
        if score.mutinf is not None:
          print( "I(S;G):  {0:1.4f}".format( score.mutinf ) );
        
        print();
        print();
        print();
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def compare_decisions(
        tsdirnameprefix,
        tsitemsdbdirname, 
        objectfilename = "McPIETAgent.tsa.xml",
        referencefilename = "gold.tsa.xml",
        tracefilename = "trace.txt"
      ):
  
  with DecisionComparer() as comparer:
    return comparer.compare_decisions(
               tsdirnameprefix = tsdirnameprefix,
               tsitemsdbdirname = tsitemsdbdirname,
               objectfilename = objectfilename,
               referencefilename = referencefilename,
               tracefilename = tracefilename
             );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
