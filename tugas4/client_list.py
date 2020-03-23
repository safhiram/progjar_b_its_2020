import json
import pandas as pd
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 1234)
print(f"connecting to {server_address}")
sock.connect(server_address)

mess = input()

try:
    message = json.dumps(dict(perintah=mess))+"xx"

    print("Data dan perintah yang dikirim dalam format json")
    print(message)

    sock.sendall(message.encode())

    daftar_list=""
    print(f"Daftar List yang tersedia")
    while True:
        diterima = sock.recv(16)
        daftar_list = daftar_list + diterima.decode()
        if daftar_list[-2:] == "\r\n":
            hasil = json.loads(daftar_list)
            print(pd.DataFrame.from_dict(hasil))
            break
finally:
    print("closing")
    sock.close()
