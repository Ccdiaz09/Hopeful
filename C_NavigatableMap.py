from colorama import Style
from C_Map import *


class NavigatableMap(Map):
    def __init__(self, map, player):
        self.grid = map.grid
        self.map = map
        self.player = player

    def translateDirectionToDXAndDY(self, direction):
        if direction == 1:
            return 0, -1
        if direction == 2:
            return 1, 0
        if direction == 3:
            return 0, 1
        if direction == 4:
            return -1, 0

    def displayAll(self):
        rowCounter = 0
        for row in self.map.grid:
            m = ""
            colCounter = 0
            for col in row:
                new = col
                if self.player.row == rowCounter and self.player.col == colCounter:
                    new = Fore.BLUE + "P" + Fore.BLACK
                m += new
                colCounter += 1
            print(m)
            rowCounter += 1

    def handleMovement(self, unit):
        destination = unit.getTargetDestination(self.player)
        valid = Map.validateMove(self, destination)
        if valid:
            unit.col = destination[0]
            unit.row = destination[1]

    def getGuyColAndRow(self, col, row):
        if self.player.col == col and self.player.row == row:
            return self.player
        for enemy in self.enemies:
            if enemy.row == row and enemy.col == col:
                return enemy
        return False
