import json
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10001)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    #pengiriman
    data = 'GET / HTTP/1.0'+"\r\n\r\n"
    sock.send(data.encode())
    receivemsg = ""
    while True:
       dataa = sock.recv(32)
       if (dataa):
           receivemsg = receivemsg + dataa.decode()  #data harus didecode agar dapat di operasikan dalam bentuk string
           if receivemsg[-4:]=='\r\n\r\n':
               print("Isi Pesan:" + receivemsg)
               break

finally:
    print("closing")
    sock.close()

