class XMLSemError( Exception ):

  ERRNO_UNDEFINED = 'u';
  ERRNOs = [ ERRNO_UNDEFINED];

  errno = None;
  errmsg = None;
  args = None;

  def __init__( self, ( errno, errmsg ) ):
    
    self.errno = errno;
    self.errmsg = errmsg;
    self.args = ( errno, errmsg );
    
  def __str__( self ):
    
    return "#%d: %s" % ( self.errno, self.errmsg );
