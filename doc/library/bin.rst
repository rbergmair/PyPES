:mod:`bin` --- binaries 
=======================

.. module:: bin
  :synopsis: binaries

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

   takes a McPIET annotation (such as :file:`dta/infer/fracas/fracas-1-1/McPIETAgent.tsa.xml`)
   and makes new entailment decisions on the basis of the numeric `r1` and `r2` fields.

   The default strategy is to say `entailment` when `r1` is `1.0`, contradiction when `r2`
   is `1.0` and `unknown` when both are `0.0`. -- This leads to strict logical decisions
   and no robustness.

   The strategy used in :function:`decide_annotation.main( [argv] )`, on the other hand,
   leads to more robustness.  Here a decision is `entailment` whenever `r1` > `r2`, and

   does the same traversal through subdirectories, given *argv* as
   :function:`compare_annotations.main`.


.. function:: extract_ergsem_smi.main( [argv] )
.. function:: extract_logical_patterns.main( [argv] )
.. function:: preprocess_fracas.main( [argv] )
.. function:: preprocess_rte.main( [argv] )
.. function:: preprocess_rte_results.main( [argv] )
.. function:: read_treebank.main( [argv] )
.. function:: run_score.main( [argv] )
.. function:: run_testsuite.main( [argv] )
.. function:: sanitize_rte.main( [argv] )

