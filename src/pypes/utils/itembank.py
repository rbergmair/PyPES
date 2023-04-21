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
    
    key = self._tbl._id_to_key( self._id );
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


  def sync( self ):
    
    key = self._tbl._id_to_key( self._id );
    self._tbl.master[ key ] = ( self._length, self._ctx_offs, self._fields )
  
  
  def _filename( self, field ):

    return self._tbl.dirname + "/" + self._tbl.dbname + "-" + field + ".items";
  
  
  def _append_file( self, field ):
    
    filename = self._filename( field );
    mode = "rt+";
    try:
      f = open( filename );
      f.close();
    except:
      mode = "wt";
    
    f = open( filename, mode, encoding="utf-8" );
    f.seek( 0, os.SEEK_END );
    return f;
  
  
  def _read_file( self, field ):

    filename = self._filename( field );
    return open( filename, "rt", encoding="utf-8" );
  
  
  def _strip_id( self, data ):

    delim = data.find( " " );
    idtok = data[ :delim ];
    data = data[ delim+1: ]
    assert idtok[0] == "[";
    assert idtok[-1] == "]";
    id = int( idtok[1:-1] );
    return ( id, data );
  
  
  def _read_item( self, f, field, offs ):

    f.seek( offs );
    line = f.readline();
    assert line[-1] == "\n";
    line = line[:-1];
    ( id, item ) = self._strip_id( line );
    assert id == self._id;
    return item;
  

  def get_ctx_str( self ):
    
    if self._ctx_offs is None:
      return None;
    
    if self._ctx_str is not None:
      return self._ctx_str;
    
    with self._read_file( "ctx" ) as f:
      self._ctx_str = self._read_item( f, "ctx", self._ctx_offs );
    
    return self._ctx_str;


  def set_ctx_str( self, ctx_str ):
    
    assert isinstance( ctx_str, str )
    assert not ctx_str in self._tbl.ctx_index;
        
    old_ctx_str = self.get_ctx_str();
    
    if old_ctx_str is not None and old_ctx_str == ctx_str:
      return;
    
    with self._append_file( "ctx" ) as f:
      
      self._ctx_offs = f.tell();
      f.write( "[{0}] {1}\n".format( self._id, ctx_str ) );

    self._ctx_str = ctx_str;
    self._length = len( ctx_str.split() );

    self.sync();
    
    if old_ctx_str is not None:
      del self._tbl.ctx_index[ old_ctx_str ];
    self._tbl.ctx_index[ ctx_str ] = self._id;


  def reset( self, field ):
    
    self._fields[ field ] = [];
    self.sync();
  
  
  def append_to( self, field, val ):
    
    if not field in self._fields:
      self._fields[ field ] = [];
    
    subid = len( self._fields[ field ] );
    
    with self._append_file( field ) as f:
      
      subitem_offs = f.tell();
      f.write( "[{0}] [{1}] {2}\n".format( self._id, subid, val ) );
      self._fields[ field ].append( subitem_offs );
    
    self.sync();
  
  
  def fetch_first( self, field ):
    
    subitem = None;
    
    with self._read_file( field ) as f:

      subitem_offs = self._fields[ field ][ 0 ];
      item = self._read_item( f, field, subitem_offs );
      ( subid_, subitem )  = self._strip_id( item );
      assert subid_ == 0;
    
    return subitem;
  
  
  def fetch_all( self, field ):

    with self._read_file( field ) as f:
    
      for subid in range( 0, len( self._fields[field] ) ):
        
        subitem_offs = self._fields[ field ][ subid ];
        item = self._read_item( f, field, subitem_offs );
        ( subid_, subitem )  = self._strip_id( item );
        assert subid_ == subid;
        yield subitem;
  
  
  def set( self, field, val ):
    
    self._fields[ field ] = val;
    self.sync();
  
  
  def get( self, field ):
    
    return self._fields[ field ];
    
    
    
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
  def _id_to_key( cls, id ):
    
    return str( id );


  @property
  def max_id( self ):
    return self._max_id;


  def has_id( self, id ):
    
    assert isinstance( id, int );
    
    key = None;
    key = self._id_to_key( id );
    return bool( key in self.master );
  
  
  def record_by_id( self, id ):
    
    assert isinstance( id, int );
    key = self._id_to_key( id );
    assert key in self.master;
    return RecordManager( ( self, id ) );
  
  
  def create_record( self, id=None ):
    
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
