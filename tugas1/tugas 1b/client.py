import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)
mess = input("File name that you request to server : ")
intt = 0
try:
    sock.sendall(mess.encode())
    data = sock.recv(16)
    file_size = int.from_bytes(data,byteorder='big')
    current_size =0
    with open("hasil_download_"+mess,'wb') as file_to_write :
        while  current_size < file_size:
            data = sock.recv(1024)
            if not data:
                    break
            if len(data)+current_size>file_size:
                data = data[:file_size-current_size]
                data_dump = data[(file_size-current_size):current_size]
                intt =1
            file_to_write.write(data)
            current_size = current_size + len(data)
    file_to_write.close()

    #respone
    if intt == 0:
        abc = sock.recv(1024)
        print(abc.decode())
        intt = 0

finally:
    print('closing')
    sock.close()
