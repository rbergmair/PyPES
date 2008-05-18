class StringReader:
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
        self.len = len(self.buf)
    # end def __init__
    def read(self, n = 0):
        if n <= 0:
            n = self.len - self.pos
        else:
            n = min(n, self.len - self.pos)
        # end if
        r = self.buf[self.pos : self.pos + n]
        self.pos = self.pos + n
        return r
    # end def read
    def readline(self):
        i = self.buf.find('\n', self.pos)
        return self.read(i + 1 - self.pos)
    # end def readline
    def readlines(self):
        lines = []
        line = self.readline()
        while line:
            lines.append(line)
            line = self.readline()
        # end while
        return lines
    # end def readlines
    # seek/tell etc. are left as an exercise for the reader
# end class StringReader

class StringWriter:
    def __init__(self):
        self.buf = ''
    # end def __init__
    def write(self, s):
        self.buf = self.buf + s
    # end def write
    def getvalue(self):
        return self.buf
    # end def getvalue
# end class StringWriter