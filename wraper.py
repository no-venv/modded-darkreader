import socket
import sys

color = sys.argv[1]
wallpaper_loc = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",9484))
s.send((color+";"+wallpaper_loc).encode())
s.close()