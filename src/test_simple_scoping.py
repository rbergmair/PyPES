import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;
import pyrmrs.mrs.robust.variable;



def mycmp( x, y ):
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



def str_pretty_scoped( rmrs, curhole, scoping ):
  
  rslt = "";
  
  for lid in scoping[ curhole ]:
    
    ep = rmrs.eps_by_lid[ lid ];
    
    rslt += ep.str_pretty();
    
    if not rmrs.ep_is_scopal( ep ):
      rslt += " & ";
      continue;
    
    rslt += "( ";
    
    rargs = None;
    if not rmrs.rargs_by_lid.has_key( ep.label.vid ):
      assert False;
    rargs = rmrs.rargs_by_lid[ ep.label.vid ];
    
    rargnames = rargs.keys();
    rargnames.sort( mycmp );
    
    for rargname in rargnames:
      var = rargs[ rargname ].var;
      if var.sort == var.SORT_HOLE:
        rslt += str_pretty_scoped( rmrs, var.vid, scoping ) + ", ";
    rslt = rslt[ : len(rslt) - 2 ];
    rslt += ") & ";
    
  rslt = rslt[ : len(rslt) - 2 ];
  return rslt;



pyrmrs.globals.initMain();
doc = open( "testdta/dragon.xml", "r" );
rmrsrd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( doc );
for rmrs in rmrsrd.getAll():
  print rmrs.str_pretty();
  scoping = rmrs.get_scoping();
  scoping.solve();
  # scoping.enumerate();
  for scoping in scoping.enumerate():
    #print str(scoping);
    print str_pretty_scoped( rmrs, rmrs.top.vid, scoping );
  print;
  #print "-------";
  #assert False;
  #print;
  #print;

doc.close();
pyrmrs.globals.destructMain();
