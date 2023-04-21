import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;

import os;
import sys;
import re;


VERBOSE = False;



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
  
  lids = [];
  
  for ep in rmrs.eps:
    if ep.label.vid in scoping[ curhole ]:
      lids.append( ep.label.vid );
  
  for lid in lids:
    
    ep = rmrs.eps_by_lid[ lid ];
    
    rslt += ep.str_pretty();
    
    if not rmrs.ep_is_scopal( ep ):
      rslt += " & ";
      continue;
    
    rslt += "(";
    
    rargs = None;
    if not rmrs.rargs_by_lid.has_key( ep.label.vid ):
      assert False;
    rargs = rmrs.rargs_by_lid[ ep.label.vid ];

    rargnames = rargs.keys();
    rargnames.sort( cmp=mycmp );
    #print rargnames;
    
    for rargname in rargnames:
      var = rargs[ rargname ].var;
      if var.sort == var.SORT_HOLE:
        rslt += str_pretty_scoped( rmrs, var.vid, scoping ) + ", ";
    rslt = rslt[ : len(rslt) - 2 ];
    rslt += ") & ";
    
  rslt = rslt[ : len(rslt) - 3 ];
  
  return rslt;



number = re.compile( "[0-9]+" );

lkb_variable = re.compile( "[xeui]?[0-9]+(, )?" );

lkb_named = re.compile( "named\(.*?\)" );


def format_my_record( line ):
  
  while True:
    
    m = number.search( line );
    if m is None:
      break;
    line = line[ : m.start() ] + line[ m.end() : ];

  line = line.replace( "_rel", "" );
  
  return line;


def format_utool_record( line ):

  while True:
    
    m = number.search( line );
    if m is None:
      break;
    line = line[ : m.start() ] + line[ m.end() : ];
    
  line = line.replace( "'", "" );
  line = line.lower();
  line = line.replace( "_rel", "" );
  line = line.replace( "&", " & " );
  line = line.replace( ",", ", " );
  
  return line;


def format_lkb_record( line ):
  
  while True:
    
    m = lkb_variable.search( line );
    if m is None:
      break;
    line = line[ : m.start() ] + line[ m.end() : ];

  line = line.replace( "*TOP*", "" );
    
  while True:
    
    m = lkb_named.search( line );
    if m is None:
      break;
    line = line[ : m.start() ] + "named" + line[ m.end() : ];
    
  line = line.replace( "  ", " " );
  line = line.replace( " /\ ", " & " );
  line = line.replace( "( ", "(" );
  line = line.replace( ", )", ")" );
  line = line.replace( "()", "" );
  line = line.lower();
  
  return line;



def process( nos ):
  
  skipped = [];
  
  for id in nos:
    
    print id;
    
    try:

      f = open( "/local/scratch/rb432/scopetest/%d.rmrs.xml" % id );
      rmrsrd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( f, True, 1 );
      rmrs = rmrsrd.getFirst();
      f.close();
      
      f = open( "/local/scratch/rb432/scopetest/%d.pl" % id );
      utooloutput = f.read();
      f.close();
    
      f = open( "/local/scratch/rb432/scopetest/%d.scmrs.txt" % id );
      lkboutput = f.read();
      f.close();
      
      try:
          
        utool_scopings = [];
        
        line = "";
        for ch in utooloutput + "\n":
          if ch == "\n":
            if len(utool_scopings) == 0:
              line = line[ 1: ];
            if line[ len(line) - 1 ] in [ ",", "]" ]:
              line = line[ : len(line) -1 ];
              utool_scopings.append( format_utool_record( line ) );
            line = "";
          else:
            line += ch;
        
        lkb_scopings = [];
        lkb_warning = False;
        
        if lkboutput.find( "Maximum scoping calls exceeded" ) != -1:
          lkb_warning = True;
          
        else:
          
          logical_record = "";
          real_line = "";
          
          for ch in lkboutput[1:] + "\n\n":
            
            if ch == "\n":
              logical_record += " ";
            else:
              logical_record += ch;
              
            real_line += ch;
            
            if ch == "\n":
              if real_line == "\n":
                if logical_record.startswith( "WARNING:" ):
                  warning = True;
                  break;
                logical_record = logical_record[ : len(logical_record)-2 ];
                if not logical_record == "":
                  lkb_scopings.append( format_lkb_record( logical_record ) );
                  logical_record = "";
                
            if ch == "\n":
              real_line = "";
              
        if lkb_warning:
          skipped.append( id );
          continue;
        
        if id in [ 68, 69, 160, 172, 173, 273, 274, 296 ]:
          skipped.append( id );
          continue;

        #if id in [ 299, 314, 319, 321, 325 ]:
        #  skipped.append( id );
        #  continue;
        
        #if id in [   2,   4,   6,   8,   9,  16,  17,  24,  25,  39,
        #            59,  78,  82,  83,  88, 118, 129, 130, 143, 151,
        #           154, 161, 162, 182, 183, 184, 193, 194, 206, 231,
        #           232, 237, 238, 241, 242, 251, 253, 266, 267, 288,
        #           289, 302, 303  ]:
        #  continue;
        #
        #if id in [  12, 13, 15, 61, 62, 157, 158, 159, 164, 165, 166,
        #           167, 209, 213, 214, 215,   ]:
        #  continue;
        
        myscopings = [];
        #print rmrs.str_pretty();
        scoping = rmrs.get_scoping();
        scoping.solve( 1 );
        
        assert len( scoping.enumerate() ) == 1;
          
        continue;
        
        for scoping in scoping.enumerate():
          #print scoping;
          scp = str_pretty_scoped( rmrs, rmrs.top.vid, scoping );
          if VERBOSE:
            print scp;
          myscopings.append( format_my_record( scp ) );

        try:
        
          assert len( utool_scopings ) == len( lkb_scopings );
          assert len( utool_scopings ) == len( myscopings );
          
          utool_scopings.sort();
          lkb_scopings.sort();
          myscopings.sort();
        
          for i in range( 0, len(utool_scopings) ):
            utool_scoping = utool_scopings[ i ];
            lkb_scoping = lkb_scopings[ i ];
            myscoping = myscopings[ i ];
            assert utool_scoping == lkb_scoping;
            assert utool_scoping == myscoping;
            assert myscoping == lkb_scoping;
        
        except:
          
          print "UTOOL SCOPINGS:";
          for scoping in utool_scopings:
            print "   " + scoping;
          print "LKB SCOPINGS:";
          for scoping in lkb_scopings:
            print "   " + scoping;
          print "MY SCOPINGS:";
          for scoping in myscopings:
            print "   " + scoping;
          raise;
        
      except:
        print len( utool_scopings );
        print len( lkb_scopings );
        print len( myscopings );
        raise;

    except:
      print id;
      raise;
  
  return skipped;


try:
  
  import profile;
  #profile.run( "print process( range(1,326) )" );
  #print process( range(100, 110) );
  #process( range(1,326) );
  process( [26] );
  
except:
  import traceback;
  traceback.print_exc();