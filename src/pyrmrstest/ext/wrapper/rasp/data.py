# -*- coding: utf-8 -*-



SPLITTER_IN = u"""How is infection transmitted? Through unprotected sexual intercourse
with an infected partner. ACET Director, Dr. Patrick Dixon, recently
told the National Symposium on Teenage Sexuality at
Swanwick. Dr. Dixon said, With up to 20 years from infection to
illness, we just have to ask how many of our congregation have been
added during that time? Three-quarters of the AIDs problem is in
London and much of the rest in Scottish cities.

Churches wanting a speaker should contact the West London offices on
081 840 7879.

The third annual report for 1990/91, subtitled "Bringing it Home" was
published on 21st June this year.

24,000 pupils are also seen by ACET educators.

The 24-page full colour schools booklet HIV - "It is Your Choice" is
now available to members of the public at a price of 50p each.

Please write to : THE EDITOR, ACET NEWSLETTER, P.O. BOX 1323, LONDON
W5 5TF.

Eric Taylor's sixth annual Exhibition of Oil Paintings in aid of
Amnesty and the Medical Foundation is being held in Tewkesbury Abbey,
Gloucestershire, from 19th - 26th June inclusive.

So far Eric Taylor has raised a magnificent £2,900 by donations and
profits.

Santiago, Chile : On a warm autumn evening in 1990 international rock
star Sting dances on stage with a group of chilean mothers and
grandmothers of the disappeared.

The annual budget for 1990 is £11 million, which represents only a
third of the money raised worldwide on Amnesty's behalf. Add to this
the money raised by new members the length and breadth of the British
Isles who contributed to the Section's annual turnover of £2.25
million with their cultural events, sponsored walks and street
collections.

Newsletter AIDs CARE, EDUCATION AND TRAINING Issue No. 7.


ACET Home Care, which moves into the building in July, will share the
offices with two other AIDS charities, P.A.L.S. (Portsmouth AIDS Link
Support) and the Link Project.

4.55 p.m. - Tony is ushered into a side ward with three doctors and I
stay outside with Mum.

Registered Office 318 St Paul's Road, Duke Street, London N1 2LP.

This virus affects the body's defence system so that it can not fight
infection.""";



SPLITTER_OUT = [
  u'How is infection transmitted?',
  u'Through unprotected sexual intercourse with an infected partner.',
  u'ACET Director, Dr. Patrick Dixon, recently told the National Symposium on Teenage Sexuality at Swanwick.',
  u'Dr. Dixon said, With up to 20 years from infection to illness, we just have to ask how many of our congregation have been added during that time?',
  u'Three-quarters of the AIDs problem is in London and much of the rest in Scottish cities.',
  u'Churches wanting a speaker should contact the West London offices on 081 840 7879.',
  u'The third annual report for 1990/91, subtitled "Bringing it Home" was published on 21st June this year.',
  u'24,000 pupils are also seen by ACET educators.',
  u'The 24-page full colour schools booklet HIV - "It is Your Choice" is now available to members of the public at a price of 50p each.',
  u'Please write to : THE EDITOR, ACET NEWSLETTER, P.O. BOX 1323, LONDON W5 5TF.',
  u"Eric Taylor's sixth annual Exhibition of Oil Paintings in aid of Amnesty and the Medical Foundation is being held in Tewkesbury Abbey, Gloucestershire, from 19th - 26th June inclusive.",
  u'So far Eric Taylor has raised a magnificent £2,900 by donations and profits.',
  u'Santiago, Chile : On a warm autumn evening in 1990 international rock star Sting dances on stage with a group of chilean mothers and grandmothers of the disappeared.',
  u"The annual budget for 1990 is £11 million, which represents only a third of the money raised worldwide on Amnesty's behalf.",
  u"Add to this the money raised by new members the length and breadth of the British Isles who contributed to the Section's annual turnover of £2.25 million with their cultural events, sponsored walks and street collections.",
  u'Newsletter AIDs CARE, EDUCATION AND TRAINING Issue No. 7.', u'ACET Home Care, which moves into the building in July, will share the offices with two other AIDS charities, P.A.L.S. (Portsmouth AIDS Link Support) and the Link Project.',
  u'4.55 p.m. - Tony is ushered into a side ward with three doctors and I stay outside with Mum.',
  u"Registered Office 318 St Paul's Road, Duke Street, London N1 2LP.",
  u"This virus affects the body's defence system so that it can not fight infection."                
];



TEXT = [
  u"The dog barks.",
  u"I saw a man with a telescope.",
  u"Hugo Chávez chased the dog.",
  u"As leaders gather in Argentina ahead of this "+
    u"weekends regional talks, Hugo Chávez, Venezuela's "+
    u"populist president is using an energy windfall to win "+
    u"friends and promote his vision of 21st-century socialism.",
  u"The cat chased the dog."
];


  
TOKENISED = [
  u"""<smaf>
    <text>The dog barks.</text>
    <lattice init="v0" final="v4" cfrom="0" cto="14">
      <edge type="token" id="t0" source="v0" target="v1" cfrom="0" cto="3">The</edge>
      <edge type="token" id="t1" source="v1" target="v2" cfrom="4" cto="7">dog</edge>
      <edge type="token" id="t2" source="v2" target="v3" cfrom="8" cto="13">barks</edge>
      <edge type="token" id="t3" source="v3" target="v4" cfrom="13" cto="14">.</edge>
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
    </lattice>
  </smaf>"""
];



TAGGED = [
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
        <slot name="weight">0.00377621</slot>
      </edge>
      <edge type="pos" id="p19" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0183804</slot>
      </edge>
      <edge type="pos" id="p20" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.00426329</slot>
      </edge>
      <edge type="pos" id="p21" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.00190728</slot>
      </edge>
      <edge type="pos" id="p22" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000439245</slot>
      </edge>
      <edge type="pos" id="p23" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00291899</slot>
      </edge>
      <edge type="pos" id="p24" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.966895</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00142001</slot>
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
        <slot name="weight">0.0172684</slot>
      </edge>
      <edge type="pos" id="p31" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.77103e-06</slot>
      </edge>
      <edge type="pos" id="p32" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000497064</slot>
      </edge>
      <edge type="pos" id="p33" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.902296</slot>
      </edge>
      <edge type="pos" id="p34" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0977044</slot>
      </edge>
      <edge type="pos" id="p35" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997405</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00259539</slot>
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
  </smaf>"""
];


MORPHED = [
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
        <slot name="weight">0.00377621</slot>
      </edge>
      <edge type="pos" id="p19" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0183804</slot>
      </edge>
      <edge type="pos" id="p20" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.00426329</slot>
      </edge>
      <edge type="pos" id="p21" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.00190728</slot>
      </edge>
      <edge type="pos" id="p22" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000439245</slot>
      </edge>
      <edge type="pos" id="p23" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00291899</slot>
      </edge>
      <edge type="pos" id="p24" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.966895</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00142001</slot>
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
        <slot name="weight">0.0172684</slot>
      </edge>
      <edge type="pos" id="p31" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.77103e-06</slot>
      </edge>
      <edge type="pos" id="p32" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000497064</slot>
      </edge>
      <edge type="pos" id="p33" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.902296</slot>
      </edge>
      <edge type="pos" id="p34" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0977044</slot>
      </edge>
      <edge type="pos" id="p35" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997405</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00259539</slot>
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
    </lattice>
  </smaf>"""
];



PARSED = [
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
        <slot name="weight">0.00377621</slot>
      </edge>
      <edge type="pos" id="p19" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0183804</slot>
      </edge>
      <edge type="pos" id="p20" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">NN2</slot>
        <slot name="weight">0.00426329</slot>
      </edge>
      <edge type="pos" id="p21" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">RR</slot>
        <slot name="weight">0.00190728</slot>
      </edge>
      <edge type="pos" id="p22" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VV0</slot>
        <slot name="weight">0.000439245</slot>
      </edge>
      <edge type="pos" id="p23" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVD</slot>
        <slot name="weight">0.00291899</slot>
      </edge>
      <edge type="pos" id="p24" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVG</slot>
        <slot name="weight">0.966895</slot>
      </edge>
      <edge type="pos" id="p25" source="v13" target="v14" cfrom="75" cto="81" deps="t13">
        <slot name="tag">VVN</slot>
        <slot name="weight">0.00142001</slot>
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
        <slot name="weight">0.0172684</slot>
      </edge>
      <edge type="pos" id="p31" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VDZ</slot>
        <slot name="weight">2.77103e-06</slot>
      </edge>
      <edge type="pos" id="p32" source="v16" target="v17" cfrom="92" cto="94" deps="t16">
        <slot name="tag">VHZ</slot>
        <slot name="weight">0.000497064</slot>
      </edge>
      <edge type="pos" id="p33" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">JJ</slot>
        <slot name="weight">0.902296</slot>
      </edge>
      <edge type="pos" id="p34" source="v17" target="v18" cfrom="95" cto="103" deps="t17">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.0977044</slot>
      </edge>
      <edge type="pos" id="p35" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NN1</slot>
        <slot name="weight">0.997405</slot>
      </edge>
      <edge type="pos" id="p36" source="v18" target="v19" cfrom="104" cto="113" deps="t18">
        <slot name="tag">NNS1</slot>
        <slot name="weight">0.00259539</slot>
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
