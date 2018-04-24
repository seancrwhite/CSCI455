import random
from Player import *

class Node:
    def __init__(self):
        self.has_key = False
        self.is_visited = False
        self.adjacent_nodes = []

    def set_adjacent(self, nodes):
        self.adjacent_nodes = nodes

class Start(Node):
    def execute(self, player):
        if self.is_visited == False:
            self.is_visited = True
            return "Welcome to the Adventure. Tell me where to go. "
        else:
            return "Nothing is here. "

class Enemy(Node):
    def __init__(self, has_key):
        super(Enemy, self)
        self.has_key = has_key
        self.health = 20
        self.is_visited = False

    def execute(self, player):
        if self.is_visited == False:
            while self.health > 0 and player.health > 0:
                hit = random.randint(1, 9)
                player.health = player.health - hit
                hit = random.randint(1, 11)
                self.health = self.health - hit

                if player.health <= 0:
                    return "I found an enemy...... Fighting...... I lost the fight, my health was depleated. "
                elif self.health <= 0 and self.has_key == True:
                    self.is_visited = True
                    player.has_key = True
                    return "I found an enemy...... Fighting...... I won the fight! And found a key! But I only have " + str(player.health) + " hit points left. "
                elif self.health < 0:
                    self.is_visited = True
                    return "I found an enemy...... Fighting...... I won the fight! But I only have " + str(player.health) + " hit points left. "
        else:
            return "There was an enemy here. "

class Chest(Node):
    def execute(self, player):
        if player.has_key == True:
            player.health = 0
            return "Chest unlocked. You win! "
        else:
            return "I see a box, but it needs a key. "

class Recharge(Node):
    def execute(self, player):
        player.health = 25
        return "Recharge station. My health has been restored to 25 hit points. "
