# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/docwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DocWidget(object):
    def setupUi(self, DocWidget):
        DocWidget.setObjectName("DocWidget")
        DocWidget.resize(582, 342)
        self.gridLayout = QtWidgets.QGridLayout(DocWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PdfView(DocWidget)
        brush = QtGui.QBrush(QtGui.QColor(117, 117, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(DocWidget)
        QtCore.QMetaObject.connectSlotsByName(DocWidget)

    def retranslateUi(self, DocWidget):
        _translate = QtCore.QCoreApplication.translate
        DocWidget.setWindowTitle(_translate("DocWidget", "Form"))

from fenril.pdfview import PdfView
