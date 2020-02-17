import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)
mess = input("Nama File yang akan dikirim ke server : ")

try:
    # Send data
    sock.sendall(mess.encode())
    filee=open(mess,"rb")
    kirim = filee.read(1024)
    while(kirim):
        sock.send(kirim)
        kirim = filee.read(1024)

    print(f"File sukses dikirim!")

finally:
    print("closing")
    sock.close()
