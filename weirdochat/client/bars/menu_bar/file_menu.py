from qtpy.QtWidgets import QAction, QMenu, qApp


class FileMenu(QMenu):
    def __init__(self, *args):
        super().__init__(*args)

        self.setTitle('&File')

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)
        self.addAction(exit_action)
