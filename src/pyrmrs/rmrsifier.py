import xml.sax;
import xml.sax.handler;

import pyrmrs.globals;

import delphin.pet;
import delphin.raspsent;
import delphin.fspp;

STDINDENT = "  ";



class RMRSifier( xml.sax.handler.ContentHandler ):

  tags = {};
  parser = None;
  copythrough = True;
  out = None;
  chbuf = [];
  
  preprocsurface = "";
  realsurface = "";
  
  petctrl = None;
  raspsentctrl = None;
  fsppctrl = None;
  
  active_tags = None;
  atindent = "";
  
  indent = "";
  
  succ = 0;
  total = 0;
  cnts = [];
  
  def __init__( self, ifile, ofile, active_tags = [ 't', 'h', 'proposition' ] ):

    self.succ = 0;
    self.total = 0;
    self.cnts = [];
    
    self.tags = {};
    self.copythrough = True;
    self.out = ofile;
    
    self.chbuf = [];
    
    self.parser = xml.sax.make_parser( \
      [ "xml.sax.xmlreader.IncrementalParser" ] );
    self.parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    self.parser.setContentHandler( self );

    self.preprocsurface = "";
    self.realsurface = "";
    
    self.active_tags = active_tags;
    self.active_tags.append( "pp" );
    
    self.petctrl = delphin.pet.PET( 5, 5 );
    self.raspsentctrl = delphin.raspsent.RaspSentenceSplitter();
    self.fsppctrl = delphin.fspp.FSPP();
    
    reading_indent = True;
    self.indent = "";

    while True:
      data = ifile.read( 1 );
      if data == "":
        break;
      data = data.replace( "\t", STDINDENT );
      if self.copythrough:
        ofile.write( data );
      if reading_indent:
        if data.find( " " ) != -1:
          self.indent += data;
        else:
          reading_indent = False;
      if data == "\n":
        reading_indent = True;
        self.indent = "";
      self.parser.feed( data );

  def startElement( self, name, attrs ):
    
    if not self.tags.has_key( name ):
      self.tags[ name ] = 1;
    else:
      self.tags[ name ] += 1;
      
    if name in self.active_tags:
      self.copythrough = False;
      self.atindent = self.indent;
      self.preprocsurface = None;
      self.surface = None;
      self.chbuf.append( "" );
    
  def characters( self, content ):
    
    if not self.copythrough:
      self.chbuf[ len( self.chbuf )-1 ] += content;

  
  def rmrsify( self, surface ):
    
    surface = surface.strip();
    
    pyrmrs.globals.logDebug( self, "|>%s<|" % surface );

    self.out.write( "\n" + self.atindent + "<analysis>" );
    self.out.write( "\n" + self.atindent );
    
    for sent in self.raspsentctrl.txtstr_to_sentstrs( surface ):

      pyrmrs.globals.logDebug( self, "|>%s<|" % sent );
      
      self.out.write( "\n" + self.atindent + "<sentence>" );
      self.out.write( "\n" + self.atindent );
      
      err = None;
      cnt = 0;
      
      try:
        
        for smaf in self.fsppctrl.sentstr_to_smafs( sent ):
          for rmrs in self.petctrl.smaf_to_rmrss( smaf ):
            
            cnt += 1;
  
            self.out.write( "\n" + self.atindent + "<!--\n" );
            self.out.write( rmrs.str_pretty() );
            self.out.write( "\n" + self.atindent + "-->\n" + self.atindent );
            self.out.write( \
              rmrs.str_xml().replace( "\n", "\n" + self.atindent ) );
            self.out.write( "\n" );
      
      except delphin.pet.PETError, e:
        self.out.write( "<error>\n" );
        self.out.write( self.atindent + self.atindent );
        self.out.write( e.errmsg.replace( "\n", "\n"+self.atindent+STDINDENT ) );
        self.out.write( "\n" + self.atindent + "</error>" );
        
        err = e;
        
      self.cnts.append( cnt );
      
      self.total += 1;
      if err == None:
        print "   --> %s" % sent;
        self.succ += 1;
      else:
        print "%2d --> %s" % ( err.errno, sent );
        #if err.errno != 1:
        #  print "       " + err.errmsg;

      self.out.write( "\n" + self.atindent + "</sentence>" );
      
    self.out.write( "\n" + self.atindent + "</analysis>" );
    self.out.write( "\n" );
    
  def endElement( self, name ):
    
    if name in self.active_tags:
    
      text = self.chbuf.pop();
      text = pyrmrs.globals.decode_str( text );
      text = text.strip();

      if name == "pp":
        self.preprocsurface = text;
      else:
        self.surface = text;

      if self.preprocsurface == None:
        self.preprocsurface = self.surface;
        
      self.out.write( "\n" + self.atindent );
      self.out.write( "<surface>\n" );
      self.out.write( \
        self.atindent+STDINDENT+
        pyrmrs.globals.encode_str( self.surface, 80-len(self.atindent+STDINDENT) ).replace( \
          "\n", "\n"+self.atindent+STDINDENT ) );
        
      self.out.write( "\n" + self.atindent + "</surface>" );

      self.preprocsurface = self.preprocsurface.replace( "\\ ", "" );

      self.rmrsify( self.preprocsurface );
      
      self.copythrough = True;
      self.out.write( self.atindent + "</%s>" % name );
