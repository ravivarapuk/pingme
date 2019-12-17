import socket as soc

###############################################################################################
# Socket -> It is an endpoint(at an ip on a port addr) that sends and receives messages or data
###############################################################################################

# Initialize the socket object with socket family type: AF_INET -> IPv4 & SOCK_STREAM -> streaming socket
s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

# Bind the host and the port addr to the socket
s.bind((soc.gethostname(), 1234))


s.listen(5)   # the arg 5 decides the queue, in case of heavy load

while True:
    client_socket, address = s.accept()
    print(f"Conn. from {address} is established!!!")
    client_socket.send(bytes("Welcome to the server!", "utf-8"))
    client_socket.close()
