import asyncio
import random

SEND_INTERVAL = random.randint(1, 3)
CLIENT_ID = str(random.randint(1111, 9999))

writer = None


async def data_receiver(reader, main_window):
    while True:
        data = await reader.read(200)
        print('received: {}'.format(data.decode()))

        history_field = main_window.centralWidget().chat_history_edit
        text = history_field.toPlainText()
        history_field.setPlainText(text + '\n' + data.decode())
        history_field.verticalScrollBar().setValue(
            history_field.verticalScrollBar().maximum())


async def data_sender(writer, main_window):
    while True:
        await asyncio.sleep(SEND_INTERVAL)
        print('send: {}'.format(CLIENT_ID))
        writer.write(CLIENT_ID.encode())


def send_message(message, history_field):
    global writer
    writer.write(message.encode())

    text = history_field.toPlainText()
    history_field.setPlainText(text + '\n' + message)
    history_field.verticalScrollBar().setValue(
        history_field.verticalScrollBar().maximum())


async def init_client(loop, main_window):
    read, write = await asyncio.open_connection('127.0.0.1', 4444,
                                                loop=loop)

    asyncio.ensure_future(data_receiver(read, main_window))
    # asyncio.ensure_future(data_sender(writer, main_window))

    global writer
    writer = write
