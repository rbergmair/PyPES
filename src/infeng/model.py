from logic import Logic;

class PredicateModel:
  
  def __init__( self, predicate=None, indivs=[] ):
    
    self.predicate = predicate;
    self.indivs = indivs;


  def _generate_random_matrix( self, n, dim ):
    
    if dim == 0:
      return Logic.rand();
  
    vec = [];
    for i in range( 0, n ):
      vec.append( self._generate_random_matrix( n, dim-1 ) );
    return vec;
  
  
  def _get_matrix_val( self, matrix, vars ):
    
    if len( vars ) == 0:
      return matrix;
    
    try:
      return self._get_matrix_val( matrix[ vars[0] ], vars[1:] );
    except:
      print matrix;
      print vars;
      raise;

    
  def set_matrix( self, matrix ):  
    
    self._matrix = matrix;
  
  
  def evaluate( self, args ):
    
    argn = args.keys();
    argn.sort();
    argn2 = self.predicate.argnames;
    argn2.sort();
    try:
      assert argn == argn2;
    except:
      print argn;
      print argn2;
      raise;
    
    vars = [];
    for arg in argn2:
      indiv = args[ arg ];
      assert indiv in self.indivs;
      vars.append( self.indivs.index( indiv ) );
    
    return self._get_matrix_val( self._matrix, vars );
