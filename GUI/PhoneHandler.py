import socket
import sys
from threading import Thread

class SocketStuff(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 5000
        self.sock.bind((self.host, self.port))
        self.phrase = ""
        self.start()

    def run(self):
        while True:
            try:
                if self.phrase is not "":
                    self.sock.send(self.phrase.encode('utf-8'))
                    print(self.phrase)
                    self.phrase = ""
            except:
                print('Client disconnected')

    def changing_phrase(self, new_phrase):
        self.phrase = new_phrase
