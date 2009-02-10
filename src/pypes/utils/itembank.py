# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.itembank";
__all__ = [ "TableManager", "RecordManager" ];

import shelve;
import pickle;


from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RecordManager( metaclass=subject ):
  

  def __init__( self ):
    
    ( tbl, newly_created, id ) = self._obj_;
    
    self._newly_created = newly_created;
    self._id = id;
    
    if newly_created:
      self._length = None;
      self._ctx_offs = None;
      self._fields = {};
    else:
      key = tbl.id_to_key( id );
      ( self._length, self._ctx_offs, self._fields ) = tbl.master[ key ];

    self._ctx_str = None;
    
    self._tbl = tbl;


  @property
  def id( self ):
    return self._id;


  @property
  def newly_created( self ):
    return self._newly_created;


  @property
  def length( self ):
    return self._length;
  
  
  def append_to( self, field ):
    
    pass;


  def reset( self, field ):
    
    pass;
  
  
  def fetch_first( self, field ):
    
    pass;
  
  
  def fetch_all( self, field ):
    
    pass;
  
    
  def get_ctx_str( self ):
    
    if self._ctx_offs is None:
      return None;
    
    if self._ctx_str is not None:
      return self._ctx_str;
    
    f = open( self._tbl.dirname + "/" + self._tbl.dbname + "-ctx.items", "r" );
    f.seek( self._ctx_offs );
    line = f.readline();
    f.close();
    assert line[-1] == "\n";
    delim = line.find( " " );
    idtok = line[ :delim ];
    self._ctx_str = line[ delim+1: ][ :-1 ];
    assert idtok[0] == "[";
    assert idtok[-1] == "]";
    assert int( idtok[1:-1] ) == self._id;
    return self._ctx_str;


  def set_ctx_str( self, ctx_str ):
    
    assert isinstance( ctx_str, str );
    
    if self._newly_created:
      if ctx_str in self._tbl.ctx_index:
        return False;
    
    old_ctx_str = self.get_ctx_str();
    
    if old_ctx_str is not None and old_ctx_str == ctx_str:
      return;
    
    self._ctx_str = ctx_str;
    
    with open( self._tbl.dirname + "/" + self._tbl.dbname + "-ctx.items", "a" ) as f:
      self._ctx_offs = f.tell();
      f.write( "[{0}] {1}\n".format( self._id, ctx_str ) );
    
    self._length = len( ctx_str.split() );
    key = self._tbl.id_to_key( self._id );
    self._tbl.master[ key ] = ( self._length, self._ctx_offs, self._fields )
    
    if old_ctx_str is not None:
      del self._tbl.ctx_index[ old_ctx_str ];
    self._tbl.ctx_index[ ctx_str ] = self._id;
    
    return True;
    
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TableManager( metaclass=subject ):
  
  
  def _enter_( self ):
    
    ( self.dirname, self.dbname ) = self._obj_;
    
    self.master = shelve.open(
                      filename = self.dirname + "/" + self.dbname + "-master",
                      flag = "c",
                      protocol = pickle.DEFAULT_PROTOCOL
                    );
                    
    self.ctx_index = shelve.open(
                         filename = self.dirname + "/" + self.dbname + "-ctx-index",
                         flag = "c",
                         protocol = pickle.DEFAULT_PROTOCOL
                       );
    
    if len( self.master ) == 0:
      self._max_id = 0;
    else:
      with open( self.dirname + "/" + self.dbname + "-maxid.pickle", "rb" ) as f:
        self._max_id = pickle.load( f );


  @classmethod
  def id_to_key( cls, id ):
    
    return str( id );
  
  
  def by_id( self, id=None ):
    
    key = None;
    if id is not None:
      key = self.id_to_key( id );
      
    if key is not None and key in self.master:
      return RecordManager( ( self, False, id ) );
    else:
      if id is None:
        self._max_id += 1;
        id = self._max_id;
      return RecordManager( ( self, True, id ) );
  
  
  def by_ctx_str( self, ctx_str ):
    
    if ctx in self.ctx_index:
      return self.by_id( self.ctx_index[ ctx_str ] );
    else:
      record = self.by_id( None );
      record.set_ctx_str( ctx_str );
      return attr;


  def sync( self ):
    
    self.master.sync();
    self.ctx_index.sync();
    
    with open( self.dirname + "/" + self.dbname + "-maxid.pickle", "wb" ) as f:
      pickle.dump( self._max_id, f );
  
  
  def _close( self ):
    
    self.sync();
    self.ctx_index.close();
    self.master.close();


  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._close();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
