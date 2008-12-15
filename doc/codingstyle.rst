*******************
PyPES Coding Style
*******************



1. Namespace for Package and Module Names
=========================================

In languages like Python or Java, it's perfectly possible to mess up
the namespace of the language not only for your own libraries, but for
all other programmes and libraries on the system, which may have to
share the same PYTHONPATH (in Java it's called a CLASSPATH) as you.

Error conditions related to the exact environment in which your code
will be called are not always easy to test for. It may all work
perfectly fine when you're testing and then break for "mysterious
reasons", usually when a user tries to install your library or, worse
even, someone else's.

Therefore, it is absolutely imperative that you understand Python's
naming mechanism, before you write a new package or module, or before
you write a single ``import`` statement, for that matter.

Knowing how exactly Python will resolve a given name isn't always
straightforward. The exact process is documented as "platform specific".

Generally, if you import from a name like ``foo``, python will look for
a file called ``foo.py`` to contain the code for module ``foo``. If you
import from a name like ``this.is.foo.bar``, python will look for a file
called ``bar.py`` in a directory called ``this/is/foo``, provided that
directory also contains a ``__init__.py``.

But the question is *where* will the interpreter go looking for these
files and directories?

If the interpreter has never imported a module of that name before,
it will first look in the directory in which the script resides, i.e.
that python file which has been passed as a parameter to the
interpreter, or it will look in the current working directory, if
the script was read from standard input.

If the file is not to be found there, it will look for it in the
standard library.

If it is not in the standard library either, then each directory of
the PYTHONPATH will be tried in turn. As an additional complication,
some users put the current working directory into their PYTHONPATH.

So when you import ``foo.bar`` and there are different bits of
code sitting in a file ``bar.py`` in a directory ``foo`` visible
to the user's interpreter, you are potentially in trouble.

* You don't normally know the script that has called your module,
  where it resides, and what other python files are sitting in that
  directory.
* You don't know how the user has set their PYTHONPATH.  You don't
  know whether it contains the current working directory, and what
  other libraries are listed in the PYTHONPATH before or after yours
  and what names are used by those libraries.

In PyPES we follow the following conventions:

Definitions:

* A *fully qualified name* is the name under which we import
  a module, assuming

  - either that the module resides in a subdirectory of a
    directory listed as an absolute pathname in the PYTHONPATH,
  - or that the module is in the Python standard library.

* *Library modules* are all modules that are accessible to
  Python by such a fully qualified name.
* *Scripts* are python source files that have been called
  by passing their filename as a parameter to the python
  interpreter, either directly, or by calling the interpreter
  using the ``#!`` directive.

Concerning our own modules:

1. We assume the ``PyPES/src`` directory is in the user's
   PYTHONPATH, or the files have been copied there.
2. We always import modules by their fully qualified names.

All PyPES modules thereby become library modules and are
called as such.

Concerning other people's scripts and modules:

3. A fully qualified name of a module provided by PyPES
   *must always* have ``pypes.`` or ``pypestest.`` as
   a prefix.

This ensures we don't mask other people's modules. -- Except
in the unlikely event that someone else has decided to call
something ``pypes``.

Concerning the working directory:

4. A dot-separated string representing the fully qualified
   name of a PyPES module *must never* have as a substring
   the prefix of another library module's fully qualified
   name.  This includes, in particular, modules provided by
   the standard library and PyPES modules.

This ensures that the right module can be found, even if the
present working directory is listed in the user's PYTHONPATH
before the ``PyPES/src`` directory and a script is executed
from anywhere inside the ``PyPES/src`` directory.

Concerning our own scripts and the ``bin`` directory:

5. We always call scripts from the dedicated ``PyPES/bin``,
   or ``PyPES/src/bin`` "binary" directories.
6. The binary directories *must not* contain a file
   ``__init__.py`` either directly or in a subdirectory.
7. The directories ``PyPES/bin`` and ``PyPES/src/bin``
   must never contain a file called ``X.py`` when
   ``X.`` is the prefix of a module's name. Again, this
   includes modules provided by the standard library and
   PyPES modules.

This ensures that we never mask such a module whose
name begins with ``X.`` for ourselves or beginning with
``bin.X.`` for ourselves or for any other library on
the system.



2. Namespace for Local Names
============================

Lorem ipsum.
