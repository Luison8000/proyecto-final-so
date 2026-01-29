import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 6000))

print(" Buscando servers...")

while True:
    data, addr = s.recvfrom(1024)
    print(f" Encontrado: {addr[0]}")
