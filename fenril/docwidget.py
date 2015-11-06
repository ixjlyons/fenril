import popplerqt5
from PyQt5 import QtWidgets, QtGui
import time

from fenril.ui.docwidget import Ui_DocWidget


class DocWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(DocWidget, self).__init__(parent)

        self.ui = Ui_DocWidget()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()

    def render_pdf(self, filename):
        self.ui.graphicsView.load_document(filename)
        #doc = popplerqt5.Poppler.Document.load(filename)
        #doc.setRenderHint(popplerqt5.Poppler.Document.Antialiasing)
        #doc.setRenderHint(popplerqt5.Poppler.Document.TextAntialiasing)

        #for i in range(doc.numPages()):
        #    page = doc.page(i)

        #    t = time.time()
        #    print("rendering to image")
        #    image = page.renderToImage()
        #    tn = time.time()
        #    print("  %.3f" % (tn-t))

        #    t = tn
        #    painter = QtGui.QPainter()
        #    print("rendering to painter")
        #    page.renderToPainter(painter)
        #    tn = time.time()
        #    print("  %3f" % (tn-t))


        #    #pixmap = QtGui.QPixmap.fromImage(image)
        #    #self.scene.addPixmap(pixmap)

        ##self.scene.setSceneRect(image.rect())

        #self.ui.graphicsView.setScene(self.scene)
