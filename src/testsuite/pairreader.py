import pyrmrs.xmltools.xmlreader;

import pair;
import pair_hyp;
import pair_text;

import rmrsbankitem;

class PairReader( pyrmrs.xmltools.xmlreader.XMLReader ):

  CLIENTS = [
      pair.Pair,
      pair_hyp.PairHyp,
      pair_text.PairText,
      rmrsbankitem.RMRSbankItem
      
    ];
    
  XMLELEM = pair.Pair.XMLELEM;
  XMLELEMs = [];

  IGNORE = [
      "ENTAILMENT-CORPUS",
      "HEADLINE"
    ];

  def __init__( self, ifile ):

    pyrmrs.xmltools.xmlreader.XMLReader.__init__( self, ifile );

for client in PairReader.CLIENTS:
  PairReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  PairReader.XMLELEMs += client.XMLELEMs;
