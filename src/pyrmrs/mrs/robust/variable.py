import pyrmrs.mrs.common.variable;

import referent;

class Variable( pyrmrs.mrs.common.variable.Variable ):
  
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:

      #self.sort = attrs[ "sort" ];
      #if self.sort in [ Variable.SORT_U, Variable.SORT_ENTITY, Variable.SORT_EVENT ]:
      self.referent = referent.Referent();
      pyrmrs.mrs.common.variable.Variable.startElement( self, name, attrs );
