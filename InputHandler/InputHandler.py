import tty
import sys
import termios
from Maestro import Controller

x = Controller()

# 0 <- body
# 1 <- wheel
# 2 <- wheel
# 3 <- head left/right
# 4 <- head up/down
# forward 2400 - 1800
# reverse 6300 - 7100

x.setTarget(1, 6000)
x.setTarget(2, 6000)

x.setSpeed(1, 30)
x.setSpeed(2, 30)

x.setAccel(1, 150)

low_range = 4000
high_range = 5000

def take_instr(direction):
        global low_range
        global high_range

        if direction == '8':
                curr_pos = x.getPosition(4)
                x.setTarget(4, curr_pos + 800)
        elif direction == '2':
                curr_pos = x.getPosition(4)
                x.setTarget(4, curr_pos - 800)
        elif direction == '7':
                curr_pos = x.getPosition(3)
                x.setTarget(3, curr_pos + 800)
        elif direction == '9':
                curr_pos = x.getPosition(3)
                x.setTarget(3, curr_pos - 800)
        elif direction == '4':
                curr_pos = x.getPosition(0)
                x.setTarget(0, curr_pos + 2000)
        elif direction == '6':
                curr_pos = x.getPosition(0)
                x.setTarget(0, curr_pos - 2000)
        elif direction == 's':
                for i in range(-1 * low_range, -1 * high_range, -1):
                        x.setTarget(1, i - 4000)
        elif direction == 'w':
                for i in range(low_range, high_range):
                        x.setTarget(1, i)
        elif direction == 'a':
                for i in range(low_range, high_range):
                        x.setTarget(2, i)
	elif direction == 'd':
                for i in range(-1 * low_range, -1 * high_range, -1):
                        x.setTarget(2, i - 4000)
        elif direction == 'z':
                x.setTarget(1, 6000)
                x.setTarget(2, 6000)
        elif direction == 'j':
                low_range = 4000
                high_range = 5000
        elif direction == 'k':
                low_range = 4000
                high_range = 4500
        elif direction == 'l':
                low_range = 0
                high_range = 1000
        elif direction == 'f':
                sys.exit()

def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
        finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

while True:
	i = getch()
        take_instr(i)





