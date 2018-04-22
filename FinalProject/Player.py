from Node import *
from PhoneHandler import *

class Player(Thread):
    def __init__(self, start_node):
        self.health = 20
        self.has_key = False
        self.curr_node = start_node
        self.server = ServerThread()
        self.client = ClientThread()
        self.result = ""

    def run(self):
        self.result = self.curr_node.execute(self)
        print("Run start", str(self.health))

        if self.health <= 0:
            self.client.send(self.result)
            print("health depleated")
            return True
        self.result += "I see a path "
        if self.curr_node.adjacent_nodes[0]:
            self.result +="north "
        if self.curr_node.adjacent_nodes[1]:
            self.result += "south "
        if self.curr_node.adjacent_nodes[2]:
            self.result += "east "
        if self.curr_node.adjacent_nodes[3]:
            self.result += "west "

        self.client.send(self.result)

        curr_node_set = False
        while curr_node_set == False:
            data = ""

            while data == "":
                data = self.server.get_phrase()

            data = data.lower().strip()
            print(data)
            if data == "north" and self.curr_node.adjacent_nodes[0]:
                self.curr_node = self.curr_node.adjacent_nodes[0]
                curr_node_set = True
                print("curr_node set")
            elif data == "south" and self.curr_node.adjacent_nodes[1]:
                self.curr_node = self.curr_node.adjacent_nodes[1]
                curr_node_set = True
            elif data == "east" and self.curr_node.adjacent_nodes[2]:
                self.curr_node = self.curr_node.adjacent_nodes[2]
                curr_node_set = True
            elif data == "west" and self.curr_node.adjacent_nodes[3]:
                self.curr_node = self.curr_node.adjacent_nodes[3]
                curr_node_set = True
            else:
                self.client.send("Invalid direction.")
        print("Out of loop")
        return False
