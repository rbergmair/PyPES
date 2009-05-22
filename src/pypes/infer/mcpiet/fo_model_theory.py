# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FirstOrderModelTheory:

  @classmethod
  def equality( model, binding, predication, logic ):
    
    ref = None;
    
    for var in predication.args.values():
      if var.sort.sid != "x":
        continue;
      indiv = binding[ var ];
      if ref is None:
        ref = indiv;
      else:
        if indiv != ref:
          return logic.rand_false();
    
    return logic.rand_false();
  
  @classmethod
  def open_pred( model, binding, predication, logic, dropped_args ):
    
    matrix = model._matrices[ predication.predicate ];
    args = model._schema.args[ predication.predicate ];
    
    dropped_args = [];

    for arg in args:
      sort = model._schema.sorts[ arg ];
      if arg not in predication.args:
        dropped_args.append( arg );
        # TODO: look into
        # assert sort.sid == "x";
    
    r = None;

    for dropped_indivs in product( [ 0, 1, 2 ], repeat = len(dropped_args) ):
      
      curidv = 0;
      submatrix = matrix;
      
      for arg in args:
        
        sort = model._schema.sorts[ arg ];
        
        indiv = None;
        
        if arg not in inst.args:
          indiv = dropped_indivs[ curidv ];
          curidv += 1;
          
        else:
          
          var = inst.args[ arg ];
          
          assert var.sort is sort;
          if not isinstance( var, Variable ):
            assert isinstance( var, Constant );
            continue;
        
          ## TODO: fix
          #if sort != "x":
          #  indiv = 0;
          #else:
          #  indiv = binding[ var ];
          indiv = binding[ var ];
          
        submatrix = submatrix[ indiv ];
        
      assert isinstance( submatrix, int );
      
      if r is None:
        r = submatrix;
      else:
        r = self._obj_._logic.weadis( r, submatrix );
    
    return r;

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
