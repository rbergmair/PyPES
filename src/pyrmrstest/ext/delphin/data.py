# -*- coding: utf-8 -*-



TEXT = [
  u"The dog barks.",
  u"I saw a man with a telescope.",
  u"As leaders gather in Argentina ahead of this "+
    u"weekends regional talks, Hugo Chávez, Venezuela's "+
    u"populist president is using an energy windfall to win "+
    u"friends and promote his vision of 21st-century socialism.",
  u"The cat chased the dog."
];



TOKENISED = [
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