:mod:`bin` --- "binaries"
=========================

.. module:: bin
  :synopsis: "binaries"

:mod:`bin` contains main programmes and command line utilities.


.. function:: compare_annotations.main( [argv] )

   compares two annotation files containing decisions on candidate
   entailments, such as :file:`dta/infer/fracas/fracas-1-1/gold.tsa.xml` and
   :file:`dta/infer/fracas/fracas-1-1/McPIETAgent.tsa.xml`.
   
   The *argv* list should contain as its first element the subdirectory
   where files are to be found (default :file:`dta/infer/fracas/fracas-1`).
   Then all directories are traversed which are subdirectories
   :file:`dta/infer/fracas` and have as a prefix ``fracas-1``.

   Within each directory, a file named in the second element in the
   *argv* list (default ``gold.tsa.xml``) is then compared against
   a file named in the third element (default ``McPIETAgent.tsa.xml``).


.. function:: decide_annotations.main( [argv] )

   takes a McPIET annotation
     (such as :file:`dta/infer/fracas/fracas-1-1/McPIETAgent.tsa.xml`)
   and makes new entailment decisions on the basis of the numeric
   `r1` and `r2` fields.

   The default strategy in McPIET is to say `entailment` when `r1` is `1.0`,
   contradiction when `r2` is `1.0` and `unknown` otherwise. -- This leads to
   strict logical decisions and no robustness.

   The strategy used in :func:`decide_annotation.main( [argv] )`, on the other
   hand, leads to more robustness.  Here a decision is `entailment` whenever
   `r1` > `r2`, and `no entailment` otherwise.

   A traversal through subdirectories is done as in
   :func:`compare_annotations.main()`
   on the basis of *argv*.  Here the second element of *argv* is the input
   annotation file and the third element is the output annotaion file.


.. function:: extract_ergsem_smi.main( [argv] )

   extracts information from the ERG's SEM-I files in the directory named in
   the first element of the *argv* list, and creates as output some python files
   in a directory named in the second element.

   In the process, it checks PyPES-internal assumptions against the grammar's
   SEM-I, so when assertions fail, then that version of the ERG should not be
   used with PyPES.  If the extraction succeeds, the output files need to go
   in :file:`src/pypes/codecs_/mrs/_smi/_ergsem_smi_checker_auto.py` and
   :file:`src/pypes/proto/lex/_erg_auto.py`.


.. function:: extract_logical_patterns.main( [argv] )

   goes through the MRS test data items, and extracts examples of
   predications, grouping them by the type of the MRS elementary
   predications, which is often useful for developing logical
   rewriting definitions.

   The input is taken from :file:`dta/test`, and the output is
   written to :file:`dta/pat`.
   *argv* is ignored.


.. function:: preprocess_fracas.main( [argv] )

   reads :file:`dta/infer/edited/fracas.bmc.xml`, and populates
   both the output directories in :file:`dta/infer/fracas`, and
   the items database in :file:`dta/items/fracas`.
   *argv* is ignored.


.. function:: preprocess_rte.main( [argv] )

   reads :file:`dta/infer/edited/rte*.rte.xml`, and populates
   both the output directories in :file:`dta/infer/rte`, and
   the items databases in :file:`dta/items/rte-*`
   *argv* is ignored.
   *(not fully implemented yet)*.


.. function:: preprocess_rte_results.main( [argv] )

   reads the system submissions from past RTE evaluations,
   from :file:`dta/infer/edited/rte-results*.tar.gz`, and
   creates annotation files in :file:`dta/infer/rte/`.
   *argv* is ignored.


.. function:: read_treebank.main( [argv] )

   reads the treebank in :file:`dta/treebanks/fracas.gz`
   and populates the database in :file:`items/fracas`
   with protoforms in basic and bdsf form.
   *argv* is ignored.


.. function:: run_score.main( [argv] )

   iterates through subdirectories of :file:`dta/infer/fracas`
   or :file:`dta/infer/rte` and creates CSV files in
   :file:`dta/infer/score` to summarize the scores for the
   different inference engines and subsets of the datasets.


.. function:: run_testsuite.main( [argv] )
.. function:: sanitize_rte.main( [argv] )

