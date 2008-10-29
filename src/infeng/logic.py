import random;


class LukasiewiczLogic:

  
  MAXINT64 = int( 2**63-1 );
  MAXINT32 = int( 2**31-1 );
  MAXINT16 = int( 2**15-1 );
  MAXINT8 = int( 2**7-1 );
  
  DES_DONTCARE = None;
  DES_TRUE = 0;
  DES_FALSE = 1;
  DES_NONTRUE = 2;
  DES_NONFALSE = 3;
  DES_UNDESIGNATED = 4;

  M = MAXINT32;

  
  def is_tv( cls, x ):
    return 0 <= x <= cls.M;
  is_tv = classmethod( is_tv );

  def is_designated_true( cls, x ):
    return x >= cls.M;
  is_designated_true = classmethod( is_designated_true );

  def is_designated_false( cls, x ):
    return x <= 0;
  is_designated_false = classmethod( is_designated_false );
  
  def to_ui_float( cls, x ):
    return float( float(x) / float(cls.M) );
  to_ui_float = classmethod( to_ui_float );
  
  def from_ui_float( cls, x ):
    return int( float( float(x) * float(cls.M) ) );
  from_ui_float = classmethod( from_ui_float );
  
  def to_int( cls, x ):
    return x;
  to_int = classmethod( to_int );
  
  def from_int( cls, x ):
    return x;
  from_int = classmethod( from_int );
  
  def to_str( cls, x ):
    str = "%1.5f" % ( cls.to_ui_float(x) );
    return str;
  to_str = classmethod( to_str );

  
  def strcon( cls, x, y ):
    return max( 0, x + y - cls.M );
  strcon = classmethod( strcon );
  
  def weacon( cls, x, y ):
    return min( x, y );
  weacon = classmethod( weacon );
  
  def strdis( cls, x, y ):
    return min( cls.M, x + y );
  strdis = classmethod( strdis );
  
  def weadis( cls, x, y ):
    return max( x, y );
  weadis = classmethod( weadis );
  
  def impl( cls, x, y ):
    return min( cls.M, cls.M - x + y );
  impl = classmethod( impl );
  
  def neg( cls, x ):
    return cls.M - x;
  neg = classmethod( neg );


  def rand( cls, designation = DES_DONTCARE ):
    
    if designation == cls.DES_DONTCARE:
      return random.randint( 0, cls.M );
    elif designation == cls.DES_TRUE:
      return cls.M;
    elif designation == cls.DES_FALSE:
      return 0;
    elif designation == cls.DES_NONTRUE:
      return random.randint( 0, cls.M-1 );
    elif designation == cls.DES_NONFALSE:
      return random.randint( 1, cls.M );
    elif designation == cls.DES_UNDESIGNATED:
      return random.randint( 1, cls.M-1 );
    else:
      assert False;
      
  rand = classmethod( rand );
  
  
  def rand_matrix( cls, n, dim ):
    
    if dim == 0:
      return cls.rand();
  
    vec = [];
    for i in range( 0, n ):
      vec.append( cls.rand_matrix( n, dim-1 ) );
    return vec;

  rand_matrix = classmethod( rand_matrix );
  
  
  def rand_nonpermutative_matrix( cls, n, dim  ):
    
    if dim < 2:
      return None;
    
    if dim > 3:
      return None;
    
    if dim == 2:
      
      matrix = [ [ None ] * n ] * n;
      
      for i in range( 0, n ):
        for j in range( 0, i ):
          ijval = None;
          jival = None;
          while True:
            ijval = cls.rand();
            jival = cls.rand();
            if cls.is_designated_false( cls.strcon( ijval, jival ) ):
              break;
          matrix[ i ][ j ] = ijval;
          matrix[ j ][ i ] = jival;
        matrix[ i ][ i ] = cls.rand( designation = cls.DES_FALSE );
      
      return matrix;
    
    if dim == 3:
      
      matrix = [ [ [ None ] * n ] * n ] * n;
      for i in range( 0, n ):
        for j in range( 0, i+1 ):
          for k in range( 0, j+1 ):
            
            vals = [];
            for i_ in range( 0, 6 ):
              vals.append( cls.rand() );
            
            max1val = max( vals );
            max2val = None;
            for val in vals:
              if val == max1val:
                continue;
              max2val = max( max2val, val );
            
            sum = max1val + max2val;
            factor = 0;
            if sum > 0:
              factor = cls.M / sum;
            
            for i_ in range( 0, 6 ):
              vals[ i_ ] = vals[ i_ ] * factor;
            
            matrix[ i ][ j ][ k ] = vals[ 0 ];
            matrix[ i ][ k ][ j ] = vals[ 1 ];
            matrix[ j ][ k ][ i ] = vals[ 2 ];
            matrix[ j ][ i ][ k ] = vals[ 3 ];
            matrix[ k ][ j ][ i ] = vals[ 4 ];
            matrix[ k ][ i ][ j ] = vals[ 5 ];
      
      for i in range( 0, n ):
        for j in range( 0, n ):
          matrix[ j ][ i ][ i ] = cls.rand( designation = cls.DES_FALSE );
          matrix[ i ][ j ][ i ] = cls.rand( designation = cls.DES_FALSE );
          matrix[ i ][ i ][ j ] = cls.rand( designation = cls.DES_FALSE );
      
      return matrix;  

  rand_nonpermutative_matrix = classmethod( rand_nonpermutative_matrix );


  def rand_equality_matrix( cls, n ):
    
    matrix = [ [ None ] * n ] * n;
    
    for i in range( 0, n ):
      for j in range( 0, i ):
        #r = cls.rand();
        r = cls.rand( designation = cls.DES_NONTRUE );
        matrix[ i ][ j ] = r;
        matrix[ j ][ i ] = r;
      matrix[ i ][ i ] = cls.rand( designation = cls.DES_TRUE );

    # TODO: THIS SHOULD BE T-TRANSITIVE, BUT ISN'T!!!!
    
    return matrix;

  rand_equality_matrix = classmethod( rand_equality_matrix );


Logic = LukasiewiczLogic;
