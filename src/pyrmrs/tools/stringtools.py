import md5;
import string;


def unindent( stri ):
  
  if stri[0] != "\n":
    return stri;
  
  if isinstance( stri, str ):
    indent = ""; 
  else:
    indent = u"";
    
  for ch in stri[1:]:
    if string.whitespace.find( ch ) == -1:
      break;
    indent += ch;
  
  return stri.replace( "\n"+indent, "\n" );
      



def debug_format( stri ):
  
  out = u"";
  for ch in stri:
    if ord(ch) < 32:
      out += u"[\\%d]" % ord(ch);
    elif string.printable.find( ch ) != -1:
      out += ch;
    else:
      out += u"[\\%d]" % ord(ch);
  return out;



def crude_hashcode( s ):
  
  md5sum = md5.new();
  i = -1;
  
  for ch in s:
    if ord(ch) > 32 and \
       string.printable.find( ch ) != -1 and \
       string.whitespace.find( ch ) == -1:
      md5sum.update( ch );

  return md5sum.digest();

def crude_match( s1, s2 ):
  
  return crude_hashcode( s1 ) == crude_hashcode( s2 );



def decode_lines( block ):
  
  if block.find( "\\\n" ) != -1:
    st = "";
    if block[ 0 ] == "\n":
      block = block[ 1: ];
    for ch in block:
      if ch == " ":
        st += " ";
      else:
        break;
    block = block.replace( "\\\n"+st, "" );
  return block;

def encode_lines( line, line_len=78 ):
  
  rslt = "";
  i = 0;
  while True:
    rslt += line[ i : i + line_len - 1 ];
    i += line_len-1;
    if i >= len( line ):
      break;
    rslt += "\\\n";
  return rslt;
