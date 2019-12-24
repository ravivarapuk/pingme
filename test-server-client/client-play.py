import socket as soc
import pickle


HEADERSIZE = 10

# code while receving objects 
full_msg = b''
d = pickle.loads(full_msg[HEADERSIZE:])

# Socket -> Socket is an endpoint(at an ip on a port) that sends and receives data
# Initialize socket with socket family type AF_INET -> IPV4 & SOCK_STREAM -> streaming socket
s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
s.connect(soc.gethostname(), 3200)

# 1024 decides the amount of data that you can receive at a time
while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")
    if len(full_msg)-HEADERSIZE == msglen:
        print('Full msg received!')
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ''

print(full_msg)
