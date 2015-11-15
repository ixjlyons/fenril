from PyQt5 import QtWidgets

from fenril.ui.docwidget import Ui_DocWidget


class DocWidget(QtWidgets.QWidget):
    """Composite QWidget for displaying a pdf document.

    Attributes
    ----------
    bibentry : dict
        BibTeX entry, see bibtexparser docs for details.
    """

    def __init__(self, bibentry, parent=None):
        super(DocWidget, self).__init__(parent)

        self.bibentry = bibentry

        self.ui = Ui_DocWidget()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()

    def load(self, filename):
        """Load and render the specified PDF file."""
        self.ui.graphicsView.load_document(filename)

    def close(self):
        """Close the document (clean up Poppler etc.)"""
        self.ui.graphicsView.close()
