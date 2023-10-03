import socket
import return_color
from simple_websocket_server import WebSocketServer,WebSocket
from threading import Thread
connected_clients = []

class SocketServer(WebSocket):

    def handle(self):
        return return_color.main()
    
    def connected(self):
        connected_clients.append(self)
        self.send_message(return_color.main())
    
    def handle_close(self):
        connected_clients.remove(self)
 
def NotifySocketTCP():

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

        color = return_color.main()
        
        for client in connected_clients:

            client.send_message(color)

        conn.close()
  

server = WebSocketServer("127.0.0.1",9483,SocketServer)
Thread(target=NotifySocketTCP).start()
server.serve_forever()