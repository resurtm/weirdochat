import sys

from qtpy.QtWidgets import QApplication

from weirdochat.client.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


if '__main__' == __name__:
    main()
