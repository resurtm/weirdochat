import asyncio
import sys

from qtpy.QtWidgets import QApplication
from quamash import QEventLoop

from weirdochat.client.client import init_client
from weirdochat.client.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    # sys.exit(app.exec_())

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    loop.run_until_complete(init_client(loop, main_window))
    loop.run_forever()


if '__main__' == __name__:
    main()
