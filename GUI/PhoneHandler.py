import socket
import sys
from threading import Thread

class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 5000
        self.phrase = ""
        self.start()

    def run(self):
        self.sock.connect((self.host, self.port))
        print("Connection Established")

        while True:
            try:
                if self.phrase is not "":
                    self.sock.send(self.phrase.encode('utf-8'))
                    print(self.phrase)
                    self.phrase = ""
            except:
                print('Client disconnected')
                self.sock.close()

    def send(self, new_phrase):
        self.phrase = new_phrase
