from tkinter import Tk
from Node import *
from Player import *
import sys

if __name__ == '__main__':
    cont = True
    while cont:
        node1 = Start()
        node2 = Chest()
        node3 = Enemy(False)
        node4 = Enemy(True)
        node5 = Recharge()

        node1.set_adjacent([node3, None, None, None])
        node2.set_adjacent([None, None, None, node3])
        node3.set_adjacent([node5, node1, node2, node4])
        node4.set_adjacent([None, None, node3, None])
        node5.set_adjacent([None, node3, None, None])

        new_player = Player(node1)
        game_over = False
        while not game_over:
            game_over = new_player.run()
        cont = new_player.play_again()
        #cont = False

    print("EXIT")
    sys.exit()
