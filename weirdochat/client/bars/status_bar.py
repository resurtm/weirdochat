from qtpy.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()

        self.showMessage('Ready')
