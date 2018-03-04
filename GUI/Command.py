from RobotController import RobotController

class Command:
    def __init__(self, controller, args):
        self.controller = controller
        self.args = args

class HeadCommand(Command):
    def run_command(self):
        pin = self.args[0]
        pos = self.args[1]

        controller.turn_head(pin, pos)

class BodyCommand(Command):
    def run_command(self):
        pos = self.args[0]

        controller.turn_body(pos)

class MoveCommand(Command):
    def run_command(self):
        pin = self.args[0]
        direction = self.args[1]
        time = self.args[2]

        controller.turn_body(pin, direction, time)
