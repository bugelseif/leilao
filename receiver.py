import json
import socket
import struct
import threading
from time import sleep

MCAST_GRP = '224.1.2.3'
MCAST_PORT = 5004

def main():
    ip = '127.0.0.1'
    port = 50000

    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect((ip, port))
    threading.Thread(target=grupo_receiver).start()


def grupo_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('', MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print('Aguardando mensagem')
        print(json.loads(sock.recv(10240)))


if __name__ == '__main__':
    main()
