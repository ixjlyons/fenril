# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/docwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DocWidget(object):
    def setupUi(self, DocWidget):
        DocWidget.setObjectName("DocWidget")
        DocWidget.resize(582, 342)
        self.gridLayout = QtWidgets.QGridLayout(DocWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(DocWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.graphicsView = PdfView(self.splitter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.tabWidget.addTab(self.infoTab, "")
        self.notesTab = QtWidgets.QWidget()
        self.notesTab.setObjectName("notesTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.notesTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.notesTextEdit = QtWidgets.QTextEdit(self.notesTab)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridLayout_2.addWidget(self.notesTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.notesTab, "")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(DocWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DocWidget)

    def retranslateUi(self, DocWidget):
        _translate = QtCore.QCoreApplication.translate
        DocWidget.setWindowTitle(_translate("DocWidget", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), _translate("DocWidget", "Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notesTab), _translate("DocWidget", "Notes"))

from fenril.pdfview import PdfView
