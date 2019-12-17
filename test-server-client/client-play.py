import socket as soc

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
s.connect((soc.gethostname(), 1234))

# 1024 decides the amount of data that you can receive at a time (Buffer Size)
msg = s.recv(0)
print(msg.decode('utf-8'))
