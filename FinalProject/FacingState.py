from RobotController import RobotController


class FacingState:
    def __init__(self):
        self.controller = RobotController()

class North(FacingState):
    def move_north(self):
        print("Move forward")

    def move_west(self):
        print("Turn left")
        print("Move forward")

    def move_south(self):
        print("Turn left")
        print("Turn left")
        print("Move forward")

    def move_east(self):
        print("Turn right")
        print("Move forward")

class West(FacingState):
    def move_north(self):
        print("Turn right")
        print("Move forward")

    def move_west(self):
        print("Move forward")

    def move_south(self):
        print("Turn left")
        print("Move forward")

    def move_east(self):
        print("Turn left")
        print("Turn left")
        print("Move forward")

class South(FacingState):
    def move_north(self):
        print("Turn left")
        print("Turn left")
        print("Move forward")

    def move_west(self):
        print("Turn right")
        print("Move forward")

    def move_south(self):
        print("Move forward")

    def move_east(self):
        print("Turn left")
        print("Move forward")

class East(FacingState):
    def move_north(self):
        print("Turn left")
        print("Move forward")

    def move_west(self):
        print("Turn left")
        print("Turn left")
        print("Move forward")

    def move_south(self):
        print("Turn right")
        print("Move forward")

    def move_east(self):
        print("Move forward")
