import os
import socket
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 1234)
print(f"connecting to {server_address}")
sock.connect(server_address)

#Input
mess = input()
cstring = mess.split(" ")

try:
    size = os.path.getsize(os.path.abspath(cstring[1]))
    filename, file_extension = os.path.splitext(os.path.abspath(cstring[1]))
    data = json.dumps(dict(perintah=cstring[0], filename=cstring[1], filesize=size, filetype=file_extension))+"xx"

    print("Data yang dikirim dalam format json")
    print(data)

    sock.sendall(data.encode())
    data = sock.recv(16).decode()

    if data == "OK":
        filee=open(cstring[1],"rb")
        kirim = filee.read(1024)
        while(kirim):
            sock.send(kirim)
            kirim = filee.read(1024)
        print(f"File sukses dikirim!")
finally:
    print("closing")
    sock.close()
