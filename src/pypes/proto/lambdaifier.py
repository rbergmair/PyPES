# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "Lambdaifier", "lambdaify", "sortseq" ];

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

class IndexCollector( ProtoProcessor, metaclass=subject ):

  
  def _enter_( self ):
    
    self._obj_._handle_references = {};
    self._obj_._handle_by_hid = {};
    
    self._obj_._variable_references = {};
    self._obj_._variable_by_sidvid = {};
    
    self._obj_._word_references = {};
    self._obj_._word_by_wid = {};
    
    self._obj_._sort_references = {};
  
  
  def _process_handle( self, inst, hid ):

    if not inst in self._obj_._handle_references:
      self._obj_._handle_references[ inst ] = 0;
    self._obj_._handle_references[ inst ] += 1;  
      
    if not hid in self._obj_._handle_by_hid:
      self._obj_._handle_by_hid[ hid ] = set();
    self._obj_._handle_by_hid[ hid ].add( inst );
    
    
  def _process_word( self, inst, wid, lemma, pos, sense, feats ):
    
    if not inst in self._obj_._word_references:
      self._obj_._word_references[ inst ] = 0;
    self._obj_._word_references[ inst ] += 1;
    
    if not wid in self._obj_._word_by_wid:
      self._obj_._word_by_wid[ wid ] = set();
    self._obj_._word_by_wid[ wid ].add( inst )


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

class Lambdaifier( metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._index = Object();
    with IndexCollector( self._index ) as coll:
      coll.process( self._obj_ );
      # print( repr( self._index._handle_by_hid ) );
  
  
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
        self._index._handle_by_hid, self._hid_by_handle,
        self._index._handle_references, rename_handles_p
      );
    
    # print( repr( self._hid_by_handle ) );

    self._invert(
        self._index._word_by_wid, self._wid_by_word,
        self._index._word_references, rename_words_p
      );
    
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

 
  def lambdaify( self, rename_handles_p=True, rename_vars_p=True,
                 rename_words_p=True ):
    
    self._hid_by_handle = {};
    self._sortvid_by_variable = {};
    self._sid_by_sort = {};
    self._wid_by_word = {};
    
    self._invert_index( rename_handles_p=rename_handles_p,
                        rename_vars_p=rename_vars_p,
                        rename_words_p=rename_words_p );
    
    return self.process( self._obj_ );


  def _process_predication( self, inst, predicate, args ):
    
    return inst.__class__(
               predicate = predicate,
               args = args
            );
    
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    return inst.__class__(
               quantifier = quantifier,
               var = var,
               rstr = rstr,
               body = body
             );
             
  def _process_modification( self, inst, modality, args, scope ):
    
    return inst.__class__(
               modality = modality,
               args = args,
               scope = scope
             );
    
  def _process_connection( self, inst, connective, lscope, rscope ):
    
    return inst.__class__(
               connective = connective,
               lscope = lscope,
               rscoep = rscope
             );
    
  def _process_handle( self, inst, hid ):
    
    return inst.__class__(
               hid = hid
             );
    
  def _process_freezer( self, inst, content ):
    
    return inst.__class__(
               content = content
             );
    
  def _process_constraint( self, inst, harg, larg ):
    
    return inst.__class__(
               harg = harg,
               larg = larg
             );
    
  def _process_protoform( self, inst, subforms, constraints ):
    
    return inst.__class__(
               subforms = subforms,
               constraints = constraints
            );
    
  def _process_predicate( self, inst, referent ):
    
    return inst.__class__(
                referent = referent
             );
    
  def _process_quantifier( self, inst, referent ):
    
    return inst.__class__(
               referent = referent
             );
    
  def _process_modality( self, inst, referent ):
    
    return inst.__class__(
               referent = referent
            );
    
  def _process_connective( self, inst, referent ):
    
    return inst.__class__(
               referent = referent
             );
    
  def _process_argument( self, inst, aid ):
    
    return inst.__class__(
               aid = aid
             );
    
  def _process_variable( self, inst, sid, vid ):
    
    return inst.__class__(
               sid = sid
             );
    
  def _process_constant( self, inst, ident ):
    
    return inst.__class__(
               ident = ident
             );
    
  def _process_sort( self, inst, sid ):
    
    return inst.__class__(
               sid = sid
             );
    
  def _process_word( self, inst, wid, lemma, pos, sense, feats ):
    
    return inst.__class__(
               wid = wid,
               lemma = lemma,
               pos = pos,
               sense = sense,
               feats = feats
             );
    
  def _process_operator( self, inst, otype ):
    
    return inst.__class__(
               otype = otype
             );

  
  def _lambdaify( self, obj ):
    
    if obj is None:
      
      return None;
    
    elif isinstance( obj, ProtoForm ):
      
      subforms = [];
      for ( hndl, subf ) in obj.subforms:
        subforms.append( ( self._lambdaify( hndl ),  self._lambdaify( subf ) ) );
      constraints = [];
      for cons in obj.constraints:
        constraints.append( self._lambdaify(cons) );
      
      return obj.__class__( subforms=subforms, constraints=constraints );
    
    elif isinstance( obj, Handle ):
      
      return obj.__class__( hid = self._hid_by_handle[obj] );
    
    elif isinstance( obj, Constraint ):
      
      return obj.__class__( harg = self._lambdaify(obj.harg),
                            larg = self._lambdaify(obj.larg) );

    elif isinstance( obj, Variable ):
      
      ( sort, vid ) = self._sortvid_by_variable[ obj ];
      sid = self._sid_by_sort[ sort ];
      return obj.__class__( sidvid = (sid,vid) );

    elif isinstance( obj, Constant ):
      
      return obj.__class__( ident = obj.ident );

    elif isinstance( obj, Quantification ):
      
      return obj.__class__( quantifier = self._lambdaify(obj.quantifier),
                            var = self._lambdaify(obj.var),
                            rstr = self._lambdaify(obj.rstr),
                            body = self._lambdaify(obj.body) );
    
    elif isinstance( obj, Quantifier ):
      
      return obj.__class__( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Connection ):
      
      return obj.__class__( connective = self._lambdaify(obj.connective),
                            lscope = self._lambdaify(obj.lscope),
                            rscope = self._lambdaify(obj.rscope) );
    
    elif isinstance( obj, Connective ):
      
      return obj.__class__( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Argument ):
      
      return obj.__class__( aid=obj.aid );
    
    elif isinstance( obj, Predication ):
      
      args = {};
      for arg in obj.args:
        args[ self._lambdaify(arg) ] = self._lambdaify( obj.args[arg] );
      
      return obj.__class__( predicate = self._lambdaify(obj.predicate),
                            args = args );
    
    elif isinstance( obj, Predicate ):
      
      return obj.__class__( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Modification ):
      
      args = {};
      for arg in obj.args:
        args[ self._lambdaify(arg) ] = self._lambdaify( obj.args[arg] );
      
      return obj.__class__( modality = self._lambdaify(obj.modality),
                            args = args,
                            scope = self._lambdaify(obj.scope) );
    
    elif isinstance( obj, Modality ):
      
      return obj.__class__( referent = self._lambdaify(obj.referent) );
    
    elif isinstance( obj, Freezer ):
      
      return obj.__class__( content = self._lambdaify(obj.content) );
    
    elif isinstance( obj, Operator ):
      
      return obj.__class__( otype=obj.otype,
                            feats=obj.feats );
    
    elif isinstance( obj, Word ):
      
      return obj.__class__( wid = self._wid_by_word[obj],
                            lemma = obj.lemma,
                            pos = obj.pos,
                            sense = obj.sense,
                            feats = obj.feats );

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
