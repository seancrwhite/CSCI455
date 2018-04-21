import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.200.14.64"
port = 5000

sock.connect((host, port))
print("Connection Established")

def get_socket():
    return sock
