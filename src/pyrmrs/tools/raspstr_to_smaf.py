import pyrmrs.smafpkg.smaf;

def raspstr_to_smaf( raspstr ):
  
  smaf = pyrmrs.smafpkg.smaf.SMAF();
  raspstr = raspstr[ : raspstr.find( "\n" ) ];
  print raspstr;