import traceback;

import pyrmrs.globals;
import pyrmrs.mrs.common.referent;
import pyrmrs.error.xmlsem_error;



class Referent( pyrmrs.mrs.common.referent.Referent ):

  NUM_SINGULAR = "sg";
  NUM_PLURAL = "pl";
  NUM_U = "u";
  num = None;

  PERS_1ST = "1";
  PERS_2ND = "2";
  PERS_3RD = "3";
  PERS_1STOR3RD = "1-or-3";
  PERS_U = "u";
  pers = None;

  GENDER_MASCULINUM = "m";
  GENDER_FEMININUM = "f";
  GENDER_NEUTRUM = "n";
  GENDER_NONNEUTRUM = "m-or-f";
  GENDER_U = "u";
  gender = None;
  
  BOOL_PLUS = "plus";
  BOOL_MINUS = "minus";
  BOOL_U = "u";
  
  divisible = None;

  COGNST_TYPE = "type-id";
  COGNST_UNIQUE = "uniq-id";
  COGNST_FAM = "fam";
  COGNST_ACTIVE = "activ";
  COGNST_INFOC = "in-foc";
  COGNST_UNIQUEORLESS = "uniq-or-less";
  COGNST_UNIQUEORFAM = "uniq-or-fam";
  COGNST_FAMORACTIVE = "fam-or-activ";
  COGNST_ACTIVEORMORE = "active-or-more";
  COGNST_FAMORLESS = "fam-or-less";
  COGNST_UNIQORFAMORACTIVE = "uniq-or-fam-or-activ";
  COGNST_FAMORMORE = "fam-or-more";
  COGNST_ACTIVORLESS = "activ-or-less";
  COGNST_UNIQUEORMORE = "uniq-or-more";
  COGNST_U = "u";
  cognst = None;

  TENSE_PAST = "past";
  TENSE_PRESENT = "present";
  TENSE_FUTURE = "future";
  TENSE_NONPAST = "non-past";
  TENSE_U = "u";
  tense = None;

  telic = None;
  protracted = None;
  stative = None;
  incept = None;
  imr = None;
  boundedness = None;
  refdistinct = None;



  def __init__( self ):
    
    self.num = None;
    self.pers = None;
    self.gender = None;
    self.divisible = None;
    self.cognst = None;
    self.tense = None;
    self.telic = None;
    self.protracted = None;
    self.stative = None;
    self.incept = None;
    self.imr = None;
    self.boundedness = None;
    self.refdistinct = None;   
    
  def mergeat( self, selfat, refat ):

    if selfat == None or ( selfat == "u" and refat != "u" ):
      selfat = refat;
    if selfat != None and refat != None:
      if refat != selfat:
        if refat != "u" and selfat != "u":
          #raise pyrmrs.error.xmlsem_error.XMLSemError( \
          #  ( pyrmrs.error.xmlsem_error.XMLSemError.ERRNO_UNDEFINED, "" ) );
          #assert False;
          pass;
            
    return selfat;
    
  def merge( self, ref2 ):
    
    try:
      
      self.num = self.mergeat( self.num, ref2.num );
      self.pers = self.mergeat( self.pers, ref2.pers );
      self.gender = self.mergeat( self.gender, ref2.gender );
      self.divisible = self.mergeat( self.divisible, ref2.divisible );
      self.cognst = self.mergeat( self.cognst, ref2.cognst );
      self.tense = self.mergeat( self.tense, ref2.tense );
      self.telic = self.mergeat( self.telic, ref2.telic );
      self.protracted = self.mergeat( self.protracted, ref2.protracted );
      self.stative = self.mergeat( self.stative, ref2.stative );
      self.incept = self.mergeat( self.incept, ref2.incept );
      self.imr = self.mergeat( self.imr, ref2.imr );
      self.boundedness = self.mergeat( self.boundedness, ref2.boundedness );
      self.refdistinct = self.mergeat( self.refdistinct, ref2.refdistinct );
    
    except:
      pyrmrs.globals.logError( self, "--- INABLE TO MERGE TWO REFERENTS ---" );
      pyrmrs.globals.logError( self, traceback.format_exc() );
      pyrmrs.globals.logError( self, "Referent 1: %s" % self.str_xml() );
      pyrmrs.globals.logError( self, "Referent 2: %s" % ref2.str_xml() );
      raise;
      
      



  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    pyrmrs.mrs.common.referent.Referent.startElement( self, name, attrs );
      
    if attrs.has_key( "num" ):
      self.num = attrs[ "num" ];

    if attrs.has_key( "pers" ):
      self.pers = attrs[ "pers" ];

    if attrs.has_key( "gender" ):
      self.gender = attrs[ "gender" ];
     
    if attrs.has_key( "divisible" ):
      self.divisible = attrs[ "divisible" ];

    if attrs.has_key( "cogn-st" ):
      self.cognst = attrs[ "cogn-st" ];

    if attrs.has_key( "tense" ):
      self.tense = attrs[ "tense" ];

    if attrs.has_key( "telic" ):
      self.telic = attrs[ "telic" ];

    if attrs.has_key( "protracted" ):
      self.protracted = attrs[ "protracted" ];

    if attrs.has_key( "stative" ):
      self.stative = attrs[ "stative" ];

    if attrs.has_key( "incept" ):
      self.incept = attrs[ "incept" ];

    if attrs.has_key( "imr" ):
      self.imr = attrs[ "imr" ];

    if attrs.has_key( "boundedness" ):
      boundedness = attrs[ "boundedness" ];

    if attrs.has_key( "refdistinct" ):
      refdistinct = attrs[ "refdistinct" ];



  def xml_base( self ):
    
    return pyrmrs.mrs.common.referent.Referent.xml_base( self );

  def xml_tmplt( self, base ):
    
    base = pyrmrs.mrs.common.referent.Referent.xml_tmplt( self, base );
    
    st = "";
    if self.num != None:
      st += " num='%s'" % self.num;
    if self.pers != None:
      st += " pers='%s'" % self.pers;
    if self.gender != None:
      st += " gender='%s'" % self.gender;
    if self.divisible != None:
      st += " divisible='%s'" % self.divisible;     
    if self.cognst != None:
      st += " cogn-st='%s'" % self.cognst;     
    if self.tense != None:
      st += " tense='%s'" % self.tense;     
    if self.telic != None:
      st += " telic='%s'" % self.telic;
    if self.protracted != None:
      st += " protracted='%s'" % self.protracted;
    if self.stative != None:
      st += " stative='%s'" % self.stative;     
    if self.incept != None:
      st += " incept='%s'" % self.incept;     
    if self.imr != None:
      st += " imr='%s'" % self.imr;     
    if self.boundedness != None:
      st += " boundedness='%s'" % self.boundedness;     
    if self.refdistinct != None:
      st += " refdistinct='%s'" % self.refdistinct;     

    base = base.replace( "%%", "%%%%" );
    return base % ( st+"%s", "%s" );
