# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.tools";
__all__ = [ "process_fracas", "main" ];

import sys;

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class CommentHandler( XMLPCharElementHandler, metaclass=subject ):
  
  
  XMLELEM = "comment";
  
  
  def __init__( self ):
    
    self._active = False;
  
  
  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    self._active = False;
    
    XMLPCharElementHandler.startElement( self, name, attrs );
    if "class" in attrs:
      if attrs[ "class" ] == "subsection":
        self._active = True;


  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    if not self._active:
      return;
    
    if self._obj_.tsfile is not None:
      self._obj_.tsfile.write( "\n</testsuite>\n" );
      self._obj_.tsfile.close();

    if self._obj_.afile is not None:
      self._obj_.afile.write( "\n</annotation>\n" );
      self._obj_.afile.close();
      
    sect = self._text.split();
    sect = sect[ 0 ];
    sect = sect.replace( ".", "-" );
    
    self._obj_.tsfile = open(
                            "{0}/fracas-{1}.ts.xml".format(
                                  self._obj_.datadir, sect
                                ),
                            "w"
                          );
    
    self._obj_.tsfile.write( "<testsuite>\n\n\n" );

    self._obj_.afile = open(
                           "{0}/fracas-{1}.tsa.xml".format(
                               self._obj_.anndir, sect
                             ),
                           "w"
                         );
                         
    
    self._obj_.afile.write( """<annotation confidence_ranked="False">\n\n\n""" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "p";

  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.antecedents.append( self._text.strip() );
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class QHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "q";

  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.question = self._text.strip();
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class HHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "h";

  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.hypothesis = self._text.strip();
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class AHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "a";

  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.answer = self._text.strip();
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class WhyHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "why";

  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.why = self._text.strip();
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class NoteHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "note";

  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.note = self._text.strip();
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ProblemHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "problem";
  
  
  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    self.antecedents = [];
    self.question = None;
    self.hypothesis = None;
    self.answer = None;
    self.why = None;
    self.note = None;
    
    self.fracas_answer = None;
    if "fracas_answer" in attrs:
      self.fracas_answer = attrs[ "fracas_answer" ];
    if "id" in attrs:
      self.id_attr = attrs[ "id" ];


  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    sentids = [];
    ids = set();
    
    for sent in self.antecedents:
      id = None;
      itemid = None;
      if sent in self._obj_.sentences:
        id = self._obj_.sentences.index( sent );
        itemid = self._obj_.itemid_by_sentid[ id ];
      else:
        id = len( self._obj_.sentences );
        self._obj_.sentences.append( sent );
        itemid = self._obj_.itemid;
        self._obj_.itemid += 1;
        self._obj_.itemid_by_sentid[ id ] = itemid;
      sentids.append( ( itemid, sent ) );
      ids.add( id );
    
    antid = None;
    if ids in self._obj_.discourses:
      id = self._obj_.discourses.index( ids );
      antid = self._obj_.itemid_by_discid[ id ];
    else:
      id = len( self._obj_.discourses );
      self._obj_.discourses.append( antid );
      antid = self._obj_.itemid;
      self._obj_.itemid += 1;
      self._obj_.itemid_by_discid[ id ] = antid;
    
    self._obj_.tsfile.write(
        """<discourse itemset="fracas" itemid="{0:d}">\n""".format( antid )
      );
    
    for ( sentid, sent ) in sentids:
      
      self._obj_.sfile.write( "[{0}] {1}\n".format( sentid, sent ) );
      
      self._obj_.tsfile.write(
          """  <sentence itemset="fracas" itemid="{0:d}">""".format( sentid )
        );
      
      self._obj_.tsfile.write( sent );
      self._obj_.tsfile.write( "</sentence>\n" );
      
    self._obj_.tsfile.write( "</discourse>\n\n" );
    
    sentid = None;
    itemid = None;
    sid = None;
    if self.question in self._obj_.sentences:
      sid = self._obj_.sentences.index( self.question );
      sentid = self._obj_.itemid_by_sentid[ sid ];
    else:
      sid = len( self._obj_.sentences );
      self._obj_.sentences.append( self.question );
      sentid = self._obj_.itemid;
      itemid = self._obj_.itemid;
      self._obj_.itemid += 1;
      self._obj_.itemid_by_sentid[ sid ] = itemid;
    
    conid = None;
    if {sid} in self._obj_.discourses:
      id = self._obj_.discourses.index( {sid} );
      conid = self._obj_.itemid_by_discid[ id ];
    else:
      id = len( self._obj_.discourses );
      self._obj_.discourses.append( {sid} );
      conid = self._obj_.itemid;
      self._obj_.itemid += 1;
      self._obj_.itemid_by_discid[ id ] = conid;
    
    self._obj_.tsfile.write(
        """<discourse itemset="fracas" itemid="{0:d}">\n""".format( conid )
      );
    
    self._obj_.tsfile.write(
        """  <sentence itemset="fracas" itemid="{0:d}">""".format( sentid )
      );
    
    self._obj_.tsfile.write( self.question );
    self._obj_.tsfile.write( "</sentence>\n" );
    
    self._obj_.tsfile.write( "</discourse>\n\n" );
    
    assert self._obj_.infid == int( self.id_attr );
    self._obj_.infid += 1;
    
    infid = self._obj_.itemid;
    self._obj_.itemid += 1;
    
    self._obj_.tsfile.write(
        '<inference itemset="fracas" infid="{0}" oid="{1}">\n'.format( infid, self.id_attr )
      );

    self._obj_.tsfile.write(
        """  <antecedent itemset="fracas" itemid="{0}"/>\n""".format( antid )
      );
      
    self._obj_.tsfile.write(
        """  <consequent itemset="fracas" itemid="{0}"/>\n""".format( conid )
      );
      
    self._obj_.tsfile.write( "</inference>\n\n\n" );
    
    
    annotation = '<annotation itemset="fracas" infid="{0}" oid="{1}"'.format( infid, self.id_attr );
    
    if self.fracas_answer is not None:
      if self.fracas_answer == "undef":
        pass;
      elif self.fracas_answer == "unknown":
        annotation += ' decision="unknown"';
      elif self.fracas_answer == "yes":
        annotation += ' decision="entailment"';
      elif self.fracas_answer == "no":
        annotation += ' decision="contradiction"';
      else:
        print( self.fracas_answer );
        assert False;
        
    attributes = "";
    
    if self.answer is not None:
      attributes += '  <value attribute="original answer">{0}</value>\n'.format( self.answer );
    
    if self.why is not None:
      attributes += '  <value attribute="explanation">{0}</value>\n'.format( self.why );

    if self.note is not None:
      attributes += '  <value attribute="note">{0}</value>\n'.format( self.note );
    
    if attributes == "":
      annotation += "/>\n";
    else:
      annotation += ">\n" + attributes + "</annotation>\n";
    
    self._obj_.afile.write( annotation );
    self._obj_.afile.write( "\n" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ProblemsHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "fracas-problems";
  
  def _enter_( self ):
    
    self.tsfile = None;
    self.afile = None;
    self.sentences = [];
    self.discourses = [];
    self.itemid_by_sentid = {};
    self.itemid_by_discid = {};
    
    assert isinstance( self._obj_, FraCaSProcessor );
    self.datadir = self._obj_.datadir;
    self.anndir = self._obj_.anndir;
    self.sfile = open( self._obj_.itemdir + "/fracas-sents.items", "wt" );
    self.dfile = open( self._obj_.itemdir + "/fracas-discs.items", "wt" );
    
    self.itemid = 1;
    self.infid = 1;
  
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self.dfile.close();
    self.sfile.close();
    
    if self.tsfile is not None:
      self.tsfile.write( "\n</testsuite>\n" );
      self.tsfile.close();
      self.tsfile = None;
      
    if self.afile is not None:
      self.afile.write( "\n</testsuite>\n" );
      self.afile.close();
      self.afile = None;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FraCaSProcessor( XMLHandler, metaclass=subject ):


  CLIENT_BYNAME = {
      ProblemsHandler.XMLELEM: ( ProblemsHandler, None ),
      CommentHandler.XMLELEM: ( CommentHandler, None ),
      ProblemHandler.XMLELEM: ( ProblemHandler, None ),
      PHandler.XMLELEM: ( PHandler, None ),
      QHandler.XMLELEM: ( QHandler, None ),
      HHandler.XMLELEM: ( HHandler, None ),
      AHandler.XMLELEM: ( AHandler, None ),
      WhyHandler.XMLELEM: ( WhyHandler, None ),
      NoteHandler.XMLELEM: ( NoteHandler, None )
    };
  
  IGNORE = {
      "why", "note"
    };

  
  def process( self, datadir, anndir, itemdir ):
    
    self.datadir = datadir;
    self.anndir = anndir;
    self.itemdir = itemdir;
    
    xmldecl = self._obj_.readline();
    self.feed( xmldecl );
    doctype = self._obj_.readline();
    stylesheet = self._obj_.readline();
    
    if isinstance( self._obj_, str ):
      self.feed( str );
    else:
      x = self._obj_.read( self.CHUNK_SIZE );
      while x:
        self.feed( x );
        x = self._obj_.read( self.CHUNK_SIZE );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  f = open( "dta/infer/orig/fracas.bmc.xml" );
  try:
    with FraCaSProcessor( f ) as proc:
      proc.process( "dta/infer/fracas/data",
                    "dta/infer/fracas/gold",
                    "dta/items/text" );
  finally:
    f.close();
  return 0;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
