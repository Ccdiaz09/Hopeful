from C_Encounter import *


class World(NavigatableMap):
    typeOfEncounter = Encounter.ENCOUNTER_TYPES_DIF_EASY

    def __init__(self, map, player):
        self.map = map
        self.grid = self.map.grid
        self.player = player
        self.lastWorldLocationCol = self.player.col
        self.lastWorldLocationRow = self.player.row

    def determineEncounter(self):
        return Encounter(Map, self.player)

    def run(self):
        r = random.randint(1, 1000)
        self.displayAll()
        self.handleMovement(self.player)
        self.lastWorldLocationCol = self.player.col
        self.lastWorldLocationRow = self.player.row
        print(self.lastWorldLocationCol, ',', self.lastWorldLocationRow)
        if r == 1:
            return False
        else:
            return True
