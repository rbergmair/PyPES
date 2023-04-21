import cPickle;
import math;
import copy;
import testsuite.pairreader;
import sys;
import string;

import random;

import stuff;


from infeng.logic import Logic;



class BasicRTEScorer:
  
  ENTAILED = True;
  NOT_ENTAILED = False;
  
  DECISIONS = [ ENTAILED, NOT_ENTAILED ];

  
  def __init__( self, scoreall=False ):
    
    self.skip_scoring = False;
    
    self.scoreall = scoreall;
    self.label = "BAS";
    if scoreall:
      self.label += " (+SA)";
    else:
      self.label += " (-SA)";


  def iterate( self, pfile, results, callback ):
    
    pfile.seek( 0 );
    preader = testsuite.pairreader.PairReader( pfile );
    
    total = 0;
    missing = 0;
    
    for pair in preader.getAll():

      total += 1;

      id = pair.id;
      
      if results.has_key( id ):
        pass;
      elif results.has_key( int(id) ):
        id = int(id);
      else:
        missing += 1;
        continue;
      
      r = results[ id ];
      ( r1, r2, duration, cnt ) = r;
      
      if cnt == 0:
        missing += 1;
        continue;
      
      callback( pair, r );
    
    return ( total, missing );


  def unsupervisedTrain( self, pfile, results ):
    
    pass;


  def supervisedTrain( self, pfile, results ):
    
    pass;
  
  
  def runStart( self ):

    print "running:";
    
    self.results = [];
    self.sumdur = 0.0;
    
    
  def score( self, r1, r2, pair ):
    
    dec = None;
    
    if Logic.is_designated_true( r1 ) and Logic.is_designated_true( r2 ):
      if self.scoreall:
        dec = self.ENTAILED;
      else:
        return ( 0.0, None );
    
    if Logic.is_designated_true( r1 ) and not Logic.is_designated_true( r2 ):
      dec = self.ENTAILED;
    
    elif not Logic.is_designated_true( r1 ) and Logic.is_designated_true( r2 ):
      dec = self.NOT_ENTAILED;
    
    elif not Logic.is_designated_true( r1 ) and not Logic.is_designated_true( r2 ):
      dec = self.NOT_ENTAILED;
    
    return ( 1.0, dec );
  
  
  def runSample( self, pair, result ):
    
    ( r1, r2, duration, cnt ) = result;
    
    try:
      assert not cnt == 0;
      # assert cnt in [16, 17];
    except:
      print cnt;
      raise;
    
    r1 /= cnt;
    r2 /= cnt;
    
    self.sumdur += duration;
    
    ( conf, dec ) = self.score( r1, r2, pair );
    
    self.results.append( ( conf, r1, r2, dec, pair.id, pair.value ) );
  
  
  def runFinish( self ):
    
    if self.skip_scoring:
      return;
    
    self.results.sort( reverse = True );
    
    zc = 0;
    cor = 0;
    
    entailing = 0;
    i = 0;
    sumap = 0.0;
    
    for ( conf, r1, r2, dec, id, gold ) in self.results:
      
      i += 1;
      
      if conf == 0.0:
        lbl = "zc   ";
        zc += 1;
      else:
        lbl = "wrong";
        if dec == gold:
          cor += 1;
          lbl = "ok   ";
      
      if gold:
        entailing += 1;
        sumap += float(entailing) / float(i);
    
      print "  %4s:   %2.4f   %s,%s   %s   ( DEC=%s, GOLD=%s )" % ( \
        id, conf,
        Logic.to_str(r1), Logic.to_str(r2),
        lbl, dec, gold );
    
    self.ap = None;
    if entailing > 0:
      self.ap = sumap / float( entailing );
      self.ap *= 100.0;
      print "  AP. = %f" % self.ap;
        
    rslt_cnt = len( self.results );
    
    self.acc = None;
    if rslt_cnt  - zc > 0:
      self.acc = ( float( cor ) / float( rslt_cnt  - zc ) );
      self.acc *= 100.0;
      print "  Acc. = %f" % self.acc;
    
    self.cvg = None;
    if self.total > 0:
      self.cvg = float( rslt_cnt - zc ) / float( self.total );
      self.cvg *= 100.0;
      print "  Cvg. = %f" % self.cvg;
      
    if rslt_cnt > 0:
      print "  Avg. Ti. = %fs" % ( float( self.sumdur ) / float( rslt_cnt ) );
    
    return ( self.acc, self.ap, self.cvg );
  
  
  def run( self, pfile, results ):
    
    self.runStart();
    ( self.total, self.missing ) = self.iterate( pfile, results, self.runSample );
    return self.runFinish();



class BaselineRTEScorer( BasicRTEScorer ):

  def __init__( self, dec ):

    self.skip_scoring = False;
    self.dec = dec;
    self.label = "BSL (%s)" % dec;

  def score( self, r1, r2, pair ):
    
    return ( 1.0, self.dec )



class DiffRTEScorer( BasicRTEScorer ):


  def __init__( self, scoreall=False ):

    self.skip_scoring = False;
    self.scoreall = scoreall;
    self.label = "DIFF";
    if scoreall:
      self.label += " (+SA)";
    else:
      self.label += " (-SA)";
  
  
  def score( self, result, r1, r2, pair ):
    
    if Logic.is_designated_true( r1 ) and Logic.is_designated_true( r2 ):
      if not self.scoreall:
        return ( 0.0, None );
  
    r1_ = Logic.to_ui_float( r1 );
    r2_ = Logic.to_ui_float( r2 );
  
    val = r1_ - r2_;
    conf = abs( val );
    
    if val > 0.0:
      return ( 1.0, self.ENTAILED );
    else:
      return ( 1.0, self.NOT_ENTAILED );



class MachLearnRTEScorer( BasicRTEScorer ):
  
  DBM_BASELINE = "BSL";
  DBM_GAUSS = "GAUSS";
  DBM_NONPARAMETRIC = "NP";


  def __init__( self, dbmethod, othp, fixedbnd=None ):
    
    self.skip_scoring = False;
    self.dbmethod = dbmethod;
    self.othp = othp;
    self.fixedbnd = fixedbnd;
    self.label = "ML (%s, %s)" % ( dbmethod, othp );
    if not self.fixedbnd is None:
      self.label += " FB=%1.1f" % fixedbnd;
  
  
  def smartMap( self, r1, r2, pair ):

    r1 = Logic.to_ui_float( r1 );
    r2 = Logic.to_ui_float( r2 );

    confidence = 2.0 - r1 - r2;
    confidence = None;
    
    if self.othp:
      
      if r1 == r2 == 1.0:
        r1_ = 0.5;
      else:
        r1_ = ( 1.0 - r2 ) / ( 2.0 - r1 - r2 );
      
    else:

      scale = 1.0 / ( r1 + r2 );
      r1_ = r1 * scale;

    return ( r1_, confidence );


  def supervisedTrainStart( self ):
    
    print "supervised training:";
    
    self.params = {};
    self.data = {};
    for dec in self.DECISIONS:
      self.params[ dec ] = ( 0, 0.0, 0.0, None, None );
      self.data[ dec ] = [];
  
  
  def supervisedTrainSample( self, pair, result ):

    ( r1, r2, duration, cnt ) = result;
    
    if cnt == 0:
      return;
    
    try:
      #assert cnt in [16, 17];
      pass;
    except:
      print cnt;
      raise;
    
    r1 /= cnt;
    r2 /= cnt;
    
    ( val, conf ) = self.smartMap( r1, r2, pair );
    dec = pair.value;
    
    if not val is None:
      self.data[ dec ].append( val );
  
  
  def computeParams( self, data ):
    
    cnt = 0;
    sum = 0.0;
    sumsq = 0.0;
    
    for x in data:
      
      cnt += 1;
      sum += x;
      sumsq += x*x;

    exp = None;
    expsq = None;
    var = None;
    if cnt > 0:
      exp = sum / float( cnt );
      expsq = sumsq / float( cnt );
      var = expsq - exp*exp;
    
    return ( exp, var );
  
  
  def gatherData( self, cls1, cls2 ):
    
    dat1 = [];
    for dec in cls1:
      dat1 += self.data[ dec ];
    dat2 = [];
    for dec in cls2:
      dat2 += self.data[ dec ];
    
    return ( dat1, dat2 );

    
  def getBslDB( self, cls1, cls2 ):
    
    ( dat1, dat2 ) = self.gatherData( cls1, cls2 );
    ( exp1, var1 ) = self.computeParams( dat1 );
    ( exp2, var2 ) = self.computeParams( dat2 );
    
    if exp1 is None or exp2 is None:
      return None;
    
    return ( exp1 + exp2 ) / 2.0;
  
  
  def getGaussDB( self, cls1, cls2 ):

    ( dat1, dat2 ) = self.gatherData( cls1, cls2 );
    ( exp1, var1 ) = self.computeParams( dat1 );
    ( exp2, var2 ) = self.computeParams( dat2 );
    
    a = (1.0/var1) - (1.0/var2);
    b = 2.0 * ( exp2/var2 - exp1/var1 );
    c = (exp1*exp1)/var1 - (exp2*exp2)/var2 + math.log(var1) - math.log(var2);
    sqrtarg = b*b - 4.0*a*c;
    decbnd1 = ( -b + math.sqrt( sqrtarg ) ) / ( 2*a );
    decbnd2 = ( -b - math.sqrt( sqrtarg ) ) / ( 2*a );
    
    print "  decbnd1 = %f" % decbnd1;
    print "  decbnd2 = %f" % decbnd2;
    
    makes_sense = True;
    
    decbnd = None;
    if exp1 <= decbnd1 <= exp2  or  exp1 >= decbnd1 >= exp2:
      decbnd = decbnd1;
    
    if exp1 <= decbnd2 <= exp2  or  exp1 >= decbnd2 >= exp2:
      if not decbnd is None:
        return None;
      decbnd = decbnd2;
    
    return decbnd;
  
  
  def getNonparametricDB( self, cls1, cls2 ):

    ( data1, data2 ) = self.gatherData( cls1, cls2 );
    
    if len( data1 ) == 0:
      return None;
    
    if len( data2 ) == 0:
      return None;
    
    data1.sort();
    data2.sort();
    
    data3 = data1 + data2;
    data3.sort();
    
    minarg = None;
    minval = None;
    
    cnt1 = len( data1 )
    cnt1leq = {};
    curcnt = 0;
    for x in data3:
      if x in data1:
        curcnt += 1;
      cnt1leq[ x ] = curcnt;

    cnt2 = len( data2 );
    cnt2leq = {};
    curcnt = 0;
    for x in data3:
      if x in data2:
        curcnt += 1;
      cnt2leq[ x ] = curcnt;
    
    cnt3 = len(data3);
    
    for x_ in data3:
      
      val = 0;
      for x in data3:
        if x < x_:
          val += cnt2leq[ x ];
        else:
          val += cnt1 - cnt1leq[ x ];
      
      if minval is None or val < minval:
        minval = val;
        minarg = x_;
    
    idx = data3.index( minarg );
    
    bnd = None;
    
    if ( len( data3 ) > idx+1 ):
      nextarg = data3[ idx+1 ];
      bnd = ( minarg + nextarg ) / 2.0;
    else:
      bnd = minarg;
    
    return bnd;
  
  
  def getDBErrorEstim( self, cls1, cls2, db ):

    ( data1, data2 ) = self.gatherData( cls1, cls2 );
    data3 = data1 + data2;
    
    error = 0;
    correct = 0;
    total = 0;
    eqs = 0;
    
    for x in data3:
      total += 1;
      if x < db and x in data2:
        error += 1;
      elif x > db and x in data1:
        error += 1;
      elif x < db and x in data1:
        correct += 1;
      elif x > db and x in data2:
        correct += 1;
      elif x == db:
        eqs += 1;
    
    assert error + correct + eqs == total;
    
    if total == 0:
      return None;
    
    return float( error ) / float( total );

  
  def supervisedTrainFinish( self ):
    
    bsl = False;
    
    if self.dbmethod == self.DBM_BASELINE:
      self.decbnd = self.getBslDB( [ self.NOT_ENTAILED ], [ self.ENTAILED ] );
      bsl = True;
    elif self.dbmethod == self.DBM_GAUSS:
      self.decbnd = self.getGaussDB( [ self.NOT_ENTAILED ], [ self.ENTAILED ] );
    elif self.dbmethod == self.DBM_NONPARAMETRIC:
      self.decbnd = self.getNonparametricDB( [ self.NOT_ENTAILED ], [ self.ENTAILED ] );
      
    decbnd2 = None;
    
    if not bsl:
      decbnd2 = self.getBslDB( [ self.NOT_ENTAILED ], [ self.ENTAILED ] );
      if self.decbnd is None:
        print "  WARNING! STATISTICS MAKE NO SENSE, REVERTING TO BASELINE."
        self.decbnd = decbnd2;
        bsl = True;
    
    if not self.fixedbnd is None:
      self.decbnd = self.fixedbnd;
    
    err = self.getDBErrorEstim( [ self.NOT_ENTAILED ], [ self.ENTAILED ], self.decbnd );
    if not self.decbnd is None:
      print "  db: %f" % self.decbnd;
    if not err is None:
      print "  error: %f" % err;
    
    if not bsl:
      err2 = self.getDBErrorEstim( [ self.NOT_ENTAILED ], [ self.ENTAILED ], decbnd2 );
      print "  baseline-db: %f" % decbnd2;
      print "  baseline-error: %f" % err;
      #if err2 < err:
      #  print "  WARNING! STATISTICS ARE BAD, REVERTING TO BASELINE."
      #  self.decbnd = decbnd2;
  
  
  def supervisedTrain( self, pfile, results ):
    
    self.supervisedTrainStart();
    self.iterate( pfile, results, self.supervisedTrainSample );
    self.supervisedTrainFinish();


  def score( self, r1, r2, pair ):
    
    ( val, conf_ ) = self.smartMap( r1, r2, pair );
    
    val -= self.decbnd;
    dec = val > 0.0;
    
    return ( val, dec );

    

class WordOverlapRTEScorer( MachLearnRTEScorer ):

  def __init__( self ):
    
    self.fixedbnd = None;
    self.skip_scoring = False;
    self.label = "WO";
    self.dbmethod = MachLearnRTEScorer.DBM_NONPARAMETRIC;
    
  def normalize( self, word ):

    wrd = "";
    for ch in word.lower():
      if string.ascii_lowercase.find( ch ) != -1:
        wrd += ch;
      elif string.digits.find( ch ) != -1:
        wrd += ch;
    
    if wrd == "":
      return None;
    
    if wrd in stuff.STOPWORDS:
      return None;
    
    wrd = stuff.PORTER_STEMMER.stem( wrd, 0, len(wrd)-1 )
    
    if wrd == "":
      return None;
    
    if wrd in stuff.STOPWORDS:
      return None;
    
    return wrd;

  def smartMap( self, r1, r2, pair ):
    
    twords = [];
    hwords = [];
    
    for item in pair.t.items:
      words = item.text.split( " " );
      for word in words:
        word = self.normalize( word );
        if word is None:
          continue;
        if not word in twords:
          twords.append( word );
    
    for item in pair.h.items:
      words = item.text.split( " " );
      for word in words:
        word = self.normalize( word );
        if word is None:
          continue;
        if not word in hwords:
          hwords.append( word );

    if len( twords ) == 0:
      return ( None, 0.0 );
    
    if len( hwords ) == 0:
      return ( None, 0.0 );
    
    union = [];
    for word in twords + hwords:
      if not word in union:
        union.append( word );
        
    intersection = [];
    for word in union:
      if word in twords and word in hwords:
        intersection.append( word );
    
    value = float( len(intersection) ) / float( len(hwords) );
    
    return ( value, 1.0 );


  def score( self, r1, r2, pair ):
    
    ( val, conf_ ) = self.smartMap( r1, r2, pair );
    
    if conf_ == 0.0:
      return ( 0.0, None  );
    
    val -= self.decbnd;
    dec = val > 0.0;
    
    return ( val, dec );



def train_scorer( scorer, tsname, datadir ):
  
  pfile = open( "testdta/processed/rte/%s.rte.xml" % tsname );

  datafile = open( "testdta/results/%s/%s.pickle" % ( datadir, tsname ) );

  unpickler = cPickle.Unpickler( datafile );
  data = unpickler.load();
  del unpickler;
 
  scorer.unsupervisedTrain( pfile, data );
  scorer.supervisedTrain( pfile, data );
  
  pfile.close();



def test_scorer( scorer, tsname, datadir ):
  
  pfile = open( "testdta/processed/rte/%s.rte.xml" % tsname );

  datafile = open( "testdta/results/%s/%s.pickle" % ( datadir, tsname ) );

  unpickler = cPickle.Unpickler( datafile );
  data = unpickler.load();
  del unpickler;
 
  r = scorer.run( pfile, data );
  
  pfile.close();
  
  return r;



def write_summary( datadir ):

  scorers = [
    # BasicRTEScorer( False ),
    # BasicRTEScorer( True ),
    # # MachLearnRTEScorer( MachLearnRTEScorer.DBM_BASELINE, False ),
    # # MachLearnRTEScorer( MachLearnRTEScorer.DBM_BASELINE, True ),
    MachLearnRTEScorer( MachLearnRTEScorer.DBM_NONPARAMETRIC, False ),
    # MachLearnRTEScorer( MachLearnRTEScorer.DBM_NONPARAMETRIC, True ),
    WordOverlapRTEScorer(),
    BaselineRTEScorer( BaselineRTEScorer.ENTAILED ),
    BaselineRTEScorer( BaselineRTEScorer.NOT_ENTAILED ),
    MachLearnRTEScorer( MachLearnRTEScorer.DBM_NONPARAMETRIC, False, fixedbnd=0.5 ),
  ];
  
  testsuites = [ "1-cd", "1-ie", "1-mt", "1-pp", "1-qa", "1-rc", "1-ir",
    "2-ie", "2-ir", "2-qa", "2-sum", "3-ie", "3-ir", "3-qa", "3-sum" ];
  #testsuites = [ "3-ie", "3-ir", "3-qa", "3-sum" ];
  
  sfile = open( "testdta/results/%s/summary.csv" % datadir, "w" );
  
  rslt = "tsname;subset";
  for scorer in scorers:
    rslt += ";%s" % scorer.label;
  
  sfile.write( rslt + "\n" );
  
  for tsname in testsuites:
    
    sfile.write( "dev"+tsname.replace("-",";") );
    
    for scorer in scorers:
      train_scorer( scorer, "dev"+tsname, datadir );
      r = test_scorer( scorer, "dev"+tsname, datadir );
      sfile.write( ";%s" % repr(r) );
      
    sfile.write( "\n" );
    
    sfile.write( "tst"+tsname.replace("-",";") );
    
    for scorer in scorers:
      r = test_scorer( scorer, "tst"+tsname, datadir );
      sfile.write( ";%s" % repr(r) );
    
    sfile.write( "\n" );
  
  sfile.close();    


write_summary( "rte" );
sys.exit( 0 );


#def run_rte_4_submission():
#  
#  for task in [ "ie", "ir", "qa", "sum" ]:
#    scorer = MachLearnRTEScorer( MachLearnRTEScorer.DBM_NONPARAMETRIC, False );
#    train_scorer( scorer, "dev3-%s" % task, "rte_boxer_1" );
#    test_scorer( scorer, "tst4-%s" % task, "rte_boxer_1" );


combined_results = [];
covered_ids = [];

for task in [ "ie", "ir", "qa", "sum" ]:
#for task in [ "cd", "ie", "mt", "pp", "qa", "rc", "ir" ]:
  
  boxer_scorer = MachLearnRTEScorer( MachLearnRTEScorer.DBM_NONPARAMETRIC, False );
  boxer_scorer.skip_scoring = True;
  train_scorer( boxer_scorer, "dev3-%s" % task, "rte" );
  test_scorer( boxer_scorer, "tst4-%s" % task, "rte" );
  
  erg_scorer = MachLearnRTEScorer( MachLearnRTEScorer.DBM_NONPARAMETRIC, False );
  erg_scorer.skip_scoring = True;
  train_scorer( erg_scorer, "dev3-%s" % task, "rte_erg_9_wordnet" );
  test_scorer( erg_scorer, "tst4-%s" % task, "rte_erg_9_wordnet" );
  
  
  erg_ids = [];
  erg_results = erg_scorer.results;
  erg_results = [];
  boxer_results = boxer_scorer.results;
  #boxer_results = [];
  
  for ( conf, r1, r2, dec, id, gold ) in erg_results:
    erg_ids.append( id );
  
  boxer_ids = [];
  combined_results += erg_results;
  for boxer_result in boxer_results:
    ( conf, r1, r2, dec, id, gold ) = boxer_result;
    if not id in erg_ids:
      boxer_ids.append( id );
      combined_results.append( boxer_result );
  
  covered_ids += erg_ids;
  covered_ids += boxer_ids;

  print "task: %s" % task;
  print "  used ERG on %d pairs" % len( erg_ids );
  print "  used BOXER on %d pairs" % len( boxer_ids );



allids = [];
pfile = open( "testdta/processed/rte/tst4-ie.rte.xml" );
preader = testsuite.pairreader.PairReader( pfile );
for pair in preader.getAll():
  allids.append( pair.id );
pfile = open( "testdta/processed/rte/tst4-ir.rte.xml" );
preader = testsuite.pairreader.PairReader( pfile );
for pair in preader.getAll():
  allids.append( pair.id );
pfile = open( "testdta/processed/rte/tst4-qa.rte.xml" );
preader = testsuite.pairreader.PairReader( pfile );
for pair in preader.getAll():
  allids.append( pair.id );
pfile = open( "testdta/processed/rte/tst4-sum.rte.xml" );
preader = testsuite.pairreader.PairReader( pfile );
for pair in preader.getAll():
  allids.append( pair.id );

import random;

random_choices = {};
for id in allids:
  if not id in covered_ids:
    random_choices[ id ] = random.choice( [ True, False ] );
    
random_choices = \
  {'622': True, '606': False, '709': False, '760': True, '703': True, '496': True,
   '953': False, '952': True, '715': False, '501': True, '675': False, '562': False,
   '460': False, '710': False, '74': True, '948': True, '949': False, '56': True,
   '51': True, '641': True, '683': False, '803': False, '802': False, '827': False,
   '295': False, '728': True, '804': False, '340': True, '403':True, '555': False,
   '612': True, '734':True };

for id in random_choices:
  if not id in covered_ids:
    combined_results.append( ( 0.0, None, None, random_choices[ id ], id, None ) );

combined_results.sort( reverse = True );

sfile = open( "testdta/results/submission.txt", "w" );
gfile = open( "testdta/results/submission-gold.txt", "w" );

for ( conf, r1, r2, dec, id, gold ) in combined_results:
  rslt = None;
  if dec:
    rslt = "ENTAILMENT";
  else:
    rslt = "NO ENTAILMENT";
  sfile.write( "%s %s\n" % ( id, rslt ) );
  gfile.write( "%s\n" % gold );

gfile.close();
sfile.close();
