import json
import socket
import threading
from time import sleep

from products import produtos

MCAST_GRP = '224.1.2.3'
MCAST_PORT = 5004

port = 50000

def run(port):
    print(f'Running server at port {port}...')
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('0.0.0.0', port))
        serverSocket.listen(5)
        while True:
            print('Waiting...')
            (clientSocket, address) = serverSocket.accept()
            print(f'connect to: {clientSocket}')
            threading.Thread(
                target=join,
                kwargs={'clientSocket': clientSocket.makefile('rw')},
            ).start()

    except Exception:
        print('RUN error')


def join(clientSocket):
    ...

def grupo_sender():
    while True:
        ttl = 2
        sock = socket.socket(socket.AF_INET,
                            socket.SOCK_DGRAM,
                            socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP,
                        socket.IP_MULTICAST_TTL,
                        ttl)
        while True:
            prods = json.dumps(produtos).encode('utf-8')            
            sock.sendto(prods, (MCAST_GRP, MCAST_PORT))
            sleep(10)
        

threading.Thread(target=grupo_sender).start()


if __name__ == '__main__':
    run(port)
