import pyrmrs.mrs.robust.rmrsreader;

import pyrmrs.xml.xmlreader;

import analysis;
import sentence;

class AnalysisReader( pyrmrs.xml.xmlreader.XMLReader ):
  
  CLIENTS = \
    pyrmrs.mrs.robust.rmrsreader.RMRSReader.CLIENTS + [
      sentence.Sentence,
      analysis.Analysis
    ];

  XMLELEMs = [];
 
  def __init__( self, ifile ):
    
    common.xmlreader.XMLReader.__init__( self, ifile );

for client in AnalysisReader.CLIENTS:
  AnalysisReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  AnalysisReader.XMLELEMs += client.XMLELEMs;
