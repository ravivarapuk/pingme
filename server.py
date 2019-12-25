import socket as sc
import select # This gives os level capabilities


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 8081


server_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server_socket.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1) 


server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket] # This will handle the list of clients 

clients = {} # PII with respect to the clients that are connected



def rec_message(client_socket):
    """
    Utility to recv messages
    """
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    # Select takes three params as lists which are the read_list, write_list and error on sockets
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_addr = server_socket.accept()

            user = rec_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new connection from {client_addr[0]}.{client_addr[1]} username: {user['data'].decode('utf-8')}")

        else:
            message = rec_message(notified_socket)

            if message is False:
                print(f"Closed conn from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Receiveed msg from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        
