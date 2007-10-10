import pyrmrs.xml.xmlreader;

import edge;
import lattice;
import smaf;
import slot;

class SMAFReader( pyrmrs.xml.xmlreader.XMLReader ):

  CLIENTS = [
    edge.Edge,
    lattice.Lattice,
    smaf.SMAF,
    slot.Slot
  ];

  XMLELEM = smaf.SMAF.XMLELEM;
  XMLELEMs = [];

  IGNORE = [ "OLAC:OLAC", "IDENTIFIER", "CREATOR", "CREATED", "TEXT", "FS", "F",
             "RMRS", "ATTRIBUTES", "DC:CREATOR", "DC:DESCRIPTION",
             "DC:IDENTIFIER", "DC:LANGUAGE" ];
  
  def __init__( self, ifile, addxml=None, limit=None ):
    
    if addxml != None:
      addxml = ( "smaf-list-mc", "smaf.dtd" );
    pyrmrs.xml.xmlreader.XMLReader.__init__( self, ifile, addxml, limit );

for client in SMAFReader.CLIENTS:
  SMAFReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  SMAFReader.XMLELEMs += client.XMLELEMs;
