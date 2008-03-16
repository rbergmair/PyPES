import pyrmrs.mrs.common.mrsem;

import variable;

import string;
import copy;

class MRSem(  pyrmrs.mrs.common.mrsem.MRSem ):
  
  XMLELEM = "MRS";
  XMLELEMs = [ XMLELEM ];
  
  topvar = None;

  
  
  def __init__( self ):
    
    pyrmrs.mrs.common.mrsem.MRSem.__init__( self );

    self.topvar = None;



  def startElement( self, name, attrs ):
    
    pyrmrs.mrs.common.mrsem.MRSem.startElement( self, name, attrs );
    if attrs.has_key( "cfrom" ):
      self.cfrom = int( attrs[ "cfrom" ] );
    if attrs.has_key( "cto" ):
      self.cto = int( attrs[ "cto" ] );
  
  def register( self, obj ):
    
    pyrmrs.mrs.common.mrsem.MRSem.register( self, obj );
    if isinstance( obj, variable.Variable ):
      
      if self.topvar == None:
        self.topvar = obj;



  def xml_base( self ):

    return "<mrs%s>%s%s\n</mrs>";
  
  def xml_tmplt( self, base ):

    base = pyrmrs.mrs.common.mrsem.MRSem.xml_tmplt( self, base );
    
    attributes = "";
    if self.cfrom != None:
      attributes += " cfrom='%s'" % self.cfrom;
    if self.cto != None:
      attributes += " cto='%s'" % self.cto;
    
    body1 = string.replace( "\n" + self.topvar.str_xml(), "\n", "\n  " );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", body1+"%s", "%s" );



  def interpret( self ):
    
    pass;

  def str_pretty( self ):

    top = self.top.str_pretty();
    ev = self.topvar.str_pretty();
    rslt = "";
    
    eps = copy.copy( self.eps );
    
    pr = True;
    while len( eps ) > 0:
      pr = not pr;
      
      i = 0;
      ep = eps[ i ];
      curvid = ep.label.vid;
      while i < len( eps ):
        ep = eps[ i ];
        if ep.label.vid == curvid:
          st = ep.str_pretty();
          st = st.replace( "  "+top+" :", "*"+top+"* :" );
          st = st.replace( "="+ev+" ", "=*"+ev+"* " );
          st = self.fmt( st, ep.surface ) + "\n";
          for fvp in ep.fvpairs:
            if fvp.var != None and fvp.var.sort == variable.Variable.SORT_HOLE:
              if self.hcons_by_hi_hid.has_key( fvp.var.vid ):
                for hcon in self.hcons_by_hi_hid[ fvp.var.vid ]:
                  st += "          :    " + hcon.str_pretty() + "\n";
          if pr:
            st = st.replace( ":", "=" );
          else:
            st = st.replace( ":", "|" );
          rslt += st;
          del eps[ i ];
        else:
          i += 1;
    
    return rslt[ :len(rslt)-1 ];
