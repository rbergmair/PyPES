# -*- coding: utf-8 -*-

import pyrmrs.globals;

import pyrmrs.tools.rasptagstr;

testcases = [
    (
      u"The dog barks.",
      u"""<w s='2' e='4'>The</w> <w s='6' e='8'>dog</w> <w s='10' e='14'>barks</w> <w s='15' e='15'>.</w>"""
    ),
    (
      u"I saw a man with a telescope.",
      u"""<w s='2' e='2'>I</w> <w s='4' e='6'>saw</w> <w s='8' e='8'>a</w> <w s='10' e='12'>man</w> <w s='14' e='17'>with</w> <w s='19' e='19'>a</w> <w s='21' e='29'>telescope</w> <w s='30' e='30'>.</w>""",
    ),
    (
      u"As leaders gather in Argentina ahead of this weekends regional talks, Hugo Chávez, Venezuela's populist president is using an energy windfall to win friends and promote his vision of 21st-century socialism.",
      u"""<w s='2' e='3'>As</w> <w s='5' e='11'>leaders</w> <w s='13' e='18'>gather</w> <w s='20' e='21'>in</w> <w s='23' e='31'>Argentina</w> <w s='33' e='37'>ahead</w> <w s='39' e='40'>of</w> <w s='42' e='45'>this</w> <w s='47' e='54'>weekends</w> <w s='56' e='63'>regional</w> <w s='65' e='69'>talks</w> <w s='70' e='70'>,</w> <w s='72' e='75'>Hugo</w> <w s='77' e='83'>Chávez</w> <w s='84' e='84'>,</w> <w s='86' e='94'>Venezuela</w> <w s='95' e='96'>'s</w>  <w s='98' e='105'>populist</w> <w s='107' e='115'>president</w> <w s='117' e='118'>is</w> <w s='120' e='124'>using</w> <w s='126' e='127'>an</w> <w s='129' e='134'>energy</w> <w s='136' e='143'>windfall</w> <w s='145' e='146'>to</w> <w s='148' e='150'>win</w> <w s='152' e='158'>friends</w> <w s='160' e='162'>and</w> <w s='164' e='170'>promote</w> <w s='172' e='174'>his</w> <w s='176' e='181'>vision</w> <w s='183' e='184'>of</w> <w s='186' e='197'>21st-century</w> <w s='199' e='207'>socialism</w> <w s='208' e='208'>.</w>""",
    ),
    (
      u"The cat chased the dog.",
      u"""<w s='2' e='4'>The</w> <w s='6' e='8'>cat</w> <w s='10' e='15'>chased</w> <w s='17' e='19'>the</w> <w s='21' e='23'>dog</w> <w s='24' e='24'>.</w>"""
    )
  ];

import pyrmrs.ext.rasptag;

pyrmrs.globals.initMain();

raspctrl = pyrmrs.ext.rasptag.RaspPosTagger();

for ( surface, toked ) in testcases:
  
  tagged = raspctrl.tokstr_to_tagstr( toked );
  smaf = pyrmrs.tools.rasptagstr.rasptagstr_to_smaf( surface, tagged );

  print "surface: %s" % surface;
  print smaf.str_xml();
  
  rpis = pyrmrs.tools.rasptagstr.smaf_to_raspparse_inputstr( smaf );
  print rpis;

pyrmrs.globals.destructMain();
