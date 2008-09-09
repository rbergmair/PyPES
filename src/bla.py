import pyrmrs.ext.wrapper.rasp.tokeniser;
import pyrmrs.ext.wrapper.rasp.tagger;
import pyrmrs.ext.wrapper.rasp.morpher;
import pyrmrs.ext.wrapper.rasp.parser;

import pyrmrs.ext.wrapper.delphin.rasprmrs;

import pyrmrs.smafpkg.smaf;

rasp_tokeniser = pyrmrs.ext.wrapper.rasp.tokeniser.Tokeniser();
rasp_tagger = pyrmrs.ext.wrapper.rasp.tagger.Tagger();
rasp_morpher = pyrmrs.ext.wrapper.rasp.morpher.Morpher();
rasp_parser = pyrmrs.ext.wrapper.rasp.parser.Parser();
rasp_rmrs = pyrmrs.ext.wrapper.delphin.rasprmrs.RaspRmrs();

smaf = pyrmrs.smafpkg.smaf.SMAF( "The dog barks." );
smaf = rasp_tokeniser.tokenise( smaf );
smaf = rasp_tagger.tag( smaf );
smaf = rasp_morpher.morph( smaf );
smaf = rasp_parser.parse( smaf );
smaf = rasp_rmrs.convert( smaf );


rmrs = None;
for rmrs_ in smaf.getRMRSes():
  rmrs = rmrs_;
  break;

try:
  scoping = rmrs.get_scoping();
  if scoping.solve( 1 ):
    scopes = scoping.enumerate();
    print len( scopes );
except:
  print rmrs.str_xml();
  raise;

print smaf.str_xml();