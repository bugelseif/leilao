import socket

group = '224.1.2.3'
port = 5004

ttl = 2

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
for i in range(3):
    sock.sendto(b'ola!', (group, port))
