import sys
import socket
import threading
from queue import Queue

host ='localhost'

def konek(port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(90000)
    try:
        # Bind the socket to the port
        server_address = (host, port)
        print(f"starting up on {server_address}")
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print("waiting for a connection")
            connection, client_address = sock.accept()
            print(f"connection from {client_address}")

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(32)
                print(f"received {data}")
                if data:
                    print("sending back data")
                    connection.sendall(data)
                else:
                    #print >>sys.stderr, 'no more data from', client_address
                    #print(f"no more data from {client_address}")
                    break
    except:
            # # Clean up the connection
        connection.close()

que = Queue()
def c_port():
    while True:
        port_c = que.get()
        konek(port_c)
        que.task_done()

for port in range(31000,31003):
    que.put(port)

for scan in range(1,4):
    t = threading.Thread(target=c_port)
    t.daemon=True
    t.start()
que.join()
