m4_include(`config.m4')
m4_sinclude(`config.m4.local')

<?xml version='1.0' encoding="UTF-8"?>

<!DOCTYPE rmrs-list SYSTEM "file://_DIR_PYRMRSHOME/dtd/rmrs.dtd">
<rmrs-list>



<!-- What nationality is Pope John Paul II? -->
<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='-1' cto='-1'><gpred>int_m_rel</gpred><label vid='1'/><var sort='h' vid='3'/></ep>
<ep cfrom='-1' cto='-1' surface='What'><realpred lemma='which' pos='q'/><label vid='6'/><var sort='x' vid='5' gender='n' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='nationality'><realpred lemma='nationality' pos='n'/><label vid='9'/><var sort='x' vid='5' gender='n' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prop_ques_m_rel</gpred><label vid='3'/><var sort='h' vid='11'/></ep>
<ep cfrom='-1' cto='-1' surface='is'><realpred lemma='be' pos='v' sense='id'/><label vid='12'/><var sort='e' vid='2' tense='present'/></ep>
<ep cfrom='-1' cto='-1'><gpred>proper_q_rel</gpred><label vid='14'/><var sort='x' vid='13' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Pope'><realpred lemma='pope' pos='n'/><label vid='17'/><var sort='x' vid='18'/></ep>
<ep cfrom='-1' cto='-1' surface='Pope'><gpred>udef_q_rel</gpred><label vid='19'/><var sort='x' vid='18'/></ep>
<ep cfrom='-1' cto='-1' surface='Pope'><gpred>title_id_rel</gpred><label vid='22'/><var sort='u' vid='23'/></ep>
<ep cfrom='-1' cto='-1' surface='John Paul II'><gpred>named_rel</gpred><label vid='10001'/><var sort='x' vid='13' pers='3' num='sg'/></ep>
<rarg><rargname>TPC</rargname><label vid='1'/><var sort='x' vid='5' gender='n' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='6'/><var sort='h' vid='8'/></rarg>
<rarg><rargname>BODY</rargname><label vid='6'/><var sort='h' vid='7'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='9'/><var sort='u' vid='10'/></rarg>
<rarg><rargname>TPC</rargname><label vid='3'/><var sort='x' vid='5' gender='n' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='12'/><var sort='x' vid='5' gender='n' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='12'/><var sort='x' vid='13' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='14'/><var sort='h' vid='15'/></rarg>
<rarg><rargname>BODY</rargname><label vid='14'/><var sort='h' vid='16'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='19'/><var sort='h' vid='20'/></rarg>
<rarg><rargname>BODY</rargname><label vid='19'/><var sort='h' vid='21'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='22'/><var sort='x' vid='18'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='22'/><var sort='x' vid='13' pers='3' num='sg'/></rarg>
<rarg><rargname>CARG</rargname><label vid='10001'/><constant>john_paul_ii</constant></rarg>
<ing><ing-a><var sort='h' vid='22'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='8'/></hi><lo><label vid='9'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='11'/></hi><lo><label vid='12'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='15'/></hi><lo><label vid='22'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='20'/></hi><lo><label vid='17'/></lo></hcons>
</rmrs>



<!-- Where is the massive North Korean nuclear complex located? -->
<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='-1' cto='-1'><gpred>int_m_rel</gpred><label vid='1'/><var sort='h' vid='3'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='3'/><var sort='h' vid='6'/></ep>
<ep cfrom='-1' cto='-1'><gpred>unspec_loc_rel</gpred><label vid='9'/><var sort='e' vid='5' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='Where'><gpred>place_rel</gpred><label vid='11'/><var sort='x' vid='10' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Where'><gpred>which_q_rel</gpred><label vid='12'/><var sort='x' vid='10' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='the'><realpred lemma='the' pos='q'/><label vid='15'/><var sort='x' vid='4' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='massive'><realpred lemma='massive' pos='a'/><label vid='18'/><var sort='e' vid='19' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='North Korean'><realpred lemma='north+korean' pos='a'/><label vid='10001'/><var sort='e' vid='20' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='nuclear'><realpred lemma='nuclear' pos='a'/><label vid='10002'/><var sort='e' vid='21' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='complex'><realpred lemma='complex' pos='n'/><label vid='10003'/><var sort='x' vid='4' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='located'><realpred lemma='locate' pos='v'/><label vid='10004'/><var sort='e' vid='2' tense='present'/></ep>
<rarg><rargname>PSV</rargname><label vid='1'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>TPC</rargname><label vid='1'/><var sort='e' vid='5' tense='u'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='9'/><var sort='e' vid='2' tense='present'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='9'/><var sort='x' vid='10' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='12'/><var sort='h' vid='13'/></rarg>
<rarg><rargname>BODY</rargname><label vid='12'/><var sort='h' vid='14'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='15'/><var sort='h' vid='17'/></rarg>
<rarg><rargname>BODY</rargname><label vid='15'/><var sort='h' vid='16'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='18'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10001'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10002'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10003'/><var sort='u' vid='22'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10004'/><var sort='u' vid='23'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='10004'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<ing><ing-a><var sort='h' vid='9'/></ing-a><ing-b><var sort='h' vid='10004'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10002'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10003'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='6'/></hi><lo><label vid='9'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='13'/></hi><lo><label vid='11'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='17'/></hi><lo><label vid='18'/></lo></hcons>
</rmrs>



<!-- Who is the prime minister of Japan? -->
<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='-1' cto='-1'><gpred>int_m_rel</gpred><label vid='1'/><var sort='h' vid='3'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='3'/><var sort='h' vid='6'/></ep>
<ep cfrom='-1' cto='-1' surface='Who'><gpred>person_rel</gpred><label vid='9'/><var sort='x' vid='5' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Who'><gpred>which_q_rel</gpred><label vid='10'/><var sort='x' vid='5' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='is'><realpred lemma='be' pos='v' sense='id'/><label vid='13'/><var sort='e' vid='2' tense='present'/></ep>
<ep cfrom='-1' cto='-1' surface='the'><realpred lemma='the' pos='q'/><label vid='15'/><var sort='x' vid='14' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='prime minister'><realpred lemma='prime+minister' pos='n'/><label vid='18'/><var sort='x' vid='14' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='of'><realpred lemma='of' pos='p' sense='sel'/><label vid='10001'/><var sort='e' vid='21' tense='u'/></ep>
<ep cfrom='-1' cto='-1'><gpred>proper_q_rel</gpred><label vid='22'/><var sort='x' vid='19' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Japan'><gpred>named_rel</gpred><label vid='25'/><var sort='x' vid='19' pers='3' num='sg'/></ep>
<rarg><rargname>TPC</rargname><label vid='1'/><var sort='x' vid='5' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='10'/><var sort='h' vid='11'/></rarg>
<rarg><rargname>BODY</rargname><label vid='10'/><var sort='h' vid='12'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='13'/><var sort='x' vid='14' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='13'/><var sort='x' vid='5' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='15'/><var sort='h' vid='17'/></rarg>
<rarg><rargname>BODY</rargname><label vid='15'/><var sort='h' vid='16'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='18'/><var sort='x' vid='19' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='10001'/><var sort='x' vid='19' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='22'/><var sort='h' vid='23'/></rarg>
<rarg><rargname>BODY</rargname><label vid='22'/><var sort='h' vid='24'/></rarg>
<rarg><rargname>CARG</rargname><label vid='25'/><constant>japan</constant></rarg>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='6'/></hi><lo><label vid='13'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='11'/></hi><lo><label vid='9'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='17'/></hi><lo><label vid='18'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='23'/></hi><lo><label vid='25'/></lo></hcons>
</rmrs>



<!-- Where is the massive North Korean nuclear complex located? -->
<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='-1' cto='-1'><gpred>int_m_rel</gpred><label vid='1'/><var sort='h' vid='3'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='3'/><var sort='h' vid='6'/></ep>
<ep cfrom='-1' cto='-1'><gpred>unspec_loc_rel</gpred><label vid='9'/><var sort='e' vid='5' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='Where'><gpred>place_rel</gpred><label vid='11'/><var sort='x' vid='10' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Where'><gpred>which_q_rel</gpred><label vid='12'/><var sort='x' vid='10' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='the'><realpred lemma='the' pos='q'/><label vid='15'/><var sort='x' vid='4' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='massive'><realpred lemma='massive' pos='a'/><label vid='18'/><var sort='e' vid='19' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='North Korean'><realpred lemma='north+korean' pos='a'/><label vid='10001'/><var sort='e' vid='20' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='nuclear'><realpred lemma='nuclear' pos='a'/><label vid='10002'/><var sort='e' vid='21' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='complex'><realpred lemma='complex' pos='n'/><label vid='10003'/><var sort='x' vid='4' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='located'><realpred lemma='locate' pos='v'/><label vid='10004'/><var sort='e' vid='2' tense='present'/></ep>
<rarg><rargname>PSV</rargname><label vid='1'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>TPC</rargname><label vid='1'/><var sort='e' vid='5' tense='u'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='9'/><var sort='e' vid='2' tense='present'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='9'/><var sort='x' vid='10' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='12'/><var sort='h' vid='13'/></rarg>
<rarg><rargname>BODY</rargname><label vid='12'/><var sort='h' vid='14'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='15'/><var sort='h' vid='17'/></rarg>
<rarg><rargname>BODY</rargname><label vid='15'/><var sort='h' vid='16'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='18'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10001'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10002'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10003'/><var sort='u' vid='22'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10004'/><var sort='u' vid='23'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='10004'/><var sort='x' vid='4' pers='3' num='sg'/></rarg>
<ing><ing-a><var sort='h' vid='9'/></ing-a><ing-b><var sort='h' vid='10004'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10002'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='18'/></ing-a><ing-b><var sort='h' vid='10003'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='6'/></hi><lo><label vid='9'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='13'/></hi><lo><label vid='11'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='17'/></hi><lo><label vid='18'/></lo></hcons>
</rmrs>



<!-- How many people live in Tokyo? -->
<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='-1' cto='-1'><gpred>int_m_rel</gpred><label vid='1'/><var sort='h' vid='3'/></ep>
<ep cfrom='-1' cto='-1' surface='How many'><gpred>udef_q_rel</gpred><label vid='6'/><var sort='x' vid='5' pers='3' num='pl'/></ep>
<ep cfrom='-1' cto='-1' surface='How many'><gpred>which_q_rel</gpred><label vid='9'/><var sort='x' vid='10'/></ep>
<ep cfrom='-1' cto='-1' surface='How many'><gpred>number_rel</gpred><label vid='13'/><var sort='x' vid='10'/></ep>
<ep cfrom='-1' cto='-1' surface='How many'><gpred>unspec_rel</gpred><label vid='10001'/><var sort='e' vid='15' tense='u'/></ep>
<ep cfrom='-1' cto='-1' surface='people'><realpred lemma='people' pos='n'/><label vid='16'/><var sort='x' vid='5' pers='3' num='pl'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prop_ques_m_rel</gpred><label vid='3'/><var sort='h' vid='18'/></ep>
<ep cfrom='-1' cto='-1' surface='live'><realpred lemma='live' pos='v' sense='1'/><label vid='19'/><var sort='e' vid='2' tense='present'/></ep>
<ep cfrom='-1' cto='-1' surface='in'><realpred lemma='in' pos='p'/><label vid='10002'/><var sort='e' vid='21' tense='u'/></ep>
<ep cfrom='-1' cto='-1'><gpred>proper_q_rel</gpred><label vid='22'/><var sort='x' vid='20' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Tokyo'><gpred>named_rel</gpred><label vid='25'/><var sort='x' vid='20' pers='3' num='sg'/></ep>
<rarg><rargname>TPC</rargname><label vid='1'/><var sort='x' vid='5' pers='3' num='pl'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='6'/><var sort='h' vid='8'/></rarg>
<rarg><rargname>BODY</rargname><label vid='6'/><var sort='h' vid='7'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='9'/><var sort='h' vid='11'/></rarg>
<rarg><rargname>BODY</rargname><label vid='9'/><var sort='h' vid='12'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='13'/><var sort='u' vid='14'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10001'/><var sort='x' vid='5' pers='3' num='pl'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='10001'/><var sort='x' vid='10'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='16'/><var sort='u' vid='17'/></rarg>
<rarg><rargname>TPC</rargname><label vid='3'/><var sort='x' vid='5' pers='3' num='pl'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='19'/><var sort='x' vid='5' pers='3' num='pl'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10002'/><var sort='e' vid='2' tense='present'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='10002'/><var sort='x' vid='20' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='22'/><var sort='h' vid='23'/></rarg>
<rarg><rargname>BODY</rargname><label vid='22'/><var sort='h' vid='24'/></rarg>
<rarg><rargname>CARG</rargname><label vid='25'/><constant>tokyo</constant></rarg>
<ing><ing-a><var sort='h' vid='13'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='19'/></ing-a><ing-b><var sort='h' vid='10002'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='8'/></hi><lo><label vid='16'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='11'/></hi><lo><label vid='13'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='18'/></hi><lo><label vid='19'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='23'/></hi><lo><label vid='25'/></lo></hcons>
</rmrs>



<!-- Who was President Cleveland's wife? -->
<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='-1' cto='-1'><gpred>int_m_rel</gpred><label vid='1'/><var sort='h' vid='3'/></ep>
<ep cfrom='-1' cto='-1' surface='Who'><gpred>person_rel</gpred><label vid='6'/><var sort='x' vid='5' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='Who'><gpred>which_q_rel</gpred><label vid='7'/><var sort='x' vid='5' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prop_ques_m_rel</gpred><label vid='3'/><var sort='h' vid='10'/></ep>
<ep cfrom='-1' cto='-1' surface='was'><realpred lemma='be' pos='v' sense='id'/><label vid='11'/><var sort='e' vid='2' tense='past'/></ep>
<ep cfrom='-1' cto='-1'><gpred>proper_q_rel</gpred><label vid='13'/><var sort='x' vid='14' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='17'/><var sort='e' vid='19' tense='u'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='20'/><var sort='x' vid='18'/></ep>
<ep cfrom='-1' cto='-1' surface='President'><realpred lemma='president' pos='n'/><label vid='23'/><var sort='x' vid='18'/></ep>
<ep cfrom='-1' cto='-1' surface='Cleveland'><gpred>named_rel</gpred><label vid='10001'/><var sort='x' vid='14' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='s'><gpred>def_explicit_q_rel</gpred><label vid='25'/><var sort='x' vid='12' pers='3' num='sg'/></ep>
<ep cfrom='-1' cto='-1' surface='s'><gpred>poss_rel</gpred><label vid='28'/><var sort='u' vid='29'/></ep>
<ep cfrom='-1' cto='-1' surface='wife'><realpred lemma='wife' pos='n'/><label vid='10002'/><var sort='x' vid='12' pers='3' num='sg'/></ep>
<rarg><rargname>TPC</rargname><label vid='1'/><var sort='x' vid='5' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='7'/><var sort='h' vid='8'/></rarg>
<rarg><rargname>BODY</rargname><label vid='7'/><var sort='h' vid='9'/></rarg>
<rarg><rargname>TPC</rargname><label vid='3'/><var sort='x' vid='5' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='11'/><var sort='x' vid='5' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='11'/><var sort='x' vid='12' pers='3' num='sg'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='13'/><var sort='h' vid='15'/></rarg>
<rarg><rargname>BODY</rargname><label vid='13'/><var sort='h' vid='16'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='17'/><var sort='x' vid='14' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='17'/><var sort='x' vid='18'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='20'/><var sort='h' vid='21'/></rarg>
<rarg><rargname>BODY</rargname><label vid='20'/><var sort='h' vid='22'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='23'/><var sort='u' vid='24'/></rarg>
<rarg><rargname>CARG</rargname><label vid='10001'/><constant>cleveland</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='25'/><var sort='h' vid='26'/></rarg>
<rarg><rargname>BODY</rargname><label vid='25'/><var sort='h' vid='27'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='28'/><var sort='x' vid='14' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='28'/><var sort='x' vid='12' pers='3' num='sg'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10002'/><var sort='u' vid='30'/></rarg>
<ing><ing-a><var sort='h' vid='17'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='10002'/></ing-a><ing-b><var sort='h' vid='28'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='8'/></hi><lo><label vid='6'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='10'/></hi><lo><label vid='11'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='15'/></hi><lo><label vid='17'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='21'/></hi><lo><label vid='23'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='26'/></hi><lo><label vid='28'/></lo></hcons>
</rmrs>



<!--
  "Nobel" "Peace" "Prize" "committee" "chairman" "Egil" "Aarvik" "," "who"
  "used" "the" "Nobel" "Peace" "Prize" "to" "encourage" "human" "rights" ","
  "has" "died"
-->
<rmrs cfrom='-1' cto='-1'>
<label vid='144'/>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='144'/><var sort='h' vid='147'/></ep>
<ep cfrom='-1' cto='-1' surface='Nobel'><gpred>proper_q_rel</gpred><label vid='1'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='Nobel'><gpred>named_rel</gpred><label vid='3'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='32'/><var sort='e' vid='35'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='36'/><var sort='x' vid='7'/></ep>
<ep cfrom='-1' cto='-1' surface='Peace'><realpred lemma='peace' pos='n'/><label vid='6'/><var sort='x' vid='7'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='23'/><var sort='e' vid='26'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='27'/><var sort='x' vid='9'/></ep>
<ep cfrom='-1' cto='-1' surface='Prize'><realpred lemma='prize' pos='n'/><label vid='8'/><var sort='x' vid='9'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='14'/><var sort='e' vid='17'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='18'/><var sort='x' vid='11'/></ep>
<ep cfrom='-1' cto='-1' surface='committee'><realpred lemma='committee' pos='n'/><label vid='10'/><var sort='x' vid='11'/></ep>
<ep cfrom='-1' cto='-1' surface='chairman'><realpred lemma='chairman' pos='n'/><label vid='12'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='Egil'><gpred>proper_q_rel</gpred><label vid='44'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='Egil'><gpred>named_rel</gpred><label vid='46'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='Aarvik'><gpred>proper_q_rel</gpred><label vid='49'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='Aarvik'><gpred>named_rel</gpred><label vid='51'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prop_ques_m_rel</gpred><label vid='128'/><var sort='h' vid='131'/></ep>
<ep cfrom='-1' cto='-1' surface='who'><realpred lemma='who' pos='x'/><label vid='62'/><var sort='u' vid='63'/></ep>
<ep cfrom='-1' cto='-1' surface='used'><realpred lemma='use' pos='v'/><label vid='64'/><var sort='e' vid='65' tense='past'/></ep>
<ep cfrom='-1' cto='-1' surface='the'><realpred lemma='the' pos='q'/><label vid='66'/><var sort='x' vid='67'/></ep>
<ep cfrom='-1' cto='-1' surface='Nobel'><gpred>proper_q_rel</gpred><label vid='68'/><var sort='x' vid='67'/></ep>
<ep cfrom='-1' cto='-1' surface='Nobel'><gpred>named_rel</gpred><label vid='70'/><var sort='x' vid='67'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='77'/><var sort='e' vid='80'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='81'/><var sort='x' vid='74'/></ep>
<ep cfrom='-1' cto='-1' surface='Peace'><realpred lemma='peace' pos='n'/><label vid='73'/><var sort='x' vid='74'/></ep>
<ep cfrom='-1' cto='-1' surface='Prize'><realpred lemma='prize' pos='n'/><label vid='75'/><var sort='x' vid='67'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='119'/><var sort='h' vid='122'/></ep>
<ep cfrom='-1' cto='-1' surface='encourage'><realpred lemma='encourage' pos='v'/><label vid='97'/><var sort='e' vid='98'/></ep>
<ep cfrom='-1' cto='-1'><gpred>bare_div_q_rel</gpred><label vid='111'/><var sort='x' vid='106'/></ep>
<ep cfrom='-1' cto='-1' surface='human'><realpred lemma='human' pos='j'/><label vid='99'/><var sort='e' vid='100'/></ep>
<ep cfrom='-1' cto='-1' surface='rights'><realpred lemma='rights' pos='n'/><label vid='105'/><var sort='x' vid='106'/></ep>
<ep cfrom='-1' cto='-1' surface='has'><realpred lemma='have' pos='v'/><label vid='138'/><var sort='e' vid='139'/></ep>
<ep cfrom='-1' cto='-1' surface='died'><realpred lemma='die' pos='v'/><label vid='140'/><var sort='e' vid='141'/></ep>
<rarg><rargname>ARG1</rargname><label vid='140'/><var sort='x' vid='2'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='1'/><var sort='h' vid='4'/></rarg>
<rarg><rargname>BODY</rargname><label vid='1'/><var sort='h' vid='5'/></rarg>
<rarg><rargname>CARG</rargname><label vid='3'/><constant>nobel</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='32'/><var sort='x' vid='2'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='32'/><var sort='x' vid='7'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='36'/><var sort='h' vid='38'/></rarg>
<rarg><rargname>BODY</rargname><label vid='36'/><var sort='h' vid='39'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='23'/><var sort='x' vid='2'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='23'/><var sort='x' vid='9'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='27'/><var sort='h' vid='29'/></rarg>
<rarg><rargname>BODY</rargname><label vid='27'/><var sort='h' vid='30'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='14'/><var sort='x' vid='2'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='14'/><var sort='x' vid='11'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='18'/><var sort='h' vid='20'/></rarg>
<rarg><rargname>BODY</rargname><label vid='18'/><var sort='h' vid='21'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='44'/><var sort='h' vid='47'/></rarg>
<rarg><rargname>BODY</rargname><label vid='44'/><var sort='h' vid='48'/></rarg>
<rarg><rargname>CARG</rargname><label vid='46'/><constant>egil</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='49'/><var sort='h' vid='52'/></rarg>
<rarg><rargname>BODY</rargname><label vid='49'/><var sort='h' vid='53'/></rarg>
<rarg><rargname>CARG</rargname><label vid='51'/><constant>aarvik</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='64'/><var sort='x' vid='63'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='64'/><var sort='x' vid='67'/></rarg>
<rarg><rargname>ARG3</rargname><label vid='64'/><var sort='h' vid='119'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='66'/><var sort='h' vid='92'/></rarg>
<rarg><rargname>BODY</rargname><label vid='66'/><var sort='h' vid='93'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='68'/><var sort='h' vid='71'/></rarg>
<rarg><rargname>BODY</rargname><label vid='68'/><var sort='h' vid='72'/></rarg>
<rarg><rargname>CARG</rargname><label vid='70'/><constant>nobel</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='77'/><var sort='x' vid='67'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='77'/><var sort='x' vid='74'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='81'/><var sort='h' vid='83'/></rarg>
<rarg><rargname>BODY</rargname><label vid='81'/><var sort='h' vid='84'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='97'/><var sort='u' vid='123'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='97'/><var sort='x' vid='106'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='111'/><var sort='h' vid='113'/></rarg>
<rarg><rargname>BODY</rargname><label vid='111'/><var sort='h' vid='114'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='99'/><var sort='x' vid='106'/></rarg>
<ing><ing-a><var sort='h' vid='32'/></ing-a><ing-b><var sort='h' vid='44'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='1'/></ing-a><ing-b><var sort='h' vid='32'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='32'/></ing-a><ing-b><var sort='h' vid='23'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='23'/></ing-a><ing-b><var sort='h' vid='14'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='14'/></ing-a><ing-b><var sort='h' vid='12'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='44'/></ing-a><ing-b><var sort='h' vid='49'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='68'/></ing-a><ing-b><var sort='h' vid='77'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='77'/></ing-a><ing-b><var sort='h' vid='75'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='105'/></ing-a><ing-b><var sort='h' vid='99'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='147'/></hi><lo><label vid='140'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='4'/></hi><lo><label vid='3'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='38'/></hi><lo><label vid='6'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='29'/></hi><lo><label vid='8'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='20'/></hi><lo><label vid='10'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='47'/></hi><lo><label vid='46'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='52'/></hi><lo><label vid='51'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='131'/></hi><lo><label vid='64'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='92'/></hi><lo><label vid='77'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='71'/></hi><lo><label vid='70'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='83'/></hi><lo><label vid='73'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='122'/></hi><lo><label vid='97'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='113'/></hi><lo><label vid='105'/></lo></hcons>
</rmrs>



<!--
  "Aarvik" "is" "survived" "by" "his" "wife" "," "Anna" "Cathrine" "," "three"
  "sons" "," "a" "daughter" "and" "11" "grandchildren")
-->
<rmrs cfrom='-1' cto='-1'>
<label vid='44'/>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='44'/><var sort='h' vid='47'/></ep>
<ep cfrom='-1' cto='-1' surface='Aarvik'><gpred>proper_q_rel</gpred><label vid='1'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='Aarvik'><gpred>named_rel</gpred><label vid='3'/><var sort='x' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='is'><realpred lemma='be' pos='v'/><label vid='6'/><var sort='e' vid='7'/></ep>
<ep cfrom='-1' cto='-1' surface='survived'><realpred lemma='survive' pos='v'/><label vid='8'/><var sort='e' vid='9'/></ep>
<ep cfrom='-1' cto='-1' surface='by'><realpred lemma='by' pos='p'/><label vid='14'/><var sort='e' vid='15'/></ep>
<ep cfrom='-1' cto='-1' surface='his'><gpred>def_explicit_q_rel</gpred><label vid='16'/><var sort='x' vid='17'/></ep>
<ep cfrom='-1' cto='-1' surface='his'><gpred>pro_poss_rel</gpred><label vid='18'/><var sort='u' vid='19'/></ep>
<ep cfrom='-1' cto='-1' surface='his'><gpred>pronoun_q_rel</gpred><label vid='20'/><var sort='x' vid='21'/></ep>
<ep cfrom='-1' cto='-1' surface='his'><gpred>pron_rel</gpred><label vid='22'/><var sort='x' vid='21'/></ep>
<ep cfrom='-1' cto='-1' surface='wife'><realpred lemma='wife' pos='n'/><label vid='25'/><var sort='x' vid='17'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='110'/><var sort='x' vid='68'/></ep>
<ep cfrom='-1' cto='-1'><gpred>implicit_conj_rel</gpred><label vid='108'/><var sort='x' vid='109'/></ep>
<ep cfrom='-1' cto='-1' surface='Anna'><gpred>proper_q_rel</gpred><label vid='52'/><var sort='x' vid='53'/></ep>
<ep cfrom='-1' cto='-1' surface='Anna'><gpred>named_rel</gpred><label vid='54'/><var sort='x' vid='53'/></ep>
<ep cfrom='-1' cto='-1' surface='Cathrine'><gpred>proper_q_rel</gpred><label vid='57'/><var sort='x' vid='53'/></ep>
<ep cfrom='-1' cto='-1' surface='Cathrine'><gpred>named_rel</gpred><label vid='59'/><var sort='x' vid='53'/></ep>
<ep cfrom='-1' cto='-1'><gpred>bare_div_q_rel</gpred><label vid='77'/><var sort='x' vid='68'/></ep>
<ep cfrom='-1' cto='-1' surface='three'><gpred>card_rel</gpred><label vid='67'/><var sort='u' vid='69'/></ep>
<ep cfrom='-1' cto='-1' surface='sons'><realpred lemma='son' pos='n'/><label vid='72'/><var sort='x' vid='68'/></ep>
<ep cfrom='-1' cto='-1' surface='a'><realpred lemma='a' pos='q'/><label vid='84'/><var sort='x' vid='85'/></ep>
<ep cfrom='-1' cto='-1' surface='daughter'><realpred lemma='daughter' pos='n'/><label vid='86'/><var sort='x' vid='87'/></ep>
<ep cfrom='-1' cto='-1' surface='and'><realpred lemma='and' pos='x'/><label vid='88'/><var sort='u' vid='89'/></ep>
<ep cfrom='-1' cto='-1' surface='11'><gpred>card_rel</gpred><label vid='90'/><var sort='u' vid='92'/></ep>
<ep cfrom='-1' cto='-1' surface='grandchildren'><realpred lemma='grandchild' pos='n'/><label vid='95'/><var sort='x' vid='91'/></ep>
<rarg><rargname>ARG1</rargname><label vid='41'/><var sort='x' vid='2'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='1'/><var sort='h' vid='4'/></rarg>
<rarg><rargname>BODY</rargname><label vid='1'/><var sort='h' vid='5'/></rarg>
<rarg><rargname>CARG</rargname><label vid='3'/><constant>aarvik</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='14'/><var sort='e' vid='12'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='14'/><var sort='x' vid='17'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='16'/><var sort='h' vid='30'/></rarg>
<rarg><rargname>BODY</rargname><label vid='16'/><var sort='h' vid='31'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='18'/><var sort='x' vid='21'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='18'/><var sort='x' vid='17'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='20'/><var sort='h' vid='23'/></rarg>
<rarg><rargname>BODY</rargname><label vid='20'/><var sort='h' vid='24'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='110'/><var sort='h' vid='108'/></rarg>
<rarg><rargname>BODY</rargname><label vid='110'/><var sort='h' vid='112'/></rarg>
<rarg><rargname>L-INDEX</rargname><label vid='108'/><var sort='x' vid='53'/></rarg>
<rarg><rargname>R-INDEX</rargname><label vid='108'/><var sort='x' vid='68'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='52'/><var sort='h' vid='55'/></rarg>
<rarg><rargname>BODY</rargname><label vid='52'/><var sort='h' vid='56'/></rarg>
<rarg><rargname>CARG</rargname><label vid='54'/><constant>anna</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='57'/><var sort='h' vid='60'/></rarg>
<rarg><rargname>BODY</rargname><label vid='57'/><var sort='h' vid='61'/></rarg>
<rarg><rargname>CARG</rargname><label vid='59'/><constant>cathrine</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='77'/><var sort='h' vid='79'/></rarg>
<rarg><rargname>BODY</rargname><label vid='77'/><var sort='h' vid='80'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='67'/><var sort='x' vid='68'/></rarg>
<rarg><rargname>CARG</rargname><label vid='67'/><constant>three</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='84'/><var sort='h' vid='105'/></rarg>
<rarg><rargname>BODY</rargname><label vid='84'/><var sort='h' vid='106'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='90'/><var sort='x' vid='91'/></rarg>
<rarg><rargname>CARG</rargname><label vid='90'/><constant>11</constant></rarg>
<ing><ing-a><var sort='h' vid='13'/></ing-a><ing-b><var sort='h' vid='14'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='52'/></ing-a><ing-b><var sort='h' vid='57'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='72'/></ing-a><ing-b><var sort='h' vid='67'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='95'/></ing-a><ing-b><var sort='h' vid='90'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='47'/></hi><lo><label vid='13'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='4'/></hi><lo><label vid='3'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='30'/></hi><lo><label vid='25'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='23'/></hi><lo><label vid='22'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='55'/></hi><lo><label vid='54'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='60'/></hi><lo><label vid='59'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='79'/></hi><lo><label vid='72'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='105'/></hi><lo><label vid='101'/></lo></hcons>
</rmrs>



<!--
  "On" "June" "2" "," "1925" "," "Wally" "Pipp" "had" "a" "headache" "and"
  "was" "replaced" "at" "first" "base" "in" "the" "New" "York" "Yankee"
  "lineup" "by" "a" "quiet" "hometown" "kid" "named" "Lou" "Gehrig"
-->

<rmrs cfrom='-1' cto='-1'>
<label vid='223'/>
<ep cfrom='-1' cto='-1' surface='On'><realpred lemma='on' pos='p'/><label vid='1'/><var sort='e' vid='2'/></ep>
<ep cfrom='-1' cto='-1' surface='June'><gpred>non_freerel_q_rel</gpred><label vid='5'/><var sort='x' vid='4'/></ep>
<ep cfrom='-1' cto='-1' surface='June'><gpred>mofy_rel</gpred><label vid='3'/><var sort='x' vid='4'/></ep>
<ep cfrom='-1' cto='-1' surface='2'><gpred>card_rel</gpred><label vid='9'/><var sort='u' vid='11'/></ep>
<ep cfrom='-1' cto='-1' surface='1925'><gpred>card_rel</gpred><label vid='16'/><var sort='u' vid='18'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='223'/><var sort='h' vid='226'/></ep>
<ep cfrom='-1' cto='-1' surface='Wally'><gpred>proper_q_rel</gpred><label vid='31'/><var sort='x' vid='32'/></ep>
<ep cfrom='-1' cto='-1' surface='Wally'><gpred>named_rel</gpred><label vid='33'/><var sort='x' vid='32'/></ep>
<ep cfrom='-1' cto='-1' surface='Pipp'><gpred>proper_q_rel</gpred><label vid='36'/><var sort='x' vid='32'/></ep>
<ep cfrom='-1' cto='-1' surface='Pipp'><gpred>named_rel</gpred><label vid='38'/><var sort='x' vid='32'/></ep>
<ep cfrom='-1' cto='-1' surface='had'><realpred lemma='have' pos='v'/><label vid='44'/><var sort='e' vid='45'/></ep>
<ep cfrom='-1' cto='-1' surface='a'><realpred lemma='a' pos='q'/><label vid='46'/><var sort='x' vid='47'/></ep>
<ep cfrom='-1' cto='-1' surface='headache'><realpred lemma='headache' pos='n'/><label vid='48'/><var sort='x' vid='47'/></ep>
<ep cfrom='-1' cto='-1' surface='and'><realpred lemma='and' pos='x'/><label vid='58'/><var sort='u' vid='59'/></ep>
<ep cfrom='-1' cto='-1' surface='was'><realpred lemma='be' pos='v'/><label vid='60'/><var sort='e' vid='61'/></ep>
<ep cfrom='-1' cto='-1' surface='replaced'><realpred lemma='replace' pos='v'/><label vid='62'/><var sort='e' vid='63'/></ep>
<ep cfrom='-1' cto='-1'><gpred>implicit_q_rel</gpred><label vid='84'/><var sort='x' vid='77'/></ep>
<ep cfrom='-1' cto='-1' surface='at'><realpred lemma='at' pos='p'/><label vid='68'/><var sort='e' vid='69'/></ep>
<ep cfrom='-1' cto='-1' surface='first'><realpred lemma='first' pos='x'/><label vid='70'/><var sort='e' vid='71'/></ep>
<ep cfrom='-1' cto='-1' surface='base'><realpred lemma='base' pos='n'/><label vid='76'/><var sort='x' vid='77'/></ep>
<ep cfrom='-1' cto='-1' surface='in'><realpred lemma='in' pos='p'/><label vid='97'/><var sort='e' vid='98'/></ep>
<ep cfrom='-1' cto='-1' surface='the'><realpred lemma='the' pos='q'/><label vid='99'/><var sort='x' vid='100'/></ep>
<ep cfrom='-1' cto='-1' surface='New'><realpred lemma='new' pos='j'/><label vid='101'/><var sort='e' vid='102'/></ep>
<ep cfrom='-1' cto='-1' surface='York'><gpred>proper_q_rel</gpred><label vid='107'/><var sort='x' vid='100'/></ep>
<ep cfrom='-1' cto='-1' surface='York'><gpred>named_rel</gpred><label vid='109'/><var sort='x' vid='100'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='116'/><var sort='e' vid='119'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='120'/><var sort='x' vid='113'/></ep>
<ep cfrom='-1' cto='-1' surface='Yankee'><realpred lemma='yankee' pos='n'/><label vid='112'/><var sort='x' vid='113'/></ep>
<ep cfrom='-1' cto='-1' surface='lineup'><realpred lemma='lineup' pos='n'/><label vid='114'/><var sort='x' vid='100'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='191'/><var sort='h' vid='192'/></ep>
<ep cfrom='-1' cto='-1' surface='by'><realpred lemma='by' pos='p'/><label vid='132'/><var sort='e' vid='133'/></ep>
<ep cfrom='-1' cto='-1'><gpred>prpstn_m_rel</gpred><label vid='183'/><var sort='h' vid='186'/></ep>
<ep cfrom='-1' cto='-1' surface='a'><realpred lemma='a' pos='q'/><label vid='134'/><var sort='x' vid='135'/></ep>
<ep cfrom='-1' cto='-1' surface='quiet'><realpred lemma='quiet' pos='j'/><label vid='136'/><var sort='e' vid='137'/></ep>
<ep cfrom='-1' cto='-1'><gpred>compound_rel</gpred><label vid='146'/><var sort='e' vid='149'/></ep>
<ep cfrom='-1' cto='-1'><gpred>udef_q_rel</gpred><label vid='150'/><var sort='x' vid='143'/></ep>
<ep cfrom='-1' cto='-1' surface='hometown'><realpred lemma='hometown' pos='n'/><label vid='142'/><var sort='x' vid='143'/></ep>
<ep cfrom='-1' cto='-1' surface='kid'><realpred lemma='kid' pos='n'/><label vid='144'/><var sort='x' vid='135'/></ep>
<ep cfrom='-1' cto='-1' surface='named'><realpred lemma='name' pos='v'/><label vid='165'/><var sort='e' vid='166'/></ep>
<ep cfrom='-1' cto='-1' surface='Lou'><gpred>proper_q_rel</gpred><label vid='167'/><var sort='x' vid='168'/></ep>
<ep cfrom='-1' cto='-1' surface='Lou'><gpred>named_rel</gpred><label vid='169'/><var sort='x' vid='168'/></ep>
<ep cfrom='-1' cto='-1' surface='Gehrig'><gpred>proper_q_rel</gpred><label vid='172'/><var sort='x' vid='168'/></ep>
<ep cfrom='-1' cto='-1' surface='Gehrig'><gpred>named_rel</gpred><label vid='174'/><var sort='x' vid='168'/></ep>
<rarg><rargname>ARG1</rargname><label vid='1'/><var sort='e' vid='221'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='1'/><var sort='x' vid='21'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='5'/><var sort='h' vid='6'/></rarg>
<rarg><rargname>BODY</rargname><label vid='5'/><var sort='h' vid='7'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='3'/><var sort='u' vid='8'/></rarg>
<rarg><rargname>CARG</rargname><label vid='3'/><constant>june</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='9'/><var sort='x' vid='10'/></rarg>
<rarg><rargname>CARG</rargname><label vid='9'/><constant>2</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='16'/><var sort='x' vid='17'/></rarg>
<rarg><rargname>CARG</rargname><label vid='16'/><constant>1925</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='225'/><var sort='x' vid='32'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='31'/><var sort='h' vid='34'/></rarg>
<rarg><rargname>BODY</rargname><label vid='31'/><var sort='h' vid='35'/></rarg>
<rarg><rargname>CARG</rargname><label vid='33'/><constant>wally</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='36'/><var sort='h' vid='39'/></rarg>
<rarg><rargname>BODY</rargname><label vid='36'/><var sort='h' vid='40'/></rarg>
<rarg><rargname>CARG</rargname><label vid='38'/><constant>pipp</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='46'/><var sort='h' vid='53'/></rarg>
<rarg><rargname>BODY</rargname><label vid='46'/><var sort='h' vid='54'/></rarg>
<rarg><rargname>R-HNDL</rargname><label vid='58'/><var sort='h' vid='67'/></rarg>
<rarg><rargname>R-INDEX</rargname><label vid='58'/><var sort='e' vid='66'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='97'/><var sort='e' vid='66'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='68'/><var sort='e' vid='66'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='84'/><var sort='h' vid='86'/></rarg>
<rarg><rargname>BODY</rargname><label vid='84'/><var sort='h' vid='87'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='68'/><var sort='x' vid='77'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='70'/><var sort='x' vid='77'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='97'/><var sort='x' vid='100'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='99'/><var sort='h' vid='203'/></rarg>
<rarg><rargname>BODY</rargname><label vid='99'/><var sort='h' vid='204'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='132'/><var sort='x' vid='100'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='101'/><var sort='x' vid='100'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='107'/><var sort='h' vid='110'/></rarg>
<rarg><rargname>BODY</rargname><label vid='107'/><var sort='h' vid='111'/></rarg>
<rarg><rargname>CARG</rargname><label vid='109'/><constant>york</constant></rarg>
<rarg><rargname>ARG1</rargname><label vid='116'/><var sort='x' vid='100'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='116'/><var sort='x' vid='113'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='120'/><var sort='h' vid='122'/></rarg>
<rarg><rargname>BODY</rargname><label vid='120'/><var sort='h' vid='123'/></rarg>
<rarg><rargname>SUBORD</rargname><label vid='132'/><var sort='h' vid='183'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='165'/><var sort='x' vid='135'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='134'/><var sort='h' vid='162'/></rarg>
<rarg><rargname>BODY</rargname><label vid='134'/><var sort='h' vid='163'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='136'/><var sort='x' vid='135'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='146'/><var sort='x' vid='135'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='146'/><var sort='x' vid='143'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='150'/><var sort='h' vid='152'/></rarg>
<rarg><rargname>BODY</rargname><label vid='150'/><var sort='h' vid='153'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='165'/><var sort='x' vid='168'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='167'/><var sort='h' vid='170'/></rarg>
<rarg><rargname>BODY</rargname><label vid='167'/><var sort='h' vid='171'/></rarg>
<rarg><rargname>CARG</rargname><label vid='169'/><constant>lou</constant></rarg>
<rarg><rargname>RSTR</rargname><label vid='172'/><var sort='h' vid='175'/></rarg>
<rarg><rargname>BODY</rargname><label vid='172'/><var sort='h' vid='176'/></rarg>
<rarg><rargname>CARG</rargname><label vid='174'/><constant>gehrig</constant></rarg>
<ing><ing-a><var sort='h' vid='225'/></ing-a><ing-b><var sort='h' vid='1'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='31'/></ing-a><ing-b><var sort='h' vid='36'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='67'/></ing-a><ing-b><var sort='h' vid='97'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='67'/></ing-a><ing-b><var sort='h' vid='68'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='76'/></ing-a><ing-b><var sort='h' vid='70'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='116'/></ing-a><ing-b><var sort='h' vid='132'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='116'/></ing-a><ing-b><var sort='h' vid='101'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='107'/></ing-a><ing-b><var sort='h' vid='116'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='116'/></ing-a><ing-b><var sort='h' vid='114'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='146'/></ing-a><ing-b><var sort='h' vid='136'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='146'/></ing-a><ing-b><var sort='h' vid='144'/></ing-b></ing>
<ing><ing-a><var sort='h' vid='167'/></ing-a><ing-b><var sort='h' vid='172'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='6'/></hi><lo><label vid='3'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='226'/></hi><lo><label vid='222'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='34'/></hi><lo><label vid='33'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='39'/></hi><lo><label vid='38'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='53'/></hi><lo><label vid='48'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='86'/></hi><lo><label vid='76'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='203'/></hi><lo><label vid='116'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='110'/></hi><lo><label vid='109'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='122'/></hi><lo><label vid='112'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='192'/></hi><lo><label vid='132'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='186'/></hi><lo><label vid='165'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='162'/></hi><lo><label vid='146'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='152'/></hi><lo><label vid='142'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='170'/></hi><lo><label vid='169'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='175'/></hi><lo><label vid='174'/></lo></hcons>
</rmrs>



</rmrs-list>