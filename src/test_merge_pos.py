import cPickle;

import pyrmrs.globals;
import pyrmrs.tools.merge_pos_into_smaf;

pyrmrs.globals.initMain();



f = open( "testdta/rtesmafs.pickle" );

while True:
  
  try:
    
    fsppsmaf = cPickle.load( f );
    raspsmaf = cPickle.load( f );
    
    #print fsppsmaf.str_xml();
    #print raspsmaf.str_xml();
    
    try:
      smaf = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( fsppsmaf, raspsmaf );
    except:
      print fsppsmaf.str_xml();
      print raspsmaf.str_xml();
      raise;
      
  except EOFError:
    break;
  


pyrmrs.globals.destructMain();
