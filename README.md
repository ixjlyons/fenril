fenril
======

**This project is a work in progress. Most of this README is a lie.**

fenril is a Qt5 reference viewer. The name is an anagram of "nil" (meaning nothing)
and "ref" (meaning reference). It is not a reference *manager*. It is the
product of my frustration with reference managers that do too much.

You need the following:

* A BibTeX library with all of your references in it. You manage this yourself.
  When you want to add an item, fire up your [text editor of
  choice](http://www.vim.org/) and add it.

* A folder of pdfs corresponding to the items in your library. The name of the
  file should match the citation ID. If you update the citation ID in your bib
  file, you should update the name of the pdf as well.

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


Migrating
---------

I made a little script to migrate from Mendeley
(`tools/migrate_from_mendeley.py`). You should set up Mendeley to
sync your library with a single BibTeX file. Point the script to that file, and
you should have a new bib file stripped of a few of the keys Mendeley adds and
a folder with all of your pdfs renamed to the corresponding citation ID.


Acknowledgments
---------------

The embedded pdf viewer code has been directly guided by
[PdfViewer](http://qt-apps.org/content/show.php?content=149637). Displaying
a pdf is certainly not a trivial exercise, so that project has been incredibly
helpful.
