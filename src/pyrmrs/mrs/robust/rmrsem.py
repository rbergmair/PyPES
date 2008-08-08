import pyrmrs.mrs.common.mrsem;
import pyrmrs.error.xmlsem_error;

import pyrmrs.scoping.rmrs_scoping;

import constant;
import elementary_predication;
import grammar_predicate;
import hole_constraint;
import in_group;
import label;
import real_predicate;
import relation_argument;
import variable;
import referent;

import copy;
import string;



class RMRSem( pyrmrs.mrs.common.mrsem.MRSem ):

  XMLELEM = "RMRS";
  XMLELEMs = [ XMLELEM ];

  eps_by_lid = {};
  rargs = [];
  rargs_by_lid = {};
  ings = [];
  groups = [];
  group_by_hid = {};
  _lbls = [];
  lbl_by_lid = {};
  vars = [];
  refs = [];
  ref_by_var = {};
  consts = [];



  def __init__( self ):
    
    pyrmrs.mrs.common.mrsem.MRSem.__init__( self );
    
    self.eps_by_lid = {};
    self.rargs = [];
    self.rargs_by_lid = {};
    self.ings = [];
    self.groups = [];
    self.group_by_hid = {};
    self._lbls = [];
    self.lbl_by_lid = {};
    self.vars = [];
    self.refs = [];
    self.ref_by_var = {};
    self.consts = [];



  def startElement( self, name, attrs ):
    
    pyrmrs.mrs.common.mrsem.MRSem.startElement( self, name, attrs );
    self.cfrom = int( attrs[ "cfrom" ] );
    self.cto = int( attrs[ "cto" ] );

  def register( self, obj ):
    
    pyrmrs.mrs.common.mrsem.MRSem.register( self, obj );

    if isinstance( obj, label.Label ):
      
      self._lbls.append( obj );
      self.lbl_by_lid[ obj.vid ] = obj;
      
    elif isinstance( obj, variable.Variable ):
      
      self.vars.append( obj );
      
      if obj.referent != None:
        var =  obj.sort + str( obj.vid );
        if self.ref_by_var.has_key( var ):
          oldref = self.ref_by_var[ var ];
          oldref.merge( obj.referent );
          obj.referent = oldref;
        else:
          self.ref_by_var[ var ] = obj.referent;
      
    elif isinstance( obj, elementary_predication.ElementaryPredication ):
      
      self.eps_by_lid[ obj.label.vid ] = obj;
      
    elif isinstance( obj, constant.Constant ):
  
      self.consts.append( obj );
      
    elif isinstance( obj, relation_argument.RelationArgument ):
      
      if not self.rargs_by_lid.has_key( obj.label.vid ):
        self.rargs_by_lid[ obj.label.vid ] = {};
      self.rargs_by_lid[ obj.label.vid ][ obj.name ] = obj;
      self.rargs.append( obj );
      
    elif isinstance( obj, in_group.InGroup ):

      self.ings.append( obj );
       
  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    


  def xml_base( self ):
    
    return "<rmrs%s>%s%s\n</rmrs>";
  
  def xml_tmplt( self, base ):
    
    base = pyrmrs.mrs.common.mrsem.MRSem.xml_tmplt( self, base );

    attributes = " cfrom='%s'" % self.cfrom;
    attributes += " cto='%s'" % self.cto;
    
    body2 = "";
    for rarg in self.rargs:
      body2 += string.replace( "\n" + rarg.str_xml(), "\n", "\n  " );
    for ing in self.ings:
      body2 += string.replace( "\n" + ing.str_xml(), "\n", "\n  " );
    body2 = body2.replace( "%", "%%" );

    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", "%s", body2+"%s" );



  def interpret( self ):
    
    for in_g in self.ings:     
      groupa = [ in_g.vara.vid ];
      if self.group_by_hid.has_key( in_g.vara.vid ):
        groupa = self.group_by_hid[ in_g.vara.vid ];
      else:
        self.group_by_hid[ in_g.vara.vid ] = groupa;
      groupb = [ in_g.varb.vid ];
      if self.group_by_hid.has_key( in_g.varb.vid ):
        groupb = self.group_by_hid[ in_g.varb.vid ];
      else:
        self.group_by_hid[ in_g.varb.vid ] = groupb;
      for item in groupb:
        if not item in groupa:
          groupa.append( item );
      for hid in self.group_by_hid:
        if self.group_by_hid[ hid ] == groupb:
          self.group_by_hid[ hid ] = groupa;
          
    for hid in self.group_by_hid:
      if not self.group_by_hid[ hid ] in self.groups:
        self.groups.append( self.group_by_hid[ hid ] );
      
    declarations = [];  
    for ep in self.eps:
      declarations.append( ep.label.vid );
    for lbl in self._lbls:
      if lbl.vid not in declarations:
        # raise error.xmlsem_error.XMLSemError( \
        #   error.xmlsem_error.XMLSemError.ERRNO_UNDEFINED );
        pass;

    resid = copy.copy( self.hcons );

    for ep in self.eps:
      
      if ep.var.sort == variable.Variable.SORT_HOLE:
        if self.hcons_by_hi_hid.has_key( ep.var.vid ):
          for hcon in self.hcons_by_hi_hid[ ep.var.vid ]:
            if hcon in resid:
              resid.remove( hcon );
          
      if self.rargs_by_lid.has_key( ep.label.vid ):
        for arg in self.rargs_by_lid[ ep.label.vid ]:
          var = self.rargs_by_lid[ep.label.vid][arg].var;
          if var == None:
            continue;
          if var.sort != variable.Variable.SORT_HOLE:
            continue;
          if not self.hcons_by_hi_hid.has_key( var.vid ):
            continue;
          for hcon in self.hcons_by_hi_hid[ var.vid ]:
            if hcon in resid:
              resid.remove( hcon );

    if len( resid ) > 0:
      # raise error.xmlsem_error.XMLSemError( \
      #   error.xmlsem_error.XMLSemError.ERRNO_UNDEFINED );
      pass;
    
  def ep_is_scopal( self, ep ):
    
    scopal = False;
    if self.rargs_by_lid.has_key( ep.label.vid ):
      for argname in self.rargs_by_lid[ ep.label.vid ]:
        arg = self.rargs_by_lid[ ep.label.vid ][ argname ];
        if not arg.var is None and arg.var.sort == arg.var.SORT_HOLE:
          scopal = True;
    return scopal;
  
  def bind_vars( self ):
    
    #for ep in self.eps:
    #  if not ep.realpred is None:
    #    if ep.realpred.pos == ep.realpred.POS_QUANTIFIER:
    #      ep.realpred.var
    pass;
        
      



  def str_pretty_ep( self, ep ):

    rslt = "\n";
    
    fl = "";

    lab = ep.label.str_pretty();
    if ep.label.vid == self.top.vid:
      lab = "*%s*" % lab;
    fl += "%9s : %s( ARG0=%s " % ( lab, ep.str_pretty(), ep.var.str_pretty() );
    
    args = [];
    if self.rargs_by_lid.has_key( ep.label.vid ):
      for arg in self.rargs_by_lid[ ep.label.vid ]:
        args.append( (arg,self.rargs_by_lid[ep.label.vid][arg]) );
    
    def mycmp( x_a, y_b ):
      (x,a) = x_a;
      (y,b) = y_b;
      if x == "BODY" and y == "RSTR":
        return +1;
      elif x == "RSTR" and y == "BODY":
        return -1;
      elif x > y:
        return +1;
      elif x < y:
        return -1;
      else:
        return 0;
    
    args.sort( cmp=mycmp );
    
    for ( argname, arg ) in args:
      fl += "%s=%s " % ( argname, arg.str_pretty() );
    fl += ") ";
    
    rslt += self.fmt( fl, ep.surface );
    
    if ep.var.sort == variable.Variable.SORT_HOLE:
      if self.hcons_by_hi_hid.has_key( ep.var.vid ):
        for hcon in self.hcons_by_hi_hid[ ep.var.vid ]:
          rslt += "\n          :    "+hcon.str_pretty();
        
    if self.rargs_by_lid.has_key( ep.label.vid ):
      for arg in self.rargs_by_lid[ ep.label.vid ]:
        var = self.rargs_by_lid[ep.label.vid][arg].var;
        if var == None:
          continue;
        if var.sort != variable.Variable.SORT_HOLE:
          continue;
        if not self.hcons_by_hi_hid.has_key( var.vid ):
          continue;
        for hcon in self.hcons_by_hi_hid[ var.vid ]:
          rslt += "\n          :    "+hcon.str_pretty();

    return rslt;

  def str_pretty( self ):
    
    self.interpret();
    
    pref = True;
    rslt = "";

    eps = copy.copy( self.eps );
    while True:
      
      if len( eps ) == 0:
        break;
      ep = eps[ 0 ];

      pref = not pref;
      
      if self.group_by_hid.has_key( ep.label.vid ):

        group = self.group_by_hid[ ep.label.vid ];
        
        i = 0;
        while True:
          if i >= len( eps ):
            break;
          ep = eps[ i ];
          if not ep.label.vid in group:
            i += 1;
            continue;
          
          res = self.str_pretty_ep( ep );
          if pref:
            res = res.replace( ":", "+" );
          else:
            res = res.replace( ":", "|" );
          rslt += res;
          del eps[ i ];

      else:
            
        res = self.str_pretty_ep( ep );
        if pref:
          res = res.replace( ":", "+" );
        else:
          res = res.replace( ":", "|" );
        rslt += res;
        del eps[ 0 ];

    return rslt[ 1: ];
 
  
  
  def get_scoping( self ):
    
    self.interpret();
    return pyrmrs.scoping.rmrs_scoping.RMRSScoping( self );
