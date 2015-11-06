fenril
======

**This project is a work in progress. Most of this README is a lie.**

fenril is a reference viewer. The name is an anagram of "nil" (meaning nothing)
and "ref" (meaning reference). It is not a reference *manager*.

You need the following:

* A BibTeX library with all of your references in it. You manage this yourself.
  When you want to add an item, fire up your [text editor of
  choice](http://www.vim.org/) and add it.

* A folder of pdfs corresponding to the items in your library. The name of the
  file should match the citation ID.

* A config file specifying where the above two items are located on your
  computer.

fenril loads up the BibTeX file and shows the items to you in an organized
format. You can sort, filter, and extract sets of items to separate BibTeX
files. Finally, you can view your pdfs in the embedded viewer.


Dependencies
------------

* [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)

* [python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser)

* [python-poppler-qt5](https://github.com/wbsoft/python-poppler-qt5)
