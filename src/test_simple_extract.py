import pyrmrs.globals;

import pyrmrs.ext.wrapper.delphin.extractmrs;
import pyrmrs.mrs.robust.rmrsreader;

import gzip;
import cStringIO;

items = gzip.open( "/local/scratch/rb432/delphin-2008-08-07/erg/gold/fracas/item.gz" );
results = gzip.open( "/local/scratch/rb432/delphin-2008-08-07/erg/gold/fracas/result.gz" );

rmrs_converter = pyrmrs.ext.wrapper.delphin.extractmrs.MrsfsToXMLRMRS();
mrs_converter = pyrmrs.ext.wrapper.delphin.extractmrs.MrsfsToXMLMRS();
scmrs_converter = pyrmrs.ext.wrapper.delphin.extractmrs.MrsfsToTXTScopedMRS();

id = 0;

while True:

  id+= 1;
  
  item = items.readline();
  if item == "":
    break;
  
  item = item.split( "@" );
  item = item[6];
  
  print item;
  
  f = open( "/local/scratch/rb432/scopetest/%d.txt" % id, "w" );
  f.write( item );
  f.close();
  
  result = results.readline();
  assert not result == "";
  
  result = result.split( "@" );
  result = result[ len(result)-2 ];
  
  print result;
  
  rmrsstr = rmrs_converter.invoke( result );
  f = open( "/local/scratch/rb432/scopetest/%d.rmrs.xml" % id, "w" );
  f.write( rmrsstr );
  f.close();
  
  print rmrsstr;
  
  mrsstr = mrs_converter.invoke( result );
  f = open( "/local/scratch/rb432/scopetest/%d.mrs.xml" % id, "w" );
  f.write( mrsstr );
  f.close();
  
  print mrsstr;

  scmrsstr = scmrs_converter.invoke( result );
  f = open( "/local/scratch/rb432/scopetest/%d.scmrs.txt" % id, "w" );
  f.write( scmrsstr );
  f.close();
  
  print scmrsstr;

  rmrsf = cStringIO.StringIO( rmrsstr );
  rmrsrd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( rmrsf, True, 1 );
  rmrs = rmrsrd.getFirst();
  f = open( "/local/scratch/rb432/scopetest/%d.rmrs.txt" % id, "w" );
  f.write( item );
  f.write( "\n" );
  f.write( rmrs.str_pretty() );
  f.write( "\n" );
  f.close();
  
