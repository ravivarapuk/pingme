import socket as sc
import select # This gives os level capabilities


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234


server_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server_socket.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1) 


server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket] # This will handle the list of clients 

clients = {}



def rec_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())

        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False
