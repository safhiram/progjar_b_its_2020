from socket import *
import socket
import threading
import logging
import json
from person_machine import PersonMachine
import os
pm = PersonMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        command="";test=0
        while True:
            diterima = self.connection.recv(16)
            command= command + diterima.decode()
            print(command)
            if command[-2:]=="xx":
                command=command[:len(command)-2]
                command=json.loads(command)

                if command['perintah']=="list":
                    hasil= pm.proses(command)
                    if hasil == "null":
                        hasil = "data kosong"
                    hasil = hasil+"\r\n"
                    self.connection.sendall(hasil.encode())
                    break

                if command['perintah']=="upload":
                    hasil = pm.proses(command)
                    print(hasil)
                    self.connection.sendall(hasil.encode())
                    filee=open('hasil_upload_'+ command['filename'],'wb')
                    dataa = self.connection.recv(1024)
                    while(dataa):
                        filee.write(dataa)
                        dataa = self.connection.recv(1024)
                    filee.close()
                    break

                if command['perintah']=="download":
                    hasil = pm.proses(command)
                    if hasil != "null":
                        file_kirim = command['filename']
                        print("file_kirim "+file_kirim)
                        #jika data ada
                        if os.path.isfile(file_kirim):
                            self.connection.sendall(hasil.encode())
                            print("file yang direquest ada")
                            if hasil!="null":
                                with open(file_kirim, 'rb') as file_to_send:
                                    for data2 in file_to_send:
                                        self.connection.sendall(data2)
                                file_to_send.close()
                                print("file berhasil dikirimkan")
                                break

        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('127.0.0.1', 1234))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()

if __name__ == "__main__":
    main()

