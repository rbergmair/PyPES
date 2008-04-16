def prepreprocess( str ):
  str = str.replace( u" \u2014 ", " - " );
  str = str.replace( u"\u2014", " - " );
  str = str.replace( u"\u201c", '"' );
  str = str.replace( u"\u201d", '"' );
  str = str.replace( u"\u2019", "'" );
  str = str.replace( u"\u2026", "..." );
  return str;