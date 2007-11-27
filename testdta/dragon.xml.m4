m4_include(`config.m4')
m4_sinclude(`config.m4.local')

<?xml version='1.0' encoding="UTF-8"?>
<!DOCTYPE rmrs-list SYSTEM "file://_DIR_PYRMRSHOME/dtd/rmrs.dtd">

<rmrs-list>


<!--
       l3 | _every_q( ARG0=x4 BODY=h5 RSTR=h6 ) 
          |    h6 qeq l7
       l7 + _nephew_n_1( ARG0=x4 ) 
   l10001 | _of_p( ARG0=e8 ARG1=x4 ARG2=x9 ) 
      l10 + _a_q( ARG0=x9 BODY=h11 RSTR=h12 ) 
          +    h12 qeq l13
      l13 | _dragon_n_1( ARG0=x9 ) 
      l14 + _snore_v_1( ARG0=e2 ARG1=x4 ) 
-->

<rmrs cfrom='-1' cto='-1'>
<label vid='1'/>
<ep cfrom='0' cto='5'><realpred lemma='every' pos='q'/><label vid='3'/><var sort='x' vid='4'/></ep>
<ep cfrom='6' cto='12'><realpred lemma='nephew' pos='n' sense='1'/><label vid='7'/><var sort='x' vid='4'/></ep>
<ep cfrom='13' cto='15'><realpred lemma='of' pos='p'/><label vid='10001'/><var sort='e' vid='8'/></ep>
<ep cfrom='16' cto='17'><realpred lemma='a' pos='q'/><label vid='10'/><var sort='x' vid='9'/></ep>
<ep cfrom='18' cto='24'><realpred lemma='dragon' pos='n' sense='1'/><label vid='13'/><var sort='x' vid='9'/></ep>
<ep cfrom='25' cto='32'><realpred lemma='snore' pos='v' sense='1'/><label vid='14'/><var sort='e' vid='2'/></ep>
<rarg><rargname>RSTR</rargname><label vid='3'/><var sort='h' vid='6'/></rarg>
<rarg><rargname>BODY</rargname><label vid='3'/><var sort='h' vid='5'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='10001'/><var sort='x' vid='4'/></rarg>
<rarg><rargname>ARG2</rargname><label vid='10001'/><var sort='x' vid='9'/></rarg>
<rarg><rargname>RSTR</rargname><label vid='10'/><var sort='h' vid='12'/></rarg>
<rarg><rargname>BODY</rargname><label vid='10'/><var sort='h' vid='11'/></rarg>
<rarg><rargname>ARG1</rargname><label vid='14'/><var sort='x' vid='4'/></rarg>
<ing><ing-a><var sort='h' vid='7'/></ing-a><ing-b><var sort='h' vid='10001'/></ing-b></ing>
<hcons hreln='qeq'><hi><var sort='h' vid='6'/></hi><lo><label vid='7'/></lo></hcons>
<hcons hreln='qeq'><hi><var sort='h' vid='12'/></hi><lo><label vid='13'/></lo></hcons>
</rmrs>

  <rmrs cfrom='-1' cto='-1'>
    <label vid='1'/>
    <ep cfrom='-1' cto='-1'>
      <gpred>udef_q_rel</gpred>
      <label vid='3'/>
      <var sort='x' vid='4'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='several' pos='a' sense='1'/>
      <label vid='7'/>
      <var sort='e' vid='8'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='delegate' pos='n' sense='1'/>
      <label vid='10001'/>
      <var sort='x' vid='4'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='get' pos='v' sense='state'/>
      <label vid='9'/>
      <var sort='e' vid='2'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='the' pos='q'/>
      <label vid='12'/>
      <var sort='x' vid='11'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='result' pos='n' sense='of'/>
      <label vid='15'/>
      <var sort='x' vid='11'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='publish' pos='v' sense='1'/>
      <label vid='17'/>
      <var sort='e' vid='18'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <gpred>parg_d_rel</gpred>
      <label vid='10002'/>
      <var sort='u' vid='20'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='in' pos='p'/>
      <label vid='10003'/>
      <var sort='e' vid='21'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <gpred>udef_q_rel</gpred>
      <label vid='23'/>
      <var sort='x' vid='22'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='major' pos='a' sense='1'/>
      <label vid='26'/>
      <var sort='e' vid='27'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='national' pos='a' sense='1'/>
      <label vid='10004'/>
      <var sort='e' vid='28'/>
    </ep>
    <ep cfrom='-1' cto='-1'>
      <realpred lemma='newspaper' pos='n' sense='of'/>
      <label vid='10005'/>
      <var sort='x' vid='22'/>
    </ep>
    <hcons hreln='qeq'>
      <hi> <var sort='h' vid='24'/> </hi>
      <lo> <label vid='10005'/> </lo>
    </hcons>
    <hcons hreln='qeq'>
      <hi> <var sort='h' vid='14'/> </hi>
      <lo> <label vid='15'/> </lo>
    </hcons>
    <hcons hreln='qeq'>
      <hi> <var sort='h' vid='10'/> </hi>
      <lo> <label vid='17'/> </lo>
    </hcons>
    <hcons hreln='qeq'>
      <hi> <var sort='h' vid='6'/> </hi>
      <lo> <label vid='10001'/> </lo>
    </hcons>
    <rarg>
      <rargname>RSTR</rargname>
      <label vid='3'/>
      <var sort='h' vid='6'/>
    </rarg>
    <rarg>
      <rargname>BODY</rargname>
      <label vid='3'/>
      <var sort='h' vid='5'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='7'/>
      <var sort='x' vid='4'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='9'/>
      <var sort='x' vid='4'/>
    </rarg>
    <rarg>
      <rargname>ARG2</rargname>
      <label vid='9'/>
      <var sort='x' vid='11'/>
    </rarg>
    <rarg>
      <rargname>ARG3</rargname>
      <label vid='9'/>
      <var sort='h' vid='10'/>
    </rarg>
    <rarg>
      <rargname>RSTR</rargname>
      <label vid='12'/>
      <var sort='h' vid='14'/>
    </rarg>
    <rarg>
      <rargname>BODY</rargname>
      <label vid='12'/>
      <var sort='h' vid='13'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='15'/>
      <var sort='u' vid='16'/>
    </rarg>
    <rarg>
      <rargname>ARG2</rargname>
      <label vid='17'/>
      <var sort='x' vid='11'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='10002'/>
      <var sort='e' vid='18'/>
    </rarg>
    <rarg>
      <rargname>ARG2</rargname>
      <label vid='10002'/>
      <var sort='x' vid='11'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='10003'/>
      <var sort='e' vid='18'/>
    </rarg>
    <rarg>
      <rargname>ARG2</rargname>
      <label vid='10003'/>
      <var sort='x' vid='22'/>
    </rarg>
    <rarg>
      <rargname>RSTR</rargname>
      <label vid='23'/>
      <var sort='h' vid='24'/>
    </rarg>
    <rarg>
      <rargname>BODY</rargname>
      <label vid='23'/>
      <var sort='h' vid='25'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='26'/>
      <var sort='x' vid='22'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='10004'/>
      <var sort='x' vid='22'/>
    </rarg>
    <rarg>
      <rargname>ARG1</rargname>
      <label vid='10005'/>
      <var sort='u' vid='29'/>
    </rarg>
    <ing>
      <ing-a> <var sort='h' vid='10001'/> </ing-a>
      <ing-b> <var sort='h' vid='7'/> </ing-b> 
    </ing>
    <ing>
      <ing-a> <var sort='h' vid='17'/> </ing-a>
      <ing-b> <var sort='h' vid='10002'/> </ing-b> 
    </ing>
    <ing>
      <ing-a> <var sort='h' vid='17'/> </ing-a>
      <ing-b> <var sort='h' vid='10003'/> </ing-b> 
    </ing>
    <ing>
      <ing-a> <var sort='h' vid='10005'/> </ing-a>
      <ing-b> <var sort='h' vid='10004'/> </ing-b> 
    </ing>
    <ing>
      <ing-a> <var sort='h' vid='10005'/> </ing-a>
      <ing-b> <var sort='h' vid='26'/> </ing-b> 
    </ing>
  </rmrs>

</rmrs-list>
