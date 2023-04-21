********
Tutorial
********



Basic Input/Output
------------------

Let's start by reading an MRS from an XML file::

  import gzip;
  import codecs;
  utf8reader = codecs.getreader( "utf8" );
  f_ = gzip.open( "dta/test/mrs-121.mrs.xml.gz", "rb" );
  f = utf8reader( f_ );
  mrs121xml = f.read();
  f.close();
  f_.close();

We now have a string ``mrs121xml``::

  print( mrs121xml );

will give us::

  <mrs>
  <label vid='1'/><var vid='2'/>
  <ep cfrom='0' cto='4'><pred>_EVERY_Q_REL</pred><label vid='3'/>
  <fvpair><rargname>ARG0</rargname><var vid='4' sort='x'>
  <extrapair><path>PERS</path><value>3</value></extrapair>
  <extrapair><path>NUM</path><value>SG</value></extrapair>
  <extrapair><path>IND</path><value>+</value></extrapair></var></fvpair>
  <fvpair><rargname>RSTR</rargname><var vid='6' sort='h'></var></fvpair>
  <fvpair><rargname>BODY</rargname><var vid='5' sort='h'></var></fvpair></ep>
  <ep cfrom='6' cto='8'><spred>_cat_n_1_rel</spred><label vid='7'/>
  [...]</ep>
  [...]
  <hcons hreln='qeq'><hi><var vid='12' sort='h'></var></hi><lo><var vid='13' sort='h'></var></lo></hcons>
  <hcons hreln='qeq'><hi><var vid='6' sort='h'></var></hi><lo><var vid='7' sort='h'></var></lo></hcons>
  </mrs>

then::

  from pypes.codecs_ import mrx_decode;
  pf121_ = mrx_decode( mrs121xml );

This gives us the "lambdaified" ("frozen") representation, which we
now have to "logify" ("thaw")::

  from pypes.proto import *;
  pf121 = pf121_( sig=ProtoSig() );

And then we can encode the result, using ``PFT``, the textual
representation for protoforms::

  from pypes.codecs_ import pft_encode;

  print( pft_encode( pf121, pretty=False, linebreaks=True ) );

will give us::

  {  3: ? |every_q|[ PERS='3', IND='+', NUM='SG', cfrom='0', cto='4' ] x4 6 5;
     7: ? |cat_n_1|[ cto='8', cfrom='6' ]( arg0=x4 );
     8: ? |chase_v_1|[ MOOD='INDICATIVE', TENSE='PAST', PROG='-', cto='15', SF='PROP', cfrom='10', PERF='-' ]( arg0=e2, arg1=x4, arg2=x9 );
    10: ? |some_q_indiv|[ PERS='3', IND='+', NUM='SG', cfrom='17', cto='20' ] x9 12 11;
    13: ? |dog_n_1|[ cto='25', cfrom='22' ]( arg0=x9 );
        ? 12 ^ 13;
        ? 6 ^ 7 }

We can also do prettyprinting as follows::

  print( pft_encode( pf121 ) );

results in::

  {     |every_q| x4 2 __;
     4: |cat_n_1|( arg0=x4 );
        |chase_v_1|( arg0=e2, arg1=x4, arg2=x9 );
        |some_q_indiv| x9 3 __;
     1: |dog_n_1|( arg0=x9 );
        3 ^ 1;
        2 ^ 4 }



Scoping
-------


Recursivization
~~~~~~~~~~~~~~~

You can also do this::

  from pypes.scoping import Solver, Recursivizer;

  with Solver( pf121 ) as solver:
    solution = solver.solve_all();
    assert solution is not None;
    with Recursivizer( solution ) as recursivizer:
      pf121_rec = recursivizer.recursivize();
      print( pft_encode( pf121_rec ) );

gives this::

  { |every_q| x4 { |cat_n_1|( arg0=x4 ) } __;
    |chase_v_1|( arg0=e2, arg1=x4, arg2=x9 );
    |some_q_indiv| x9 { |dog_n_1|( arg0=x9 ) } __ }


Enumeration
~~~~~~~~~~~

To enumerate, you do this::

  from pypes.scoping import Enumerator;

  with Solver( pf121 ) as solver:
    solution = solver.solve_all();
    with Enumerator( solution ) as enumerator:
      for solution in enumerator.enumerate():
        with Recursivizer( solution ) as recursivizer:
          pf121_enu = recursivizer.recursivize();
          print( pft_encode( pf121_enu ) );

This will give you::

  { |every_q| x4 { |cat_n_1|( arg0=x4 ) }
      { |some_q_indiv| x9 { |dog_n_1|( arg0=x9 ) }
          { |chase_v_1|( arg0=e2, arg1=x4, arg2=x9 ) } } }

  { |some_q_indiv| x9 { |dog_n_1|( arg0=x9 ) }
      { |every_q| x4 { |cat_n_1|( arg0=x4 ) }
          { |chase_v_1|( arg0=e2, arg1=x4, arg2=x9 ) } } }



Rewriting
---------


First-Order Rewriting
~~~~~~~~~~~~~~~~~~~~~

In order to apply first-order rewriting, you can do this sort of thing::

  from pypes.rewriting import erg_to_basic;

  print( pft_encode( erg_to_basic( pf121 ) ) );
  print( pft_encode( erg_to_basic( pf121_rec ) ) );
  print( pft_encode( erg_to_basic( pf121_enu ) ) );

giving the following result::

  >>> print( pft_encode( erg_to_basic( pf121 ) ) );
  {     ALL x4 4 __;
     3: |cat_n_1|( arg0=x4 );
        |chase_v_1|( KEY=e2, arg1=x4, arg2=x9 );
        SOME x9 1 __;
     2: |dog_n_1|( arg0=x9 );
        1 ^ 2;
        4 ^ 3 }

  >>> print( pft_encode( erg_to_basic( pf121_rec ) ) );
  { ALL x4 { |cat_n_1|( arg0=x4 ) } __;
    |chase_v_1|( KEY=e2, arg1=x4, arg2=x9 );
    SOME x9 { |dog_n_1|( arg0=x9 ) } __ }

  >>> print( pft_encode( erg_to_basic( pf121_enu ) ) );
  { SOME x9 { |dog_n_1|( arg0=x9 ) }
      { ALL x4 { |cat_n_1|( arg0=x4 ) }
          { |chase_v_1|( KEY=e2, arg1=x4, arg2=x9 ) } } }


Syllogistic Forms
~~~~~~~~~~~~~~~~~

To get syllogistic forms::

  from pypes.rewriting import mr_to_dsf, erg_to_bdsf;

  pf121 = pf121_( sig=ProtoSig() );
  print( pft_encode( mr_to_dsf( pf121 ) ) );
  print( pft_encode( erg_to_bdsf( pf121 ) ) );

gives the following output::

  >>> print( pft_encode( mr_to_dsf( pf121 ) ) );
  { |chase_v_1|:1( arg0=e2 );
    __ /\ __;
    { { |every_q| x4 { |cat_n_1|( arg0=x4 ) }
          { |chase_v_1|:1( arg1=x4 ) } }
      /\ { |some_q_indiv| x9 { |dog_n_1|( arg0=x9 ) }
             { |chase_v_1|:1( arg2=x9 ) } } } }

  >>> print( pft_encode( erg_to_bdsf( pf121 ) ) );
  { |chase_v_1|:1( KEY=e2 );
    __ /\ __;
    { { ALL x4 { |cat_n_1|( arg0=x4 ) }
          { |chase_v_1|:1( KEY=e2, arg1=x4 ) } }
      /\ { SOME x9 { |dog_n_1|( arg0=x9 ) }
             { |chase_v_1|:1( KEY=e2, arg2=x9 ) } } } }



Inferencing
-----------


Preprocessing for Inferencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is how to run McPIET on the FraCaS testsuite:
The process starts with the file ``dta/infer/orig/fracas.bmc.xml``, which contains
the test inferences produced by the FraCaS consortium in 1996 in a machine-readable
format by Bill MacCartney.  PyPES comes with a ``Makefile`` which applies edits from
a ``sed`` script called ``dta/infer/edits/fracas.bmc.xml.sed`` to produce
``dta/infer/edited/fracas.bmc.xml``::

  $ make data
  cp dta/infer/orig/fracas.bmc.xml dta/infer/sanitized/fracas.bmc.xml
  cat dta/infer/sanitized/fracas.bmc.xml | sed -f dta/infer/edits/fracas.bmc.xml.sed > dta/infer/edited/fracas.bmc.xml

Next, you need to use ``src/pypes/bin/preprocess_fracas.py`` to produce a couple of files
in ``dta/infer/fracas``::

  $ python3 src/pypes/bin/preprocess_fracas.py

The files in ``dta/infer/fracas`` are split up by this process into various subdirectories,
corresponding to the section-structure of the original fracas testsuite.  For example
``dta/infer/fracas/fracas-1-1`` will contain all data for the 1.1 section of FraCaS.  The
textual data and the structures putting texts together into candidate entailments can
be found in the file called ``data.ts.xml``.  It will look like this::

  <?xml version="1.0" encoding="UTF-8"?>

  <testsuite>

  [...]

  <group>

  <discourse discid="4">
    <sentence sentid="3">Every Italian man wants to be a great tenor.</sentence>
    <sentence sentid="4">Some Italian men are great tenors.</sentence>
  </discourse>

  <discourse discid="5">
    <sentence sentid="5">Are there Italian men who want to be a great tenor?</sentence>
  </discourse>

  <inference discid="6" infid="002">
    <antecedent discid="4"/>
    <consequent discid="5"/>
  </inference>

  </group>

  [...]

  <group>

  <discourse discid="7">
    <sentence sentid="6">All Italian men want to be a great tenor.</sentence>
    <sentence sentid="4">Some Italian men are great tenors.</sentence>
  </discourse>

  [...]

  </group>

  [...]

  </testsuite>

This declares discourses (with discourse ids), and the sentences contained within
the discourses (with their sentence ids).  If two sentences or discourses match
on their cleartexts, they will also be assigned the same ids.  In addition, all
unique sentences and discourses will be recorded in cleartext item files in
``dta/items/fracas/sentence-ctx.items`` and ``dta/items/fracas/discourse-ctx.items``.

In particular, the ``dta/items/fracas/sentence-ctx.items`` is in the input format
for the `[incr tsdb()] <http://wiki.delph-in.net/moin/ItsdbTop>`_.  You will have
to use this tool offline to do the treebanking.  The resulting ``result.gz``, in
the case of FraCaS, is distributed with the `ERG <http://www.delph-in.net/erg/>`_
under ``gold/fracas/result.gz``, and redistributed with PyPES under
``dta/treebank/fracas.gz``.  You can then read those results back into the
database under ``dta/items/fracas``, as follows::

  $ python3 src/pypes/bin/read_treebank.py
    1: An Italian became the world's greatest tenor.
    2: Was there an Italian who became the world's greatest tenor?
    3: Every Italian man wants to be a great tenor.
    4: Some Italian men are great tenors.
    5: Are there Italian men who want to be a great tenor?
       [...]
  639: Smith saw Jones sign the contract or cross out the crucial clause.
  640: Did Smith either see Jones sign the contract or see Jones cross out the crucial clause?

  --- SUMMARY ---
  total number of items: 640
  syntax errors: 29 (95% good)
    {261, 274, 279, 32, 296, 298, 300, 302, 305, 185, 186, 578, 323, 325, 328, 330, 333, 339, 341, 598, 599, 473, 476, 349, 606, 226, 227, 372, 637}
  scoping errors: 3 (99% good)
    {185, 186, 473}
  rewriting errors: 4 (99% good)
    {32, 606, 349, 598}
  total number of processed items: 611 (95% good)

In addition to just reading the MRS structures, this programme will also apply the
rewriting machinery, to translate the MRSes into syllogistic first-order protoforms.
The resulting protoforms will be stored in ``dta/items/fracas/sentence-bdsf.items``
and are required for the subsequent inferencing.


Running McPIET
~~~~~~~~~~~~~~

Once the database under ``dta/items/fracas`` is populated as described before,
the actual inference machineary can be run as follows::

  $ python3 src/pypes/bin/run_testsuite.py
  dta/infer/fracas/fracas-1-1
     001
     002
     [...]
     016
  [...]
  dta/infer/fracas/fracas-1-5
     065
     [...]
     080

then you can look at the results like this::

  $ python3 src/pypes/bin/compare_annotations.py
  reference file:  dta/infer/fracas/fracas-1-1/gold.tsa.xml
  object file:     dta/infer/fracas/fracas-1-1/McPIETAgent.tsa.xml

        | REFERENCE               | OBJECT
  -----------------------------------------------------------
    001 | entailment              | entailment
    002 | entailment              | entailment
    003 | entailment              | entailment
    004 | entailment              | entailment
    005 | entailment              | entailment
    006 | contradiction           | contradiction
    007 | entailment              | entailment
    008 | entailment              | entailment
    009 | entailment              | entailment
  * 010 | entailment              | unknown
    011 | entailment              | entailment
    012 | None                    | -
  * 013 | entailment              | unknown
    014 | contradiction           | -
    015 | entailment              | entailment
    016 | None                    | -
  -----------------------------------------------------------

  error:                                     3
  coverage:                                81%
  acc( sys; gold ):                        84%
  2w-acc( sys; gold ):                     84%
  2w'-acc( sys; gold ):                   100%
  acc( gold | sys = entailment ):         100%
  acc( gold | sys = unknown ):              0%
  acc( gold | sys = contradiction ):      100%

  [...]

