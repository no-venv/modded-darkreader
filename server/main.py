import socket
import return_color
from simple_websocket_server import WebSocketServer,WebSocket
from threading import Thread

connected_clients = []

class SocketServer(WebSocket):

    def handle(self):
        pass
    
    def connected(self):
        connected_clients.append(self)
    
    def handle_close(self):
        connected_clients.remove(self)
 
def NotifySocketTCP():

    """
    
        this socket is for sending the wallpaper location
        so that pywal can generate a palette and send it 
        to connected browsers
    
    """

    HOST = "127.0.0.1"
    PORT = 9484 
    
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET.bind((HOST, PORT))
    SOCKET.listen()

    while True:

        """

            accept socket and fire to all connected clients of new 
            wallpaper colour change
        
        """
        
        conn, addr = SOCKET.accept()

        args = conn.recv(4096).decode().split(";")

        color_dict_index = args[0]
        wallpaper_location = args[1]

        color = return_color.main(
            color_dict_index,
            wallpaper_location
        )
   
        for client in connected_clients:

            client.send_message(color)

        conn.close()
  

server = WebSocketServer("127.0.0.1",9483,SocketServer)
Thread(target=NotifySocketTCP).start()
server.serve_forever()