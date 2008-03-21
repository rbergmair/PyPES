m4_include(`config.m4')
m4_sinclude(`config.m4.local')

<?xml version='1.0' encoding="UTF-8"?>

<!DOCTYPE mrs-list SYSTEM "file://_DIR_PYRMRSHOME/dtd/mrs.dtd">
<mrs-list>



<!-- The dog barks. -->

<mrs>
<label vid='1'/><var vid='2'/>
<ep cfrom='0' cto='3'><pred>PRPSTN_M_REL</pred><label vid='1'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>--TPC</path><value>LUK</value></extrapair>
<extrapair><path>E.TENSE</path><value>PRESENT</value></extrapair>
<extrapair><path>E.MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>E.ASPECT.PROGR</path><value>-</value></extrapair>
<extrapair><path>E.ASPECT.PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='3' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='5' sort='u'></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='4' sort='u'></var></fvpair></ep>
<ep cfrom='0' cto='1'><pred>_THE_Q_REL</pred><label vid='6'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>--TPC</path><value>LUK</value></extrapair>
<extrapair><path>PRONTYPE</path><value>PRONTYPE</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair>
<extrapair><path>PNG.GEN</path><value>REAL_GENDER</value></extrapair>
<extrapair><path>PNG.PN</path><value>3SG</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='8' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='9' sort='h'></var></fvpair></ep>
<ep cfrom='1' cto='2'><spred>_dog_n_1_rel</spred><label vid='10'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>--TPC</path><value>LUK</value></extrapair>
<extrapair><path>PRONTYPE</path><value>PRONTYPE</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair>
<extrapair><path>PNG.GEN</path><value>REAL_GENDER</value></extrapair>
<extrapair><path>PNG.PN</path><value>3SG</value></extrapair></var></fvpair></ep>
<ep cfrom='2' cto='3'><spred>_bark_v_1_rel</spred><label vid='11'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>--TPC</path><value>LUK</value></extrapair>
<extrapair><path>E.TENSE</path><value>PRESENT</value></extrapair>
<extrapair><path>E.MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>E.ASPECT.PROGR</path><value>-</value></extrapair>
<extrapair><path>E.ASPECT.PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='7' sort='x'>
<extrapair><path>--TPC</path><value>LUK</value></extrapair>
<extrapair><path>PRONTYPE</path><value>PRONTYPE</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair>
<extrapair><path>PNG.GEN</path><value>REAL_GENDER</value></extrapair>
<extrapair><path>PNG.PN</path><value>3SG</value></extrapair></var></fvpair></ep>
<hcons hreln='qeq'><hi><var vid='3' sort='h'></var></hi><lo><var vid='11' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='8' sort='h'></var></hi><lo><var vid='10' sort='h'></var></lo></hcons>
</mrs>



<!-- The cat chased the dog. -->
<mrs>
<label vid='1'/><var vid='2'/>
<ep cfrom='0' cto='5'><pred>PRPSTN_M_REL</pred><label vid='1'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PAST</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='3' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='5' sort='u'></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='4' sort='u'></var></fvpair></ep>
<ep cfrom='0' cto='1' surface='The'><pred>_THE_Q_REL</pred><label vid='6'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='8' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='9' sort='h'></var></fvpair></ep>
<ep cfrom='1' cto='2' surface='cat'><spred>_cat_n_1_rel</spred><label vid='10'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='2' cto='3' surface='chased'><spred>_chase_v_1_rel</spred><label vid='11'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PAST</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG2</rargname><var vid='12' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='3' cto='4' surface='the'><pred>_THE_Q_REL</pred><label vid='13'/>
<fvpair><rargname>ARG0</rargname><var vid='12' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='14' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='15' sort='h'></var></fvpair></ep>
<ep cfrom='4' cto='5' surface='dog'><spred>_dog_n_1_rel</spred><label vid='16'/>
<fvpair><rargname>ARG0</rargname><var vid='12' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<hcons hreln='qeq'><hi><var vid='3' sort='h'></var></hi><lo><var vid='11' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='8' sort='h'></var></hi><lo><var vid='10' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='14' sort='h'></var></hi><lo><var vid='16' sort='h'></var></lo></hcons>
</mrs>



<!-- Kim wants Sandy to like the dog. -->
<mrs>
<label vid='1'/><var vid='2'/>
<ep cfrom='0' cto='7'><pred>PRPSTN_M_REL</pred><label vid='1'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PRES</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='3' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='5' sort='u'></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='4' sort='u'></var></fvpair></ep>
<ep cfrom='0' cto='1'><pred>PROPER_Q_REL</pred><label vid='6'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='8' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='9' sort='h'></var></fvpair></ep>
<ep cfrom='0' cto='1'><pred>NAMED_REL</pred><label vid='10'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>CARG</rargname><constant>kim</constant></fvpair></ep>
<ep cfrom='1' cto='2'><spred>_want_v_1_rel</spred><label vid='11'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PRES</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG2</rargname><var vid='12' sort='h'></var></fvpair></ep>
<ep cfrom='2' cto='3'><pred>PROPER_Q_REL</pred><label vid='13'/>
<fvpair><rargname>ARG0</rargname><var vid='14' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='15' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='16' sort='h'></var></fvpair></ep>
<ep cfrom='2' cto='3'><pred>NAMED_REL</pred><label vid='17'/>
<fvpair><rargname>ARG0</rargname><var vid='14' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>CARG</rargname><constant>sandy</constant></fvpair></ep>
<ep cfrom='3' cto='7'><pred>PRPSTN_M_REL</pred><label vid='12'/>
<fvpair><rargname>ARG0</rargname><var vid='20' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='18' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='19' sort='u'></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='21' sort='u'></var></fvpair></ep>
<ep cfrom='4' cto='5'><spred>_like_v_1_rel</spred><label vid='22'/>
<fvpair><rargname>ARG0</rargname><var vid='20' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='14' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG2</rargname><var vid='23' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='5' cto='6'><pred>_THE_Q_REL</pred><label vid='24'/>
<fvpair><rargname>ARG0</rargname><var vid='23' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='25' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='26' sort='h'></var></fvpair></ep>
<ep cfrom='6' cto='7'><spred>_dog_n_1_rel</spred><label vid='27'/>
<fvpair><rargname>ARG0</rargname><var vid='23' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<hcons hreln='qeq'><hi><var vid='3' sort='h'></var></hi><lo><var vid='11' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='8' sort='h'></var></hi><lo><var vid='10' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='15' sort='h'></var></hi><lo><var vid='17' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='18' sort='h'></var></hi><lo><var vid='22' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='25' sort='h'></var></hi><lo><var vid='27' sort='h'></var></lo></hcons>
</mrs>



<!-- I can can a can. -->
<mrs>
<label vid='1'/><var vid='2'/>
<ep cfrom='0' cto='5'><pred>PRPSTN_M_REL</pred><label vid='1'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PRES</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='3' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='5' sort='u'></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='4' sort='u'></var></fvpair></ep>
<ep cfrom='0' cto='1'><pred>PRON_REL</pred><label vid='6'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>1</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>PRONTYPE</path><value>STD_PRON</value></extrapair></var></fvpair></ep>
<ep cfrom='0' cto='1'><pred>PRONOUN_Q_REL</pred><label vid='8'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>1</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>PRONTYPE</path><value>STD_PRON</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='9' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='10' sort='h'></var></fvpair></ep>
<ep cfrom='1' cto='2'><pred>_CAN_V_MODAL_REL</pred><label vid='11'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PRES</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='12' sort='h'></var></fvpair></ep>
<ep cfrom='2' cto='3'><spred>_can_v_1_rel</spred><label vid='13'/>
<fvpair><rargname>ARG0</rargname><var vid='15' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>1</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>PRONTYPE</path><value>STD_PRON</value></extrapair></var></fvpair>
<fvpair><rargname>ARG2</rargname><var vid='14' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='3' cto='4'><pred>_A_Q_REL</pred><label vid='16'/>
<fvpair><rargname>ARG0</rargname><var vid='14' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='17' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='18' sort='h'></var></fvpair></ep>
<ep cfrom='4' cto='5'><spred>_can_n_1_rel</spred><label vid='19'/>
<fvpair><rargname>ARG0</rargname><var vid='14' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<hcons hreln='qeq'><hi><var vid='3' sort='h'></var></hi><lo><var vid='11' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='9' sort='h'></var></hi><lo><var vid='6' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='12' sort='h'></var></hi><lo><var vid='13' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='17' sort='h'></var></hi><lo><var vid='19' sort='h'></var></lo></hcons>
</mrs>



<!-- The horse raced past the barn fell. -->
<mrs>
<label vid='1'/><var vid='2'/>
<ep cfrom='0' cto='7'><pred>PRPSTN_M_REL</pred><label vid='1'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PAST</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='3' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='5' sort='u'></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='4' sort='u'></var></fvpair></ep>
<ep cfrom='0' cto='1'><pred>_THE_Q_REL</pred><label vid='6'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='8' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='9' sort='h'></var></fvpair></ep>
<ep cfrom='1' cto='2'><spred>_horse_n_1_rel</spred><label vid='10'/>
<fvpair><rargname>ARG0</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='2' cto='6'><pred>PRPSTN_M_REL</pred><label vid='10'/>
<fvpair><rargname>ARG0</rargname><var vid='12' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>MARG</rargname><var vid='11' sort='h'></var></fvpair>
<fvpair><rargname>PSV</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>TPC</rargname><var vid='13' sort='u'></var></fvpair></ep>
<ep cfrom='2' cto='3'><spred>_race_v_1_rel</spred><label vid='14'/>
<fvpair><rargname>ARG0</rargname><var vid='12' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='15' sort='u'></var></fvpair>
<fvpair><rargname>ARG2</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='3' cto='4'><pred>_PAST_P_REL</pred><label vid='14'/>
<fvpair><rargname>ARG0</rargname><var vid='17' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='12' sort='e'>
<extrapair><path>TENSE</path><value>UNTENSED</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG2</rargname><var vid='16' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='4' cto='5'><pred>_THE_Q_REL</pred><label vid='18'/>
<fvpair><rargname>ARG0</rargname><var vid='16' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>RSTR</rargname><var vid='19' sort='h'></var></fvpair>
<fvpair><rargname>BODY</rargname><var vid='20' sort='h'></var></fvpair></ep>
<ep cfrom='5' cto='6'><spred>_barn_n_1_rel</spred><label vid='21'/>
<fvpair><rargname>ARG0</rargname><var vid='16' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<ep cfrom='6' cto='7'><spred>_fall_v_1_rel</spred><label vid='22'/>
<fvpair><rargname>ARG0</rargname><var vid='2' sort='e'>
<extrapair><path>TENSE</path><value>PAST</value></extrapair>
<extrapair><path>MOOD</path><value>INDICATIVE</value></extrapair>
<extrapair><path>PROG</path><value>-</value></extrapair>
<extrapair><path>PERF</path><value>-</value></extrapair></var></fvpair>
<fvpair><rargname>ARG1</rargname><var vid='7' sort='x'>
<extrapair><path>PERS</path><value>3</value></extrapair>
<extrapair><path>NUM</path><value>SG</value></extrapair>
<extrapair><path>DIV</path><value>-</value></extrapair></var></fvpair></ep>
<hcons hreln='qeq'><hi><var vid='3' sort='h'></var></hi><lo><var vid='22' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='8' sort='h'></var></hi><lo><var vid='10' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='11' sort='h'></var></hi><lo><var vid='14' sort='h'></var></lo></hcons>
<hcons hreln='qeq'><hi><var vid='19' sort='h'></var></hi><lo><var vid='21' sort='h'></var></lo></hcons>
</mrs>




</mrs-list>