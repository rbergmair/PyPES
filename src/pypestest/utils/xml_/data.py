INDATA = r"""<?xml version="1.0" encoding="UTF-8"?>

  <!DOCTYPE html
       PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

  <head>
    <title>This is a test.</title>
  </head>

  <body>

  <h1>This is a test.</h1>

  <p>
    This is a <strong>test</strong>.
    This is another test.
  </p>

  </body>

  </html>
  """;

OUTDATA = """<?xml version="1.0" encoding="UTF-8"?>

  <!DOCTYPE html
       PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

  <head>
    <title>This is a test.</title>
  </head>

  <body>

  <h1>This is a test.</h1>

  <p>
    This is a <strong>*TEST*</strong>.
    This is another TEST.
  </p>

  </body>

  </html>
  """;
