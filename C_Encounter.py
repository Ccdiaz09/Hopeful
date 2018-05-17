from Units import*
from C_NavigatableMap import *


class Encounter(NavigatableMap):
    encounterCounter = 0
    encounterLevel = 0
    GOBLIN = 1
    ORC = 2
    OGRES = 3
    DRAGON = 4
    THIEVES = 5
    GIANT_ASS_SPIDER = 6
    BUG_BEAR = 7
    HOBGOBLIN = 8
    BOGEY = 9
    PIXIE = 10
    GHOST_KNIGHT = 11
    FLYING_SABERTOOTH_BATS = 12
    RABID_RED_EYED_FAIRIES = 13
    MILITANT_CENTAURS = 14
    WELL_EDUCATED_CYCLOPS = 15
    LONELY_SIRENS = 16
    LONG_HAIRED_WOOLLY_MAMMOTHS_WITH_ATTITUDE = 17
    CYBORG_BADGER = 18
    STAG_WOLF = 19
    ENCOUNTER_TYPES_DIF_EASY = [BOGEY, GOBLIN, ORC, THIEVES, PIXIE, RABID_RED_EYED_FAIRIES]
    ENCOUNTER_TYPES_DIF_MEDIUM = [BUG_BEAR, OGRES, GIANT_ASS_SPIDER, FLYING_SABERTOOTH_BATS, LONELY_SIRENS]
    ENCOUNTER_TYPES_DIF_HARD = [DRAGON, HOBGOBLIN, GHOST_KNIGHT, STAG_WOLF]

    def __init__(self, map, player):
        self.player = player
        self.enemies = []
        if Encounter.encounterLevel < 2:
            self.currentEncounter = random.choice(Encounter.ENCOUNTER_TYPES_DIF_EASY)
        if 4 > Encounter.encounterLevel >= 2:
            self.currentEncounter = random.choice(Encounter.ENCOUNTER_TYPES_DIF_MEDIUM)
        if Encounter.encounterLevel >= 4:
            self.currentEncounter = random.choice(Encounter.ENCOUNTER_TYPES_DIF_HARD)
        self.map = Map(10, 15, 'The Temporary Encounter Map', False)
        self.grid = self.map.grid
        print(Style.BRIGHT + Fore.BLACK)
        # you should consider moving all of this mess.
        if self.currentEncounter == Encounter.GOBLIN:
            # what makes a gobby encounter
            n = random.randint(1, 3)
            for i in range(n):
                self.enemies.append(Enemy(Enemy.GOBLIN_NAMES, 10, 7, 3, 4, 2, Fore.RED + chr(60) + Fore.BLACK, False))
        if self.currentEncounter == Encounter.ORC:
            j = random.randint(1, 3)
            for k in range(j):
                self.enemies.append(Enemy(Enemy.ORC_NAMES, 20, 5, 1, 6, 2, chr(536), False))
        if self.currentEncounter == Encounter.OGRES:
            l = random.randint(1, 2)
            for k in range(l):
                self.enemies.append(Enemy(Enemy.OGRE_NAMES, 25, 5, 1, 4, 3, chr(789), False))
        if self.currentEncounter == Encounter.DRAGON:
            self.enemies.append(Enemy(Enemy.DRAGON_NAMES, 50, 20, 5, 10, 5, chr(10644), False))
        if self.currentEncounter == Encounter.THIEVES:
            something = random.randint(2, 4)
            for k in range(something):
                self.enemies.append(Enemy(Enemy.THIEF_NAMES, 10, 8, 6, 2, 1, chr(439), False))
        if self.currentEncounter == Encounter.GIANT_ASS_SPIDER:
            self.enemies.append(Enemy(Enemy.GIANT_ASS_SPIDER_NAMES, 30, 8, 2, 2, 1, chr(9000), False))
        if self.currentEncounter == Encounter.BUG_BEAR:
            self.enemies.append(Enemy(Enemy.BUG_BEAR_NAMES, 15, 10, 0, 0, 0, chr(769), False))
        if self.currentEncounter == Encounter.BOGEY:
            self.enemies.append(Enemy(Enemy.BOGEY_NAMES, 40, 3, 0, 0, 0, Fore.RED + chr(987) + Fore.BLACK, False))
        if self.currentEncounter == Encounter.HOBGOBLIN:
            self.enemies.append(Enemy(Enemy.HOBGOBLIN_NAMES, 50, 15, 6, 13, 4, chr(1756), False))
        if self.currentEncounter == Encounter.PIXIE:
            somethingElse = random.randint(3, 4)
            for i in range(somethingElse):
                self.enemies.append(Enemy(Enemy.PIXIE_NAMES, 5, 8, 3, 7, 1, chr(1111111), False))
        if self.currentEncounter == Encounter.GHOST_KNIGHT:
            self.enemies.append(Enemy(Enemy.GHOST_KNIGHT_NAMES, 35, 13, 8, 10, 5, chr(10002), False))
        if self.currentEncounter == Encounter.FLYING_SABERTOOTH_BATS:
            tooManyVariables = random.randint(4, 6)
            for i in range(tooManyVariables):
                self.enemies.append(Enemy(Enemy.FLYING_SABERTOOTH_BAT_NAMES, 1, 25, 17, 1, 1, chr(597), False))
        if self.currentEncounter == Encounter.RABID_RED_EYED_FAIRIES:
            fuckers = random.randint(2, 4)
            for i in range(fuckers):
                self.enemies.append(Enemy(Enemy.RABBID_RED_EYED_FARIE_NAMES, 1, 20, 10, 10, 4, chr(73), False))
        if self.currentEncounter == Encounter.MILITANT_CENTAURS:
            toga = random.randint(2, 3)
            for i in range(toga):
                self.enemies.append(Enemy(Enemy.MILLITANT_CENTAUR_NAMES, 1, 1, 1, 1, 1, chr(576), False))
        if self.currentEncounter == Encounter.WELL_EDUCATED_CYCLOPS:
            self.enemies.append(Enemy(Enemy.WELL_EDUCATED_CYCLOPS_NAMES, 1, 1, 1, 1, 1, chr(9402), False))
        if self.currentEncounter == Encounter.LONELY_SIRENS:
            iLoveInNOut = random.randint(1, 3)
            for i in range(iLoveInNOut):
                self.enemies.append(Enemy(Enemy.LONLEY_SIREN_NAMES, 30, 10, 5, 7, 1, chr(132), False))
        if self.currentEncounter == Encounter.STAG_WOLF:
            self.enemies.append(Enemy(Enemy.STAG_WOLF_NAMES, 30, 15, 2, 5, 2, chr(6973), False))
        if self.currentEncounter == Encounter.LONG_HAIRED_WOOLLY_MAMMOTHS_WITH_ATTITUDE:
            self.enemies.append(Enemy(Enemy.LONG_HARIED_WOOLY_MAMMOTH_WITH_ATTITUDE_NAMES, 1, 1, 1, 1, 1,
                                      chr(879), False))
        if self.currentEncounter == Encounter.CYBORG_BADGER:
            self.enemies.append(Enemy(Enemy.CYBORG_BADGER_NAMES, 1, 1, 1, 1, 1, chr(1234), False))
        self.placeEnemy()

    def placeEnemy(self):
        cols = self.map.grid[0].__len__()
        rows = self.map.grid.__len__()
        for guy in self.enemies:
            valid = False
            while not valid:
                valid = True
                col = random.randint(0, cols - 1)
                row = random.randint(0, rows - 1)
                for other in self.enemies:
                    if other.col == col and other.row == row and not other == guy:
                        valid = False
                    if col == self.player.col and row == self.player.row:
                        valid = False
                    if valid:
                        guy.col = col
                        guy.row = row

    def displayAll(self):
        rowCounter = 0
        for row in self.map.grid:
            m = ""
            colCounter = 0
            for col in row:
                new = col
                if self.player.row == rowCounter and self.player.col == colCounter:
                    new = Fore.BLUE + "P" + Fore.BLACK + Style.BRIGHT
                for enemy in self.enemies:
                    if enemy.row == rowCounter and enemy.col == colCounter:
                        new = Fore.RED + enemy.symbol + Fore.BLACK
                m += new
                colCounter += 1
            print(m)
            rowCounter += 1

    def handleMovement(self, unit):
        destination = unit.getTargetDestination(self.player)
        valid = self.validateMove(destination)
        if valid:
            occupied = self.getGuyColAndRow(destination[0], destination[1])
            if not occupied:
                unit.col = destination[0]
                unit.row = destination[1]
            else:
                if not (isinstance(unit, Enemy) and isinstance(occupied, Enemy)):  # enemies don't attack each other
                    unit.attack(occupied)

    def run(self):
        while self.player.hp > 0:
            dead = []
            self.displayAll()
            self.handleMovement(self.player)
            for enemy in self.enemies:
                enemy.lookForPlayer(self.player)
                self.handleMovement(enemy)
                if enemy.hp < 1:
                    dead.append(enemy)
            for corpse in dead:
                self.enemies.remove(corpse)
            if self.enemies.__len__() == 0:
                return False
