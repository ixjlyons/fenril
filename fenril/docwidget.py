from PyQt5 import QtWidgets

from fenril.ui.docwidget import Ui_DocWidget


class DocWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(DocWidget, self).__init__(parent)

        self.ui = Ui_DocWidget()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()

    def render_pdf(self, filename):
        self.ui.graphicsView.load_document(filename)
