from PyQt5 import QtWidgets


type_layouts = {
    'article': ['title', 'author', 'journal'],
    'inproceedings': ['title', 'author', 'booktitle']
}


class TitleDisplay(QtWidgets.QTextEdit):

    def __init__(self, entry, parent=None):
        super(TitleDisplay, self).__init__(parent)
        self.setText(entry['title'])

    def row_content(self):
        return (self,)


class AuthorDisplay(QtWidgets.QLineEdit):

    def __init__(self, entry, parent=None):
        super(AuthorDisplay, self).__init__(parent)
        self.setText(entry['author'])

    def row_content(self):
        return ("Authors:", self)


class JournalDisplay(QtWidgets.QLineEdit):

    def __init__(self, entry, parent=None):
        super(JournalDisplay, self).__init__(parent)
        self.setText(entry['journal'])

    def row_content(self):
        return ("Journal:", self)


class ProcDisplay(QtWidgets.QLineEdit):

    def __init__(self, entry, parent=None):
        super(ProcDisplay, self).__init__(parent)
        self.setText(entry['booktitle'])

    def row_content(self):
        return ("Proc. Title:", self)


layout_classes = {
    'title': TitleDisplay,
    'author': AuthorDisplay,
    'journal': JournalDisplay,
    'booktitle': ProcDisplay
}


def inflate(widget, entry):
    layout = widget.layout()
    if layout is None:
        layout = QtWidgets.QFormLayout()
        widget.setLayout(layout)
    else:
        _clear_layout(layout)

    fields = type_layouts[entry['ENTRYTYPE']]
    for field in fields:
        item = layout_classes[field](entry)
        layout.addRow(*item.row_content())


def _clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        child.widget().deleteLater()
