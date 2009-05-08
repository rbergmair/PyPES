# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "RenamingRewriter", "renaming_rewrite", "sortseq" ];

from pypes.utils.mc import subject, Object;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.proto_processor import ProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def sortseq( int_ ):

  SORT_CHARS = "cdfghklmnorstuvw";
  
  rslt = "";
  while int_ > 0:
    rest = int_ & 0xF;
    int_ = int_ >> 4;
    rslt += SORT_CHARS[ rest ];
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _IndexCollector( ProtoProcessor, metaclass=subject ):

  
  def _enter_( self ):
    
    self._obj_._handle_references = {};
    self._obj_._handle_by_hid = {};
    
    self._obj_._variable_references = {};
    self._obj_._variable_by_sidvid = {};
    
    self._obj_._funct_references = {};
    self._obj_._funct_by_fid = {};
    
    self._obj_._sort_references = {};
  
  
  def _process_handle( self, inst, hid ):
    
    assert inst.hid == hid;
    
    if not inst in self._obj_._handle_references:
      self._obj_._handle_references[ inst ] = 0;
    self._obj_._handle_references[ inst ] += 1;  
      
    if not hid in self._obj_._handle_by_hid:
      self._obj_._handle_by_hid[ hid ] = set();
    self._obj_._handle_by_hid[ hid ].add( inst );
    
    
  def _process_functor( self, inst, fid, referent, feats ):
    
    if not inst in self._obj_._funct_references:
      self._obj_._funct_references[ inst ] = 0;
    self._obj_._funct_references[ inst ] += 1;
    
    if not fid in self._obj_._funct_by_fid:
      self._obj_._funct_by_fid[ fid ] = set();
    self._obj_._funct_by_fid[ fid ].add( inst )


  def _process_variable( self, inst, sid, vid ):

    if not inst in self._obj_._variable_references:
      self._obj_._variable_references[ inst ] = 0;
    self._obj_._variable_references[ inst ] += 1;
  
    if not inst.sort in self._obj_._sort_references:
      self._obj_._sort_references[ inst.sort ] = 0;
    self._obj_._sort_references[ inst.sort ] += 1;  
      
    sidvid = ( sid, vid );
    if not sidvid in self._obj_._variable_by_sidvid:
      self._obj_._variable_by_sidvid[ sidvid ] = set();
    self._obj_._variable_by_sidvid[ sidvid ].add( inst );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RenamingRewriter( metaclass=subject ):
  

  def _enter_( self ):
    
    self._index = Object();
    self._collector_ctx = _IndexCollector( self._index );
    self._collector = self._collector_ctx.__enter__();
    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._collector = None;
    self._collector_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  
  def _reallocate( self, invidx, reallocate_objs ):
    
    newid = 1;
    for obj in reallocate_objs:
      while newid in invidx.values():
        newid += 1;
      invidx[ obj ] = newid;
      newid += 1;


  def _invert_renaming( self, idx, invidx, refs, force_p=False ):
    
    reallocate_objs = set();
    
    for id in idx:
      
      objs = idx[ id ].copy();
      
      if id is not None and not force_p:
        obj = None;
        for obj_ in objs:
          if refs[ obj_ ] > 1:
            obj = obj_;
        if obj is None:
          obj = objs.pop();
        else:
          objs.remove( obj );
        invidx[ obj ] = id;
        
      for obj in objs:
        assert refs[ obj ] >= 1;
        if refs[ obj ] <= 1:
          invidx[ obj ] = None;
        else:
          reallocate_objs.add( obj );
    
    self._reallocate( invidx, reallocate_objs );


  def _invert_merging( self, idx, invidx, refs, force_p=False ):
    
    reallocate_objs = set();
    
    #print( force_p );
    #print( idx );
    
    for id in idx:
      objs = idx[ id ];
      for obj in objs:
        if ( id is None and refs[ obj ] > 1 ) or force_p:
          reallocate_objs.add( obj );
        else:
          invidx[ obj ] = id;

    #print( invidx );
    
    assert len( reallocate_objs ) == 0;

    self._reallocate( invidx, reallocate_objs );
  
  
  def _invert( self, idx, invidx, refs, rename_p, force_p=False ):
    
    if rename_p:
      self._invert_renaming( idx, invidx, refs, force_p );
    else:
      self._invert_merging( idx, invidx, refs, force_p );
  
  
  def _invert_index( self, rename_handles_p=True, rename_vars_p=True,
                     rename_functs_p=True, force_rename_handles_p=False ):

    self._invert(
        self._index._handle_by_hid, self._hid_by_handle,
        self._index._handle_references, rename_handles_p,
        force_p = force_rename_handles_p
      );
    
    # print( repr( self._hid_by_handle ) );

    self._invert(
        self._index._funct_by_fid, self._fid_by_funct,
        self._index._funct_references, rename_functs_p
      );

    # print( repr( self._fid_by_funct ) );
    
    reallocate_vars = set();
    sidvids = set();
    
    for (sid,vid) in self._index._variable_by_sidvid:
      
      vars = self._index._variable_by_sidvid[ (sid,vid) ].copy();
      
      if not rename_vars_p:
        
        if sid is not None and vid is not None:
          for var in vars:
            self._sortvid_by_variable[ var ] = ( var.sort, vid );
            sidvids.add( (sid, vid ) );
      
      else:
        
        if vid is not None:
          var = None;
          for var_ in vars:
            if self._index._variable_references[ var_ ] > 1:
              var = var_;
          if var is None:
            var = vars.pop();
          else:
            vars.remove( var );
          self._sortvid_by_variable[ var ] = (var.sort,vid);
          sidvids.add( (sid,vid) );
          assert var.vid == vid;
          
        for var in vars:
          assert self._index._variable_references[ var ] >= 1;
          if self._index._variable_references[ var ] <= 1:
            self._sortvid_by_variable[ var ] = (var.sort,None);
            sidvids.add( (sid,None) );
          else:
            reallocate_vars.add( var );

    for var in reallocate_vars:
      
      newvid = 1;
      while (var.sort.sid,newvid) in sidvids:
        newvid += 1;
      
      self._sortvid_by_variable[ var ] = (var.sort,newvid);
      sidvids.add( (var.sort.sid,newvid) );

    reallocate_sorts = set();
    
    for (sort,vid) in self._sortvid_by_variable.values():
      if sort.sid is None and self._index._sort_references[ sort ] > 1:
        reallocate_sorts.add( sort );
      else:
        self._sid_by_sort[ sort ] = sort.sid;
    
    newsid = 1;
    for sort in reallocate_sorts:
      while sortseq( newsid ) in self._sid_by_sort[ sort ].values():
        newsid += 1;
      self._sid_by_sort[ sort ] = sortseq( newsid );
      newsid += 1;


  def process_handle( self, inst ):
    
    return inst.__class__(
               hid = self._hid_by_handle[ inst ]
             );


  def process_variable( self, inst ):

    ( sort, vid_ ) = self._sortvid_by_variable[ inst ];
    sid_ = self._sid_by_sort[ sort ];
    
    return inst.__class__(
               sidvid = (sid_,vid_)
             );


  def process_functor( self, inst ):
    
    return inst.__class__(
               fid = self._fid_by_funct[ inst ],
               referent = self.process( inst.referent ),
               feats = inst.feats
             );


  def process_pf( self, pf ):
    
    self._collector.process( pf );
  
  
  def invert( self, rename_handles_p=True, rename_vars_p=True,
              rename_functs_p=True, force_rename_handles_p=False ):
    
    self._hid_by_handle = {};
    self._sortvid_by_variable = {};
    self._sid_by_sort = {};
    self._fid_by_funct = {};
    
    self._invert_index(
        rename_handles_p = rename_handles_p,
        rename_vars_p = rename_vars_p,
        rename_functs_p = rename_functs_p,
        force_rename_handles_p = force_rename_handles_p
      );

      
  def rewrite( self, pf ):
      
    return self.process( pf );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def renaming_rewrite( obj, rename_handles_p=True, rename_vars_p=True,
                      rename_functs_p=True, force_rename_handles_p=False ):
  
  rslt = None;
  with RenamingRewriter( None ) as rewriter:
    rewriter.process_pf( obj );
    rewriter.invert(
        rename_handles_p = rename_handles_p,
        rename_vars_p = rename_vars_p,
        rename_functs_p = rename_functs_p,
        force_rename_handles_p = force_rename_handles_p
      );
    rslt = rewriter.rewrite( obj );
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
