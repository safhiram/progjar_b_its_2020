import sys
import socket
import os.path

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    data = connection.recv(1024)
    data = data.decode()
    print(f"Berhasil dikirim {data}")

    filee=open("diterima_"+data,'wb')
    dataa = connection.recv(1024)
    while(dataa):
        filee.write(dataa)
        dataa = connection.recv(1024)
    print("Transfer File Sukses")

    filee.close()

    # Clean up the connection
    connection.close()
