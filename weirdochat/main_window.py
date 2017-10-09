from qtpy.QtWidgets import QMainWindow, QDesktopWidget

from weirdochat.bars.menu_bar import MenuBar
from weirdochat.bars.status_bar import StatusBar
from weirdochat.central_widget import CentralWidget


class MainWindow(QMainWindow):
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 800
    WINDOW_TITLE = 'weirdochat'

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(CentralWidget())
        self.setMenuBar(MenuBar())
        self.setStatusBar(StatusBar())

        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.move(QDesktopWidget().rect().center() - self.rect().center())
        self.setWindowTitle(self.WINDOW_TITLE)
        self.show()
