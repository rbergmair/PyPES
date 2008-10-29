import pyrmrs.xmltools.xmlreader;

import formula;

import negation;
import ref;

class FormulaReader( pyrmrs.xmltools.xmlreader.XMLReader ):

  CLIENTS = [ \
      negation.Negation,
      ref.Ref
    ];
    
  XMLELEM = None;

  XMLELEMs = [];

  def __init__( self, ifile ):

    pyrmrs.xmltools.xmlreader.XMLReader.__init__( self, ifile );

for client in FormulaReader.CLIENTS:
  FormulaReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  FormulaReader.XMLELEMs += client.XMLELEMs;