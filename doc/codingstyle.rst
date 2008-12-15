*******************
PyPES Coding Style
*******************

Package and Module Names, import-namespace
==========================================

don't mask the standard library
-------------------------------

Make sure your package names and module names are never a
prefix of a package name or module name that is accessible
from the user's PYTHONPATH (whatever that may be).
