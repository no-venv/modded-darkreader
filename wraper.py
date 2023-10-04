import socket
import sys

def send(color,wal):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1",9484))
    s.send((str(color)+";"+wal).encode())
    s.close()

if __name__ == "__main__":
    send(sys.argv[1],sys.argv[2])