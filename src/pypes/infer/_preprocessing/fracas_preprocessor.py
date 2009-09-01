# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "FraCaSPreprocessor", "preprocess_fracas" ];

from pypes.utils.mc import subject;
from pypes.utils.itembank import *;
from pypes.utils.xml_ import *;



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
      self._obj_.afile.write( "\n</annotations>\n" );
      self._obj_.afile.close();
      
    sect = self._text.split();
    sect = sect[ 0 ];
    sect = sect.replace( ".", "-" );
    
    self._obj_.tsfile = open(
                            "{0}/fracas-{1}/data.ts.xml".format(
                                  self._obj_.datadir,
                                  sect
                                ),
                            "wt",
                            encoding="utf-8"
                          );
    
    self._obj_.tsfile.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
    self._obj_.tsfile.write( '<testsuite>\n\n\n' );

    self._obj_.afile = open(
                           "{0}/fracas-{1}/gold.tsa.xml".format(
                               self._obj_.datadir,
                               sect
                             ),
                           "wt",
                           encoding="utf-8"
                         );
                         
    self._obj_.afile.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
    self._obj_.afile.write( """<annotations descriptor="GOLD" labelset="three-way">\n\n\n""" );



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
    self.fracas_nonstandard = None;
    if "fracas_nonstandard" in attrs:
      self.fracas_nonstandard = attrs[ "fracas_nonstandard" ];
    if "id" in attrs:
      self.id_attr = attrs[ "id" ];
  
  
  def _concatenate_sents( self, sents ):
    
    try:
      assert len( sents ) > 0;
    except:
      print( self.id_attr );
      raise;
    disc = sents[ 0 ];
    for sent in sents[ 1: ]:
      disc += "  " + sent;
    return disc;
  
  
  def _output_discourse( self, discourse ):

    disc = self._concatenate_sents( discourse );
    discid = self._obj_.discs.add_ctx_str( disc );
    self._obj_.tsfile.write(
        """<discourse discid="{0:d}">\n""".format( discid )
      );
    
    for sent in discourse:
      sentid = self._obj_.sents.add_ctx_str( sent );
      self._obj_.tsfile.write(
          """  <sentence sentid="{0:d}">""".format( sentid )
        );
      self._obj_.tsfile.write( sent );
      self._obj_.tsfile.write( "</sentence>\n" );
      
    self._obj_.tsfile.write( "</discourse>\n\n" );
    
    return discid;


  def _output_inference( self, inference, antid, conid ):
    
    infdisc = self._concatenate_sents( inference );
    infdiscid = self._obj_.discs.add_ctx_str( infdisc );
    
    self._obj_.tsfile.write(
        '<inference discid="{0}" infid="{1}">\n'.format(
                                                     infdiscid, self.id_attr
                                                   )
      );
    self._obj_.tsfile.write( '  <antecedent discid="{0}"/>\n'.format( antid ) );
    self._obj_.tsfile.write( '  <consequent discid="{0}"/>\n'.format( conid ) );
    self._obj_.tsfile.write( "</inference>\n\n" );
  
  
  def _output_annotation( self ):

    answer = None;
    
    if self.fracas_answer is not None:
      if self.fracas_answer == "undef":
        pass;
      elif self.fracas_answer == "unknown":
        answer = "unknown";
      elif self.fracas_answer == "yes":
        answer = "entailment";
      elif self.fracas_answer == "no":
        answer = "contradiction";
      else:
        print( self.fracas_answer );
        assert False;
        
    attributes = "";
    
    if self.answer is not None:
      attributes += '  <value attribute="original answer">{0}</value>\n'.format( self.answer );

    if self.fracas_nonstandard is not None:
      attributes += '  <value attribute="nonstandard">{0}</value>\n'.format( self.fracas_nonstandard );
    
    if self.why is not None:
      attributes += '  <value attribute="explanation">{0}</value>\n'.format( self.why );

    if self.note is not None:
      attributes += '  <value attribute="note">{0}</value>\n'.format( self.note );


    annotation = '<annotation infid="{0}"'.format( self.id_attr );
    
    if answer is not None:
      annotation += ' decision="' + answer + '"';
    
    if attributes == "":
      annotation += "/>\n";
    else:
      annotation += ">\n" + attributes + "</annotation>\n";
    
    self._obj_.afile.write( annotation );
    self._obj_.afile.write( "\n" );


  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    
    if not self.antecedents:
      return;
    
    if not self.question:
      return;
    
    val = False;
    for ant in self.antecedents:
      if ant:
        val = True;
        break;
    
    if not val:
      return;
    
    self._obj_.tsfile.write( "<group>\n\n" );

    antid = self._output_discourse( self.antecedents );
    conid = self._output_discourse( [ self.question ] );

    self.antecedents.append( self.question );
    self._output_inference( self.antecedents, antid, conid );
    
    self._output_annotation();

    self._obj_.tsfile.write( "</group>\n\n\n" );



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
    
    assert isinstance( self._obj_, FraCaSPreprocessor );
    self.datadir = self._obj_.datadir;
    
    self.sents_ctx_mgr = TableManager( ( self._obj_.itemdir, "sentence" ) );
    self.sents = self.sents_ctx_mgr.__enter__();
    self.discs_ctx_mgr = TableManager( ( self._obj_.itemdir, "discourse" ) );
    self.discs = self.discs_ctx_mgr.__enter__();
    
    self.itemid = 1;
    self.infid = 1;
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self.discs = None;
    self.discs_ctx_mgr.__exit__( exc_type, exc_val, exc_tb );
    
    self.sents = None;
    self.sents_ctx_mgr.__exit__( exc_type, exc_val, exc_tb );
    
    if self.tsfile is not None:
      self.tsfile.write( "\n</testsuite>\n" );
      self.tsfile.close();
      self.tsfile = None;
      
    if self.afile is not None:
      self.afile.write( "\n</testsuite>\n" );
      self.afile.close();
      self.afile = None;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FraCaSPreprocessor( XMLProcessor, metaclass=subject ):


  HANDLER_BYNAME = {
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
  
  IGNORE = {};


  def process( self, f, datadir, itemdir ):
    
    self.datadir = datadir;
    self.itemdir = itemdir;
    
    xmldecl = f.readline();
    self.feed( xmldecl );
    doctype = f.readline();
    stylesheet = f.readline();
    
    XMLProcessor.process( self, f );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def preprocess_fracas():
  
  f = open( "dta/infer/edited/fracas.bmc.xml", "rb" );
  try:
    with FraCaSPreprocessor() as proc:
      proc.process( f, "dta/infer/fracas", "dta/items/fracas" );
  finally:
    f.close();
  return 0;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
