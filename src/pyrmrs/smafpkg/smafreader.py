import pyrmrs.xmltools.xmlreader;
import pyrmrs.mrs.robust.rmrsreader;

import generic_edge;
import lattice;
import smaf;
import slot;
import text;

class SMAFReader( pyrmrs.xmltools.xmlreader.XMLReader ):

  CLIENTS = [
    generic_edge.GenericEdge,
    lattice.Lattice,
    smaf.SMAF,
    slot.Slot,
    text.Text
  ];

  XMLELEM = smaf.SMAF.XMLELEM;
  XMLELEMs = [];

  IGNORE = [ "OLAC:OLAC", "IDENTIFIER", "CREATOR", "CREATED", "TEXT", "FS", "F",
             "RMRS", "ATTRIBUTES", "DC:CREATOR", "DC:DESCRIPTION",
             "DC:IDENTIFIER", "DC:LANGUAGE", "SMAF-LIST-MC" ] \
         + pyrmrs.mrs.robust.rmrsreader.RMRSReader.XMLELEMs;
  
  def __init__( self, ifile, addxml=None, limit=None ):
    
    if addxml != None:
      addxml = ( "smaf-list-mc", "smaf.dtd" );
    pyrmrs.xmltools.xmlreader.XMLReader.__init__( self, ifile, addxml, limit );

for client in SMAFReader.CLIENTS:
  SMAFReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  SMAFReader.XMLELEMs += client.XMLELEMs;
