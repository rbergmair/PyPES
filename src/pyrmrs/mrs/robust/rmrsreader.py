import pyrmrs.xml.xmlreader;

import rmrsem;
import elementary_predication;
import real_predicate;
import grammar_predicate;
import label;
import variable;
import relation_argument;
import constant;
import in_group;
import hole_constraint;

class RMRSReader( pyrmrs.xml.xmlreader.XMLReader ):

  CLIENTS = [
    rmrsem.RMRSem,
    elementary_predication.ElementaryPredication,
    real_predicate.RealPredicate,
    grammar_predicate.GrammarPredicate,
    label.Label,
    variable.Variable,
    relation_argument.RelationArgument,
    constant.Constant,
    in_group.InGroup,
    hole_constraint.HoleConstraint
  ];
  
  XMLELEM = rmrsem.RMRSem.XMLELEM;
  XMLELEMs = [];

  IGNORE = [
    "RMRS-LIST", "RMRS-LIST-MC",
  ];
  
  def __init__( self, ifile, addxml=None, limit=None ):
    
    if addxml != None:
      addxml = ( "rmrs-list-mc", "rmrs.dtd" );
    pyrmrs.xml.xmlreader.XMLReader.__init__( self, ifile, addxml, limit );

for client in RMRSReader.CLIENTS:
  RMRSReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  RMRSReader.XMLELEMs += client.XMLELEMs;  
