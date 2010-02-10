# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";

__all__ = [
    "AnnotationReader", "read_annotation", "compare_decisions",
    "reconsider_decisions", "Score", "score_decisions"
  ];

from pypes.infer._evaluation.annotation_reader import AnnotationReader;
from pypes.infer._evaluation.annotation_reader import read_annotation;
from pypes.infer._evaluation.compare_decisions import compare_decisions;
from pypes.infer._evaluation.reconsider_decisions import reconsider_decisions;
from pypes.infer._evaluation.score import Score;
from pypes.infer._evaluation.score import score_decisions;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
