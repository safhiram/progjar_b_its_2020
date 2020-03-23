import json
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 1234)
print(f"connecting to {server_address}")
sock.connect(server_address)

#input
mess = input()
cstring = mess.split(" ")

try:
    data = json.dumps(dict(perintah=cstring[0], filename=cstring[1]))+"xx"

    print("Data yang dikirim dalam format json")
    print(data)

    #dikirimi data ada arau tidak
    sock.send(data.encode())
    data = sock.recv(1000).decode()

    #jika sudah ada
    if data!="null":
        with open("hasil_download_"+cstring[1], 'wb') as file_receive:
            while True:
                diterima = sock.recv(1024)
                if not diterima:
                    print("File berhasil didownload!")
                    break
                file_receive.write(diterima)
        file_receive.close()
finally:
    print("closing")
    sock.close()
