import codecs;
import sys;

import rmrsbank.smafbank;

import infeng.logintboxer.logintboxerfol;


#sys.exit( 0 );


testsuites = [ "1-cd", "1-ie", "1-mt", "1-pp", "1-qa", "1-rc",
  "2-ie", "2-ir", "2-qa", "2-sum", "3-ie", "3-ir", "3-qa",
  "3-sum" ];

#testsuites = [ "1-cd" ];
#testsuites = [ "1-cd" ];  


complexities = [];


prefixes = [];
total = 0;
err1 = [];
err2 = [];

gpreds = [ "card" ]

ofilens = [ "p", "n", "v", "r", "l", "a", "o", "c", "t" ];
ofiles = {};
for ofilen in ofilens:
  ofiles[ ofilen ] = codecs.open( "/local/scratch/rb432/boxerpredicates-%s.txt" % ofilen, "w", encoding="utf-8" );

SMAFBANK = rmrsbank.smafbank.SmafBank();


for fname in testsuites:
  for tstdev in [ "tst", "dev" ]:
    for th in [ "t", "h" ]:
      
      filename = "%s%s-%s" % ( tstdev, fname, th );
      
      file = SMAFBANK.get_file( "smafs-ccg", "rte", filename );
      file.load_index();
      
      for i in range( 1, file.max_id+1 ):
        
        total += 1;
        
        idx = file.get_index_by_id( i );
        assert not idx is None;
        smaf = file.get_smaf_by_index( idx );

        diagn = ( filename, smaf.text );
        
        boxerdat = None;
        for boxerdat_ in smaf.getWhatevers():
          boxerdat = boxerdat_;
        
        if boxerdat is None:
          err1.append( diagn );
          continue;
        
        if boxerdat.find( "usage: boxer [options]" ) != -1:
          err2.append( diagn );
          continue;
        
        try:
          formula = infeng.logintboxer.logintboxerfol.Interpret( boxerdat );
        except:
          print boxerdat;
          print smaf.text;
          raise;
        
        try:
          assert len( formula.signature.unbound_vars ) == 0;
        except:
          print smaf.text;
          print boxerdat;
          print formula.str_pretty_indent();
          print formula.signature.unbound_vars;
          print;
          raise;
          
        complexity = 0;
        complexity += len( formula.signature.indefinite_vars );
        complexity += len( formula.signature.definite_vars );
        complexity += len( formula.signature.unbound_vars );
        complexities.append( complexity );
        
        for pred in formula.signature.preds:
          
          if pred.name in gpreds:
            continue;
          
          r = pred.name.find( "_" );
          
          try:
            assert not r == -1;
          except:
            print boxerdat;
            print pred.name;
            #raise;

          prefix = pred.name[ : r ];
          if prefix == "":
            continue;

          if not prefix in prefixes:
            prefixes.append( prefix );
          
          ofiles[ prefix ].write( u"%s\n" % pred.name );
        
        #assert False;
        #print formula.str_pretty_indent();
        #print;
        #break;

f = codecs.open( "/home/rb432/report.txt", "w", encoding="utf-8" );

f.write( str( total ) + "\n" );
f.write( "ERR1 (%d)\n" % len(err1) );
for diagn in err1:
  f.write( "%10s     %s\n" % diagn );
f.write( "ERR2 (%d)\n" % len(err2) );
for diagn in err2:
  f.write( "%10s     %s\n" % diagn );
f.write( str( prefixes ) );

f.close();

for key in ofiles:
  ofiles[ key ].close();

complexities.sort();

print " 10th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.10 ) - 1 ];
print " 20th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.20 ) - 1 ];
print " 30th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.30 ) - 1 ];
print " 40th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.40 ) - 1 ];
print " 50th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.50 ) - 1 ];
print " 60th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.60 ) - 1 ];
print " 70th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.70 ) - 1 ];
print " 80th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.80 ) - 1 ];
print " 85th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.85 ) - 1 ];
print " 90th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.90 ) - 1 ];
print " 95th percentile: %d" % complexities[ int( float( len(complexities) ) * 0.95 ) - 1 ];
print "100th percentile: %d" % complexities[ int( float( len(complexities) ) * 1.00 ) - 1 ];
