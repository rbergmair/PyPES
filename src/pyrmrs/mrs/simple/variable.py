import common.variable;

import referent;

class Variable( common.variable.Variable ):
  
  def startElement( self, name, attrs ):
    
    common.variable.Variable.startElement( self, name, attrs );
    
    if name == self.XMLELEM:
      
      if attrs.has_key( "sort" ):
        self.sort = attrs[ "sort" ];
      else:
        self.sort = Variable.SORT_EVENT;
      
      if self.sort in [ Variable.SORT_U, Variable.SORT_ENTITY, Variable.SORT_EVENT ]:
        self.referent = referent.Referent();
        self.referent.startElement( name, attrs );