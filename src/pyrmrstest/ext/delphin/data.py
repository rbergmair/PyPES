# -*- coding: utf-8 -*-



TEXT_EASY = [
  u"The dog barks.",
  u"I saw a man with a telescope.",
  u"The cat chased the dog."
];

TEXT_HARD = [
  u"As leaders gather in Argentina ahead of this "+
    u"weekends regional talks, Hugo Chávez, Venezuela's "+
    u"populist president is using an energy windfall to win "+
    u"friends and promote his vision of 21st-century socialism.",
];

TEXT = TEXT_EASY + TEXT_HARD;



TOKENISED_EASY = [
  u"""<smaf>
    <lattice init="v0" final="v3">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">barks.</edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <lattice init="v0" final="v7">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t6" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t7" source="v6" target="v7" cfrom="19" cto="29">telescope.</edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <lattice init="v0" final="v5">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="19" cto="23">dog.</edge>
    </lattice>
  </smaf>"""
];
  
TOKENISED_HARD = [
  u"""<smaf>
    <lattice init="v0" final="v33">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="2">As</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="3" cto="10">leaders</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="11" cto="17">gather</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="18" cto="20">in</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="21" cto="30">Argentina</edge>
      <edge type="token" id="t6" source="v5" target="v6" cfrom="31" cto="36">ahead</edge>
      <edge type="token" id="t7" source="v6" target="v7" cfrom="37" cto="39">of</edge>
      <edge type="token" id="t8" source="v7" target="v8" cfrom="40" cto="44">this</edge>
      <edge type="token" id="t9" source="v8" target="v9" cfrom="45" cto="53">weekends</edge>
      <edge type="token" id="t10" source="v9" target="v10" cfrom="54" cto="62">regional</edge>
      <edge type="token" id="t11" source="v10" target="v11" cfrom="63" cto="69">talks,</edge>
      <edge type="token" id="t12" source="v11" target="v12" cfrom="70" cto="74">Hugo</edge>
      <edge type="token" id="t13" source="v12" target="v13" cfrom="75" cto="82">Chávez,</edge>
      <edge type="token" id="t14" source="v13" target="v14" cfrom="83" cto="92">Venezuela</edge>
      <edge type="token" id="t15" source="v14" target="v15" cfrom="92" cto="95">'s</edge>
      <edge type="token" id="t16" source="v15" target="v16" cfrom="95" cto="103">populist</edge>
      <edge type="token" id="t17" source="v16" target="v17" cfrom="104" cto="113">president</edge>
      <edge type="token" id="t18" source="v17" target="v18" cfrom="114" cto="116">is</edge>
      <edge type="token" id="t19" source="v18" target="v19" cfrom="117" cto="122">using</edge>
      <edge type="token" id="t20" source="v19" target="v20" cfrom="123" cto="125">an</edge>
      <edge type="token" id="t21" source="v20" target="v21" cfrom="126" cto="132">energy</edge>
      <edge type="token" id="t22" source="v21" target="v22" cfrom="133" cto="141">windfall</edge>
      <edge type="token" id="t23" source="v22" target="v23" cfrom="142" cto="144">to</edge>
      <edge type="token" id="t24" source="v23" target="v24" cfrom="145" cto="148">win</edge>
      <edge type="token" id="t25" source="v24" target="v25" cfrom="149" cto="156">friends</edge>
      <edge type="token" id="t26" source="v25" target="v26" cfrom="157" cto="160">and</edge>
      <edge type="token" id="t27" source="v26" target="v27" cfrom="161" cto="168">promote</edge>
      <edge type="token" id="t28" source="v27" target="v28" cfrom="169" cto="172">his</edge>
      <edge type="token" id="t29" source="v28" target="v29" cfrom="173" cto="179">vision</edge>
      <edge type="token" id="t30" source="v29" target="v30" cfrom="180" cto="182">of</edge>
      <edge type="token" id="t31" source="v30" target="v31" cfrom="183" cto="188">21st-</edge>
      <edge type="token" id="t32" source="v31" target="v32" cfrom="188" cto="195">century</edge>
      <edge type="token" id="t33" source="v32" target="v33" cfrom="196" cto="206">socialism.</edge>
    </lattice>
  </smaf>""",
];

TOKENISED = TOKENISED_EASY + TOKENISED_HARD;



PARSED_EASY = [
  u"""<smaf>
    <lattice init="v0" final="v3">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">barks.</edge>
      <edge type="rmrs" id="r0" source="v0" target="v3">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='14'> <gpred>unknown_rel</gpred> <label vid='3'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='0' cto='3'> <realpred lemma='the' pos='q'/> <label vid='5'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='4' cto='14'> <gpred>compound_rel</gpred> <label vid='8'/> <var sort='e' vid='10'/> </ep>
          <ep cfrom='4' cto='14'> <gpred>udef_q_rel</gpred> <label vid='11'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='4' cto='7'> <realpred lemma='dog' pos='n' sense='1'/> <label vid='14'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='8' cto='14'> <realpred lemma='bark' pos='n' sense='1'/> <label vid='10001'/> <var sort='x' vid='4'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='8'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='13'/> </hi>   <lo> <label vid='14'/> </lo>   </hcons>
          <rarg> <rargname>ARG</rargname> <label vid='3'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='11'/> <var sort='h' vid='13'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='11'/> <var sort='h' vid='12'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='8'/> </ing-a>   <ing-b> <var sort='h' vid='10001'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r1" source="v0" target="v3">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='3'> <realpred lemma='the' pos='q'/> <label vid='3'/> <var sort='x' vid='6'/> </ep>
          <ep cfrom='4' cto='7'> <realpred lemma='dog' pos='n' sense='1'/> <label vid='7'/> <var sort='x' vid='6'/> </ep>
          <ep cfrom='8' cto='14'> <realpred lemma='bark' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='3'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='3'/> <var sort='h' vid='4'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='6'/> </rarg>
        </rmrs>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <lattice init="v0" final="v7">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t6" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t7" source="v6" target="v7" cfrom="19" cto="29">telescope.</edge>
      <edge type="rmrs" id="r0" source="v0" target="v7">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='3'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='see' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='10'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n' sense='1'/> <label vid='13'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='10001'/> <var sort='e' vid='14'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='16'/> <var sort='x' vid='15'/> </ep>
          <ep cfrom='19' cto='29'> <realpred lemma='telescope' pos='n' sense='1'/> <label vid='19'/> <var sort='x' vid='15'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='12'/> </hi>   <lo> <label vid='13'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='19'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='10'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='10'/> <var sort='h' vid='11'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='10001'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10001'/> <var sort='x' vid='15'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='16'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='16'/> <var sort='h' vid='17'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='13'/> </ing-a>   <ing-b> <var sort='h' vid='10001'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r1" source="v0" target="v7">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='3'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='saw' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='10'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n' sense='1'/> <label vid='13'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='10001'/> <var sort='e' vid='14'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='16'/> <var sort='x' vid='15'/> </ep>
          <ep cfrom='19' cto='29'> <realpred lemma='telescope' pos='n' sense='1'/> <label vid='19'/> <var sort='x' vid='15'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='12'/> </hi>   <lo> <label vid='13'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='19'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='10'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='10'/> <var sort='h' vid='11'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='10001'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10001'/> <var sort='x' vid='15'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='16'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='16'/> <var sort='h' vid='17'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='13'/> </ing-a>   <ing-b> <var sort='h' vid='10001'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r2" source="v0" target="v7">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='3'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='saw' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='10'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n' sense='1'/> <label vid='13'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='10001'/> <var sort='e' vid='15'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='16'/> <var sort='x' vid='14'/> </ep>
          <ep cfrom='19' cto='29'> <realpred lemma='telescope' pos='n' sense='1'/> <label vid='19'/> <var sort='x' vid='14'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='12'/> </hi>   <lo> <label vid='13'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='19'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='10'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='10'/> <var sort='h' vid='11'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='10001'/> <var sort='e' vid='2'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10001'/> <var sort='x' vid='14'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='16'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='16'/> <var sort='h' vid='17'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='8'/> </ing-a>   <ing-b> <var sort='h' vid='10001'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r3" source="v0" target="v7">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='3'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='see' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='10'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n' sense='1'/> <label vid='13'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='10001'/> <var sort='e' vid='15'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='16'/> <var sort='x' vid='14'/> </ep>
          <ep cfrom='19' cto='29'> <realpred lemma='telescope' pos='n' sense='1'/> <label vid='19'/> <var sort='x' vid='14'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='12'/> </hi>   <lo> <label vid='13'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='19'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='10'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='10'/> <var sort='h' vid='11'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='10001'/> <var sort='e' vid='2'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10001'/> <var sort='x' vid='14'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='16'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='16'/> <var sort='h' vid='17'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='8'/> </ing-a>   <ing-b> <var sort='h' vid='10001'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r4" source="v0" target="v7">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='3'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='see' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='11'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n' sense='1'/> <label vid='14'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='15'/> <var sort='e' vid='17'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='18'/> <var sort='x' vid='16'/> </ep>
          <ep cfrom='19' cto='29'> <realpred lemma='telescope' pos='n' sense='1'/> <label vid='21'/> <var sort='x' vid='16'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='10'/> </hi>   <lo> <label vid='15'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='13'/> </hi>   <lo> <label vid='14'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='20'/> </hi>   <lo> <label vid='21'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>ARG3</rargname> <label vid='8'/> <var sort='h' vid='10'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='11'/> <var sort='h' vid='13'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='11'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='15'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='15'/> <var sort='x' vid='16'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='18'/> <var sort='h' vid='20'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='18'/> <var sort='h' vid='19'/> </rarg>
        </rmrs>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <lattice init="v0" final="v5">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="19" cto="23">dog.</edge>
      <edge type="rmrs" id="r0" source="v0" target="v5">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='3'> <realpred lemma='the' pos='q'/> <label vid='3'/> <var sort='x' vid='6'/> </ep>
          <ep cfrom='4' cto='7'> <realpred lemma='cat' pos='n' sense='1'/> <label vid='7'/> <var sort='x' vid='6'/> </ep>
          <ep cfrom='8' cto='14'> <realpred lemma='chase' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='15' cto='18'> <realpred lemma='the' pos='q'/> <label vid='10'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='19' cto='23'> <realpred lemma='dog' pos='n' sense='1'/> <label vid='13'/> <var sort='x' vid='9'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='12'/> </hi>   <lo> <label vid='13'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='3'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='3'/> <var sort='h' vid='4'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='6'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='10'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='10'/> <var sort='h' vid='11'/> </rarg>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r1" source="v0" target="v5">
        <rmrs cfrom='-1' cto='-1'>
          <label vid='1'/>
          <ep cfrom='0' cto='23'> <gpred>unknown_rel</gpred> <label vid='3'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='0' cto='23'> <gpred>appos_rel</gpred> <label vid='5'/> <var sort='e' vid='6'/> </ep>
          <ep cfrom='0' cto='3'> <realpred lemma='the' pos='q'/> <label vid='8'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='4' cto='7'> <realpred lemma='cat' pos='n' sense='1'/> <label vid='10001'/> <var sort='x' vid='4'/> </ep>
          <ep cfrom='8' cto='14'> <realpred lemma='chase' pos='v' sense='1'/> <label vid='10002'/> <var sort='e' vid='11'/> </ep>
          <ep cfrom='8' cto='14'> <gpred>parg_d_rel</gpred> <label vid='10003'/> <var sort='e' vid='13'/> </ep>
          <ep cfrom='15' cto='18'> <realpred lemma='the' pos='q'/> <label vid='14'/> <var sort='x' vid='7'/> </ep>
          <ep cfrom='19' cto='23'> <realpred lemma='dog' pos='n' sense='1'/> <label vid='17'/> <var sort='x' vid='7'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='10'/> </hi>   <lo> <label vid='5'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='15'/> </hi>   <lo> <label vid='17'/> </lo>   </hcons>
          <rarg> <rargname>ARG</rargname> <label vid='3'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='5'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='5'/> <var sort='x' vid='7'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='8'/> <var sort='h' vid='10'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='8'/> <var sort='h' vid='9'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='10002'/> <var sort='u' vid='12'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10002'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='10003'/> <var sort='e' vid='11'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10003'/> <var sort='x' vid='4'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='14'/> <var sort='h' vid='15'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='14'/> <var sort='h' vid='16'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='5'/> </ing-a>   <ing-b> <var sort='h' vid='10002'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='5'/> </ing-a>   <ing-b> <var sort='h' vid='10001'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='5'/> </ing-a>   <ing-b> <var sort='h' vid='10003'/> </ing-b>   </ing>
        </rmrs>
      </edge>
    </lattice>
  </smaf>"""
];

PARSED_HARD = [
];

PARSED = PARSED_EASY + PARSED_HARD;