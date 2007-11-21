import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;
import pyrmrs.mrs.robust.variable;



def str_pretty_scoped( rmrs, curhole, scoping ):
  
  rslt = "";
  
  for lid in scoping[ curhole ]:
    
    ep = rmrs.eps_by_lid[ lid ];
    
    if ep.realpred is None or ep.realpred.pos != ep.realpred.POS_QUANTIFIER:
      rslt += ep.str_pretty() + " & ";
      continue;
    
    rargs = None;
    if not rmrs.rargs_by_lid.has_key( ep.label.vid ):
      assert False;
    rargs = rmrs.rargs_by_lid[ ep.label.vid ];
    
    rstr = None;
    if not rargs.has_key( "RSTR" ):
      assert False;
    var = rargs[ "RSTR" ].var;
    if not var.sort == var.SORT_HOLE:
      assert False;
    rstr = var.vid;
      
    body = None;
    if not rargs.has_key( "BODY" ):
      assert False;
    var = rargs[ "BODY" ].var;
    if not var.sort == var.SORT_HOLE:
      assert False
    body = var.vid;
    
    rslt += "%s( %s, %s ) & " % ( \
             ep.str_pretty(),
             str_pretty_scoped( rmrs, rstr, scoping ),
             str_pretty_scoped( rmrs, body, scoping )
           );
  
  rslt = rslt[ : len(rslt) - 2 ];
  return rslt;



pyrmrs.globals.initMain();



doc = open( "testdta/dragon.xml", "r" );
rmrsrd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( doc );
rmrs = None;
for rmrs_ in rmrsrd:
  rmrs = rmrs_;
doc.close();

#       l3 | _every_q( ARG0=x4 BODY=h5 RSTR=h6 ) 
#          |    h6 qeq l7
#       l7 + _nephew_n_1( ARG0=x4 ) 
#   l10001 | _of_p( ARG0=e8 ARG1=x4 ARG2=x9 ) 
#      l10 + _a_q( ARG0=x9 BODY=h11 RSTR=h12 ) 
#          +    h12 qeq l13
#      l13 | _dragon_n_1( ARG0=x9 ) 
#      l14 + _snore_v_1( ARG0=e2 ARG1=x4 ) 
print rmrs.str_pretty();
#print rmrs.str_xml();

print;

scoping = rmrs.get_scoping();
scoping.solve();
for scoping in scoping.enumerate():
  print str_pretty_scoped( rmrs, rmrs.top.vid, scoping );

pyrmrs.globals.destructMain();
