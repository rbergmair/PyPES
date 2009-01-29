# -*-  coding: ascii -*-

__package__ = "pypes.proto";
__all__ = [ "Lambdaifier", "lambdaify", "sortseq" ];

from pypes.utils.mc import subject;
from pypes.proto.form import *;
from pypes.proto.sig import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def sortseq( int_ ):

  SORT_CHARS = "cdfghklmnorstuvwCDFGHKLMNORSTUVW";
  
  rslt = "";
  while int_ > 0:
    rest = int_ & 0x1F;
    int_ = int_ >> 5;
    rslt += SORT_CHARS[ rest ];
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Lambdaifier( metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._handle_by_hid = {};
    self._variable_by_sidvid = {};
    self._word_by_wid = {};
    
    self._handle_references = {};
    self._variable_references = {};
    self._sort_references = {};
    self._word_references = {};
    
    self._collect_index( self._obj_ );
  
  
  def _collect_index( self, obj ):
    
    if isinstance( obj, ProtoForm ):
      
      for handle in obj.subforms:
        
        assert isinstance( handle, Handle );
        self._collect_index( handle );
        
        self._collect_index( obj.subforms[handle] );
        
      for constraint in obj.constraints:
        
        self._collect_index( constraint );
    
    elif isinstance( obj, Constraint ):
      
      assert isinstance( obj.harg, Handle );
      self._collect_index( obj.harg );
      
      assert isinstance( obj.larg, Handle );
      self._collect_index( obj.larg );
        
    elif isinstance( obj, Handle ):
      
      if not obj in self._handle_references:
        self._handle_references[ obj ] = 0;
      self._handle_references[ obj ] += 1;  
        
      if not obj.hid in self._handle_by_hid:
        self._handle_by_hid[ obj.hid ] = set();
      self._handle_by_hid[ obj.hid ].add( obj );
    
    elif isinstance( obj, Freezer ):
      
      self._collect_index( obj.content );

    elif isinstance( obj, Connective ) or \
         isinstance( obj, Quantifier ) or \
         isinstance( obj, Modality ) or \
         isinstance( obj, Predicate ):
      
      self._collect_index( obj.referent );
    
    elif isinstance( obj, Word ):
      
      if not obj in self._word_references:
        self._word_references[ obj ] = 0;
      self._word_references[ obj ] += 1;
      
      if not obj.wid in self._word_by_wid:
        self._word_by_wid[ obj.wid ] = set();
      self._word_by_wid[ obj.wid ].add( obj )
    
    elif isinstance( obj, Connection ):

      self._collect_index( obj.connective );
      self._collect_index( obj.lscope );
      self._collect_index( obj.rscope );
    
    elif isinstance( obj, Modification ) or isinstance( obj, Predication ):

      if isinstance( obj, Predication ):

        self._collect_index( obj.predicate );
        
      elif isinstance( obj, Modification ):
        
        self._collect_index( obj.modality );
        self._collect_index( obj.scope );
      
      for arg in obj.args:
        var = obj.args[ arg ];
        assert isinstance( var, Variable );
        self._collect_index( var );

    elif isinstance( obj, Quantification ):

      self._collect_index( obj.quantifier );
      self._collect_index( obj.var );
      self._collect_index( obj.rstr );
      self._collect_index( obj.body );
    
    elif isinstance( obj, Variable ):
      
      if not obj in self._variable_references:
        self._variable_references[ obj ] = 0;
      self._variable_references[ obj ] += 1;

      if not obj.sort in self._sort_references:
        self._sort_references[ obj.sort ] = 0;
      self._sort_references[ obj.sort ] += 1;  
        
      sid = obj.sort.sid;
      vid = obj.vid;
      sidvid = ( sid, vid );
      if not sidvid in self._variable_by_sidvid:
        self._variable_by_sidvid[ sidvid ] = set();
      self._variable_by_sidvid[ sidvid ].add( obj );
  
  
  def _reallocate( self, invidx, reallocate_objs ):
    
    newid = 1;
    for obj in reallocate_objs:
      while newid in invidx.values():
        newid += 1;
      invidx[ obj ] = newid;
      newid += 1;


  def _invert_renaming( self, idx, invidx, refs ):
    
    reallocate_objs = set();
    
    for id in idx:
      
      objs = idx[ id ].copy();
      
      if id is not None:
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


  def _invert_merging( self, idx, invidx, refs ):
    
    reallocate_objs = set();
    
    for id in idx:
      objs = idx[ id ];
      for obj in objs:
        if id is None and refs[ obj ] > 1:
          reallocate_objs.add( obj );
        else:
          invidx[ obj ] = id;

    self._reallocate( invidx, reallocate_objs );
  
  
  def _invert( self, idx, invidx, refs, rename_p ):
    
    if rename_p:
      self._invert_renaming( idx, invidx, refs );
    else:
      self._invert_merging( idx, invidx, refs );
  
  
  def _invert_index( self, rename_handles_p=True, rename_vars_p=True,
                     rename_words_p=True ):

    self._invert(
        self._handle_by_hid, self._hid_by_handle,
        self._handle_references, rename_handles_p
      );

    self._invert(
        self._word_by_wid, self._wid_by_word,
        self._word_references, rename_words_p
      );
    
    reallocate_vars = set();
    sidvids = set();
    
    for (sid,vid) in self._variable_by_sidvid:
      
      vars = self._variable_by_sidvid[ (sid,vid) ].copy();
      
      if not rename_vars_p:
        
        if sid is not None and vid is not None:
          for var in vars:
            self._sortvid_by_variable[ var ] = ( var.sort, vid );
            sidvids.add( (sid, vid ) );
      
      else:
        
        if vid is not None:
          var = None;
          for var_ in vars:
            if self._variable_references[ var_ ] > 1:
              var = var_;
          if var is None:
            var = vars.pop();
          else:
            vars.remove( var );
          self._sortvid_by_variable[ var ] = (var.sort,vid);
          sidvids.add( (sid,vid) );
          assert var.vid == vid;
          
        for var in vars:
          assert self._variable_references[ var ] >= 1;
          if self._variable_references[ var ] <= 1:
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
      if sort.sid is None and self._sort_references[ sort ] > 1:
        reallocate_sorts.add( sort );
      else:
        self._sid_by_sort[ sort ] = sort.sid;
    
    newsid = 1;
    for sort in reallocate_sorts:
      while sortseq( newsid ) in self._sid_by_sort[ sort ].values():
        newsid += 1;
      self._sid_by_sort[ sort ] = sortseq( newsid );
      newsid += 1;

 
  def lambdaify( self, rename_handles_p=True, rename_vars_p=True,
                 rename_words_p=True ):
    
    self._hid_by_handle = {};
    self._sortvid_by_variable = {};
    self._sid_by_sort = {};
    self._wid_by_word = {};
    
    self._invert_index( rename_handles_p=rename_handles_p,
                        rename_vars_p=rename_vars_p,
                        rename_words_p=rename_words_p );
    
    return self._lambdaify( self._obj_ );
    #return None;
  
  
  def _lambdaify( self, obj ):
    
    if obj is None:
      
      return None;
    
    elif isinstance( obj, ProtoForm ):
      
      subforms = {};
      for hndl in obj.subforms:
        subforms[ self._lambdaify( hndl ) ] = \
          self._lambdaify( obj.subforms[hndl] );
      constraints = set();
      for cons in obj.constraints:
        constraints.add( self._lambdaify(cons) );
      
      return ProtoForm( subforms=subforms, constraints=constraints );
    
    elif isinstance( obj, Handle ):
      
      return Handle( hid = self._hid_by_handle[obj] );
    
    elif isinstance( obj, Constraint ):
      
      return Constraint( harg = self._lambdaify(obj.harg),
                         larg = self._lambdaify(obj.larg) );

    elif isinstance( obj, Variable ):
      
      ( sort, vid ) = self._sortvid_by_variable[ obj ];
      sid = self._sid_by_sort[ sort ];
      return Variable( sidvid = (sid,vid) );

    elif isinstance( obj, Quantification ):
      
      return Quantification( quantifier = self._lambdaify(obj.quantifier),
                             var = self._lambdaify(obj.var),
                             rstr = self._lambdaify(obj.rstr),
                             body = self._lambdaify(obj.body) );
    
    elif isinstance( obj, Quantifier ):
      
      return Quantifier( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Connection ):
      
      return Connection( connective = self._lambdaify(obj.connective),
                         lscope = self._lambdaify(obj.lscope),
                         rscope = self._lambdaify(obj.rscope) );
    
    elif isinstance( obj, Connective ):
      
      return Connective( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Argument ):
      
      return Argument( aid=obj.aid );
    
    elif isinstance( obj, Predication ):
      
      args = {};
      for arg in obj.args:
        args[ self._lambdaify(arg) ] = self._lambdaify( obj.args[arg] );
      
      return Predication( predicate = self._lambdaify(obj.predicate),
                          args = args );
    
    elif isinstance( obj, Predicate ):
      
      return Predicate( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Modification ):
      
      args = {};
      for arg in obj.args:
        args[ self._lambdaify(arg) ] = self._lambdaify( obj.args[arg] );
      
      return Modification( modality = self._lambdaify(obj.modality),
                           args = args,
                           scope = self._lambdaify(obj.scope) );
    
    elif isinstance( obj, Modality ):
      
      return Modality( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Freezer ):
      
      return Freezer( content = self._lambdaify(obj.content) );
    
    elif isinstance( obj, Operator ):
      
      return Operator( otype=obj.otype );
    
    elif isinstance( obj, Word ):
      
      return Word( wid = self._wid_by_word[obj],
                   lemma = obj.lemma,
                   scf = obj.scf,
                   pos = obj.pos,
                   sense = obj.sense );

    print( obj );
    assert False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def lambdaify( obj, rename_handles_p=True, rename_vars_p=True,
                 rename_words_p=True ):
  
  rslt = None;
  with Lambdaifier( obj ) as lambdaifier:
    rslt = lambdaifier.lambdaify( rename_handles_p=rename_handles_p,
                                  rename_vars_p=rename_vars_p,
                                  rename_words_p=rename_words_p );
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
