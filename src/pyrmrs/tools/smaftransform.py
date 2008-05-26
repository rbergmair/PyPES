import codecs;

import pyrmrs.globals;

import pyrmrs.xmltools;
import pyrmrs.xmltools.reader_element;

import pyrmrs.smafpkg.smafreader;



class Item( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "ITEM";
  XMLELEMs = [];
  
  itemid = None;
  smaf = None;
  
  def __init__( self ):
    
    self.itemid = None;
    self.smaf = None;
  
  def startElement( self, name, attrs ):
    
    if attrs.has_key( "id" ):
      self.itemid = int( attrs[ "id" ] );
  
  def register( self, obj ):
    
    if isinstance( obj, pyrmrs.smafpkg.smaf.SMAF ):
      self.smaf = obj;



class SmafBankReader( pyrmrs.smafpkg.smafreader.SMAFReader ):
  
  CLIENTS = pyrmrs.smafpkg.smafreader.SMAFReader.CLIENTS + [ Item ];
  
  XMLELEM = "SMAFBANK";
  XMLELEMs = [];
  
  IGNORE = pyrmrs.smafpkg.smafreader.SMAFReader.CLIENTS
  
  def __init__( self, ifile ):
    
    pyrmrs.xmltools.xmlreader.XMLReader.__init__( self, ifile, None, None );
    
for client in SmafBankReader.CLIENTS:
  
  SmafBankReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  SmafBankReader.XMLELEMs += client.XMLELEMs;



def smaftransform( ifile, ofile, transform ):
  
  ofile = codecs.getwriter( encoding="utf-8" )( ofile );

  ofile.write( "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\n" );
  ofile.write( "<smafbank>\n\n" );
  
  sbr = SmafBankReader( ifile );
  
  for item in sbr.getAll():
    
    ofile.write( "\n\n<item id=\"%d\">\n\n" % item.itemid );
    ofile.flush();
    smaf = transform( item.smaf );
    ofile.write( smaf.str_xml() );
    ofile.write( "\n\n</item>\n" );
  
  ofile.write( "\n\n\n</smafbank>" );
