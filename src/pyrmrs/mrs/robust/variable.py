import common.variable;

import referent;

class Variable( common.variable.Variable ):
  
  def startElement( self, name, attrs ):
    
    common.variable.Variable.startElement( self, name, attrs );
    
    if name == self.XMLELEM:

      self.sort = attrs[ "sort" ];

      if self.sort in [ Variable.SORT_U, Variable.SORT_ENTITY, Variable.SORT_EVENT ]:
        self.referent = referent.Referent();
        self.referent.startElement( name, attrs );