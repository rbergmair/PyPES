# -*- coding: utf-8 -*-



ERG_TOKENISED = [
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
  </smaf>""",
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
  </smaf>"""
];



RASP_TAGGED = [
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
    </lattice>
  </smaf>""",
  u"""<smaf>
    <text>Hugo Chávez chased the dog</text>
    <lattice init="v0" final="v5" cfrom="0" cto="26">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="4">Hugo</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="5" cto="11">Chávez</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="12" cto="18">chased</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="19" cto="22">the</edge>
      <edge type="token" id="t4" source="v4" target="v5" cfrom="23" cto="26">dog</edge>
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
        <slot name="weight">0.997692</slot>
      </edge>
      <edge type="pos" id="p13" source="v4" target="v5" cfrom="23" cto="26" deps="t4">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00230797</slot>
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
        <slot name="weight">0.0337125</slot>
      </edge>
      <edge type="pos" id="p19" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.783491</slot>
      </edge>
      <edge type="pos" id="p20" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.110038</slot>
      </edge>
      <edge type="pos" id="p21" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.0173089</slot>
      </edge>
      <edge type="pos" id="p22" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.00391381</slot>
      </edge>
      <edge type="pos" id="p23" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.0491277</slot>
      </edge>
      <edge type="pos" id="p24" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.000974584</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00143255</slot>
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
        <slot name="weight">0.982721</slot>
      </edge>
      <edge type="pos" id="p29" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">PPIO2</slot>
        <slot name="weight">2.43739e-308</slot>
      </edge>
      <edge type="pos" id="p30" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VBZ</slot>
        <slot name="weight">0.016791</slot>
      </edge>
      <edge type="pos" id="p31" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.75874e-06</slot>
      </edge>
      <edge type="pos" id="p32" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000484776</slot>
      </edge>
      <edge type="pos" id="p33" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.876188</slot>
      </edge>
      <edge type="pos" id="p34" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.123812</slot>
      </edge>
      <edge type="pos" id="p35" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997338</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00266191</slot>
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
    </lattice>
  </smaf>"""
];



MERGED = [
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