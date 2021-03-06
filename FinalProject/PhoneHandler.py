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
                print('Client disconnected')
                self.sock.close()
                break

    def send(self, new_phrase):
        self.phrase = new_phrase

class ServerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sock = Socket.get_socket()
        self.phrase = ""
        self.start()

    def run(self):
        while True:
            try:
                data = self.sock.recv(2048)
                command = str(data, 'utf-8')
                if self.phrase:
                    #print("Recieved: ", command)
                    self.phrase = command
            except:
                print('Server disconnected')
                self.sock.close()
                break

    def get_phrase(self):
        if self.phrase != "":
            print("Current phrase: ", self.phrase)

        result, self.phrase = self.phrase, ""

        return result
