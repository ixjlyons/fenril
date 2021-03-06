import sys
import argparse

from PyQt5.QtWidgets import QApplication

from fenril import mainwindow


def main():
    parser = argparse.ArgumentParser(
        description="Minimal BibTeX reference manager and PDF viewer.")
    parser.add_argument(
        '-c', '--config',
        help="Config file.")
    parser.add_argument(
        '-b', '--bibfile',
        help="BibTeX file to use for the library.")
    parser.add_argument(
        '-p', '--pdfdir',
        help="Path to directory containing PDF documents.")
    args = parser.parse_args()

    app = QApplication([])
    main_window = mainwindow.MainWindow(bibfile=args.bibfile,
                                        pdfdir=args.pdfdir)
    main_window.show()
    app.exec_()
    app.deleteLater()
    sys.exit(0)
