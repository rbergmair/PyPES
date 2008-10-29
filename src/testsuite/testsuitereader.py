import formula.formulareader;

import pyrmrs.xmltools.xmlreader;

import testsuite;
import testsuiteref;
import testcase;

import check;

import theory;
import conclusion;

import proposition;
import rmrsbankitem;

class TestsuiteReader( pyrmrs.xmltools.xmlreader.XMLReader ):
  
  CLIENTS = \
    formula.formulareader.FormulaReader.CLIENTS + [
      testsuite.Testsuite,
      testsuiteref.TestsuiteRef,
      testcase.Testcase,
      theory.Theory,
      conclusion.Conclusion,
      proposition.Proposition,
      rmrsbankitem.RMRSbankItem
    ];
    
  IGNORE = formula.formulareader.FormulaReader.IGNORE;
    
  XMLELEM = testsuite.Testsuite.XMLELEM;
  XMLELEMs = [];
  
  def __init__( self, ifile ):
    
    pyrmrs.xmltools.xmlreader.XMLReader.__init__( self, ifile );

for client in TestsuiteReader.CLIENTS:
  TestsuiteReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  TestsuiteReader.XMLELEMs += client.XMLELEMs;
TestsuiteReader.CLIENTS.append( check.Check );
for checkt in check.Check.CHECKs:
  TestsuiteReader.CLIENT_BYNAME[ checkt ] = check.Check;
  TestsuiteReader.XMLELEMs.append( checkt );
