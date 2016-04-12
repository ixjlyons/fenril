# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.libraryTab = QtWidgets.QWidget()
        self.libraryTab.setObjectName("libraryTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.libraryTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.libraryTab)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.libraryTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(250, 35))
        self.dockWidget.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.menu_File.addAction(self.actionQuit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.libraryTab), _translate("MainWindow", "Library"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))

