from os.path import isfile
import socket
import sys

def send(color : str):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1",9484))
    s.send(bytes(color,"utf-8"))
    s.close()


def wallpaper_color(wallpaper : str):

    from haishoku.haishoku import Haishoku
    color = Haishoku.getDominant(wallpaper)
    return '{:02x}{:02x}{:02x}'.format(color[0],color[1],color[2])

if __name__ == "__main__":

    if not sys.argv.__len__() > 1:
        print("""
        please provide an argument
        
        python3 interface.py FF00FF 
        
        or 
              
        python3 interface.py /home/me/Pictures/whatever.png

        """)
        exit()
    
    argument = sys.argv[1]

    color = isfile(argument) and wallpaper_color(argument) or argument

    send(color)