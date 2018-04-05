import sys
from threading import Thread
import Socket

class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sock = Socket.get_socket()
        self.phrase = ""
        self.start()

    def run(self):
        while True:
            try:
                if self.phrase is not "":
                    self.phrase += '\n'
                    self.sock.send(self.phrase.encode('utf-8'))
                    print("Sent: ", self.phrase)
                    self.phrase = ""
            except:
                #print('Client disconnected')
                self.sock.close()

    def send(self, new_phrase):
        self.phrase = new_phrase

class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.root_window = window
        self.sock = Socket.get_socket()
        self.start()

    def run(self):
        while True:
            try:
                data = self.sock.recv(2048)
                command = str(data, 'utf-8')
                print("Recieved: ", command)
                self.root_window.take_voice_command(command)
            except:
                #print('Server disconnected')
                self.sock.close()
