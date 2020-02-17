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
    file_kirim = connection.recv(1024)
    file_kirim = file_kirim.decode()

    #jika data ada
    if os.path.isfile(file_kirim):
        print("file that you request is available.")
        size_file = os.path.getsize(file_kirim)
        connection.send(size_file.to_bytes(4,byteorder='big'))
        with open(file_kirim, 'rb') as file_to_send:
            for data in file_to_send:
                connection.sendall(data)
        file_to_send.close()

        msg = 'Success for download ' + file_kirim
        connection.sendall(msg.encode())
    else :
        print("file that you request is not available")

    connection.close()


