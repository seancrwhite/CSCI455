from RobotController import RobotController
from PhoneHandler import *

global client
client = ClientThread()

class Command:
    def __init__(self, args):
        self.controller = RobotController()
        self.args = args

class HeadCommand(Command):
    def run_command(self):
        pin = self.args[0]
        pos = self.args[1]

        self.controller.turn_head(pin, pos)

class BodyCommand(Command):
    def run_command(self):
        pos = self.args[0]

        self.controller.turn_body(pos)

class MoveCommand(Command):
    def run_command(self):
        pin = self.args[0]
        direction = self.args[1]
        time = self.args[2]

        self.controller.move_motors(pin, direction, time)

class TalkCommand(Command):
    def run_command(self):
        phrase = self.args[0]

        global client
        client.send(phrase)
