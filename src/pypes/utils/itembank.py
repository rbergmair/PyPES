# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.itembank";
__all__ = [ "TableManager", "RecordManager" ];

import shelve;
import pickle;
import os;


from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RecordManager( metaclass=subject ):
  

  def __init__( self ):
    
    ( self._tbl, self._id ) = self._obj_;
    
    self._length = None;
    self._ctx_offs = None;
    self._fields = {};

    self._ctx_str = None;
    
    key = self._tbl.id_to_key( self._id );
    if key in self._tbl.master:
      ( self._length, self._ctx_offs, self._fields ) = self._tbl.master[ key ];
    else:
      self._tbl.master[ key ] = ( self._length, self._ctx_offs, self._fields );


  @property
  def id( self ):
    return self._id;


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
    
    try:
      assert int( idtok[1:-1] ) == self._id;
    except:
      print( idtok );
      print( self._id );
      raise;
    
    return self._ctx_str;


  def set_ctx_str( self, ctx_str ):
    
    assert isinstance( ctx_str, str );
    assert not ctx_str in self._tbl.ctx_index;
        
    old_ctx_str = self.get_ctx_str();
    
    if old_ctx_str is not None and old_ctx_str == ctx_str:
      return;
    
    filename = self._tbl.dirname + "/" + self._tbl.dbname + "-ctx.items";
    mode = "rt+";
    try:
      with open( filename ) as f:
        pass;
    except:
      mode = "wt";
    
    with open( filename, mode ) as f:
      f.seek( 0, os.SEEK_END );
      self._ctx_offs = f.tell();
      f.write( "[{0}] {1}\n".format( self._id, ctx_str ) );

    self._ctx_str = ctx_str;
    self._length = len( ctx_str.split() );
    
    key = self._tbl.id_to_key( self._id );
    self._tbl.master[ key ] = ( self._length, self._ctx_offs, self._fields )
    
    if old_ctx_str is not None:
      del self._tbl.ctx_index[ old_ctx_str ];
    self._tbl.ctx_index[ ctx_str ] = self._id;
    
    
    
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


  def has_id( self, id ):
    
    assert isinstance( id, int );
    
    key = None;
    key = self.id_to_key( id );
    return bool( key in self.master );
  
  
  def record_by_id( self, id ):
    
    assert isinstance( id, int );
    key = self.id_to_key( id );
    assert key in self.master;
    return RecordManager( ( self, id ) );
  
  
  def create_record( self, id ):
    
    if id is None:
      self._max_id += 1;
      id = self._max_id;
    else:
      self._max_id = max( self._max_id, id );
    return RecordManager( ( self, id ) );


  def id_by_ctx_str( self, ctx_str=None ):

    if ctx_str in self.ctx_index:
      return self.ctx_index[ ctx_str ];
    
    return None;
  
  
  def add_ctx_str( self, ctx_str=None ):
    
    id = self.id_by_ctx_str( ctx_str );
    if id is not None:
      return id;
    with self.create_record( None ) as rec:
      id = rec.id;
      rec.set_ctx_str( ctx_str );
    return id;


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
