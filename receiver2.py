import socket
import struct
import threading
import sys


IP = '127.0.0.1'
PORT = 50000

MCAST_GRP = '224.1.2.3'
MCAST_PORT = 5004

def main():
    print('Iniciando cliente...')
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    entra = input("Gostaria de entrar no grupo?")
    if entra != 'sim':
        sys.exit()
    else:
        clientSock.sendto(bytes('join', 'utf-8'), (IP, PORT))
        pedido_join = clientSock.recv(1024)
        print(f'Recebido: {pedido_join}', end='\n\n\n')
        threading.Thread(target=grupo_receiver).start()
    

def grupo_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('', MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print('Aguardando mensagem')
        print(sock.recv(10240))

if __name__ == '__main__':
    main()
