import pyrmrs.xml.reader_element;

class RealPredicate( pyrmrs.xml.reader_element.ReaderElement ):
  
  XMLELEM = "REALPRED";
  XMLELEMs = [ XMLELEM ];

  POS_VERB = 'v';
  POS_NOUN = 'n';
  POS_ADJECTIVE = 'j';
  POS_ADVERB = 'r';
  POS_PREPOSITION = 'p';
  POS_QUANTIFIER = 'q';
  POS_COORDINATOR = 'c';
  POS_NOT = 'x';
  POS_A = 'a';
  POS_U = 'u';

  lemma = None;
  pos = None;
  sense = None;



  def __init__( self ):

    self.lemma = None;
    self.pos = None;
    self.sense = None;



  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      
      self.lemma = attrs[ "lemma" ];
  
      self.pos = attrs[ "pos" ];
      
      if attrs.has_key( "sense" ):
        self.sense = attrs[ "sense" ];



  def xml_base( self ):
    
    return "<realpred%s/>%s";
  
  def xml_tmplt( self, base ):
    
    attributes = " lemma='%s'" % self.lemma;
    attributes += " pos='%s'" % self.pos;
    if self.sense != None:
      attributes += " sense='%s'" % self.sense;
    attributes = attributes.replace( "%", "%%" );
      
    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", "%s" );



  def str_pretty( self ):

    stri = "_%s" % self.lemma;
    if self.pos != None:
      stri += "_%s" % self.pos;
    if self.sense != None:
      stri += "_%s" % self.sense;

    return stri;
