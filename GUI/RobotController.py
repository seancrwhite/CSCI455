from Maestro import Controller

class RobotController:
    def __init__(self):
        self.controller = Controller()

        self.body = 0
        self.motor_move = 1
        self.motor_turn = 2
        self.head_vert = 3
        self.head_hor = 4

        self.controller.setTarget(self.motor_1, 6000)
        self.controller.setTarget(self.motor_2, 6000)

        self.low_range = 4000
        self.high_range = 5000

    def turn_body(self, pos):
        self.controller.setTarget(self.body, pos)

    def head_vertical(self, pos):
        self.controller.setTarget(self.head_vert, pos)

    def head_horizontal(self, pos):
        self.controller.setTarget(self.head_hor, pos)

    def move_motors(self, dir, dist, speed=1):
        self.controller.setTarget(self.motor_1, dir) #TODO: Implement movement

    def turn_motors(self, dir, degrees, speed=1):
        self.controller.setTarget(self.motor_2, dir) #TODO: Implement turning
