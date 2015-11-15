import os
import bibtexparser

from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtWidgets import QMainWindow

from fenril.ui.mainwindow import Ui_MainWindow
from fenril import docwidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None, bibfile=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if bibfile:
            self.init_bib(bibfile)

        self.doc_tabs = []
        self.ui.tableView.doubleClicked.connect(self.doubleclick_callback)

        self.init_tab_widget()

    def init_tab_widget(self):
        self.ui.tabWidget.tabCloseRequested.connect(self.on_tab_close)

    def init_bib(self, bibfile):
        self.bibfile = bibfile
        bib_data = None
        with open(bibfile) as f:
            bib_data = bibtexparser.load(f)

        if bib_data is None:
            # TODO show warning and return
            return

        model = Model(bib_data.entries)
        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.horizontalHeader().sortIndicatorChanged.connect(
            self.ui.tableView.sortByColumn)

    def on_tab_close(self, index):
        if index == 0:
            return
        self.ui.tabWidget.removeTab(index)
        del(self.doc_tabs[index-1])

    def doubleclick_callback(self, index):
        data = self.ui.tableView.model().item(index)
        widget = docwidget.DocWidget()
        self.doc_tabs.append({'data': data, 'widget': widget})
        self.ui.tabWidget.addTab(widget, _get_val(data, 'title'))

        filepath = os.path.abspath(
            os.path.join(
                os.path.dirname(self.bibfile),
                'pdfs',
                data['ID'] + '.pdf'))
        if os.path.isfile(filepath):
            widget.render_pdf(filepath)

        self.ui.tabWidget.setCurrentWidget(widget)


class Model(QAbstractTableModel):

    COLS = ['author', 'title', 'year']

    def __init__(self, entries, parent=None):
        super(Model, self).__init__(parent)
        self.entries = entries

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.COLS[section]

        elif role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return self._align_col(section)

        else:
            return QVariant()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            c = index.column()
            entry = self.entries[index.row()]
            return _get_val(entry, self.COLS[c])

        elif role == Qt.TextAlignmentRole:
            return self._align_col(index.column())

        else:
            return QVariant()

    def sort(self, column, order=Qt.AscendingOrder):
        self.layoutAboutToBeChanged.emit()

        colname = self.COLS[column]
        if order == Qt.AscendingOrder:
            self.entries = sorted(self.entries, key=lambda k: k[colname])
        else:
            self.entries = sorted(
                self.entries, key=lambda k: k[colname], reverse=True)

        self.layoutChanged.emit()

    def _align_col(self, col):
        if self.COLS[col] == 'year':
            return Qt.AlignVCenter + Qt.AlignRight
        else:
            return Qt.AlignVCenter + Qt.AlignLeft

    def item(self, index):
        return self.entries[index.row()]

    def rowCount(self, parent=QModelIndex()):
        return len(self.entries)

    def columnCount(self, parent=QModelIndex()):
        return 3


def _get_val(entry, key):
    try:
        ret = entry[key]
    except KeyError:
        ret = ""
    return ret
