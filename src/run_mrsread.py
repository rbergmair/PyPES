import codecs;

import pyrmrs.globals;
import pyrmrs.delphin.mrsread;

pyrmrs.globals.initMain();


mrsreadctrl = pyrmrs.delphin.mrsread.MRSRead();

for rmrs in mrsreadctrl.mrsread( """[ LTOP: h1 INDEX: e2 [ e TENSE: PRES MOOD: INDICATIVE PROG: - PERF: - SF: QUES ] RELS: < [ proper_q_rel LBL: h3 ARG0: x5 [ x PERS: 3 NUM: SG GEND: M IND: + DIV: - ] RSTR: h4 BODY: h6 ] [ named_rel LBL: h7 ARG0: x5 CARG: "John" ] [ "_successful_a_1_rel" LBL: h8 ARG0: e2 ARG1: x5 ] > HCONS: < h4 qeq h7 > ]""" ):
  print rmrs.str_pretty();
  print;

print;
print;

for rmrs in mrsreadctrl.mrsread( """[ LTOP: h1 INDEX: e2 [ e TENSE: PRES MOOD: INDICATIVE PROG: - PERF: - SF: QUES ] RELS: < [ proper_q_rel LBL: h3 ARG0: x5 [ x PERS: 3 NUM: SG GEND: M IND: + DIV: - ] RSTR: h4 BODY: h6 ] [ named_rel LBL: h7 ARG0: x5 CARG: "John" ] [ "_successful_a_1_rel" LBL: h8 ARG0: e2 ARG1: x5 ] > HCONS: < h4 qeq h7 > ]""" ):
  print rmrs.str_pretty();
  print;

pyrmrs.globals.destructMain();
