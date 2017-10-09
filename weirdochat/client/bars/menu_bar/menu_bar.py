from qtpy.QtWidgets import QMenuBar

from weirdochat.client.bars.menu_bar.file_menu import FileMenu


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        self.addMenu(FileMenu(self))
