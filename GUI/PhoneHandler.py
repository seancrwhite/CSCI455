import socket
import sys
from threading import Thread

class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "10.200.60.119"
        self.port = 5000
        self.phrase = ""
        self.start()

    def run(self):
        self.sock.connect((self.host, self.port))
        print("Connection Established")

        while True:
            try:
                if self.phrase is not "":
                    self.phrase += '\n'
                    self.sock.send(self.phrase.encode('utf-8'))
                    print("Sent: ", self.phrase)
                    self.phrase = ""
            except:
                print('Server disconnected')
                self.sock.close()

    def send(self, new_phrase):
        self.phrase = new_phrase

class ServerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("NOT IMPLEMENTED")
