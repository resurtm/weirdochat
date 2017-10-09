from qtpy.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QPushButton


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        chat_history_label = QLabel('Chat history')
        chat_history_edit = QTextEdit()
        chat_history_edit.setReadOnly(True)

        message_label = QLabel('Message')
        message_edit = QLineEdit()
        message_button = QPushButton('Send')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(chat_history_label, 0, 0, 1, 3)
        grid.addWidget(chat_history_edit, 1, 0, 1, 3)

        grid.addWidget(message_label, 2, 0, 1, 1)
        grid.addWidget(message_edit, 2, 1, 1, 1)
        grid.addWidget(message_button, 2, 2, 1, 1)

        self.setLayout(grid)
