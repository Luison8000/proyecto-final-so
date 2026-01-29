import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    s.sendto(b"SERVER_PROCESOS", ("255.255.255.255", 6000))
    time.sleep(5)
