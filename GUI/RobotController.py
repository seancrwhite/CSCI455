from Maestro import Controller
from time import sleep

class RobotController:
    def __init__(self):
        self.controller = Controller()

        self.body = 0
        self.motor_move = 1
        self.motor_turn = 2
        self.head_vert = 3
        self.head_hor = 4

        self.low_range = 4000
        self.high_range = 5000
        self.kill = 6000

        #must kill motors before starting
        self.controller.setTarget(self.motor_move, self.kill)
        self.controller.setTarget(self.motor_turn, self.kill)

    def turn_body(self, pos):
        self.controller.setTarget(self.body, pos)

    def turn_head(self, pin, pos):
        self.controller.setTarget(pin, pos)

    def move_motors(self, pin, direction, time, speed=1):
        for i in range(direction*self.low_range, direction*self.high_range, direction) #TODO: Implement speed
            self.controller.setTarget(pin, i)

        sleep(time)

        self.controller.setTarget(pin, self.kill)
