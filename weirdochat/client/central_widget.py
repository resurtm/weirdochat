from qtpy.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, \
    QPushButton

from weirdochat.client.client import send_message


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.chat_history_edit = None
        self.init_ui()

    def init_ui(self):
        chat_history_label = QLabel('Chat history')
        self.chat_history_edit = QTextEdit()
        self.chat_history_edit.setReadOnly(True)
        # self.chat_history_edit.setPlainText('test')

        message_label = QLabel('Message')
        self.message_edit = QLineEdit()
        message_button = QPushButton('Send')
        message_button.clicked.connect(self.message_button_clicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(chat_history_label, 0, 0, 1, 3)
        grid.addWidget(self.chat_history_edit, 1, 0, 1, 3)

        grid.addWidget(message_label, 2, 0, 1, 1)
        grid.addWidget(self.message_edit, 2, 1, 1, 1)
        grid.addWidget(message_button, 2, 2, 1, 1)

        self.setLayout(grid)

    def message_button_clicked(self):
        send_message(self.message_edit.text(), self.chat_history_edit)
        # WRITER.write(self.message_edit.toPlainText().encode())
