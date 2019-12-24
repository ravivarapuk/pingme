import socket as soc
import time

HEADERSIZE = 10

# Socket -> Socket is an endpoint(at an ip on a port) that sends and receives data
# Initialize socket with socket family type AF_INET -> IPV4 & SOCK_STREAM -> streaming socket
s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

# Bind the host and the port to the socket
s.bind((soc.gethostname(), 3200))
s.listen(5)    # the arg 5 defines the queue, in case oif heavy loads

while True:
    client_socket, address = s.accept()
    print(f"Conn. from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    
    client_socket.send(bytes(msg, "utf-8"))
    
    while True:
        time.sleep(5)

        msg = f"The time is {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg

        client_socket.send(bytes(msg, "utf-8"))
