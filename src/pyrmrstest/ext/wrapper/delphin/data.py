# -*- coding: utf-8 -*-



TEXT_EASY = [
  u"The dog barks.",
  u"I saw a man with a telescope.",
  u"The cat chased the dog."
];

TEXT_HARD = [
  u"Hugo Chávez chased the dog.",
  u"As leaders gather in Argentina ahead of this "+
    u"weekends regional talks, Hugo Chávez, Venezuela's "+
    u"populist president is using an energy windfall to win "+
    u"friends and promote his vision of 21st-century socialism.",
  u"Was backup command pilot for Gemini 5, command pilot for "+
    u"Gemini 8, backup command pilot for Gemini 11, backup commander for "+
    u"Apollo 8, and commander for Apollo 11: "+
    u"successfully completing the first moonwalk."
];

TEXT = TEXT_EASY + TEXT_HARD;



TOKENISED_EASY = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v3" cfrom="0" cto="14">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">barks.</edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>I saw a man with a telescope.</text>
    <lattice init="v0" final="v7" cfrom="0" cto="29">
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
    <text>The cat chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="23">
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
    <text>Hugo Chávez chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="27">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="4">Hugo</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="5" cto="11">Chávez</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="23" cto="27">dog.</edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>As leaders gather in Argentina ahead of this weekends regional talks, Hugo Chávez, Venezuela's populist president is using an energy windfall to win friends and promote his vision of 21st-century socialism.</text>
    <lattice init="v0" final="v33" cfrom="0" cto="206">
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
  u"""<smaf>
    <text>Was backup command pilot for Gemini 5, command pilot for Gemini 8, backup command pilot for Gemini 11, backup commander for Apollo 8, and commander for Apollo 11: successfully completing the first moonwalk.</text>
    <lattice init="v0" final="v37" cfrom="0" cto="206">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">Was</edge>
      <edge type="token" id="t2" source="v1" target="v3" cfrom="4" cto="10">backup</edge>
      <edge type="token" id="t35" source="v1" target="v2" cfrom="4" cto="10">back</edge>
      <edge type="token" id="t36" source="v2" target="v3" cfrom="4" cto="10">up</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="11" cto="18">command</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="19" cto="24">pilot</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="25" cto="28">for</edge>
      <edge type="token" id="t6" source="v6" target="v7" cfrom="29" cto="35">Gemini</edge>
      <edge type="ersatz" id="t41" source="v7" target="v8" cfrom="36" cto="37">
        <slot name="name">OneDigitErsatz,</slot>
        <slot name="surface">5</slot>
      </edge>
      <edge type="token" id="t8" source="v8" target="v9" cfrom="39" cto="46">command</edge>
      <edge type="token" id="t9" source="v9" target="v10" cfrom="47" cto="52">pilot</edge>
      <edge type="token" id="t10" source="v10" target="v11" cfrom="53" cto="56">for</edge>
      <edge type="token" id="t11" source="v11" target="v12" cfrom="57" cto="63">Gemini</edge>
      <edge type="ersatz" id="t42" source="v12" target="v13" cfrom="64" cto="65">
        <slot name="name">OneDigitErsatz,</slot>
        <slot name="surface">8</slot>
      </edge>
      <edge type="token" id="t13" source="v13" target="v15" cfrom="67" cto="73">backup</edge>
      <edge type="token" id="t37" source="v13" target="v14" cfrom="67" cto="73">back</edge>
      <edge type="token" id="t38" source="v14" target="v15" cfrom="67" cto="73">up</edge>
      <edge type="token" id="t14" source="v15" target="v16" cfrom="74" cto="81">command</edge>
      <edge type="token" id="t15" source="v16" target="v17" cfrom="82" cto="87">pilot</edge>
      <edge type="token" id="t16" source="v17" target="v18" cfrom="88" cto="91">for</edge>
      <edge type="token" id="t17" source="v18" target="v19" cfrom="92" cto="98">Gemini</edge>
      <edge type="ersatz" id="t45" source="v19" target="v20" cfrom="99" cto="101">
        <slot name="name">TwoDigitErsatz,</slot>
        <slot name="surface">11</slot>
      </edge>
      <edge type="token" id="t19" source="v20" target="v22" cfrom="103" cto="109">backup</edge>
      <edge type="token" id="t39" source="v20" target="v21" cfrom="103" cto="109">back</edge>
      <edge type="token" id="t40" source="v21" target="v22" cfrom="103" cto="109">up</edge>
      <edge type="token" id="t20" source="v22" target="v23" cfrom="110" cto="119">commander</edge>
      <edge type="token" id="t21" source="v23" target="v24" cfrom="120" cto="123">for</edge>
      <edge type="token" id="t22" source="v24" target="v25" cfrom="124" cto="130">Apollo</edge>
      <edge type="ersatz" id="t43" source="v25" target="v26" cfrom="131" cto="132">
        <slot name="name">OneDigitErsatz,</slot>
        <slot name="surface">8</slot>
      </edge>
      <edge type="token" id="t24" source="v26" target="v27" cfrom="134" cto="137">and</edge>
      <edge type="token" id="t25" source="v27" target="v28" cfrom="138" cto="147">commander</edge>
      <edge type="token" id="t26" source="v28" target="v29" cfrom="148" cto="151">for</edge>
      <edge type="token" id="t27" source="v29" target="v30" cfrom="152" cto="158">Apollo</edge>
      <edge type="ersatz" id="t44" source="v30" target="v31" cfrom="159" cto="161">
        <slot name="name">TwoDigitErsatz</slot>
        <slot name="surface">11</slot>
      </edge>
      <edge type="token" id="t29" source="v31" target="v32" cfrom="161" cto="162">:</edge>
      <edge type="token" id="t30" source="v32" target="v33" cfrom="163" cto="175">successfully</edge>
      <edge type="token" id="t31" source="v33" target="v34" cfrom="176" cto="186">completing</edge>
      <edge type="token" id="t32" source="v34" target="v35" cfrom="187" cto="190">the</edge>
      <edge type="token" id="t33" source="v35" target="v36" cfrom="191" cto="196">first</edge>
      <edge type="token" id="t34" source="v36" target="v37" cfrom="197" cto="206">moonwalk.</edge>
    </lattice>
  </smaf>"""
];

TOKENISED = TOKENISED_EASY + TOKENISED_HARD;



BASIC_PARSED_EASY = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v3" cfrom="0" cto="14">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">barks.</edge>
      <edge type="rmrs" id="r0" source="v0" target="v3" cfrom="0" cto="14">
        <rmrs cfrom='0' cto='14'>
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
      <edge type="rmrs" id="r1" source="v0" target="v3" cfrom="0" cto="14">
        <rmrs cfrom='0' cto='14'>
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
    <text>I saw a man with a telescope.</text>
    <lattice init="v0" final="v7" cfrom="0" cto="29">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t6" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t7" source="v6" target="v7" cfrom="19" cto="29">telescope.</edge>
      <edge type="rmrs" id="r0" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r1" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r2" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r3" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r4" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
    <text>The cat chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="23">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="19" cto="23">dog.</edge>
      <edge type="rmrs" id="r0" source="v0" target="v5" cfrom="0" cto="23">
        <rmrs cfrom='0' cto='23'>
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
      <edge type="rmrs" id="r1" source="v0" target="v5" cfrom="0" cto="23">
        <rmrs cfrom='0' cto='23'>
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

BASIC_PARSED_HARD = [
];

BASIC_PARSED = BASIC_PARSED_EASY + BASIC_PARSED_HARD;



TAGGED_EASY = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v3" cfrom="0" cto="14">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">barks.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t1">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999729</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="4" cto="7" deps="t2">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00027066</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.750875</slot>
      </edge>
      <edge type="pos" id="p4" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.249125</slot>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>I saw a man with a telescope.</text>
    <lattice init="v0" final="v7" cfrom="0" cto="29">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t6" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t7" source="v6" target="v7" cfrom="19" cto="29">telescope.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="1" deps="t1">
        <slot name="tag">MC</slot>
        <slot name="weight">0.000427712</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="1" deps="t1">
        <slot name="tag">PPIS1</slot>
        <slot name="weight">0.936841</slot>
      </edge>
      <edge type="pos" id="p2" source="v0" target="v1" cfrom="0" cto="1" deps="t1">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">0.0627313</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="2" cto="5" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.000105329</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="2" cto="5" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.999895</slot>
      </edge>
      <edge type="pos" id="p5" source="v2" target="v3" cfrom="6" cto="7" deps="t3">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.998334</slot>
      </edge>
      <edge type="pos" id="p6" source="v2" target="v3" cfrom="6" cto="7" deps="t3">
        <slot name="tag">II</slot>
        <slot name="weight">0.00164698</slot>
      </edge>
      <edge type="pos" id="p7" source="v2" target="v3" cfrom="6" cto="7" deps="t3">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">1.89096e-05</slot>
      </edge>
      <edge type="pos" id="p8" source="v3" target="v4" cfrom="8" cto="11" deps="t4">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999525</slot>
      </edge>
      <edge type="pos" id="p9" source="v3" target="v4" cfrom="8" cto="11" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000475218</slot>
      </edge>
      <edge type="pos" id="p10" source="v4" target="v5" cfrom="12" cto="16" deps="t5">
        <slot name="tag">IW</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v5" target="v6" cfrom="17" cto="18" deps="t6">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999927</slot>
      </edge>
      <edge type="pos" id="p12" source="v5" target="v6" cfrom="17" cto="18" deps="t6">
        <slot name="tag">II</slot>
        <slot name="weight">1.0498e-05</slot>
      </edge>
      <edge type="pos" id="p13" source="v5" target="v6" cfrom="17" cto="18" deps="t6">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">6.2175e-05</slot>
      </edge>
      <edge type="pos" id="p14" source="v6" target="v7" cfrom="19" cto="29" deps="t7">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999617</slot>
      </edge>
      <edge type="pos" id="p15" source="v6" target="v7" cfrom="19" cto="29" deps="t7">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000383388</slot>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>The cat chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="23">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="19" cto="23">dog.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t1">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p2" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.90372</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.0962799</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="15" cto="18" deps="t4">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p5" source="v4" target="v5" cfrom="19" cto="23" deps="t5">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999833</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="19" cto="23" deps="t5">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000166966</slot>
      </edge>
    </lattice>
  </smaf>"""
];

TAGGED_HARD = [
  u"""<smaf>
    <text>Hugo_Chávez chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="27">
      <edge type="token" id="t1" source="v0" target="v2" cfrom="0" cto="11">Hugo_Chávez</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="23" cto="27">dog.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="4" deps="t1">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p9" source="v2" target="v3" cfrom="12" cto="18" deps="t3">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.886745</slot>
      </edge>
      <edge type="pos" id="p10" source="v2" target="v3" cfrom="12" cto="18" deps="t3">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.113255</slot>
      </edge>
      <edge type="pos" id="p11" source="v3" target="v4" cfrom="19" cto="22" deps="t4">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v4" target="v5" cfrom="23" cto="27" deps="t5">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997692</slot>
      </edge>
      <edge type="pos" id="p13" source="v4" target="v5" cfrom="23" cto="27" deps="t5">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00230797</slot>
      </edge>
    </lattice>
  </smaf>""",  
  u"""<smaf>
    <text>Hugo Chávez chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="27">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="4">Hugo</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="5" cto="11">Chávez</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="23" cto="27">dog.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="4" deps="t1">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.00357779</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.792963</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.151421</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">RR</slot>
        <slot name="weight">0.0461225</slot>
      </edge>
      <edge type="pos" id="p5" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000336622</slot>
      </edge>
      <edge type="pos" id="p6" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00531652</slot>
      </edge>
      <edge type="pos" id="p7" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.000113307</slot>
      </edge>
      <edge type="pos" id="p8" source="v1" target="v2" cfrom="5" cto="11" deps="t2">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.000149814</slot>
      </edge>
      <edge type="pos" id="p9" source="v2" target="v3" cfrom="12" cto="18" deps="t3">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.886745</slot>
      </edge>
      <edge type="pos" id="p10" source="v2" target="v3" cfrom="12" cto="18" deps="t3">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.113255</slot>
      </edge>
      <edge type="pos" id="p11" source="v3" target="v4" cfrom="19" cto="22" deps="t4">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v4" target="v5" cfrom="23" cto="27" deps="t5">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997692</slot>
      </edge>
      <edge type="pos" id="p13" source="v4" target="v5" cfrom="23" cto="27" deps="t5">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00230797</slot>
      </edge>
    </lattice>
  </smaf>""",  
  u"""<smaf>
    <text>As leaders gather in Argentina ahead of this weekends regional talks, Hugo Chávez, Venezuela's populist president is using an energy windfall to win friends and promote his vision of 21st-century socialism.</text>
    <lattice init="v0" final="v33" cfrom="0" cto="206">
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
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="2" deps="t1">
        <slot name="tag">CSA</slot>
        <slot name="weight">0.993802</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="2" deps="t1">
        <slot name="tag">NP1</slot>
        <slot name="weight">0.00619808</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="3" cto="10" deps="t2">
        <slot name="tag">NN2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="11" cto="17" deps="t3">
        <slot name="tag">VV0</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="18" cto="20" deps="t4">
        <slot name="tag">II</slot>
        <slot name="weight">0.983505</slot>
      </edge>
      <edge type="pos" id="p5" source="v3" target="v4" cfrom="18" cto="20" deps="t4">
        <slot name="tag">RP</slot>
        <slot name="weight">0.0164951</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="21" cto="30" deps="t5">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p7" source="v5" target="v6" cfrom="31" cto="36" deps="t6">
        <slot name="tag">II</slot>
        <slot name="weight">0.000308034</slot>
      </edge>
      <edge type="pos" id="p8" source="v5" target="v6" cfrom="31" cto="36" deps="t6">
        <slot name="tag">RL</slot>
        <slot name="weight">0.0256448</slot>
      </edge>
      <edge type="pos" id="p9" source="v5" target="v6" cfrom="31" cto="36" deps="t6">
        <slot name="tag">RR</slot>
        <slot name="weight">0.974047</slot>
      </edge>
      <edge type="pos" id="p10" source="v6" target="v7" cfrom="37" cto="39" deps="t7">
        <slot name="tag">IO</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v7" target="v8" cfrom="40" cto="44" deps="t8">
        <slot name="tag">DD1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v8" target="v9" cfrom="45" cto="53" deps="t9">
        <slot name="tag">NNT2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p13" source="v9" target="v10" cfrom="54" cto="62" deps="t10">
        <slot name="tag">JJ</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p14" source="v10" target="v11" cfrom="63" cto="69" deps="t11">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.999157</slot>
      </edge>
      <edge type="pos" id="p15" source="v10" target="v11" cfrom="63" cto="69" deps="t11">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.000843389</slot>
      </edge>
      <edge type="pos" id="p16" source="v11" target="v12" cfrom="70" cto="74" deps="t12">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p17" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.0337125</slot>
      </edge>
      <edge type="pos" id="p18" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.783491</slot>
      </edge>
      <edge type="pos" id="p19" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.110038</slot>
      </edge>
      <edge type="pos" id="p20" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.0173089</slot>
      </edge>
      <edge type="pos" id="p21" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00391381</slot>
      </edge>
      <edge type="pos" id="p22" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.0491277</slot>
      </edge>
      <edge type="pos" id="p23" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.000974584</slot>
      </edge>
      <edge type="pos" id="p24" source="v12" target="v13" cfrom="75" cto="82" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00143255</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="83" cto="92" deps="t14">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p26" source="v14" target="v15" cfrom="92" cto="95" deps="t15">
        <slot name="tag">$</slot>
        <slot name="weight">0.982721</slot>
      </edge>
      <edge type="pos" id="p27" source="v14" target="v15" cfrom="92" cto="95" deps="t15">
        <slot name="tag">PPIO2</slot>
        <slot name="weight">2.43739e-308</slot>
      </edge>
      <edge type="pos" id="p28" source="v14" target="v15" cfrom="92" cto="95" deps="t15">
        <slot name="tag">VBZ</slot>
        <slot name="weight">0.016791</slot>
      </edge>
      <edge type="pos" id="p29" source="v14" target="v15" cfrom="92" cto="95" deps="t15">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.75874e-06</slot>
      </edge>
      <edge type="pos" id="p30" source="v14" target="v15" cfrom="92" cto="95" deps="t15">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000484776</slot>
      </edge>
      <edge type="pos" id="p31" source="v15" target="v16" cfrom="95" cto="103" deps="t16">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.876188</slot>
      </edge>
      <edge type="pos" id="p32" source="v15" target="v16" cfrom="95" cto="103" deps="t16">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.123812</slot>
      </edge>
      <edge type="pos" id="p33" source="v16" target="v17" cfrom="104" cto="113" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997338</slot>
      </edge>
      <edge type="pos" id="p34" source="v16" target="v17" cfrom="104" cto="113" deps="t17">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00266191</slot>
      </edge>
      <edge type="pos" id="p35" source="v17" target="v18" cfrom="114" cto="116" deps="t18">
        <slot name="tag">VBZ</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="117" cto="122" deps="t19">
        <slot name="tag">VVG</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p37" source="v19" target="v20" cfrom="123" cto="125" deps="t20">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999911</slot>
      </edge>
      <edge type="pos" id="p38" source="v19" target="v20" cfrom="123" cto="125" deps="t20">
        <slot name="tag">NP1</slot>
        <slot name="weight">8.92656e-05</slot>
      </edge>
      <edge type="pos" id="p39" source="v20" target="v21" cfrom="126" cto="132" deps="t21">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p40" source="v21" target="v22" cfrom="133" cto="141" deps="t22">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p41" source="v22" target="v23" cfrom="142" cto="144" deps="t23">
        <slot name="tag">II</slot>
        <slot name="weight">0.00434461</slot>
      </edge>
      <edge type="pos" id="p42" source="v22" target="v23" cfrom="142" cto="144" deps="t23">
        <slot name="tag">TO</slot>
        <slot name="weight">0.995655</slot>
      </edge>
      <edge type="pos" id="p43" source="v23" target="v24" cfrom="145" cto="148" deps="t24">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.00409246</slot>
      </edge>
      <edge type="pos" id="p44" source="v23" target="v24" cfrom="145" cto="148" deps="t24">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.995908</slot>
      </edge>
      <edge type="pos" id="p45" source="v24" target="v25" cfrom="149" cto="156" deps="t25">
        <slot name="tag">NN2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p46" source="v25" target="v26" cfrom="157" cto="160" deps="t26">
        <slot name="tag">CC</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p47" source="v26" target="v27" cfrom="161" cto="168" deps="t27">
        <slot name="tag">VV0</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p48" source="v27" target="v28" cfrom="169" cto="172" deps="t28">
        <slot name="tag">APP$</slot>
        <slot name="weight">0.998336</slot>
      </edge>
      <edge type="pos" id="p49" source="v27" target="v28" cfrom="169" cto="172" deps="t28">
        <slot name="tag">PP$</slot>
        <slot name="weight">0.00166391</slot>
      </edge>
      <edge type="pos" id="p50" source="v28" target="v29" cfrom="173" cto="179" deps="t29">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999981</slot>
      </edge>
      <edge type="pos" id="p51" source="v28" target="v29" cfrom="173" cto="179" deps="t29">
        <slot name="tag">VV0</slot>
        <slot name="weight">1.89791e-05</slot>
      </edge>
      <edge type="pos" id="p52" source="v29" target="v30" cfrom="180" cto="182" deps="t30">
        <slot name="tag">IO</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p53" source="v30" target="v31" cfrom="183" cto="188" deps="t31">
        <slot name="tag">JB</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p54" source="v31" target="v32" cfrom="188" cto="195" deps="t32">
        <slot name="tag">JB</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p55" source="v32" target="v33" cfrom="196" cto="206" deps="t33">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
    </lattice>
  </smaf>"""
];

TAGGED = TAGGED_EASY + TAGGED_HARD;



TAG_PARSED_EASY = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v3" cfrom="0" cto="14">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">barks.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t1">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999729</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="4" cto="7" deps="t2">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00027066</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.750875</slot>
      </edge>
      <edge type="pos" id="p4" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.249125</slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v3" cfrom="0" cto="14">
        <rmrs cfrom='0' cto='14'>
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
      <edge type="rmrs" id="r1" source="v0" target="v3" cfrom="0" cto="14">
        <rmrs cfrom='0' cto='14'>
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
    <text>I saw a man with a telescope.</text>
    <lattice init="v0" final="v7" cfrom="0" cto="29">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t6" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t7" source="v6" target="v7" cfrom="19" cto="29">telescope.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="1" deps="t1">
        <slot name="tag">MC</slot>
        <slot name="weight">0.000427712</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="1" deps="t1">
        <slot name="tag">PPIS1</slot>
        <slot name="weight">0.936841</slot>
      </edge>
      <edge type="pos" id="p2" source="v0" target="v1" cfrom="0" cto="1" deps="t1">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">0.0627313</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="2" cto="5" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.000105329</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="2" cto="5" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.999895</slot>
      </edge>
      <edge type="pos" id="p5" source="v2" target="v3" cfrom="6" cto="7" deps="t3">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.998334</slot>
      </edge>
      <edge type="pos" id="p6" source="v2" target="v3" cfrom="6" cto="7" deps="t3">
        <slot name="tag">II</slot>
        <slot name="weight">0.00164698</slot>
      </edge>
      <edge type="pos" id="p7" source="v2" target="v3" cfrom="6" cto="7" deps="t3">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">1.89096e-05</slot>
      </edge>
      <edge type="pos" id="p8" source="v3" target="v4" cfrom="8" cto="11" deps="t4">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999525</slot>
      </edge>
      <edge type="pos" id="p9" source="v3" target="v4" cfrom="8" cto="11" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000475218</slot>
      </edge>
      <edge type="pos" id="p10" source="v4" target="v5" cfrom="12" cto="16" deps="t5">
        <slot name="tag">IW</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v5" target="v6" cfrom="17" cto="18" deps="t6">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999927</slot>
      </edge>
      <edge type="pos" id="p12" source="v5" target="v6" cfrom="17" cto="18" deps="t6">
        <slot name="tag">II</slot>
        <slot name="weight">1.0498e-05</slot>
      </edge>
      <edge type="pos" id="p13" source="v5" target="v6" cfrom="17" cto="18" deps="t6">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">6.2175e-05</slot>
      </edge>
      <edge type="pos" id="p14" source="v6" target="v7" cfrom="19" cto="29" deps="t7">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999617</slot>
      </edge>
      <edge type="pos" id="p15" source="v6" target="v7" cfrom="19" cto="29" deps="t7">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000383388</slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r1" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r2" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r3" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
      <edge type="rmrs" id="r4" source="v0" target="v7" cfrom="0" cto="29">
        <rmrs cfrom='0' cto='29'>
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
    <text>The cat chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="23">
      <edge type="token" id="t1" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t2" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="19" cto="23">dog.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t1">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t2">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p2" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.90372</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="14" deps="t3">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.0962799</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="15" cto="18" deps="t4">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p5" source="v4" target="v5" cfrom="19" cto="23" deps="t5">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999833</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="19" cto="23" deps="t5">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000166966</slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v5" cfrom="0" cto="23">
        <rmrs cfrom='0' cto='23'>
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
      <edge type="rmrs" id="r1" source="v0" target="v5" cfrom="0" cto="23">
        <rmrs cfrom='0' cto='23'>
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

TAG_PARSED_HARD = [
  u"""<smaf>
    <text>Hugo_Chávez chased the dog.</text>
    <lattice init="v0" final="v5" cfrom="0" cto="27">
      <edge type="token" id="t1" source="v0" target="v2" cfrom="0" cto="11">Hugo_Chávez</edge>
      <edge type="token" id="t3" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t4" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t5" source="v4" target="v5" cfrom="23" cto="27">dog.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="4" deps="t1">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p9" source="v2" target="v3" cfrom="12" cto="18" deps="t3">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.886745</slot>
      </edge>
      <edge type="pos" id="p10" source="v2" target="v3" cfrom="12" cto="18" deps="t3">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.113255</slot>
      </edge>
      <edge type="pos" id="p11" source="v3" target="v4" cfrom="19" cto="22" deps="t4">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v4" target="v5" cfrom="23" cto="27" deps="t5">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997692</slot>
      </edge>
      <edge type="pos" id="p13" source="v4" target="v5" cfrom="23" cto="27" deps="t5">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00230797</slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v5" cfrom="0" cto="27">
        <rmrs cfrom='0' cto='27'>
          <label vid='1'/>
          <ep cfrom='0' cto='11'> <gpred>proper_q_rel</gpred> <label vid='3'/> <var sort='x' vid='5'/> </ep>
          <ep cfrom='0' cto='11'> <gpred>named_rel</gpred> <label vid='7'/> <var sort='x' vid='5'/> </ep>
          <ep cfrom='12' cto='18'> <realpred lemma='chase' pos='v' sense='1'/> <label vid='8'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='the' pos='q'/> <label vid='10'/> <var sort='x' vid='9'/> </ep>
          <ep cfrom='23' cto='27'> <realpred lemma='dog' pos='n' sense='1'/> <label vid='13'/> <var sort='x' vid='9'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='6'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='12'/> </hi>   <lo> <label vid='13'/> </lo>   </hcons>
          <rarg> <rargname>RSTR</rargname> <label vid='3'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='3'/> <var sort='h' vid='4'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='7'/> <constant>*TOP*</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='8'/> <var sort='x' vid='5'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='8'/> <var sort='x' vid='9'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='10'/> <var sort='h' vid='12'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='10'/> <var sort='h' vid='11'/> </rarg>
        </rmrs>
      </edge>
    </lattice>
  </smaf>"""
];

TAG_PARSED = TAG_PARSED_EASY + TAG_PARSED_HARD;



RASP_PARSED = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v4" cfrom="0" cto="14">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="8" cto="13">barks</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="13" cto="14">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t0">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999729</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="4" cto="7" deps="t1">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00027066</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="13" deps="t2">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.750875</slot>
      </edge>
      <edge type="pos" id="p4" source="v2" target="v3" cfrom="8" cto="13" deps="t2">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.249125</slot>
      </edge>
      <edge type="pos" id="p5" source="v3" target="v4" cfrom="13" cto="14" deps="t3">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v2" target="v3" cfrom="8" cto="13" deps="p3">bark+s</edge>
      <edge type="morph" id="m2" source="v2" target="v3" cfrom="8" cto="13" deps="p4">bark+s</edge>
      <edge type="syntree" id="s0" source="v0" target="v4" cfrom="0" cto="14">
        <slot name="weight">-4.440</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp|
          (|NP/det_n1| |&lt;w s='0' e='3'&gt;The_AT&lt;/w&gt;|
           (|N1/n| |&lt;w s='4' e='7'&gt;dog_NN1&lt;/w&gt;|))
          (|V1/v| |&lt;w s='8' e='13'&gt;bark+s_VVZ&lt;/w&gt;|))
         (|End-punct3/-| |&lt;w s='13' e='14'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>I saw a man with a telescope.</text>
    <lattice init="v0" final="v8" cfrom="0" cto="29">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t6" source="v6" target="v7" cfrom="19" cto="28">telescope</edge>
      <edge type="token" id="t7" source="v7" target="v8" cfrom="28" cto="29">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="1" deps="t0">
        <slot name="tag">MC</slot>
        <slot name="weight">0.000427712</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="1" deps="t0">
        <slot name="tag">PPIS1</slot>
        <slot name="weight">0.936841</slot>
      </edge>
      <edge type="pos" id="p2" source="v0" target="v1" cfrom="0" cto="1" deps="t0">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">0.0627313</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="2" cto="5" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.000105329</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="2" cto="5" deps="t1">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.999895</slot>
      </edge>
      <edge type="pos" id="p5" source="v2" target="v3" cfrom="6" cto="7" deps="t2">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.998334</slot>
      </edge>
      <edge type="pos" id="p6" source="v2" target="v3" cfrom="6" cto="7" deps="t2">
        <slot name="tag">II</slot>
        <slot name="weight">0.00164698</slot>
      </edge>
      <edge type="pos" id="p7" source="v2" target="v3" cfrom="6" cto="7" deps="t2">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">1.89096e-05</slot>
      </edge>
      <edge type="pos" id="p8" source="v3" target="v4" cfrom="8" cto="11" deps="t3">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999525</slot>
      </edge>
      <edge type="pos" id="p9" source="v3" target="v4" cfrom="8" cto="11" deps="t3">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000475218</slot>
      </edge>
      <edge type="pos" id="p10" source="v4" target="v5" cfrom="12" cto="16" deps="t4">
        <slot name="tag">IW</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v5" target="v6" cfrom="17" cto="18" deps="t5">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999927</slot>
      </edge>
      <edge type="pos" id="p12" source="v5" target="v6" cfrom="17" cto="18" deps="t5">
        <slot name="tag">II</slot>
        <slot name="weight">1.0498e-05</slot>
      </edge>
      <edge type="pos" id="p13" source="v5" target="v6" cfrom="17" cto="18" deps="t5">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">6.2175e-05</slot>
      </edge>
      <edge type="pos" id="p14" source="v6" target="v7" cfrom="19" cto="28" deps="t6">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999617</slot>
      </edge>
      <edge type="pos" id="p15" source="v6" target="v7" cfrom="19" cto="28" deps="t6">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000383388</slot>
      </edge>
      <edge type="pos" id="p16" source="v7" target="v8" cfrom="28" cto="29" deps="t7">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v1" target="v2" cfrom="2" cto="5" deps="p4">see+ed</edge>
      <edge type="syntree" id="s0" source="v0" target="v8" cfrom="0" cto="29">
        <slot name="weight">-6.821</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp| |&lt;w s='0' e='1'&gt;I_PPIS1&lt;/w&gt;|
          (|V1/v_np_pp| |&lt;w s='2' e='5'&gt;see+ed_VVD&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='6' e='7'&gt;a_AT1&lt;/w&gt;|
            (|N1/n| |&lt;w s='8' e='11'&gt;man_NN1&lt;/w&gt;|))
           (|PP/p1|
            (|P1/p_np| |&lt;w s='12' e='16'&gt;with_IW&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='17' e='18'&gt;a_AT1&lt;/w&gt;|
              (|N1/n| |&lt;w s='19' e='28'&gt;telescope_NN1&lt;/w&gt;|))))))
         (|End-punct3/-| |&lt;w s='28' e='29'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s1" source="v0" target="v8" cfrom="0" cto="29">
        <slot name="weight">-7.233</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp| |&lt;w s='0' e='1'&gt;I_PPIS1&lt;/w&gt;|
          (|V1/v_np| |&lt;w s='2' e='5'&gt;see+ed_VVD&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='6' e='7'&gt;a_AT1&lt;/w&gt;|
            (|N1/n1_pp3| (|N1/n| |&lt;w s='8' e='11'&gt;man_NN1&lt;/w&gt;|)
             (|PP/p1|
              (|P1/p_np| |&lt;w s='12' e='16'&gt;with_IW&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='17' e='18'&gt;a_AT1&lt;/w&gt;|
                (|N1/n| |&lt;w s='19' e='28'&gt;telescope_NN1&lt;/w&gt;|))))))))
         (|End-punct3/-| |&lt;w s='28' e='29'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s2" source="v0" target="v8" cfrom="0" cto="29">
        <slot name="weight">-8.501</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp| |&lt;w s='0' e='1'&gt;I_PPIS1&lt;/w&gt;|
          (|V1/vp_pp|
           (|V1/v_np| |&lt;w s='2' e='5'&gt;see+ed_VVD&lt;/w&gt;|
            (|NP/det_n1| |&lt;w s='6' e='7'&gt;a_AT1&lt;/w&gt;|
             (|N1/n| |&lt;w s='8' e='11'&gt;man_NN1&lt;/w&gt;|)))
           (|PP/p1|
            (|P1/p_np| |&lt;w s='12' e='16'&gt;with_IW&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='17' e='18'&gt;a_AT1&lt;/w&gt;|
              (|N1/n| |&lt;w s='19' e='28'&gt;telescope_NN1&lt;/w&gt;|))))))
         (|End-punct3/-| |&lt;w s='28' e='29'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>Hugo Chávez chased the dog.</text>
    <lattice init="v0" final="v6" cfrom="0" cto="27">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="4">Hugo</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="5" cto="11">Chávez</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="23" cto="26">dog</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="26" cto="27">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="4" deps="t0">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.00357779</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.792963</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.151421</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">RR</slot>
        <slot name="weight">0.0461225</slot>
      </edge>
      <edge type="pos" id="p5" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000336622</slot>
      </edge>
      <edge type="pos" id="p6" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00531652</slot>
      </edge>
      <edge type="pos" id="p7" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.000113307</slot>
      </edge>
      <edge type="pos" id="p8" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.000149814</slot>
      </edge>
      <edge type="pos" id="p9" source="v2" target="v3" cfrom="12" cto="18" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.886745</slot>
      </edge>
      <edge type="pos" id="p10" source="v2" target="v3" cfrom="12" cto="18" deps="t2">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.113255</slot>
      </edge>
      <edge type="pos" id="p11" source="v3" target="v4" cfrom="19" cto="22" deps="t3">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v4" target="v5" cfrom="23" cto="26" deps="t4">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999833</slot>
      </edge>
      <edge type="pos" id="p13" source="v4" target="v5" cfrom="23" cto="26" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000166966</slot>
      </edge>
      <edge type="pos" id="p14" source="v5" target="v6" cfrom="26" cto="27" deps="t5">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v2" target="v3" cfrom="12" cto="18" deps="p9">chase+ed</edge>
      <edge type="morph" id="m2" source="v2" target="v3" cfrom="12" cto="18" deps="p10">chase+ed</edge>
      <edge type="syntree" id="s0" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-7.775</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/n1_vp|
          (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
           (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN1&lt;/w&gt;|))
          (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVD&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
            (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
         (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s1" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-8.669</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/n1_vp|
          (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
           (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN1&lt;/w&gt;|))
          (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVN&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
            (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
         (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s2" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-9.361</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp|
          (|NP/n1-plu|
           (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
            (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN2&lt;/w&gt;|)))
          (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVD&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
            (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
         (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s3" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-9.863</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp| (|NP/n1-name| (|N1/n-name| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|))
          (|V1/adv_vp| (|AP/a1| (|A1/a| |&lt;w s='5' e='11'&gt;Chávez_RR&lt;/w&gt;|))
           (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVD&lt;/w&gt;|
            (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
             (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|)))))
         (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s4" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-10.255</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp|
          (|NP/n1-plu|
           (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
            (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN2&lt;/w&gt;|)))
          (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVN&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
            (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
         (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>As leaders gather in Argentina ahead of this weekends regional talks, Hugo Chávez, Venezuela's populist president is using an energy windfall to win friends and promote his vision of 21st-century socialism.</text>
    <lattice init="v0" final="v35" cfrom="0" cto="206">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="2">As</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="3" cto="10">leaders</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="11" cto="17">gather</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="18" cto="20">in</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="21" cto="30">Argentina</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="31" cto="36">ahead</edge>
      <edge type="token" id="t6" source="v6" target="v7" cfrom="37" cto="39">of</edge>
      <edge type="token" id="t7" source="v7" target="v8" cfrom="40" cto="44">this</edge>
      <edge type="token" id="t8" source="v8" target="v9" cfrom="45" cto="53">weekends</edge>
      <edge type="token" id="t9" source="v9" target="v10" cfrom="54" cto="62">regional</edge>
      <edge type="token" id="t10" source="v10" target="v11" cfrom="63" cto="68">talks</edge>
      <edge type="token" id="t11" source="v11" target="v12" cfrom="68" cto="69">,</edge>
      <edge type="token" id="t12" source="v12" target="v13" cfrom="70" cto="74">Hugo</edge>
      <edge type="token" id="t13" source="v13" target="v14" cfrom="75" cto="81">Chávez</edge>
      <edge type="token" id="t14" source="v14" target="v15" cfrom="81" cto="82">,</edge>
      <edge type="token" id="t15" source="v15" target="v16" cfrom="83" cto="92">Venezuela</edge>
      <edge type="token" id="t16" source="v16" target="v17" cfrom="92" cto="94">'s</edge>
      <edge type="token" id="t17" source="v17" target="v18" cfrom="95" cto="103">populist</edge>
      <edge type="token" id="t18" source="v18" target="v19" cfrom="104" cto="113">president</edge>
      <edge type="token" id="t19" source="v19" target="v20" cfrom="114" cto="116">is</edge>
      <edge type="token" id="t20" source="v20" target="v21" cfrom="117" cto="122">using</edge>
      <edge type="token" id="t21" source="v21" target="v22" cfrom="123" cto="125">an</edge>
      <edge type="token" id="t22" source="v22" target="v23" cfrom="126" cto="132">energy</edge>
      <edge type="token" id="t23" source="v23" target="v24" cfrom="133" cto="141">windfall</edge>
      <edge type="token" id="t24" source="v24" target="v25" cfrom="142" cto="144">to</edge>
      <edge type="token" id="t25" source="v25" target="v26" cfrom="145" cto="148">win</edge>
      <edge type="token" id="t26" source="v26" target="v27" cfrom="149" cto="156">friends</edge>
      <edge type="token" id="t27" source="v27" target="v28" cfrom="157" cto="160">and</edge>
      <edge type="token" id="t28" source="v28" target="v29" cfrom="161" cto="168">promote</edge>
      <edge type="token" id="t29" source="v29" target="v30" cfrom="169" cto="172">his</edge>
      <edge type="token" id="t30" source="v30" target="v31" cfrom="173" cto="179">vision</edge>
      <edge type="token" id="t31" source="v31" target="v32" cfrom="180" cto="182">of</edge>
      <edge type="token" id="t32" source="v32" target="v33" cfrom="183" cto="195">21st-century</edge>
      <edge type="token" id="t33" source="v33" target="v34" cfrom="196" cto="205">socialism</edge>
      <edge type="token" id="t34" source="v34" target="v35" cfrom="205" cto="206">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="2" deps="t0">
        <slot name="tag">CSA</slot>
        <slot name="weight">0.993802</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="2" deps="t0">
        <slot name="tag">NP1</slot>
        <slot name="weight">0.00619808</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="3" cto="10" deps="t1">
        <slot name="tag">NN2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="11" cto="17" deps="t2">
        <slot name="tag">VV0</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="18" cto="20" deps="t3">
        <slot name="tag">II</slot>
        <slot name="weight">0.983505</slot>
      </edge>
      <edge type="pos" id="p5" source="v3" target="v4" cfrom="18" cto="20" deps="t3">
        <slot name="tag">RP</slot>
        <slot name="weight">0.0164951</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="21" cto="30" deps="t4">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p7" source="v5" target="v6" cfrom="31" cto="36" deps="t5">
        <slot name="tag">II</slot>
        <slot name="weight">0.000308034</slot>
      </edge>
      <edge type="pos" id="p8" source="v5" target="v6" cfrom="31" cto="36" deps="t5">
        <slot name="tag">RL</slot>
        <slot name="weight">0.0256448</slot>
      </edge>
      <edge type="pos" id="p9" source="v5" target="v6" cfrom="31" cto="36" deps="t5">
        <slot name="tag">RR</slot>
        <slot name="weight">0.974047</slot>
      </edge>
      <edge type="pos" id="p10" source="v6" target="v7" cfrom="37" cto="39" deps="t6">
        <slot name="tag">IO</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v7" target="v8" cfrom="40" cto="44" deps="t7">
        <slot name="tag">DD1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v8" target="v9" cfrom="45" cto="53" deps="t8">
        <slot name="tag">NNT2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p13" source="v9" target="v10" cfrom="54" cto="62" deps="t9">
        <slot name="tag">JJ</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p14" source="v10" target="v11" cfrom="63" cto="68" deps="t10">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.999157</slot>
      </edge>
      <edge type="pos" id="p15" source="v10" target="v11" cfrom="63" cto="68" deps="t10">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.000843389</slot>
      </edge>
      <edge type="pos" id="p16" source="v11" target="v12" cfrom="68" cto="69" deps="t11">
        <slot name="tag">,</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p17" source="v12" target="v13" cfrom="70" cto="74" deps="t12">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p18" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.00377618</slot>
      </edge>
      <edge type="pos" id="p19" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0183885</slot>
      </edge>
      <edge type="pos" id="p20" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.00426326</slot>
      </edge>
      <edge type="pos" id="p21" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.00190727</slot>
      </edge>
      <edge type="pos" id="p22" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000438305</slot>
      </edge>
      <edge type="pos" id="p23" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00291896</slot>
      </edge>
      <edge type="pos" id="p24" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.966888</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00142</slot>
      </edge>
      <edge type="pos" id="p26" source="v14" target="v15" cfrom="81" cto="82" deps="t14">
        <slot name="tag">,</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p27" source="v15" target="v16" cfrom="83" cto="92" deps="t15">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p28" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">$</slot>
        <slot name="weight">0.982232</slot>
      </edge>
      <edge type="pos" id="p29" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">PPIO2</slot>
        <slot name="weight">2.44046e-308</slot>
      </edge>
      <edge type="pos" id="p30" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VBZ</slot>
        <slot name="weight">0.0172677</slot>
      </edge>
      <edge type="pos" id="p31" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.77101e-06</slot>
      </edge>
      <edge type="pos" id="p32" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000497046</slot>
      </edge>
      <edge type="pos" id="p33" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.902257</slot>
      </edge>
      <edge type="pos" id="p34" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0977435</slot>
      </edge>
      <edge type="pos" id="p35" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997405</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00259549</slot>
      </edge>
      <edge type="pos" id="p37" source="v19" target="v20" cfrom="114" cto="116" deps="t19">
        <slot name="tag">VBZ</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p38" source="v20" target="v21" cfrom="117" cto="122" deps="t20">
        <slot name="tag">VVG</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p39" source="v21" target="v22" cfrom="123" cto="125" deps="t21">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999911</slot>
      </edge>
      <edge type="pos" id="p40" source="v21" target="v22" cfrom="123" cto="125" deps="t21">
        <slot name="tag">NP1</slot>
        <slot name="weight">8.92656e-05</slot>
      </edge>
      <edge type="pos" id="p41" source="v22" target="v23" cfrom="126" cto="132" deps="t22">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p42" source="v23" target="v24" cfrom="133" cto="141" deps="t23">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p43" source="v24" target="v25" cfrom="142" cto="144" deps="t24">
        <slot name="tag">II</slot>
        <slot name="weight">0.00434461</slot>
      </edge>
      <edge type="pos" id="p44" source="v24" target="v25" cfrom="142" cto="144" deps="t24">
        <slot name="tag">TO</slot>
        <slot name="weight">0.995655</slot>
      </edge>
      <edge type="pos" id="p45" source="v25" target="v26" cfrom="145" cto="148" deps="t25">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.00409246</slot>
      </edge>
      <edge type="pos" id="p46" source="v25" target="v26" cfrom="145" cto="148" deps="t25">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.995908</slot>
      </edge>
      <edge type="pos" id="p47" source="v26" target="v27" cfrom="149" cto="156" deps="t26">
        <slot name="tag">NN2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p48" source="v27" target="v28" cfrom="157" cto="160" deps="t27">
        <slot name="tag">CC</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p49" source="v28" target="v29" cfrom="161" cto="168" deps="t28">
        <slot name="tag">VV0</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p50" source="v29" target="v30" cfrom="169" cto="172" deps="t29">
        <slot name="tag">APP$</slot>
        <slot name="weight">0.998336</slot>
      </edge>
      <edge type="pos" id="p51" source="v29" target="v30" cfrom="169" cto="172" deps="t29">
        <slot name="tag">PP$</slot>
        <slot name="weight">0.00166391</slot>
      </edge>
      <edge type="pos" id="p52" source="v30" target="v31" cfrom="173" cto="179" deps="t30">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999981</slot>
      </edge>
      <edge type="pos" id="p53" source="v30" target="v31" cfrom="173" cto="179" deps="t30">
        <slot name="tag">VV0</slot>
        <slot name="weight">1.89791e-05</slot>
      </edge>
      <edge type="pos" id="p54" source="v31" target="v32" cfrom="180" cto="182" deps="t31">
        <slot name="tag">IO</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p55" source="v32" target="v33" cfrom="183" cto="195" deps="t32">
        <slot name="tag">JB</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p56" source="v33" target="v34" cfrom="196" cto="205" deps="t33">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p57" source="v34" target="v35" cfrom="205" cto="206" deps="t34">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v1" target="v2" cfrom="3" cto="10" deps="p2">leader+s</edge>
      <edge type="morph" id="m2" source="v8" target="v9" cfrom="45" cto="53" deps="p12">weekend+s</edge>
      <edge type="morph" id="m3" source="v10" target="v11" cfrom="63" cto="68" deps="p14">talk+s</edge>
      <edge type="morph" id="m4" source="v10" target="v11" cfrom="63" cto="68" deps="p15">talk+s</edge>
      <edge type="morph" id="m5" source="v16" target="v17" cfrom="92" cto="94" deps="p28">'s+</edge>
      <edge type="morph" id="m6" source="v16" target="v17" cfrom="92" cto="94" deps="p30">be+s</edge>
      <edge type="morph" id="m7" source="v16" target="v17" cfrom="92" cto="94" deps="p31">do+s</edge>
      <edge type="morph" id="m8" source="v16" target="v17" cfrom="92" cto="94" deps="p32">have+s</edge>
      <edge type="morph" id="m9" source="v19" target="v20" cfrom="114" cto="116" deps="p37">be+s</edge>
      <edge type="morph" id="m10" source="v20" target="v21" cfrom="117" cto="122" deps="p38">use+ing</edge>
      <edge type="morph" id="m11" source="v26" target="v27" cfrom="149" cto="156" deps="p47">friend+s</edge>
      <edge type="syntree" id="s0" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-70.013</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/pp-sfin_s/+|
          (|PP/p1|
           (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
            (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
             (|V1/v_pp| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
              (|PP/p1|
               (|P1/p_np| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                (|NP/n1-name_np-r|
                 (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                  (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                   (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                    (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                     (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                     (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|)))))
                 (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|)))))))))
          |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
          (|S/np_vp|
           (|NP/np-poss_n1|
            (|NP/np_n-poss|
             (|NP/n1-name|
              (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
               (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
             |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
            (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
             (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
           (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
            (|V1/v_np_inf| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
              (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
               (|N1/n| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|)))
             (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
              (|V1/vp_vp-coord/-|
               (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
               (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                 (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                  (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                   (|PP/p1|
                    (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                     (|N1/ap_n1/-|
                      (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                      (|N1/n| |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|))))))))))))))
         (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s1" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-70.966</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/pp-sfin_s/+|
          (|PP/p1|
           (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
            (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
             (|V1/v_pp| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
              (|PP/p1|
               (|P1/p_np| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                (|NP/n1-name_np-r|
                 (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                  (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                   (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                    (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                     (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                     (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|)))))
                 (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|)))))))))
          |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
          (|S/np_vp|
           (|NP/np-poss_n1|
            (|NP/np_n-poss|
             (|NP/n1-name|
              (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
               (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
             |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
            (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
             (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
           (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
            (|V1/v_np| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
              (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
               (|N1/n_inf| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|
                (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                 (|V1/vp_vp-coord/-|
                  (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                   (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                  (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                   (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                    (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                     (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                      (|PP/p1|
                       (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                        (|N1/ap_n1/-|
                         (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                         (|N1/n|
                          |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|)))))))))))))))))
         (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s2" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-71.363</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/pp-sfin_s/+|
          (|PP/p1|
           (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
            (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
             (|V1/v_pp_np-hs-r| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
              (|PP/p1|
               (|P1/p_np-name| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                (|NP/n1-name|
                 (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                  (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                   (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                    (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                     (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                     (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|))))))))
              (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|))))))
          |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
          (|S/np_vp|
           (|NP/np-poss_n1|
            (|NP/np_n-poss|
             (|NP/n1-name|
              (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
               (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
             |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
            (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
             (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
           (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
            (|V1/v_np_inf| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
              (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
               (|N1/n| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|)))
             (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
              (|V1/vp_vp-coord/-|
               (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
               (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                 (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                  (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                   (|PP/p1|
                    (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                     (|N1/ap_n1/-|
                      (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                      (|N1/n| |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|))))))))))))))
         (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s3" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-71.389</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/pp-sfin_s/+|
          (|PP/p1|
           (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
            (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
             (|V1/vp_pp| (|V1/v| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|)
              (|PP/p1|
               (|P1/p_np| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                (|NP/n1-name_np-r|
                 (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                  (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                   (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                    (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                     (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                     (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|)))))
                 (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|)))))))))
          |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
          (|S/np_vp|
           (|NP/np-poss_n1|
            (|NP/np_n-poss|
             (|NP/n1-name|
              (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
               (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
             |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
            (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
             (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
           (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
            (|V1/v_np_inf| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
              (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
               (|N1/n| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|)))
             (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
              (|V1/vp_vp-coord/-|
               (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
               (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                 (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                  (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                   (|PP/p1|
                    (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                     (|N1/ap_n1/-|
                      (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                      (|N1/n| |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|))))))))))))))
         (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s4" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-72.316</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/pp-sfin_s/+|
          (|PP/p1|
           (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
            (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
             (|V1/v_pp_np-hs-r| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
              (|PP/p1|
               (|P1/p_np-name| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                (|NP/n1-name|
                 (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                  (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                   (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                    (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                     (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                     (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|))))))))
              (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|))))))
          |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
          (|S/np_vp|
           (|NP/np-poss_n1|
            (|NP/np_n-poss|
             (|NP/n1-name|
              (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
               (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
             |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
            (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
             (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
           (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
            (|V1/v_np| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
              (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
               (|N1/n_inf| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|
                (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                 (|V1/vp_vp-coord/-|
                  (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                   (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                  (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                   (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                    (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                     (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                      (|PP/p1|
                       (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                        (|N1/ap_n1/-|
                         (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                         (|N1/n|
                          |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|)))))))))))))))))
         (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>The cat chased the dog.</text>
    <lattice init="v0" final="v6" cfrom="0" cto="23">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="19" cto="22">dog</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="22" cto="23">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t0">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p2" source="v2" target="v3" cfrom="8" cto="14" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.90372</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="14" deps="t2">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.0962799</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="15" cto="18" deps="t3">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p5" source="v4" target="v5" cfrom="19" cto="22" deps="t4">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999833</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="19" cto="22" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000166966</slot>
      </edge>
      <edge type="pos" id="p7" source="v5" target="v6" cfrom="22" cto="23" deps="t5">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v2" target="v3" cfrom="8" cto="14" deps="p2">chase+ed</edge>
      <edge type="morph" id="m2" source="v2" target="v3" cfrom="8" cto="14" deps="p3">chase+ed</edge>
      <edge type="syntree" id="s0" source="v0" target="v6" cfrom="0" cto="23">
        <slot name="weight">-4.679</slot>
        <slot name="tree">
        (|T/txt-sc1/-+|
         (|S/np_vp|
          (|NP/det_n1| |&lt;w s='0' e='3'&gt;The_AT&lt;/w&gt;|
           (|N1/n| |&lt;w s='4' e='7'&gt;cat_NN1&lt;/w&gt;|))
          (|V1/v_np| |&lt;w s='8' e='14'&gt;chase+ed_VVD&lt;/w&gt;|
           (|NP/det_n1| |&lt;w s='15' e='18'&gt;the_AT&lt;/w&gt;|
            (|N1/n| |&lt;w s='19' e='22'&gt;dog_NN1&lt;/w&gt;|))))
         (|End-punct3/-| |&lt;w s='22' e='23'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
    </lattice>
  </smaf>"""
];



RASP_RMRSED = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v4" cfrom="0" cto="14">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="8" cto="13">barks</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="13" cto="14">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t0">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999729</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="4" cto="7" deps="t1">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00027066</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="13" deps="t2">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.750875</slot>
      </edge>
      <edge type="pos" id="p4" source="v2" target="v3" cfrom="8" cto="13" deps="t2">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.249125</slot>
      </edge>
      <edge type="pos" id="p5" source="v3" target="v4" cfrom="13" cto="14" deps="t3">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v2" target="v3" cfrom="8" cto="13" deps="p3">bark+s</edge>
      <edge type="morph" id="m2" source="v2" target="v3" cfrom="8" cto="13" deps="p4">bark+s</edge>
      <edge type="syntree" id="s0" source="v0" target="v4" cfrom="0" cto="14">
        <slot name="weight">-4.440</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp|
            (|NP/det_n1| |&lt;w s='0' e='3'&gt;The_AT&lt;/w&gt;|
             (|N1/n| |&lt;w s='4' e='7'&gt;dog_NN1&lt;/w&gt;|))
            (|V1/v| |&lt;w s='8' e='13'&gt;bark+s_VVZ&lt;/w&gt;|))
           (|End-punct3/-| |&lt;w s='13' e='14'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v4" cfrom="0" cto="14" deps="s0">
        <rmrs cfrom='0' cto='14'>
          <label vid='23'/>
          <ep cfrom='0' cto='3'> <realpred lemma='the' pos='q'/> <label vid='3'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='4' cto='7'> <realpred lemma='dog' pos='n'/> <label vid='4'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='8' cto='13'> <realpred lemma='bark' pos='v'/> <label vid='12'/> <var sort='e' vid='13' tense='present'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='9'/> </hi>   <lo> <label vid='4'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='x' vid='2' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='1'/> <var sort='h' vid='9'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='1'/> <var sort='h' vid='10'/> </rarg>
        </rmrs>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>I saw a man with a telescope.</text>
    <lattice init="v0" final="v8" cfrom="0" cto="29">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="1">I</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="2" cto="5">saw</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="6" cto="7">a</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="8" cto="11">man</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="12" cto="16">with</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="17" cto="18">a</edge>
      <edge type="token" id="t6" source="v6" target="v7" cfrom="19" cto="28">telescope</edge>
      <edge type="token" id="t7" source="v7" target="v8" cfrom="28" cto="29">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="1" deps="t0">
        <slot name="tag">MC</slot>
        <slot name="weight">0.000427712</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="1" deps="t0">
        <slot name="tag">PPIS1</slot>
        <slot name="weight">0.936841</slot>
      </edge>
      <edge type="pos" id="p2" source="v0" target="v1" cfrom="0" cto="1" deps="t0">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">0.0627313</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="2" cto="5" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.000105329</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="2" cto="5" deps="t1">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.999895</slot>
      </edge>
      <edge type="pos" id="p5" source="v2" target="v3" cfrom="6" cto="7" deps="t2">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.998334</slot>
      </edge>
      <edge type="pos" id="p6" source="v2" target="v3" cfrom="6" cto="7" deps="t2">
        <slot name="tag">II</slot>
        <slot name="weight">0.00164698</slot>
      </edge>
      <edge type="pos" id="p7" source="v2" target="v3" cfrom="6" cto="7" deps="t2">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">1.89096e-05</slot>
      </edge>
      <edge type="pos" id="p8" source="v3" target="v4" cfrom="8" cto="11" deps="t3">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999525</slot>
      </edge>
      <edge type="pos" id="p9" source="v3" target="v4" cfrom="8" cto="11" deps="t3">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000475218</slot>
      </edge>
      <edge type="pos" id="p10" source="v4" target="v5" cfrom="12" cto="16" deps="t4">
        <slot name="tag">IW</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v5" target="v6" cfrom="17" cto="18" deps="t5">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999927</slot>
      </edge>
      <edge type="pos" id="p12" source="v5" target="v6" cfrom="17" cto="18" deps="t5">
        <slot name="tag">II</slot>
        <slot name="weight">1.0498e-05</slot>
      </edge>
      <edge type="pos" id="p13" source="v5" target="v6" cfrom="17" cto="18" deps="t5">
        <slot name="tag">ZZ1</slot>
        <slot name="weight">6.2175e-05</slot>
      </edge>
      <edge type="pos" id="p14" source="v6" target="v7" cfrom="19" cto="28" deps="t6">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999617</slot>
      </edge>
      <edge type="pos" id="p15" source="v6" target="v7" cfrom="19" cto="28" deps="t6">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000383388</slot>
      </edge>
      <edge type="pos" id="p16" source="v7" target="v8" cfrom="28" cto="29" deps="t7">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v1" target="v2" cfrom="2" cto="5" deps="p4">see+ed</edge>
      <edge type="syntree" id="s0" source="v0" target="v8" cfrom="0" cto="29">
        <slot name="weight">-6.821</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp| |&lt;w s='0' e='1'&gt;I_PPIS1&lt;/w&gt;|
            (|V1/v_np_pp| |&lt;w s='2' e='5'&gt;see+ed_VVD&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='6' e='7'&gt;a_AT1&lt;/w&gt;|
              (|N1/n| |&lt;w s='8' e='11'&gt;man_NN1&lt;/w&gt;|))
             (|PP/p1|
              (|P1/p_np| |&lt;w s='12' e='16'&gt;with_IW&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='17' e='18'&gt;a_AT1&lt;/w&gt;|
                (|N1/n| |&lt;w s='19' e='28'&gt;telescope_NN1&lt;/w&gt;|))))))
           (|End-punct3/-| |&lt;w s='28' e='29'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s1" source="v0" target="v8" cfrom="0" cto="29">
        <slot name="weight">-7.233</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp| |&lt;w s='0' e='1'&gt;I_PPIS1&lt;/w&gt;|
            (|V1/v_np| |&lt;w s='2' e='5'&gt;see+ed_VVD&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='6' e='7'&gt;a_AT1&lt;/w&gt;|
              (|N1/n1_pp3| (|N1/n| |&lt;w s='8' e='11'&gt;man_NN1&lt;/w&gt;|)
               (|PP/p1|
                (|P1/p_np| |&lt;w s='12' e='16'&gt;with_IW&lt;/w&gt;|
                 (|NP/det_n1| |&lt;w s='17' e='18'&gt;a_AT1&lt;/w&gt;|
                  (|N1/n| |&lt;w s='19' e='28'&gt;telescope_NN1&lt;/w&gt;|))))))))
           (|End-punct3/-| |&lt;w s='28' e='29'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s2" source="v0" target="v8" cfrom="0" cto="29">
        <slot name="weight">-8.501</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp| |&lt;w s='0' e='1'&gt;I_PPIS1&lt;/w&gt;|
            (|V1/vp_pp|
             (|V1/v_np| |&lt;w s='2' e='5'&gt;see+ed_VVD&lt;/w&gt;|
              (|NP/det_n1| |&lt;w s='6' e='7'&gt;a_AT1&lt;/w&gt;|
               (|N1/n| |&lt;w s='8' e='11'&gt;man_NN1&lt;/w&gt;|)))
             (|PP/p1|
              (|P1/p_np| |&lt;w s='12' e='16'&gt;with_IW&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='17' e='18'&gt;a_AT1&lt;/w&gt;|
                (|N1/n| |&lt;w s='19' e='28'&gt;telescope_NN1&lt;/w&gt;|))))))
           (|End-punct3/-| |&lt;w s='28' e='29'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v8" cfrom="0" cto="29" deps="s0">
        <rmrs cfrom='0' cto='29'>
          <label vid='51'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='sg' pers='1'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='sg' pers='1'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='see' pos='v'/> <label vid='7'/> <var sort='e' vid='8' tense='past'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='11'/> <var sort='x' vid='10' num='sg'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n'/> <label vid='12'/> <var sort='x' vid='10' num='sg'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='20'/> <var sort='u' vid='21'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='24'/> <var sort='x' vid='23' num='sg'/> </ep>
          <ep cfrom='19' cto='28'> <realpred lemma='telescope' pos='n'/> <label vid='25'/> <var sort='x' vid='23' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='4'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='17'/> </hi>   <lo> <label vid='12'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='30'/> </hi>   <lo> <label vid='25'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='7'/> <var sort='x' vid='2' num='sg' pers='1'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='3'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='3'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='7'/> <var sort='x' vid='10' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='20'/> <var sort='u' vid='43'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='9'/> <var sort='h' vid='17'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='9'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='20'/> <var sort='x' vid='23' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='22'/> <var sort='h' vid='30'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='22'/> <var sort='h' vid='31'/> </rarg>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r1" source="v0" target="v8" cfrom="0" cto="29" deps="s1">
        <rmrs cfrom='0' cto='29'>
          <label vid='49'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='sg' pers='1'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='sg' pers='1'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='see' pos='v'/> <label vid='7'/> <var sort='e' vid='8' tense='past'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='11'/> <var sort='x' vid='10' num='sg'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n'/> <label vid='12'/> <var sort='x' vid='10' num='sg'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='14'/> <var sort='u' vid='15'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='18'/> <var sort='x' vid='17' num='sg'/> </ep>
          <ep cfrom='19' cto='28'> <realpred lemma='telescope' pos='n'/> <label vid='19'/> <var sort='x' vid='17' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='4'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='36'/> </hi>   <lo> <label vid='12'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='24'/> </hi>   <lo> <label vid='19'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='7'/> <var sort='x' vid='2' num='sg' pers='1'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='3'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='3'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='7'/> <var sort='x' vid='10' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='9'/> <var sort='h' vid='36'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='9'/> <var sort='h' vid='37'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='14'/> <var sort='x' vid='17' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='16'/> <var sort='h' vid='24'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='16'/> <var sort='h' vid='25'/> </rarg>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r2" source="v0" target="v8" cfrom="0" cto="29" deps="s2">
        <rmrs cfrom='0' cto='29'>
          <label vid='54'/>
          <ep cfrom='0' cto='1'> <gpred>pron_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='sg' pers='1'/> </ep>
          <ep cfrom='0' cto='1'> <gpred>pronoun_q_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='sg' pers='1'/> </ep>
          <ep cfrom='2' cto='5'> <realpred lemma='see' pos='v'/> <label vid='7'/> <var sort='e' vid='8' tense='past'/> </ep>
          <ep cfrom='6' cto='7'> <realpred lemma='a' pos='q'/> <label vid='11'/> <var sort='x' vid='10' num='sg'/> </ep>
          <ep cfrom='8' cto='11'> <realpred lemma='man' pos='n'/> <label vid='12'/> <var sort='x' vid='10' num='sg'/> </ep>
          <ep cfrom='12' cto='16'> <realpred lemma='with' pos='p'/> <label vid='23'/> <var sort='u' vid='24'/> </ep>
          <ep cfrom='17' cto='18'> <realpred lemma='a' pos='q'/> <label vid='27'/> <var sort='x' vid='26' num='sg'/> </ep>
          <ep cfrom='19' cto='28'> <realpred lemma='telescope' pos='n'/> <label vid='28'/> <var sort='x' vid='26' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='4'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='17'/> </hi>   <lo> <label vid='12'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='33'/> </hi>   <lo> <label vid='28'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='7'/> <var sort='x' vid='2' num='sg' pers='1'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='3'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='3'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='23'/> <var sort='e' vid='8' tense='past'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='7'/> <var sort='x' vid='10' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='9'/> <var sort='h' vid='17'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='9'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='23'/> <var sort='x' vid='26' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='25'/> <var sort='h' vid='33'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='25'/> <var sort='h' vid='34'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='7'/> </ing-a>   <ing-b> <var sort='h' vid='23'/> </ing-b>   </ing>
        </rmrs>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>Hugo Chávez chased the dog.</text>
    <lattice init="v0" final="v6" cfrom="0" cto="27">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="4">Hugo</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="5" cto="11">Chávez</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="23" cto="26">dog</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="26" cto="27">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="4" deps="t0">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.00357779</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.792963</slot>
      </edge>
      <edge type="pos" id="p3" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.151421</slot>
      </edge>
      <edge type="pos" id="p4" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">RR</slot>
        <slot name="weight">0.0461225</slot>
      </edge>
      <edge type="pos" id="p5" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000336622</slot>
      </edge>
      <edge type="pos" id="p6" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00531652</slot>
      </edge>
      <edge type="pos" id="p7" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.000113307</slot>
      </edge>
      <edge type="pos" id="p8" source="v1" target="v2" cfrom="5" cto="11" deps="t1">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.000149814</slot>
      </edge>
      <edge type="pos" id="p9" source="v2" target="v3" cfrom="12" cto="18" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.886745</slot>
      </edge>
      <edge type="pos" id="p10" source="v2" target="v3" cfrom="12" cto="18" deps="t2">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.113255</slot>
      </edge>
      <edge type="pos" id="p11" source="v3" target="v4" cfrom="19" cto="22" deps="t3">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v4" target="v5" cfrom="23" cto="26" deps="t4">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999833</slot>
      </edge>
      <edge type="pos" id="p13" source="v4" target="v5" cfrom="23" cto="26" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000166966</slot>
      </edge>
      <edge type="pos" id="p14" source="v5" target="v6" cfrom="26" cto="27" deps="t5">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v2" target="v3" cfrom="12" cto="18" deps="p9">chase+ed</edge>
      <edge type="morph" id="m2" source="v2" target="v3" cfrom="12" cto="18" deps="p10">chase+ed</edge>
      <edge type="syntree" id="s0" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-7.775</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/n1_vp|
            (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
             (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN1&lt;/w&gt;|))
            (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVD&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
              (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
           (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s1" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-8.669</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/n1_vp|
            (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
             (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN1&lt;/w&gt;|))
            (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVN&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
              (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
           (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s2" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-9.361</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp|
            (|NP/n1-plu|
             (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
              (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN2&lt;/w&gt;|)))
            (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVD&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
              (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
           (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s3" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-9.863</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp| (|NP/n1-name| (|N1/n-name| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|))
            (|V1/adv_vp| (|AP/a1| (|A1/a| |&lt;w s='5' e='11'&gt;Chávez_RR&lt;/w&gt;|))
             (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVD&lt;/w&gt;|
              (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
               (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|)))))
           (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s4" source="v0" target="v6" cfrom="0" cto="27">
        <slot name="weight">-10.255</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp|
            (|NP/n1-plu|
             (|N1/n-name_n1| |&lt;w s='0' e='4'&gt;Hugo_NP1&lt;/w&gt;|
              (|N1/n| |&lt;w s='5' e='11'&gt;Chávez_NN2&lt;/w&gt;|)))
            (|V1/v_np| |&lt;w s='12' e='18'&gt;chase+ed_VVN&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='19' e='22'&gt;the_AT&lt;/w&gt;|
              (|N1/n| |&lt;w s='23' e='26'&gt;dog_NN1&lt;/w&gt;|))))
           (|End-punct3/-| |&lt;w s='26' e='27'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v6" cfrom="0" cto="27" deps="s0">
        <rmrs cfrom='0' cto='27'>
          <label vid='39'/>
          <ep cfrom='0' cto='26'> <gpred>udef_q_rel</gpred> <label vid='31'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>proper_q_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>named_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='5' cto='11'> <realpred lemma='chávez' pos='n'/> <label vid='7'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='12' cto='18'> <realpred lemma='chase' pos='v'/> <label vid='12'/> <var sort='e' vid='13' tense='past'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='the' pos='q'/> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='23' cto='26'> <realpred lemma='dog' pos='n'/> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='33'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='22'/> </hi>   <lo> <label vid='17'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='x' vid='2' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='31'/> <var sort='h' vid='33'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='31'/> <var sort='h' vid='34'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='4'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='4'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='3'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='14'/> <var sort='h' vid='22'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='14'/> <var sort='h' vid='23'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='1'/> </ing-a>   <ing-b> <var sort='h' vid='7'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r1" source="v0" target="v6" cfrom="0" cto="27" deps="s1">
        <rmrs cfrom='0' cto='27'>
          <label vid='39'/>
          <ep cfrom='0' cto='26'> <gpred>udef_q_rel</gpred> <label vid='31'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>proper_q_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>named_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='5' cto='11'> <realpred lemma='chávez' pos='n'/> <label vid='7'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='12' cto='18'> <realpred lemma='chase' pos='v'/> <label vid='12'/> <var sort='e' vid='13'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='the' pos='q'/> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='23' cto='26'> <realpred lemma='dog' pos='n'/> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='33'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='22'/> </hi>   <lo> <label vid='17'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='x' vid='2' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='31'/> <var sort='h' vid='33'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='31'/> <var sort='h' vid='34'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='4'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='4'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='3'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='14'/> <var sort='h' vid='22'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='14'/> <var sort='h' vid='23'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='1'/> </ing-a>   <ing-b> <var sort='h' vid='7'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r2" source="v0" target="v6" cfrom="0" cto="27" deps="s2">
        <rmrs cfrom='0' cto='27'>
          <label vid='40'/>
          <ep cfrom='0' cto='11'> <gpred>udef_q_rel</gpred> <label vid='12'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>proper_q_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>named_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='5' cto='11'> <realpred lemma='chávez' pos='n'/> <label vid='7'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='12' cto='18'> <realpred lemma='chase' pos='v'/> <label vid='17'/> <var sort='e' vid='18' tense='past'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='the' pos='q'/> <label vid='21'/> <var sort='x' vid='20' num='sg'/> </ep>
          <ep cfrom='23' cto='26'> <realpred lemma='dog' pos='n'/> <label vid='22'/> <var sort='x' vid='20' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='14'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='27'/> </hi>   <lo> <label vid='22'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='17'/> <var sort='x' vid='2' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='12'/> <var sort='h' vid='14'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='12'/> <var sort='h' vid='15'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='4'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='4'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='3'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='17'/> <var sort='x' vid='20' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='19'/> <var sort='h' vid='27'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='19'/> <var sort='h' vid='28'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='1'/> </ing-a>   <ing-b> <var sort='h' vid='7'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r3" source="v0" target="v6" cfrom="0" cto="27" deps="s3">
        <rmrs cfrom='0' cto='27'>
          <label vid='40'/>
          <ep cfrom='0' cto='4'> <gpred>proper_q_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>named_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='5' cto='11'> <realpred lemma='chávez' pos='r'/> <label vid='7'/> <var sort='e' vid='8'/> </ep>
          <ep cfrom='12' cto='18'> <realpred lemma='chase' pos='v'/> <label vid='13'/> <var sort='e' vid='14' tense='past'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='the' pos='q'/> <label vid='17'/> <var sort='x' vid='16' num='sg'/> </ep>
          <ep cfrom='23' cto='26'> <realpred lemma='dog' pos='n'/> <label vid='18'/> <var sort='x' vid='16' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='23'/> </hi>   <lo> <label vid='18'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='13'/> <var sort='x' vid='2' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='4'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='4'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='3'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='7'/> <var sort='e' vid='14' tense='past'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='13'/> <var sort='x' vid='16' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='15'/> <var sort='h' vid='23'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='15'/> <var sort='h' vid='24'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='13'/> </ing-a>   <ing-b> <var sort='h' vid='7'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r4" source="v0" target="v6" cfrom="0" cto="27" deps="s4">
        <rmrs cfrom='0' cto='27'>
          <label vid='40'/>
          <ep cfrom='0' cto='11'> <gpred>udef_q_rel</gpred> <label vid='12'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>proper_q_rel</gpred> <label vid='4'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='0' cto='4'> <gpred>named_rel</gpred> <label vid='3'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='5' cto='11'> <realpred lemma='chávez' pos='n'/> <label vid='7'/> <var sort='x' vid='2' num='pl'/> </ep>
          <ep cfrom='12' cto='18'> <realpred lemma='chase' pos='v'/> <label vid='17'/> <var sort='e' vid='18'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='the' pos='q'/> <label vid='21'/> <var sort='x' vid='20' num='sg'/> </ep>
          <ep cfrom='23' cto='26'> <realpred lemma='dog' pos='n'/> <label vid='22'/> <var sort='x' vid='20' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='14'/> </hi>   <lo> <label vid='7'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='5'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='27'/> </hi>   <lo> <label vid='22'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='17'/> <var sort='x' vid='2' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='12'/> <var sort='h' vid='14'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='12'/> <var sort='h' vid='15'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='4'/> <var sort='h' vid='5'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='4'/> <var sort='h' vid='6'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='3'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='17'/> <var sort='x' vid='20' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='19'/> <var sort='h' vid='27'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='19'/> <var sort='h' vid='28'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='1'/> </ing-a>   <ing-b> <var sort='h' vid='7'/> </ing-b>   </ing>
        </rmrs>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>As leaders gather in Argentina ahead of this weekends regional talks, Hugo Chávez, Venezuela's populist president is using an energy windfall to win friends and promote his vision of 21st-century socialism.</text>
    <lattice init="v0" final="v35" cfrom="0" cto="206">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="2">As</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="3" cto="10">leaders</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="11" cto="17">gather</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="18" cto="20">in</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="21" cto="30">Argentina</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="31" cto="36">ahead</edge>
      <edge type="token" id="t6" source="v6" target="v7" cfrom="37" cto="39">of</edge>
      <edge type="token" id="t7" source="v7" target="v8" cfrom="40" cto="44">this</edge>
      <edge type="token" id="t8" source="v8" target="v9" cfrom="45" cto="53">weekends</edge>
      <edge type="token" id="t9" source="v9" target="v10" cfrom="54" cto="62">regional</edge>
      <edge type="token" id="t10" source="v10" target="v11" cfrom="63" cto="68">talks</edge>
      <edge type="token" id="t11" source="v11" target="v12" cfrom="68" cto="69">,</edge>
      <edge type="token" id="t12" source="v12" target="v13" cfrom="70" cto="74">Hugo</edge>
      <edge type="token" id="t13" source="v13" target="v14" cfrom="75" cto="81">Chávez</edge>
      <edge type="token" id="t14" source="v14" target="v15" cfrom="81" cto="82">,</edge>
      <edge type="token" id="t15" source="v15" target="v16" cfrom="83" cto="92">Venezuela</edge>
      <edge type="token" id="t16" source="v16" target="v17" cfrom="92" cto="94">'s</edge>
      <edge type="token" id="t17" source="v17" target="v18" cfrom="95" cto="103">populist</edge>
      <edge type="token" id="t18" source="v18" target="v19" cfrom="104" cto="113">president</edge>
      <edge type="token" id="t19" source="v19" target="v20" cfrom="114" cto="116">is</edge>
      <edge type="token" id="t20" source="v20" target="v21" cfrom="117" cto="122">using</edge>
      <edge type="token" id="t21" source="v21" target="v22" cfrom="123" cto="125">an</edge>
      <edge type="token" id="t22" source="v22" target="v23" cfrom="126" cto="132">energy</edge>
      <edge type="token" id="t23" source="v23" target="v24" cfrom="133" cto="141">windfall</edge>
      <edge type="token" id="t24" source="v24" target="v25" cfrom="142" cto="144">to</edge>
      <edge type="token" id="t25" source="v25" target="v26" cfrom="145" cto="148">win</edge>
      <edge type="token" id="t26" source="v26" target="v27" cfrom="149" cto="156">friends</edge>
      <edge type="token" id="t27" source="v27" target="v28" cfrom="157" cto="160">and</edge>
      <edge type="token" id="t28" source="v28" target="v29" cfrom="161" cto="168">promote</edge>
      <edge type="token" id="t29" source="v29" target="v30" cfrom="169" cto="172">his</edge>
      <edge type="token" id="t30" source="v30" target="v31" cfrom="173" cto="179">vision</edge>
      <edge type="token" id="t31" source="v31" target="v32" cfrom="180" cto="182">of</edge>
      <edge type="token" id="t32" source="v32" target="v33" cfrom="183" cto="195">21st-century</edge>
      <edge type="token" id="t33" source="v33" target="v34" cfrom="196" cto="205">socialism</edge>
      <edge type="token" id="t34" source="v34" target="v35" cfrom="205" cto="206">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="2" deps="t0">
        <slot name="tag">CSA</slot>
        <slot name="weight">0.993802</slot>
      </edge>
      <edge type="pos" id="p1" source="v0" target="v1" cfrom="0" cto="2" deps="t0">
        <slot name="tag">NP1</slot>
        <slot name="weight">0.00619808</slot>
      </edge>
      <edge type="pos" id="p2" source="v1" target="v2" cfrom="3" cto="10" deps="t1">
        <slot name="tag">NN2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="11" cto="17" deps="t2">
        <slot name="tag">VV0</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="18" cto="20" deps="t3">
        <slot name="tag">II</slot>
        <slot name="weight">0.983505</slot>
      </edge>
      <edge type="pos" id="p5" source="v3" target="v4" cfrom="18" cto="20" deps="t3">
        <slot name="tag">RP</slot>
        <slot name="weight">0.0164951</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="21" cto="30" deps="t4">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p7" source="v5" target="v6" cfrom="31" cto="36" deps="t5">
        <slot name="tag">II</slot>
        <slot name="weight">0.000308034</slot>
      </edge>
      <edge type="pos" id="p8" source="v5" target="v6" cfrom="31" cto="36" deps="t5">
        <slot name="tag">RL</slot>
        <slot name="weight">0.0256448</slot>
      </edge>
      <edge type="pos" id="p9" source="v5" target="v6" cfrom="31" cto="36" deps="t5">
        <slot name="tag">RR</slot>
        <slot name="weight">0.974047</slot>
      </edge>
      <edge type="pos" id="p10" source="v6" target="v7" cfrom="37" cto="39" deps="t6">
        <slot name="tag">IO</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p11" source="v7" target="v8" cfrom="40" cto="44" deps="t7">
        <slot name="tag">DD1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p12" source="v8" target="v9" cfrom="45" cto="53" deps="t8">
        <slot name="tag">NNT2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p13" source="v9" target="v10" cfrom="54" cto="62" deps="t9">
        <slot name="tag">JJ</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p14" source="v10" target="v11" cfrom="63" cto="68" deps="t10">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.999157</slot>
      </edge>
      <edge type="pos" id="p15" source="v10" target="v11" cfrom="63" cto="68" deps="t10">
        <slot name="tag">VVZ</slot>
        <slot name="weight">0.000843389</slot>
      </edge>
      <edge type="pos" id="p16" source="v11" target="v12" cfrom="68" cto="69" deps="t11">
        <slot name="tag">,</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p17" source="v12" target="v13" cfrom="70" cto="74" deps="t12">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p18" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.00377618</slot>
      </edge>
      <edge type="pos" id="p19" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0183885</slot>
      </edge>
      <edge type="pos" id="p20" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.00426326</slot>
      </edge>
      <edge type="pos" id="p21" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.00190727</slot>
      </edge>
      <edge type="pos" id="p22" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000438305</slot>
      </edge>
      <edge type="pos" id="p23" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00291896</slot>
      </edge>
      <edge type="pos" id="p24" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.966888</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00142</slot>
      </edge>
      <edge type="pos" id="p26" source="v14" target="v15" cfrom="81" cto="82" deps="t14">
        <slot name="tag">,</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p27" source="v15" target="v16" cfrom="83" cto="92" deps="t15">
        <slot name="tag">NP1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p28" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">$</slot>
        <slot name="weight">0.982232</slot>
      </edge>
      <edge type="pos" id="p29" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">PPIO2</slot>
        <slot name="weight">2.44046e-308</slot>
      </edge>
      <edge type="pos" id="p30" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VBZ</slot>
        <slot name="weight">0.0172677</slot>
      </edge>
      <edge type="pos" id="p31" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.77101e-06</slot>
      </edge>
      <edge type="pos" id="p32" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000497046</slot>
      </edge>
      <edge type="pos" id="p33" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.902257</slot>
      </edge>
      <edge type="pos" id="p34" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0977435</slot>
      </edge>
      <edge type="pos" id="p35" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997405</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00259549</slot>
      </edge>
      <edge type="pos" id="p37" source="v19" target="v20" cfrom="114" cto="116" deps="t19">
        <slot name="tag">VBZ</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p38" source="v20" target="v21" cfrom="117" cto="122" deps="t20">
        <slot name="tag">VVG</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p39" source="v21" target="v22" cfrom="123" cto="125" deps="t21">
        <slot name="tag">AT1</slot>
        <slot name="weight">0.999911</slot>
      </edge>
      <edge type="pos" id="p40" source="v21" target="v22" cfrom="123" cto="125" deps="t21">
        <slot name="tag">NP1</slot>
        <slot name="weight">8.92656e-05</slot>
      </edge>
      <edge type="pos" id="p41" source="v22" target="v23" cfrom="126" cto="132" deps="t22">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p42" source="v23" target="v24" cfrom="133" cto="141" deps="t23">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p43" source="v24" target="v25" cfrom="142" cto="144" deps="t24">
        <slot name="tag">II</slot>
        <slot name="weight">0.00434461</slot>
      </edge>
      <edge type="pos" id="p44" source="v24" target="v25" cfrom="142" cto="144" deps="t24">
        <slot name="tag">TO</slot>
        <slot name="weight">0.995655</slot>
      </edge>
      <edge type="pos" id="p45" source="v25" target="v26" cfrom="145" cto="148" deps="t25">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.00409246</slot>
      </edge>
      <edge type="pos" id="p46" source="v25" target="v26" cfrom="145" cto="148" deps="t25">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.995908</slot>
      </edge>
      <edge type="pos" id="p47" source="v26" target="v27" cfrom="149" cto="156" deps="t26">
        <slot name="tag">NN2</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p48" source="v27" target="v28" cfrom="157" cto="160" deps="t27">
        <slot name="tag">CC</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p49" source="v28" target="v29" cfrom="161" cto="168" deps="t28">
        <slot name="tag">VV0</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p50" source="v29" target="v30" cfrom="169" cto="172" deps="t29">
        <slot name="tag">APP$</slot>
        <slot name="weight">0.998336</slot>
      </edge>
      <edge type="pos" id="p51" source="v29" target="v30" cfrom="169" cto="172" deps="t29">
        <slot name="tag">PP$</slot>
        <slot name="weight">0.00166391</slot>
      </edge>
      <edge type="pos" id="p52" source="v30" target="v31" cfrom="173" cto="179" deps="t30">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999981</slot>
      </edge>
      <edge type="pos" id="p53" source="v30" target="v31" cfrom="173" cto="179" deps="t30">
        <slot name="tag">VV0</slot>
        <slot name="weight">1.89791e-05</slot>
      </edge>
      <edge type="pos" id="p54" source="v31" target="v32" cfrom="180" cto="182" deps="t31">
        <slot name="tag">IO</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p55" source="v32" target="v33" cfrom="183" cto="195" deps="t32">
        <slot name="tag">JB</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p56" source="v33" target="v34" cfrom="196" cto="205" deps="t33">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p57" source="v34" target="v35" cfrom="205" cto="206" deps="t34">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v1" target="v2" cfrom="3" cto="10" deps="p2">leader+s</edge>
      <edge type="morph" id="m2" source="v8" target="v9" cfrom="45" cto="53" deps="p12">weekend+s</edge>
      <edge type="morph" id="m3" source="v10" target="v11" cfrom="63" cto="68" deps="p14">talk+s</edge>
      <edge type="morph" id="m4" source="v10" target="v11" cfrom="63" cto="68" deps="p15">talk+s</edge>
      <edge type="morph" id="m5" source="v16" target="v17" cfrom="92" cto="94" deps="p28">'s+</edge>
      <edge type="morph" id="m6" source="v16" target="v17" cfrom="92" cto="94" deps="p30">be+s</edge>
      <edge type="morph" id="m7" source="v16" target="v17" cfrom="92" cto="94" deps="p31">do+s</edge>
      <edge type="morph" id="m8" source="v16" target="v17" cfrom="92" cto="94" deps="p32">have+s</edge>
      <edge type="morph" id="m9" source="v19" target="v20" cfrom="114" cto="116" deps="p37">be+s</edge>
      <edge type="morph" id="m10" source="v20" target="v21" cfrom="117" cto="122" deps="p38">use+ing</edge>
      <edge type="morph" id="m11" source="v26" target="v27" cfrom="149" cto="156" deps="p47">friend+s</edge>
      <edge type="syntree" id="s0" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-70.013</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/pp-sfin_s/+|
            (|PP/p1|
             (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
              (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
               (|V1/v_pp| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
                (|PP/p1|
                 (|P1/p_np| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                  (|NP/n1-name_np-r|
                   (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                    (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                     (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                      (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                       (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                       (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|)))))
                   (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|)))))))))
            |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
            (|S/np_vp|
             (|NP/np-poss_n1|
              (|NP/np_n-poss|
               (|NP/n1-name|
                (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
                 (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                  |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                  (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
               |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
              (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
               (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
             (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
              (|V1/v_np_inf| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
                (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
                 (|N1/n| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|)))
               (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                (|V1/vp_vp-coord/-|
                 (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                  (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                 (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                  (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                   (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                    (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                     (|PP/p1|
                      (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                       (|N1/ap_n1/-|
                        (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                        (|N1/n| |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|))))))))))))))
           (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s1" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-70.966</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/pp-sfin_s/+|
            (|PP/p1|
             (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
              (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
               (|V1/v_pp| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
                (|PP/p1|
                 (|P1/p_np| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                  (|NP/n1-name_np-r|
                   (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                    (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                     (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                      (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                       (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                       (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|)))))
                   (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|)))))))))
            |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
            (|S/np_vp|
             (|NP/np-poss_n1|
              (|NP/np_n-poss|
               (|NP/n1-name|
                (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
                 (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                  |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                  (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
               |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
              (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
               (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
             (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
              (|V1/v_np| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
                (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
                 (|N1/n_inf| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|
                  (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                   (|V1/vp_vp-coord/-|
                    (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                     (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                    (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                     (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                      (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                       (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                        (|PP/p1|
                         (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                          (|N1/ap_n1/-|
                           (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                           (|N1/n|
                            |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|)))))))))))))))))
           (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s2" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-71.363</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/pp-sfin_s/+|
            (|PP/p1|
             (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
              (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
               (|V1/v_pp_np-hs-r| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
                (|PP/p1|
                 (|P1/p_np-name| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                  (|NP/n1-name|
                   (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                    (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                     (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                      (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                       (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                       (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|))))))))
                (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|))))))
            |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
            (|S/np_vp|
             (|NP/np-poss_n1|
              (|NP/np_n-poss|
               (|NP/n1-name|
                (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
                 (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                  |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                  (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
               |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
              (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
               (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
             (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
              (|V1/v_np_inf| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
                (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
                 (|N1/n| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|)))
               (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                (|V1/vp_vp-coord/-|
                 (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                  (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                 (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                  (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                   (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                    (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                     (|PP/p1|
                      (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                       (|N1/ap_n1/-|
                        (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                        (|N1/n| |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|))))))))))))))
           (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s3" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-71.389</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/pp-sfin_s/+|
            (|PP/p1|
             (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
              (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
               (|V1/vp_pp| (|V1/v| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|)
                (|PP/p1|
                 (|P1/p_np| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                  (|NP/n1-name_np-r|
                   (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                    (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                     (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                      (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                       (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                       (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|)))))
                   (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|)))))))))
            |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
            (|S/np_vp|
             (|NP/np-poss_n1|
              (|NP/np_n-poss|
               (|NP/n1-name|
                (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
                 (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                  |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                  (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
               |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
              (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
               (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
             (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
              (|V1/v_np_inf| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
                (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
                 (|N1/n| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|)))
               (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                (|V1/vp_vp-coord/-|
                 (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                  (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                 (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                  (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                   (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                    (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                     (|PP/p1|
                      (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                       (|N1/ap_n1/-|
                        (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                        (|N1/n| |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|))))))))))))))
           (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="syntree" id="s4" source="v0" target="v35" cfrom="0" cto="206">
        <slot name="weight">-72.316</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/pp-sfin_s/+|
            (|PP/p1|
             (|P1/p_s| |&lt;w s='0' e='2'&gt;As_CSA&lt;/w&gt;|
              (|S/np_vp| (|NP/n1-plu| (|N1/n| |&lt;w s='3' e='10'&gt;leader+s_NN2&lt;/w&gt;|))
               (|V1/v_pp_np-hs-r| |&lt;w s='11' e='17'&gt;gather_VV0&lt;/w&gt;|
                (|PP/p1|
                 (|P1/p_np-name| |&lt;w s='18' e='20'&gt;in_II&lt;/w&gt;|
                  (|NP/n1-name|
                   (|N1/n_pp-of| |&lt;w s='21' e='30'&gt;Argentina_NP1&lt;/w&gt;|
                    (|PP/adv_p1| (|AP/a1| (|A1/a| |&lt;w s='31' e='36'&gt;ahead_RR&lt;/w&gt;|))
                     (|P1/p_np| |&lt;w s='37' e='39'&gt;of_IO&lt;/w&gt;|
                      (|NP/det_a1-r/+-| |&lt;w s='40' e='44'&gt;this_DD1&lt;/w&gt;|
                       (|N1/n-nt| |&lt;w s='45' e='53'&gt;weekend+s_NNT2&lt;/w&gt;|)
                       (|A1/a| |&lt;w s='54' e='62'&gt;regional_JJ&lt;/w&gt;|))))))))
                (|NP/n1-plu| (|N1/n| |&lt;w s='63' e='68'&gt;talk+s_NN2&lt;/w&gt;|))))))
            |&lt;w s='68' e='69'&gt;,_,&lt;/w&gt;|
            (|S/np_vp|
             (|NP/np-poss_n1|
              (|NP/np_n-poss|
               (|NP/n1-name|
                (|N1/n-name_n1-name| |&lt;w s='70' e='74'&gt;Hugo_NP1&lt;/w&gt;|
                 (|N1/ing_n1-r/-+| |&lt;w s='75' e='81'&gt;Chávez_VVG&lt;/w&gt;|
                  |&lt;w s='81' e='82'&gt;,_,&lt;/w&gt;|
                  (|N1/n-name| |&lt;w s='83' e='92'&gt;Venezuela_NP1&lt;/w&gt;|))))
               |&lt;w s='92' e='94'&gt;'s+_$&lt;/w&gt;|)
              (|N1/ap_n1/-| (|AP/a1| (|A1/a| |&lt;w s='95' e='103'&gt;populist_JJ&lt;/w&gt;|))
               (|N1/n| |&lt;w s='104' e='113'&gt;president_NN1&lt;/w&gt;|)))
             (|V1/be_ing/--| |&lt;w s='114' e='116'&gt;be+s_VBZ&lt;/w&gt;|
              (|V1/v_np| |&lt;w s='117' e='122'&gt;use+ing_VVG&lt;/w&gt;|
               (|NP/det_n1| |&lt;w s='123' e='125'&gt;an_AT1&lt;/w&gt;|
                (|N1/n_n1| |&lt;w s='126' e='132'&gt;energy_NN1&lt;/w&gt;|
                 (|N1/n_inf| |&lt;w s='133' e='141'&gt;windfall_NN1&lt;/w&gt;|
                  (|V1/to_bse/-| |&lt;w s='142' e='144'&gt;to_TO&lt;/w&gt;|
                   (|V1/vp_vp-coord/-|
                    (|V1/v_np| |&lt;w s='145' e='148'&gt;win_VV0&lt;/w&gt;|
                     (|NP/n1-plu| (|N1/n| |&lt;w s='149' e='156'&gt;friend+s_NN2&lt;/w&gt;|)))
                    (|V1/cj-end_vp/--| |&lt;w s='157' e='160'&gt;and_CC&lt;/w&gt;|
                     (|V1/v_np| |&lt;w s='161' e='168'&gt;promote_VV0&lt;/w&gt;|
                      (|NP/det_n1| |&lt;w s='169' e='172'&gt;his_APP$&lt;/w&gt;|
                       (|N1/n_pp-of| |&lt;w s='173' e='179'&gt;vision_NN1&lt;/w&gt;|
                        (|PP/p1|
                         (|P1/p_n1| |&lt;w s='180' e='182'&gt;of_IO&lt;/w&gt;|
                          (|N1/ap_n1/-|
                           (|AP/a1| (|A1/a| |&lt;w s='183' e='195'&gt;21st-century_JB&lt;/w&gt;|))
                           (|N1/n|
                            |&lt;w s='196' e='205'&gt;socialism_NN1&lt;/w&gt;|)))))))))))))))))
           (|End-punct3/-| |&lt;w s='205' e='206'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v35" cfrom="0" cto="206" deps="s0">
        <rmrs cfrom='0' cto='206'>
          <label vid='232'/>
          <ep cfrom='0' cto='2'> <realpred lemma='as' pos='x'/> <label vid='1'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='3' cto='10'> <gpred>udef_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='3' cto='10'> <realpred lemma='leader' pos='n'/> <label vid='3'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='11' cto='17'> <realpred lemma='gather' pos='v'/> <label vid='10'/> <var sort='e' vid='11'/> </ep>
          <ep cfrom='18' cto='20'> <realpred lemma='in' pos='p'/> <label vid='12'/> <var sort='e' vid='13'/> </ep>
          <ep cfrom='21' cto='68'> <gpred>appos_rel</gpred> <label vid='54'/> <var sort='e' vid='55'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>proper_q_rel</gpred> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>named_rel</gpred> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='31' cto='36'> <realpred lemma='ahead' pos='r'/> <label vid='20'/> <var sort='e' vid='21'/> </ep>
          <ep cfrom='37' cto='39'> <realpred lemma='of' pos='p'/> <label vid='26'/> <var sort='e' vid='27'/> </ep>
          <ep cfrom='40' cto='44'> <realpred lemma='this' pos='q'/> <label vid='30'/> <var sort='x' vid='29'/> </ep>
          <ep cfrom='45' cto='53'> <realpred lemma='weekend' pos='n'/> <label vid='31'/> <var sort='x' vid='32'/> </ep>
          <ep cfrom='54' cto='62'> <realpred lemma='regional' pos='j'/> <label vid='33'/> <var sort='e' vid='34'/> </ep>
          <ep cfrom='63' cto='68'> <gpred>udef_q_rel</gpred> <label vid='47'/> <var sort='x' vid='46' num='pl'/> </ep>
          <ep cfrom='63' cto='68'> <realpred lemma='talk' pos='n'/> <label vid='45'/> <var sort='x' vid='46' num='pl'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>def_explicit_q_rel</gpred> <label vid='113'/> <var sort='x' vid='104' num='sg'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>poss_rel</gpred> <label vid='114'/> <var sort='u' vid='115'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>proper_q_rel</gpred> <label vid='79'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>named_rel</gpred> <label vid='78'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='75' cto='81'> <realpred lemma='chávez' pos='v'/> <label vid='82'/> <var sort='e' vid='83'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>proper_q_rel</gpred> <label vid='89'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>named_rel</gpred> <label vid='88'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='95' cto='103'> <realpred lemma='populist' pos='j'/> <label vid='99'/> <var sort='e' vid='100'/> </ep>
          <ep cfrom='104' cto='113'> <realpred lemma='president' pos='n'/> <label vid='105'/> <var sort='x' vid='106' num='sg'/> </ep>
          <ep cfrom='117' cto='122'> <realpred lemma='use' pos='v'/> <label vid='121'/> <var sort='e' vid='122'/> </ep>
          <ep cfrom='123' cto='125'> <realpred lemma='an' pos='q'/> <label vid='125'/> <var sort='x' vid='124' num='sg'/> </ep>
          <ep cfrom='126' cto='141'> <gpred>compound_rel</gpred> <label vid='130'/> <var sort='e' vid='133'/> </ep>
          <ep cfrom='126' cto='141'> <gpred>udef_q_rel</gpred> <label vid='134'/> <var sort='x' vid='127' num='sg'/> </ep>
          <ep cfrom='126' cto='132'> <realpred lemma='energy' pos='n'/> <label vid='126'/> <var sort='x' vid='127' num='sg'/> </ep>
          <ep cfrom='133' cto='141'> <realpred lemma='windfall' pos='n'/> <label vid='128'/> <var sort='x' vid='124' num='sg'/> </ep>
          <ep cfrom='145' cto='148'> <realpred lemma='win' pos='v'/> <label vid='147'/> <var sort='e' vid='148'/> </ep>
          <ep cfrom='149' cto='156'> <gpred>udef_q_rel</gpred> <label vid='151'/> <var sort='x' vid='150' num='pl'/> </ep>
          <ep cfrom='149' cto='156'> <realpred lemma='friend' pos='n'/> <label vid='149'/> <var sort='x' vid='150' num='pl'/> </ep>
          <ep cfrom='157' cto='160'> <realpred lemma='and' pos='c'/> <label vid='159'/> <var sort='u' vid='160'/> </ep>
          <ep cfrom='161' cto='168'> <realpred lemma='promote' pos='v'/> <label vid='161'/> <var sort='e' vid='162'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>def_explicit_q_rel</gpred> <label vid='165'/> <var sort='x' vid='164' num='sg'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>poss_rel</gpred> <label vid='163'/> <var sort='e' vid='166'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pronoun_q_rel</gpred> <label vid='167'/> <var sort='x' vid='168'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pron_rel</gpred> <label vid='169'/> <var sort='x' vid='168'/> </ep>
          <ep cfrom='173' cto='179'> <realpred lemma='vision' pos='n'/> <label vid='172'/> <var sort='x' vid='164' num='sg'/> </ep>
          <ep cfrom='180' cto='205'> <gpred>implicit_q_rel</gpred> <label vid='190'/> <var sort='x' vid='181' num='sg'/> </ep>
          <ep cfrom='180' cto='182'> <realpred lemma='of' pos='p'/> <label vid='174'/> <var sort='e' vid='175'/> </ep>
          <ep cfrom='183' cto='195'> <realpred lemma='21st-century' pos='j'/> <label vid='176'/> <var sort='u' vid='177'/> </ep>
          <ep cfrom='196' cto='205'> <realpred lemma='socialism' pos='n'/> <label vid='182'/> <var sort='x' vid='181' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='16'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='49'/> </hi>   <lo> <label vid='45'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='116'/> </hi>   <lo> <label vid='114'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='80'/> </hi>   <lo> <label vid='78'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='90'/> </hi>   <lo> <label vid='88'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='142'/> </hi>   <lo> <label vid='130'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='136'/> </hi>   <lo> <label vid='126'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='153'/> </hi>   <lo> <label vid='149'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='206'/> </hi>   <lo> <label vid='172'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='170'/> </hi>   <lo> <label vid='169'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='192'/> </hi>   <lo> <label vid='182'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='10'/> <var sort='x' vid='4' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='8'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='e' vid='11'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='54'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='54'/> <var sort='x' vid='46' num='pl'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='14'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='17'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='17'/> <var sort='h' vid='19'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='16'/> <constant>argentina</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='26'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='47'/> <var sort='h' vid='49'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='47'/> <var sort='h' vid='50'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='119'/> <var sort='x' vid='104' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='113'/> <var sort='h' vid='116'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='113'/> <var sort='h' vid='117'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='114'/> <var sort='x' vid='104' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='114'/> <var sort='x' vid='77' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='79'/> <var sort='h' vid='80'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='79'/> <var sort='h' vid='81'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='78'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='89'/> <var sort='h' vid='90'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='89'/> <var sort='h' vid='91'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='88'/> <constant>venezuela</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='99'/> <var sort='x' vid='104' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='121'/> <var sort='x' vid='124' num='sg'/> </rarg>
          <rarg> <rargname>ARG3</rargname> <label vid='121'/> <var sort='h' vid='161'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='123'/> <var sort='h' vid='142'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='123'/> <var sort='h' vid='143'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='130'/> <var sort='x' vid='124' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='130'/> <var sort='x' vid='127' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='134'/> <var sort='h' vid='136'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='134'/> <var sort='h' vid='137'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='161'/> <var sort='u' vid='220'/> </rarg>
          <rarg> <rargname>L-HNDL</rargname> <label vid='161'/> <var sort='h' vid='147'/> </rarg>
          <rarg> <rargname>L-INDEX</rargname> <label vid='161'/> <var sort='e' vid='148'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='147'/> <var sort='x' vid='216'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='147'/> <var sort='x' vid='150' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='151'/> <var sort='h' vid='153'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='151'/> <var sort='h' vid='154'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='161'/> <var sort='x' vid='164' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='163'/> <var sort='h' vid='206'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='163'/> <var sort='h' vid='207'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='163'/> <var sort='x' vid='164' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='163'/> <var sort='x' vid='168'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='167'/> <var sort='h' vid='170'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='167'/> <var sort='h' vid='171'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='172'/> <var sort='x' vid='174'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='190'/> <var sort='h' vid='192'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='190'/> <var sort='h' vid='193'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='174'/> <var sort='x' vid='181' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='176'/> <var sort='x' vid='181' num='sg'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='10'/> </ing-a>   <ing-b> <var sort='h' vid='12'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='54'/> </ing-a>   <ing-b> <var sort='h' vid='40'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='14'/> </ing-a>   <ing-b> <var sort='h' vid='26'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='105'/> </ing-a>   <ing-b> <var sort='h' vid='114'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='76'/> </ing-a>   <ing-b> <var sort='h' vid='86'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='105'/> </ing-a>   <ing-b> <var sort='h' vid='99'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='130'/> </ing-a>   <ing-b> <var sort='h' vid='128'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='172'/> </ing-a>   <ing-b> <var sort='h' vid='174'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='182'/> </ing-a>   <ing-b> <var sort='h' vid='176'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r1" source="v0" target="v35" cfrom="0" cto="206" deps="s1">
        <rmrs cfrom='0' cto='206'>
          <label vid='234'/>
          <ep cfrom='0' cto='2'> <realpred lemma='as' pos='x'/> <label vid='1'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='3' cto='10'> <gpred>udef_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='3' cto='10'> <realpred lemma='leader' pos='n'/> <label vid='3'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='11' cto='17'> <realpred lemma='gather' pos='v'/> <label vid='10'/> <var sort='e' vid='11'/> </ep>
          <ep cfrom='18' cto='20'> <realpred lemma='in' pos='p'/> <label vid='12'/> <var sort='e' vid='13'/> </ep>
          <ep cfrom='21' cto='68'> <gpred>appos_rel</gpred> <label vid='54'/> <var sort='e' vid='55'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>proper_q_rel</gpred> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>named_rel</gpred> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='31' cto='36'> <realpred lemma='ahead' pos='r'/> <label vid='20'/> <var sort='e' vid='21'/> </ep>
          <ep cfrom='37' cto='39'> <realpred lemma='of' pos='p'/> <label vid='26'/> <var sort='e' vid='27'/> </ep>
          <ep cfrom='40' cto='44'> <realpred lemma='this' pos='q'/> <label vid='30'/> <var sort='x' vid='29'/> </ep>
          <ep cfrom='45' cto='53'> <realpred lemma='weekend' pos='n'/> <label vid='31'/> <var sort='x' vid='32'/> </ep>
          <ep cfrom='54' cto='62'> <realpred lemma='regional' pos='j'/> <label vid='33'/> <var sort='e' vid='34'/> </ep>
          <ep cfrom='63' cto='68'> <gpred>udef_q_rel</gpred> <label vid='47'/> <var sort='x' vid='46' num='pl'/> </ep>
          <ep cfrom='63' cto='68'> <realpred lemma='talk' pos='n'/> <label vid='45'/> <var sort='x' vid='46' num='pl'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>def_explicit_q_rel</gpred> <label vid='113'/> <var sort='x' vid='104' num='sg'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>poss_rel</gpred> <label vid='114'/> <var sort='u' vid='115'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>proper_q_rel</gpred> <label vid='79'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>named_rel</gpred> <label vid='78'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='75' cto='81'> <realpred lemma='chávez' pos='v'/> <label vid='82'/> <var sort='e' vid='83'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>proper_q_rel</gpred> <label vid='89'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>named_rel</gpred> <label vid='88'/> <var sort='x' vid='77' num='sg'/> </ep>
          <ep cfrom='95' cto='103'> <realpred lemma='populist' pos='j'/> <label vid='99'/> <var sort='e' vid='100'/> </ep>
          <ep cfrom='104' cto='113'> <realpred lemma='president' pos='n'/> <label vid='105'/> <var sort='x' vid='106' num='sg'/> </ep>
          <ep cfrom='117' cto='122'> <realpred lemma='use' pos='v'/> <label vid='121'/> <var sort='e' vid='122'/> </ep>
          <ep cfrom='123' cto='125'> <realpred lemma='an' pos='q'/> <label vid='125'/> <var sort='x' vid='124' num='sg'/> </ep>
          <ep cfrom='126' cto='205'> <gpred>compound_rel</gpred> <label vid='209'/> <var sort='e' vid='212'/> </ep>
          <ep cfrom='126' cto='205'> <gpred>udef_q_rel</gpred> <label vid='213'/> <var sort='x' vid='127' num='sg'/> </ep>
          <ep cfrom='126' cto='132'> <realpred lemma='energy' pos='n'/> <label vid='126'/> <var sort='x' vid='127' num='sg'/> </ep>
          <ep cfrom='133' cto='141'> <realpred lemma='windfall' pos='n'/> <label vid='128'/> <var sort='x' vid='124' num='sg'/> </ep>
          <ep cfrom='145' cto='148'> <realpred lemma='win' pos='v'/> <label vid='132'/> <var sort='e' vid='133'/> </ep>
          <ep cfrom='149' cto='156'> <gpred>udef_q_rel</gpred> <label vid='136'/> <var sort='x' vid='135' num='pl'/> </ep>
          <ep cfrom='149' cto='156'> <realpred lemma='friend' pos='n'/> <label vid='134'/> <var sort='x' vid='135' num='pl'/> </ep>
          <ep cfrom='157' cto='160'> <realpred lemma='and' pos='c'/> <label vid='144'/> <var sort='u' vid='145'/> </ep>
          <ep cfrom='161' cto='168'> <realpred lemma='promote' pos='v'/> <label vid='146'/> <var sort='e' vid='147'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>def_explicit_q_rel</gpred> <label vid='150'/> <var sort='x' vid='149' num='sg'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>poss_rel</gpred> <label vid='148'/> <var sort='e' vid='151'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pronoun_q_rel</gpred> <label vid='152'/> <var sort='x' vid='153'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pron_rel</gpred> <label vid='154'/> <var sort='x' vid='153'/> </ep>
          <ep cfrom='173' cto='179'> <realpred lemma='vision' pos='n'/> <label vid='157'/> <var sort='x' vid='149' num='sg'/> </ep>
          <ep cfrom='180' cto='205'> <gpred>implicit_q_rel</gpred> <label vid='175'/> <var sort='x' vid='166' num='sg'/> </ep>
          <ep cfrom='180' cto='182'> <realpred lemma='of' pos='p'/> <label vid='159'/> <var sort='e' vid='160'/> </ep>
          <ep cfrom='183' cto='195'> <realpred lemma='21st-century' pos='j'/> <label vid='161'/> <var sort='u' vid='162'/> </ep>
          <ep cfrom='196' cto='205'> <realpred lemma='socialism' pos='n'/> <label vid='167'/> <var sort='x' vid='166' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='16'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='49'/> </hi>   <lo> <label vid='45'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='116'/> </hi>   <lo> <label vid='114'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='80'/> </hi>   <lo> <label vid='78'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='90'/> </hi>   <lo> <label vid='88'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='221'/> </hi>   <lo> <label vid='209'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='215'/> </hi>   <lo> <label vid='126'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='138'/> </hi>   <lo> <label vid='134'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='191'/> </hi>   <lo> <label vid='157'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='155'/> </hi>   <lo> <label vid='154'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='177'/> </hi>   <lo> <label vid='167'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='10'/> <var sort='x' vid='4' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='8'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='e' vid='11'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='54'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='54'/> <var sort='x' vid='46' num='pl'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='14'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='17'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='17'/> <var sort='h' vid='19'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='16'/> <constant>argentina</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='26'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='47'/> <var sort='h' vid='49'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='47'/> <var sort='h' vid='50'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='119'/> <var sort='x' vid='104' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='113'/> <var sort='h' vid='116'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='113'/> <var sort='h' vid='117'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='114'/> <var sort='x' vid='104' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='114'/> <var sort='x' vid='77' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='79'/> <var sort='h' vid='80'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='79'/> <var sort='h' vid='81'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='78'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='89'/> <var sort='h' vid='90'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='89'/> <var sort='h' vid='91'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='88'/> <constant>venezuela</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='99'/> <var sort='x' vid='104' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='121'/> <var sort='x' vid='124' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='123'/> <var sort='h' vid='221'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='123'/> <var sort='h' vid='222'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='209'/> <var sort='x' vid='124' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='209'/> <var sort='x' vid='127' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='213'/> <var sort='h' vid='215'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='213'/> <var sort='h' vid='216'/> </rarg>
          <rarg> <rargname>ARGN</rargname> <label vid='146'/> <var sort='x' vid='124' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='146'/> <var sort='u' vid='205'/> </rarg>
          <rarg> <rargname>L-HNDL</rargname> <label vid='146'/> <var sort='h' vid='132'/> </rarg>
          <rarg> <rargname>L-INDEX</rargname> <label vid='146'/> <var sort='e' vid='133'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='132'/> <var sort='x' vid='201'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='132'/> <var sort='x' vid='135' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='136'/> <var sort='h' vid='138'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='136'/> <var sort='h' vid='139'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='146'/> <var sort='x' vid='149' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='148'/> <var sort='h' vid='191'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='148'/> <var sort='h' vid='192'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='148'/> <var sort='x' vid='149' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='148'/> <var sort='x' vid='153'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='152'/> <var sort='h' vid='155'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='152'/> <var sort='h' vid='156'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='157'/> <var sort='x' vid='159'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='175'/> <var sort='h' vid='177'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='175'/> <var sort='h' vid='178'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='159'/> <var sort='x' vid='166' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='161'/> <var sort='x' vid='166' num='sg'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='10'/> </ing-a>   <ing-b> <var sort='h' vid='12'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='54'/> </ing-a>   <ing-b> <var sort='h' vid='40'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='14'/> </ing-a>   <ing-b> <var sort='h' vid='26'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='105'/> </ing-a>   <ing-b> <var sort='h' vid='114'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='76'/> </ing-a>   <ing-b> <var sort='h' vid='86'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='105'/> </ing-a>   <ing-b> <var sort='h' vid='99'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='209'/> </ing-a>   <ing-b> <var sort='h' vid='128'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='157'/> </ing-a>   <ing-b> <var sort='h' vid='159'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='167'/> </ing-a>   <ing-b> <var sort='h' vid='161'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r2" source="v0" target="v35" cfrom="0" cto="206" deps="s2">
        <rmrs cfrom='0' cto='206'>
          <label vid='227'/>
          <ep cfrom='0' cto='2'> <realpred lemma='as' pos='x'/> <label vid='1'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='3' cto='10'> <gpred>udef_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='3' cto='10'> <realpred lemma='leader' pos='n'/> <label vid='3'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='11' cto='17'> <realpred lemma='gather' pos='v'/> <label vid='10'/> <var sort='e' vid='11'/> </ep>
          <ep cfrom='18' cto='20'> <realpred lemma='in' pos='p'/> <label vid='12'/> <var sort='e' vid='13'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>proper_q_rel</gpred> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>named_rel</gpred> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='31' cto='36'> <realpred lemma='ahead' pos='r'/> <label vid='20'/> <var sort='e' vid='21'/> </ep>
          <ep cfrom='37' cto='39'> <realpred lemma='of' pos='p'/> <label vid='26'/> <var sort='e' vid='27'/> </ep>
          <ep cfrom='40' cto='44'> <realpred lemma='this' pos='q'/> <label vid='30'/> <var sort='x' vid='29'/> </ep>
          <ep cfrom='45' cto='53'> <realpred lemma='weekend' pos='n'/> <label vid='31'/> <var sort='x' vid='32'/> </ep>
          <ep cfrom='54' cto='62'> <realpred lemma='regional' pos='j'/> <label vid='33'/> <var sort='e' vid='34'/> </ep>
          <ep cfrom='63' cto='68'> <gpred>udef_q_rel</gpred> <label vid='53'/> <var sort='x' vid='52' num='pl'/> </ep>
          <ep cfrom='63' cto='68'> <realpred lemma='talk' pos='n'/> <label vid='51'/> <var sort='x' vid='52' num='pl'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>def_explicit_q_rel</gpred> <label vid='108'/> <var sort='x' vid='99' num='sg'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>poss_rel</gpred> <label vid='109'/> <var sort='u' vid='110'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>proper_q_rel</gpred> <label vid='74'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>named_rel</gpred> <label vid='73'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='75' cto='81'> <realpred lemma='chávez' pos='v'/> <label vid='77'/> <var sort='e' vid='78'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>proper_q_rel</gpred> <label vid='84'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>named_rel</gpred> <label vid='83'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='95' cto='103'> <realpred lemma='populist' pos='j'/> <label vid='94'/> <var sort='e' vid='95'/> </ep>
          <ep cfrom='104' cto='113'> <realpred lemma='president' pos='n'/> <label vid='100'/> <var sort='x' vid='101' num='sg'/> </ep>
          <ep cfrom='117' cto='122'> <realpred lemma='use' pos='v'/> <label vid='116'/> <var sort='e' vid='117'/> </ep>
          <ep cfrom='123' cto='125'> <realpred lemma='an' pos='q'/> <label vid='120'/> <var sort='x' vid='119' num='sg'/> </ep>
          <ep cfrom='126' cto='141'> <gpred>compound_rel</gpred> <label vid='125'/> <var sort='e' vid='128'/> </ep>
          <ep cfrom='126' cto='141'> <gpred>udef_q_rel</gpred> <label vid='129'/> <var sort='x' vid='122' num='sg'/> </ep>
          <ep cfrom='126' cto='132'> <realpred lemma='energy' pos='n'/> <label vid='121'/> <var sort='x' vid='122' num='sg'/> </ep>
          <ep cfrom='133' cto='141'> <realpred lemma='windfall' pos='n'/> <label vid='123'/> <var sort='x' vid='119' num='sg'/> </ep>
          <ep cfrom='145' cto='148'> <realpred lemma='win' pos='v'/> <label vid='142'/> <var sort='e' vid='143'/> </ep>
          <ep cfrom='149' cto='156'> <gpred>udef_q_rel</gpred> <label vid='146'/> <var sort='x' vid='145' num='pl'/> </ep>
          <ep cfrom='149' cto='156'> <realpred lemma='friend' pos='n'/> <label vid='144'/> <var sort='x' vid='145' num='pl'/> </ep>
          <ep cfrom='157' cto='160'> <realpred lemma='and' pos='c'/> <label vid='154'/> <var sort='u' vid='155'/> </ep>
          <ep cfrom='161' cto='168'> <realpred lemma='promote' pos='v'/> <label vid='156'/> <var sort='e' vid='157'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>def_explicit_q_rel</gpred> <label vid='160'/> <var sort='x' vid='159' num='sg'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>poss_rel</gpred> <label vid='158'/> <var sort='e' vid='161'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pronoun_q_rel</gpred> <label vid='162'/> <var sort='x' vid='163'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pron_rel</gpred> <label vid='164'/> <var sort='x' vid='163'/> </ep>
          <ep cfrom='173' cto='179'> <realpred lemma='vision' pos='n'/> <label vid='167'/> <var sort='x' vid='159' num='sg'/> </ep>
          <ep cfrom='180' cto='205'> <gpred>implicit_q_rel</gpred> <label vid='185'/> <var sort='x' vid='176' num='sg'/> </ep>
          <ep cfrom='180' cto='182'> <realpred lemma='of' pos='p'/> <label vid='169'/> <var sort='e' vid='170'/> </ep>
          <ep cfrom='183' cto='195'> <realpred lemma='21st-century' pos='j'/> <label vid='171'/> <var sort='u' vid='172'/> </ep>
          <ep cfrom='196' cto='205'> <realpred lemma='socialism' pos='n'/> <label vid='177'/> <var sort='x' vid='176' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='16'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='55'/> </hi>   <lo> <label vid='51'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='111'/> </hi>   <lo> <label vid='109'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='75'/> </hi>   <lo> <label vid='73'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='85'/> </hi>   <lo> <label vid='83'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='137'/> </hi>   <lo> <label vid='125'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='131'/> </hi>   <lo> <label vid='121'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='148'/> </hi>   <lo> <label vid='144'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='201'/> </hi>   <lo> <label vid='167'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='165'/> </hi>   <lo> <label vid='164'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='187'/> </hi>   <lo> <label vid='177'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='10'/> <var sort='x' vid='4' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='8'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='e' vid='11'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='52' num='pl'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10'/> <var sort='x' vid='52' num='pl'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='14'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='17'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='17'/> <var sort='h' vid='19'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='16'/> <constant>argentina</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='26'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='53'/> <var sort='h' vid='55'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='53'/> <var sort='h' vid='56'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='114'/> <var sort='x' vid='99' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='108'/> <var sort='h' vid='111'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='108'/> <var sort='h' vid='112'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='109'/> <var sort='x' vid='99' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='109'/> <var sort='x' vid='72' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='74'/> <var sort='h' vid='75'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='74'/> <var sort='h' vid='76'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='73'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='84'/> <var sort='h' vid='85'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='84'/> <var sort='h' vid='86'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='83'/> <constant>venezuela</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='94'/> <var sort='x' vid='99' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='116'/> <var sort='x' vid='119' num='sg'/> </rarg>
          <rarg> <rargname>ARG3</rargname> <label vid='116'/> <var sort='h' vid='156'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='118'/> <var sort='h' vid='137'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='118'/> <var sort='h' vid='138'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='125'/> <var sort='x' vid='119' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='125'/> <var sort='x' vid='122' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='129'/> <var sort='h' vid='131'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='129'/> <var sort='h' vid='132'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='156'/> <var sort='u' vid='215'/> </rarg>
          <rarg> <rargname>L-HNDL</rargname> <label vid='156'/> <var sort='h' vid='142'/> </rarg>
          <rarg> <rargname>L-INDEX</rargname> <label vid='156'/> <var sort='e' vid='143'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='142'/> <var sort='x' vid='211'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='142'/> <var sort='x' vid='145' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='146'/> <var sort='h' vid='148'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='146'/> <var sort='h' vid='149'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='156'/> <var sort='x' vid='159' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='158'/> <var sort='h' vid='201'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='158'/> <var sort='h' vid='202'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='158'/> <var sort='x' vid='159' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='158'/> <var sort='x' vid='163'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='162'/> <var sort='h' vid='165'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='162'/> <var sort='h' vid='166'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='167'/> <var sort='x' vid='169'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='185'/> <var sort='h' vid='187'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='185'/> <var sort='h' vid='188'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='169'/> <var sort='x' vid='176' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='171'/> <var sort='x' vid='176' num='sg'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='10'/> </ing-a>   <ing-b> <var sort='h' vid='12'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='14'/> </ing-a>   <ing-b> <var sort='h' vid='26'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='100'/> </ing-a>   <ing-b> <var sort='h' vid='109'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='71'/> </ing-a>   <ing-b> <var sort='h' vid='81'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='100'/> </ing-a>   <ing-b> <var sort='h' vid='94'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='125'/> </ing-a>   <ing-b> <var sort='h' vid='123'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='167'/> </ing-a>   <ing-b> <var sort='h' vid='169'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='177'/> </ing-a>   <ing-b> <var sort='h' vid='171'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r3" source="v0" target="v35" cfrom="0" cto="206" deps="s3">
        <rmrs cfrom='0' cto='206'>
          <label vid='236'/>
          <ep cfrom='0' cto='2'> <realpred lemma='as' pos='x'/> <label vid='1'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='3' cto='10'> <gpred>udef_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='3' cto='10'> <realpred lemma='leader' pos='n'/> <label vid='3'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='11' cto='17'> <realpred lemma='gather' pos='v'/> <label vid='10'/> <var sort='e' vid='11'/> </ep>
          <ep cfrom='18' cto='20'> <realpred lemma='in' pos='p'/> <label vid='14'/> <var sort='e' vid='15'/> </ep>
          <ep cfrom='21' cto='68'> <gpred>appos_rel</gpred> <label vid='56'/> <var sort='e' vid='57'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>proper_q_rel</gpred> <label vid='19'/> <var sort='x' vid='17' num='sg'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>named_rel</gpred> <label vid='18'/> <var sort='x' vid='17' num='sg'/> </ep>
          <ep cfrom='31' cto='36'> <realpred lemma='ahead' pos='r'/> <label vid='22'/> <var sort='e' vid='23'/> </ep>
          <ep cfrom='37' cto='39'> <realpred lemma='of' pos='p'/> <label vid='28'/> <var sort='e' vid='29'/> </ep>
          <ep cfrom='40' cto='44'> <realpred lemma='this' pos='q'/> <label vid='32'/> <var sort='x' vid='31'/> </ep>
          <ep cfrom='45' cto='53'> <realpred lemma='weekend' pos='n'/> <label vid='33'/> <var sort='x' vid='34'/> </ep>
          <ep cfrom='54' cto='62'> <realpred lemma='regional' pos='j'/> <label vid='35'/> <var sort='e' vid='36'/> </ep>
          <ep cfrom='63' cto='68'> <gpred>udef_q_rel</gpred> <label vid='49'/> <var sort='x' vid='48' num='pl'/> </ep>
          <ep cfrom='63' cto='68'> <realpred lemma='talk' pos='n'/> <label vid='47'/> <var sort='x' vid='48' num='pl'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>def_explicit_q_rel</gpred> <label vid='117'/> <var sort='x' vid='108' num='sg'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>poss_rel</gpred> <label vid='118'/> <var sort='u' vid='119'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>proper_q_rel</gpred> <label vid='83'/> <var sort='x' vid='81' num='sg'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>named_rel</gpred> <label vid='82'/> <var sort='x' vid='81' num='sg'/> </ep>
          <ep cfrom='75' cto='81'> <realpred lemma='chávez' pos='v'/> <label vid='86'/> <var sort='e' vid='87'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>proper_q_rel</gpred> <label vid='93'/> <var sort='x' vid='81' num='sg'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>named_rel</gpred> <label vid='92'/> <var sort='x' vid='81' num='sg'/> </ep>
          <ep cfrom='95' cto='103'> <realpred lemma='populist' pos='j'/> <label vid='103'/> <var sort='e' vid='104'/> </ep>
          <ep cfrom='104' cto='113'> <realpred lemma='president' pos='n'/> <label vid='109'/> <var sort='x' vid='110' num='sg'/> </ep>
          <ep cfrom='117' cto='122'> <realpred lemma='use' pos='v'/> <label vid='125'/> <var sort='e' vid='126'/> </ep>
          <ep cfrom='123' cto='125'> <realpred lemma='an' pos='q'/> <label vid='129'/> <var sort='x' vid='128' num='sg'/> </ep>
          <ep cfrom='126' cto='141'> <gpred>compound_rel</gpred> <label vid='134'/> <var sort='e' vid='137'/> </ep>
          <ep cfrom='126' cto='141'> <gpred>udef_q_rel</gpred> <label vid='138'/> <var sort='x' vid='131' num='sg'/> </ep>
          <ep cfrom='126' cto='132'> <realpred lemma='energy' pos='n'/> <label vid='130'/> <var sort='x' vid='131' num='sg'/> </ep>
          <ep cfrom='133' cto='141'> <realpred lemma='windfall' pos='n'/> <label vid='132'/> <var sort='x' vid='128' num='sg'/> </ep>
          <ep cfrom='145' cto='148'> <realpred lemma='win' pos='v'/> <label vid='151'/> <var sort='e' vid='152'/> </ep>
          <ep cfrom='149' cto='156'> <gpred>udef_q_rel</gpred> <label vid='155'/> <var sort='x' vid='154' num='pl'/> </ep>
          <ep cfrom='149' cto='156'> <realpred lemma='friend' pos='n'/> <label vid='153'/> <var sort='x' vid='154' num='pl'/> </ep>
          <ep cfrom='157' cto='160'> <realpred lemma='and' pos='c'/> <label vid='163'/> <var sort='u' vid='164'/> </ep>
          <ep cfrom='161' cto='168'> <realpred lemma='promote' pos='v'/> <label vid='165'/> <var sort='e' vid='166'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>def_explicit_q_rel</gpred> <label vid='169'/> <var sort='x' vid='168' num='sg'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>poss_rel</gpred> <label vid='167'/> <var sort='e' vid='170'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pronoun_q_rel</gpred> <label vid='171'/> <var sort='x' vid='172'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pron_rel</gpred> <label vid='173'/> <var sort='x' vid='172'/> </ep>
          <ep cfrom='173' cto='179'> <realpred lemma='vision' pos='n'/> <label vid='176'/> <var sort='x' vid='168' num='sg'/> </ep>
          <ep cfrom='180' cto='205'> <gpred>implicit_q_rel</gpred> <label vid='194'/> <var sort='x' vid='185' num='sg'/> </ep>
          <ep cfrom='180' cto='182'> <realpred lemma='of' pos='p'/> <label vid='178'/> <var sort='e' vid='179'/> </ep>
          <ep cfrom='183' cto='195'> <realpred lemma='21st-century' pos='j'/> <label vid='180'/> <var sort='u' vid='181'/> </ep>
          <ep cfrom='196' cto='205'> <realpred lemma='socialism' pos='n'/> <label vid='186'/> <var sort='x' vid='185' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='20'/> </hi>   <lo> <label vid='18'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='51'/> </hi>   <lo> <label vid='47'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='120'/> </hi>   <lo> <label vid='118'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='84'/> </hi>   <lo> <label vid='82'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='94'/> </hi>   <lo> <label vid='92'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='146'/> </hi>   <lo> <label vid='134'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='140'/> </hi>   <lo> <label vid='130'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='157'/> </hi>   <lo> <label vid='153'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='210'/> </hi>   <lo> <label vid='176'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='174'/> </hi>   <lo> <label vid='173'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='196'/> </hi>   <lo> <label vid='186'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='10'/> <var sort='x' vid='4' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='8'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='14'/> <var sort='e' vid='11'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='14'/> <var sort='x' vid='17' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='56'/> <var sort='x' vid='17' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='56'/> <var sort='x' vid='48' num='pl'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='16'/> <var sort='x' vid='31'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='19'/> <var sort='h' vid='20'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='19'/> <var sort='h' vid='21'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='18'/> <constant>argentina</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='28'/> <var sort='x' vid='31'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='49'/> <var sort='h' vid='51'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='49'/> <var sort='h' vid='52'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='123'/> <var sort='x' vid='108' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='117'/> <var sort='h' vid='120'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='117'/> <var sort='h' vid='121'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='118'/> <var sort='x' vid='108' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='118'/> <var sort='x' vid='81' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='83'/> <var sort='h' vid='84'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='83'/> <var sort='h' vid='85'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='82'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='93'/> <var sort='h' vid='94'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='93'/> <var sort='h' vid='95'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='92'/> <constant>venezuela</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='103'/> <var sort='x' vid='108' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='125'/> <var sort='x' vid='128' num='sg'/> </rarg>
          <rarg> <rargname>ARG3</rargname> <label vid='125'/> <var sort='h' vid='165'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='127'/> <var sort='h' vid='146'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='127'/> <var sort='h' vid='147'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='134'/> <var sort='x' vid='128' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='134'/> <var sort='x' vid='131' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='138'/> <var sort='h' vid='140'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='138'/> <var sort='h' vid='141'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='165'/> <var sort='u' vid='224'/> </rarg>
          <rarg> <rargname>L-HNDL</rargname> <label vid='165'/> <var sort='h' vid='151'/> </rarg>
          <rarg> <rargname>L-INDEX</rargname> <label vid='165'/> <var sort='e' vid='152'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='151'/> <var sort='x' vid='220'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='151'/> <var sort='x' vid='154' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='155'/> <var sort='h' vid='157'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='155'/> <var sort='h' vid='158'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='165'/> <var sort='x' vid='168' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='167'/> <var sort='h' vid='210'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='167'/> <var sort='h' vid='211'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='167'/> <var sort='x' vid='168' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='167'/> <var sort='x' vid='172'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='171'/> <var sort='h' vid='174'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='171'/> <var sort='h' vid='175'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='176'/> <var sort='x' vid='178'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='194'/> <var sort='h' vid='196'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='194'/> <var sort='h' vid='197'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='178'/> <var sort='x' vid='185' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='180'/> <var sort='x' vid='185' num='sg'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='10'/> </ing-a>   <ing-b> <var sort='h' vid='14'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='56'/> </ing-a>   <ing-b> <var sort='h' vid='42'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='16'/> </ing-a>   <ing-b> <var sort='h' vid='28'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='109'/> </ing-a>   <ing-b> <var sort='h' vid='118'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='80'/> </ing-a>   <ing-b> <var sort='h' vid='90'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='109'/> </ing-a>   <ing-b> <var sort='h' vid='103'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='134'/> </ing-a>   <ing-b> <var sort='h' vid='132'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='176'/> </ing-a>   <ing-b> <var sort='h' vid='178'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='186'/> </ing-a>   <ing-b> <var sort='h' vid='180'/> </ing-b>   </ing>
        </rmrs>
      </edge>
      <edge type="rmrs" id="r4" source="v0" target="v35" cfrom="0" cto="206" deps="s4">
        <rmrs cfrom='0' cto='206'>
          <label vid='229'/>
          <ep cfrom='0' cto='2'> <realpred lemma='as' pos='x'/> <label vid='1'/> <var sort='e' vid='2'/> </ep>
          <ep cfrom='3' cto='10'> <gpred>udef_q_rel</gpred> <label vid='5'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='3' cto='10'> <realpred lemma='leader' pos='n'/> <label vid='3'/> <var sort='x' vid='4' num='pl'/> </ep>
          <ep cfrom='11' cto='17'> <realpred lemma='gather' pos='v'/> <label vid='10'/> <var sort='e' vid='11'/> </ep>
          <ep cfrom='18' cto='20'> <realpred lemma='in' pos='p'/> <label vid='12'/> <var sort='e' vid='13'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>proper_q_rel</gpred> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='21' cto='30'> <gpred>named_rel</gpred> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='31' cto='36'> <realpred lemma='ahead' pos='r'/> <label vid='20'/> <var sort='e' vid='21'/> </ep>
          <ep cfrom='37' cto='39'> <realpred lemma='of' pos='p'/> <label vid='26'/> <var sort='e' vid='27'/> </ep>
          <ep cfrom='40' cto='44'> <realpred lemma='this' pos='q'/> <label vid='30'/> <var sort='x' vid='29'/> </ep>
          <ep cfrom='45' cto='53'> <realpred lemma='weekend' pos='n'/> <label vid='31'/> <var sort='x' vid='32'/> </ep>
          <ep cfrom='54' cto='62'> <realpred lemma='regional' pos='j'/> <label vid='33'/> <var sort='e' vid='34'/> </ep>
          <ep cfrom='63' cto='68'> <gpred>udef_q_rel</gpred> <label vid='53'/> <var sort='x' vid='52' num='pl'/> </ep>
          <ep cfrom='63' cto='68'> <realpred lemma='talk' pos='n'/> <label vid='51'/> <var sort='x' vid='52' num='pl'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>def_explicit_q_rel</gpred> <label vid='108'/> <var sort='x' vid='99' num='sg'/> </ep>
          <ep cfrom='70' cto='113'> <gpred>poss_rel</gpred> <label vid='109'/> <var sort='u' vid='110'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>proper_q_rel</gpred> <label vid='74'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='70' cto='74'> <gpred>named_rel</gpred> <label vid='73'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='75' cto='81'> <realpred lemma='chávez' pos='v'/> <label vid='77'/> <var sort='e' vid='78'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>proper_q_rel</gpred> <label vid='84'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='83' cto='92'> <gpred>named_rel</gpred> <label vid='83'/> <var sort='x' vid='72' num='sg'/> </ep>
          <ep cfrom='95' cto='103'> <realpred lemma='populist' pos='j'/> <label vid='94'/> <var sort='e' vid='95'/> </ep>
          <ep cfrom='104' cto='113'> <realpred lemma='president' pos='n'/> <label vid='100'/> <var sort='x' vid='101' num='sg'/> </ep>
          <ep cfrom='117' cto='122'> <realpred lemma='use' pos='v'/> <label vid='116'/> <var sort='e' vid='117'/> </ep>
          <ep cfrom='123' cto='125'> <realpred lemma='an' pos='q'/> <label vid='120'/> <var sort='x' vid='119' num='sg'/> </ep>
          <ep cfrom='126' cto='205'> <gpred>compound_rel</gpred> <label vid='204'/> <var sort='e' vid='207'/> </ep>
          <ep cfrom='126' cto='205'> <gpred>udef_q_rel</gpred> <label vid='208'/> <var sort='x' vid='122' num='sg'/> </ep>
          <ep cfrom='126' cto='132'> <realpred lemma='energy' pos='n'/> <label vid='121'/> <var sort='x' vid='122' num='sg'/> </ep>
          <ep cfrom='133' cto='141'> <realpred lemma='windfall' pos='n'/> <label vid='123'/> <var sort='x' vid='119' num='sg'/> </ep>
          <ep cfrom='145' cto='148'> <realpred lemma='win' pos='v'/> <label vid='127'/> <var sort='e' vid='128'/> </ep>
          <ep cfrom='149' cto='156'> <gpred>udef_q_rel</gpred> <label vid='131'/> <var sort='x' vid='130' num='pl'/> </ep>
          <ep cfrom='149' cto='156'> <realpred lemma='friend' pos='n'/> <label vid='129'/> <var sort='x' vid='130' num='pl'/> </ep>
          <ep cfrom='157' cto='160'> <realpred lemma='and' pos='c'/> <label vid='139'/> <var sort='u' vid='140'/> </ep>
          <ep cfrom='161' cto='168'> <realpred lemma='promote' pos='v'/> <label vid='141'/> <var sort='e' vid='142'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>def_explicit_q_rel</gpred> <label vid='145'/> <var sort='x' vid='144' num='sg'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>poss_rel</gpred> <label vid='143'/> <var sort='e' vid='146'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pronoun_q_rel</gpred> <label vid='147'/> <var sort='x' vid='148'/> </ep>
          <ep cfrom='169' cto='172'> <gpred>pron_rel</gpred> <label vid='149'/> <var sort='x' vid='148'/> </ep>
          <ep cfrom='173' cto='179'> <realpred lemma='vision' pos='n'/> <label vid='152'/> <var sort='x' vid='144' num='sg'/> </ep>
          <ep cfrom='180' cto='205'> <gpred>implicit_q_rel</gpred> <label vid='170'/> <var sort='x' vid='161' num='sg'/> </ep>
          <ep cfrom='180' cto='182'> <realpred lemma='of' pos='p'/> <label vid='154'/> <var sort='e' vid='155'/> </ep>
          <ep cfrom='183' cto='195'> <realpred lemma='21st-century' pos='j'/> <label vid='156'/> <var sort='u' vid='157'/> </ep>
          <ep cfrom='196' cto='205'> <realpred lemma='socialism' pos='n'/> <label vid='162'/> <var sort='x' vid='161' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='7'/> </hi>   <lo> <label vid='3'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='18'/> </hi>   <lo> <label vid='16'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='55'/> </hi>   <lo> <label vid='51'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='111'/> </hi>   <lo> <label vid='109'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='75'/> </hi>   <lo> <label vid='73'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='85'/> </hi>   <lo> <label vid='83'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='216'/> </hi>   <lo> <label vid='204'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='210'/> </hi>   <lo> <label vid='121'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='133'/> </hi>   <lo> <label vid='129'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='186'/> </hi>   <lo> <label vid='152'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='150'/> </hi>   <lo> <label vid='149'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='172'/> </hi>   <lo> <label vid='162'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='10'/> <var sort='x' vid='4' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='5'/> <var sort='h' vid='7'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='5'/> <var sort='h' vid='8'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='e' vid='11'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='52' num='pl'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='10'/> <var sort='x' vid='52' num='pl'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='14'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='17'/> <var sort='h' vid='18'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='17'/> <var sort='h' vid='19'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='16'/> <constant>argentina</constant> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='26'/> <var sort='x' vid='29'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='53'/> <var sort='h' vid='55'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='53'/> <var sort='h' vid='56'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='114'/> <var sort='x' vid='99' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='108'/> <var sort='h' vid='111'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='108'/> <var sort='h' vid='112'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='109'/> <var sort='x' vid='99' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='109'/> <var sort='x' vid='72' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='74'/> <var sort='h' vid='75'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='74'/> <var sort='h' vid='76'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='73'/> <constant>hugo</constant> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='84'/> <var sort='h' vid='85'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='84'/> <var sort='h' vid='86'/> </rarg>
          <rarg> <rargname>CARG</rargname> <label vid='83'/> <constant>venezuela</constant> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='94'/> <var sort='x' vid='99' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='116'/> <var sort='x' vid='119' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='118'/> <var sort='h' vid='216'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='118'/> <var sort='h' vid='217'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='204'/> <var sort='x' vid='119' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='204'/> <var sort='x' vid='122' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='208'/> <var sort='h' vid='210'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='208'/> <var sort='h' vid='211'/> </rarg>
          <rarg> <rargname>ARGN</rargname> <label vid='141'/> <var sort='x' vid='119' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='141'/> <var sort='u' vid='200'/> </rarg>
          <rarg> <rargname>L-HNDL</rargname> <label vid='141'/> <var sort='h' vid='127'/> </rarg>
          <rarg> <rargname>L-INDEX</rargname> <label vid='141'/> <var sort='e' vid='128'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='127'/> <var sort='x' vid='196'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='127'/> <var sort='x' vid='130' num='pl'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='131'/> <var sort='h' vid='133'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='131'/> <var sort='h' vid='134'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='141'/> <var sort='x' vid='144' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='143'/> <var sort='h' vid='186'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='143'/> <var sort='h' vid='187'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='143'/> <var sort='x' vid='144' num='sg'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='143'/> <var sort='x' vid='148'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='147'/> <var sort='h' vid='150'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='147'/> <var sort='h' vid='151'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='152'/> <var sort='x' vid='154'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='170'/> <var sort='h' vid='172'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='170'/> <var sort='h' vid='173'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='154'/> <var sort='x' vid='161' num='sg'/> </rarg>
          <rarg> <rargname>ARG1</rargname> <label vid='156'/> <var sort='x' vid='161' num='sg'/> </rarg>
          <ing>   <ing-a> <var sort='h' vid='10'/> </ing-a>   <ing-b> <var sort='h' vid='12'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='14'/> </ing-a>   <ing-b> <var sort='h' vid='26'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='100'/> </ing-a>   <ing-b> <var sort='h' vid='109'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='71'/> </ing-a>   <ing-b> <var sort='h' vid='81'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='100'/> </ing-a>   <ing-b> <var sort='h' vid='94'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='204'/> </ing-a>   <ing-b> <var sort='h' vid='123'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='152'/> </ing-a>   <ing-b> <var sort='h' vid='154'/> </ing-b>   </ing>
          <ing>   <ing-a> <var sort='h' vid='162'/> </ing-a>   <ing-b> <var sort='h' vid='156'/> </ing-b>   </ing>
        </rmrs>
      </edge>
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>The cat chased the dog.</text>
    <lattice init="v0" final="v6" cfrom="0" cto="23">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="4" cto="7">cat</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="8" cto="14">chased</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="15" cto="18">the</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="19" cto="22">dog</edge>
      <edge type="token" id="t5" source="v5" target="v6" cfrom="22" cto="23">.</edge>
      <edge type="pos" id="p0" source="v0" target="v1" cfrom="0" cto="3" deps="t0">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p1" source="v1" target="v2" cfrom="4" cto="7" deps="t1">
        <slot name="tag">NN1</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p2" source="v2" target="v3" cfrom="8" cto="14" deps="t2">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.90372</slot>
      </edge>
      <edge type="pos" id="p3" source="v2" target="v3" cfrom="8" cto="14" deps="t2">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.0962799</slot>
      </edge>
      <edge type="pos" id="p4" source="v3" target="v4" cfrom="15" cto="18" deps="t3">
        <slot name="tag">AT</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="pos" id="p5" source="v4" target="v5" cfrom="19" cto="22" deps="t4">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.999833</slot>
      </edge>
      <edge type="pos" id="p6" source="v4" target="v5" cfrom="19" cto="22" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000166966</slot>
      </edge>
      <edge type="pos" id="p7" source="v5" target="v6" cfrom="22" cto="23" deps="t5">
        <slot name="tag">.</slot>
        <slot name="weight">1</slot>
      </edge>
      <edge type="morph" id="m1" source="v2" target="v3" cfrom="8" cto="14" deps="p2">chase+ed</edge>
      <edge type="morph" id="m2" source="v2" target="v3" cfrom="8" cto="14" deps="p3">chase+ed</edge>
      <edge type="syntree" id="s0" source="v0" target="v6" cfrom="0" cto="23">
        <slot name="weight">-4.679</slot>
        <slot name="tree">
          (|T/txt-sc1/-+|
           (|S/np_vp|
            (|NP/det_n1| |&lt;w s='0' e='3'&gt;The_AT&lt;/w&gt;|
             (|N1/n| |&lt;w s='4' e='7'&gt;cat_NN1&lt;/w&gt;|))
            (|V1/v_np| |&lt;w s='8' e='14'&gt;chase+ed_VVD&lt;/w&gt;|
             (|NP/det_n1| |&lt;w s='15' e='18'&gt;the_AT&lt;/w&gt;|
              (|N1/n| |&lt;w s='19' e='22'&gt;dog_NN1&lt;/w&gt;|))))
           (|End-punct3/-| |&lt;w s='22' e='23'&gt;._.&lt;/w&gt;|))
        </slot>
      </edge>
      <edge type="rmrs" id="r0" source="v0" target="v6" cfrom="0" cto="23" deps="s0">
        <rmrs cfrom='0' cto='23'>
          <label vid='35'/>
          <ep cfrom='0' cto='3'> <realpred lemma='the' pos='q'/> <label vid='3'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='4' cto='7'> <realpred lemma='cat' pos='n'/> <label vid='4'/> <var sort='x' vid='2' num='sg'/> </ep>
          <ep cfrom='8' cto='14'> <realpred lemma='chase' pos='v'/> <label vid='12'/> <var sort='e' vid='13' tense='past'/> </ep>
          <ep cfrom='15' cto='18'> <realpred lemma='the' pos='q'/> <label vid='16'/> <var sort='x' vid='15' num='sg'/> </ep>
          <ep cfrom='19' cto='22'> <realpred lemma='dog' pos='n'/> <label vid='17'/> <var sort='x' vid='15' num='sg'/> </ep>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='9'/> </hi>   <lo> <label vid='4'/> </lo>   </hcons>
          <hcons hreln='qeq'>   <hi> <var sort='h' vid='22'/> </hi>   <lo> <label vid='17'/> </lo>   </hcons>
          <rarg> <rargname>ARG1</rargname> <label vid='12'/> <var sort='x' vid='2' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='1'/> <var sort='h' vid='9'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='1'/> <var sort='h' vid='10'/> </rarg>
          <rarg> <rargname>ARG2</rargname> <label vid='12'/> <var sort='x' vid='15' num='sg'/> </rarg>
          <rarg> <rargname>RSTR</rargname> <label vid='14'/> <var sort='h' vid='22'/> </rarg>
          <rarg> <rargname>BODY</rargname> <label vid='14'/> <var sort='h' vid='23'/> </rarg>
        </rmrs>
      </edge>
    </lattice>
  </smaf>"""
];