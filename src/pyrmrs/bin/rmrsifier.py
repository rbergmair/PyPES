import sys;
import cStringIO;

import pyrmrs.smafpkg.smafreader;

import pyrmrs.ext.wrapper.rasp.tokeniser;
import pyrmrs.ext.wrapper.rasp.tagger;
import pyrmrs.ext.wrapper.rasp.morpher;
import pyrmrs.ext.wrapper.rasp.parser;

import pyrmrs.ext.wrapper.delphin.rasprmrs;

import pyrmrs.ext.wrapper.delphin.fspp;
import pyrmrs.ext.wrapper.delphin.pet;

import pyrmrs.ext.glue.merge_rasp_erg_pp;



class Worker:
  
  rasp_tokeniser = None;
  rasp_tagger = None;
  
  erg_tokeniser = None;
  
  rasp_morpher = None;
  rasp_parser = None;
  rasp_rmrs = None;
  
  erg_parser = None;

  def global_init( self ):  

    self.rasp_tokeniser = pyrmrs.ext.wrapper.rasp.tokeniser.Tokeniser();
    self.rasp_tagger = pyrmrs.ext.wrapper.rasp.tagger.Tagger();
    
    self.erg_tokeniser = pyrmrs.ext.wrapper.delphin.fspp.Fspp();
    
    self.rasp_morpher = pyrmrs.ext.wrapper.rasp.morpher.Morpher();
    self.rasp_parser = pyrmrs.ext.wrapper.rasp.parser.Parser();
    
    self.rasp_rmrs = pyrmrs.ext.wrapper.delphin.rasprmrs.RaspRmrs();
    
    self.erg_parser = pyrmrs.ext.wrapper.delphin.pet.TaggedPet();
  
  def global_del( self ):
    
    del self.erg_parser;
    del self.rasp_rmrs;
    del self.rasp_parser;
    del self.rasp_morpher;
    del self.erg_tokeniser;
    del self.rasp_tagger;
    del self.rasp_tokeniser;
  
  def work( self, strin ):

    strinio = cStringIO.StringIO( strin );
    try:
      smafrd = pyrmrs.smafpkg.smafreader.SMAFReader( strinio, True );
      ismaf = smafrd.getFirst();
    except:
      pyrmrs.globals.logError( self, "error while parsing input SMAF" );
      pyrmrs.globals.logError( self, traceback.format_exc() );
      pyrmrs.globals.logError( self, "--- INPUT ---" );
      pyrmrs.globals.logError( self, unicode( strin, encoding="utf-8" ) );
      pyrmrs.globals.logError( self, "-------------" );
      raise;
      
    rsmaf = self.rasp_tokeniser.tokenise( ismaf );
    rsmaf = self.rasp_tagger.tag( rsmaf );
    
    esmaf = self.erg_tokeniser.tokenise( ismaf );
    
    msmaf = pyrmrs.ext.glue.merge_rasp_erg_pp.merge_rasp_erg_pp( esmaf, rsmaf );
    
    rsmaf = self.rasp_morpher.morph( rsmaf );
    rsmaf = self.rasp_parser.parse( rsmaf );
    rsmaf = self.rasp_rmrs.convert( rsmaf );
    
    esmaf = self.erg_parser.parse( msmaf );
    
    strout = rsmaf.str_xml();
    strout += "\n\n\n";
    strout += esmaf.str_xml();
    strout += "\n";
    
    return strout.encode( "utf-8" );

  

class Dispatcher:
  
  def __init__( self, istring=None, ofile=None ):

    self.done = False;
    
    self.ofile = None;
    if ofile is None:
      self.ofile = sys.stdout;
    else:
      self.ofile = ofile;
      
    self.istring = None;
    if istring is None:
      self.istring = "The dog barks.";
    else:
      self.istring = istring;

  def get_workitem_by_id( self, id ):
    
    if not id is None:
      return None;
    return ( None, self.istring );
  
  def get_next_workitem( self ):
    
    if self.done:
      return None;
    self.done = True;
    return ( None, self.istring );
  
  def handle_result( self, id, result ):
    
    ifile = cStringIO.StringIO( result );
    rd = pyrmrs.smafpkg.smafreader.SMAFReader( ifile, True );
    it = rd.getAll();
    
    raspsmaf = None;
    
    try:
      raspsmaf = it.next();
    except:
      pyrmrs.globals.logError( self, "failed parsing SMAF returned by remote RASP." );
      pyrmrs.globals.logError( self, "--- INPUT ---" );
      pyrmrs.globals.logError( self, unicode( result, encoding="utf-8" ) );
      pyrmrs.globals.logError( self, "-------------" );
    
    ergsmaf = None;
    try:  
      ergsmaf = it.next();
    except:
      pyrmrs.globals.logError( self, "failed parsing SMAF returned by remote ERG." );
      pyrmrs.globals.logError( self, "--- INPUT ---" );
      pyrmrs.globals.logError( self, unicode( result, encoding="utf-8" ) );
      pyrmrs.globals.logError( self, "-------------" );
    
    self.handle_smafs( id, raspsmaf, ergsmaf );
    
  def handle_smafs( self, id, raspsmaf, ergsmaf ):
    
    self.ofile.write( raspsmaf.str_xml() );
    self.ofile.write( "\n\n\n" );
    self.ofile.write( ergsmaf.str_xml() );
    self.ofile.write( "\n" );
