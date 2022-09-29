import socket
import threading
from time import sleep

IP = '0.0.0.0'
PORT = 50000

MCAST_GRP = '224.1.2.3'
MCAST_PORT = 5004

def main():
    print('Iniciando servidor...', end='\n\n\n')
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((IP, PORT))
    while True:
        pedido_join, client = serverSock.recvfrom(1024)
        pedido_join = pedido_join.decode()
        print(pedido_join)
        serverSock.sendto(bytes('224.1.2.3', 'utf-8'), client)


def grupo_sender():
    ttl = 2
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM,
                        socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_MULTICAST_TTL,
                    ttl)
    while True:
        sock.sendto(b'Entrou no grupo', (MCAST_GRP, MCAST_PORT))
        sleep(10)

threading.Thread(target=grupo_sender).start()


if __name__ == '__main__':
    main()
