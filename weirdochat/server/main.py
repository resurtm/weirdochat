import asyncio

clients = []


class ProtocolFactory(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info('peername')
        print('connection established: {}'.format(self.peername))
        clients.append(self)

    def data_received(self, data):
        print('data received: {}'.format(data.decode()))
        for client in clients:
            if client is self:
                continue
            # client.transport.write(
            #     "{}: {}".format(self.peername, data.decode()).encode())
            client.transport.write(data)

    def connection_lost(self, ex):
        print('connection lost: {}'.format(self.peername))
        clients.remove(self)


def main():
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ProtocolFactory, '127.0.0.1', 4444)
    server = loop.run_until_complete(coro)

    for socket in server.sockets:
        print('serving on {}'.format(socket.getsockname()))

    loop.run_forever()


if '__main__' == __name__:
    main()
