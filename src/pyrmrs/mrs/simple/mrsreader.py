import pyrmrs.xml.xmlreader;

import mrsem;
import constant;
import elementary_predication;
import extrapair;
import fvpair;
import hole_constraint;
import label;
import predicate;
import real_predicate;
import referent;
import spredicate;
import variable;



class MRSReader( pyrmrs.xml.xmlreader.XMLReader ):

  CLIENTS = [
    mrsem.MRSem,
    constant.Constant,
    elementary_predication.ElementaryPredication,
    extrapair.ExtraPair,
    fvpair.FvPair,
    hole_constraint.HoleConstraint,
    label.Label,
    predicate.Predicate,
    real_predicate.RealPredicate,
    referent.Referent,
    spredicate.SPredicate,
    variable.Variable
  ];
  
  XMLELEMs = [];
  
  IGNORE = [
    "MRS-LIST", "MRS-LIST-MC"
  ];
  
  def __init__( self, ifile, addxml=None, limit=None ):
    
    if addxml != None:
      addxml = ( "mrs-list-mc", "mrs.dtd" );
    pyrmrs.xml.xmlreader.XMLReader.__init__( self, ifile, addxml, limit );
    
for client in MRSReader.CLIENTS:
  MRSReader.CLIENT_BYNAME[ client.XMLELEM ] = client;
  MRSReader.XMLELEMs += client.XMLELEMs;