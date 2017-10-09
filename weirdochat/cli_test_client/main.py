import asyncio
import random

SEND_INTERVAL = random.randint(1, 3)
CLIENT_ID = str(random.randint(1111, 9999))


async def data_receiver(reader):
    while True:
        data = await reader.read(200)
        print('received: {}'.format(data.decode()))


async def data_sender(writer):
    while True:
        await asyncio.sleep(SEND_INTERVAL)
        print('send: {}'.format(CLIENT_ID))
        writer.write(CLIENT_ID.encode())


async def init_client(loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 4444,
                                                   loop=loop)

    asyncio.ensure_future(data_receiver(reader))
    asyncio.ensure_future(data_sender(writer))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_client(loop))

    loop.run_forever()


if '__main__' == __name__:
    main()
