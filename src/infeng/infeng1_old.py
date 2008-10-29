import math;
import basic_infeng;


class InferenceEngine1( basic_infeng.BasicInferenceEngine ):
  

  def _disambiguate_propositions( self ):
    
    for key in self._propositions:
      proposition = self._propositions[ key ];
      
      if len( proposition.items[ 0 ].rmrslist ) == 0:
        continue;
      
      proposition.items[ 0 ].rmrslist = proposition.items[ 0 ].rmrslist[ 0:1 ];


  def compare_formulae( self, formula1, formula2 ):
    
    assert False;
    
    
  def _evaluate_normal_formula( self, formula_ ):
    
    worlds = self._find_worlds( formula_ );
    patterns = self._find_patterns( worlds )
  
  
  def _find_worlds( self, formula_, m=4 ):

    worlds = [];
    
    i = 0;

    sumr = 0.0;
    sumrsq = 0.0;
    
    scores = [];
    
    while True:
      
      new_world = self._generate_random_world();
      
      self._model_checker.model = new_world;
      r = self._model_checker.check_formula( formula_ );
      
      worlds.append( new_world );
      scores.append( ( r, i ) );
      
      i += 1;
      
      sumr += r;
      sumrsq += r*r;
      
      er = sumr / float(i);
      ersq = sumrsq / float(i);
      
      var = ersq - er*er;
      
      if var > 0:

        stddev = math.sqrt( var );
        
        nneg = 0;
        npos = 0;
        
        for ( r, i ) in scores:
          if r < er-var:
            nneg += 1;
          elif r >= er+var:
            npos += 1;
        
        if npos >= m and nneg >= m:
          break;
        
        #print nneg;
        #print npos;
        
    nmin = min( nneg, npos );
      
    scores.sort();
    
    neg = [];
    for idx in range( 0, nmin ):
      ( r, i ) = scores[ idx ];
      neg.append( worlds[i] );
      
    pos = [];
    for idx in range( len(scores)-1, len(scores)-1-nmin, -1 ):
      ( r, i ) = scores[ idx ];
      pos.append( worlds[i] );
    
    return ( neg, pos );
  
  
  def _find_patterns( self, worlds ):
    
    ( neg, pos ) = worlds;
    
    print;
    
    print len(neg);
    print len(pos);
    
    wrld0 = pos[0];
    wrld0[ ("universe",1) ] = None;
    
    for (rstr_predicate,rstr_arity) in pos[0]:
      print "%s/%d" % ( rstr_predicate, rstr_arity );
      
