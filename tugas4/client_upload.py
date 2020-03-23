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
mess = input("Nama File yang akan dikirim ke server : ")

try:
    size = os.path.getsize(os.path.abspath(mess))
    filename, file_extension = os.path.splitext(os.path.abspath(mess))
    data = json.dumps(dict(perintah="upload", filename=mess, filesize=size, filetype=file_extension))+"xx"

    print("Data yang dikirim dalam format json")
    print(data)

    sock.sendall(data.encode())
    data = sock.recv(16).decode()

    if data == "OK":
        filee=open(mess,"rb")
        kirim = filee.read(1024)
        while(kirim):
            sock.send(kirim)
            kirim = filee.read(1024)
        print(f"File sukses dikirim!")
finally:
    print("closing")
    sock.close()
