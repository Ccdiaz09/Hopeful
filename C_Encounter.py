from C_Map import*
from Units import*
from colorama import Fore, Back, Style


class Encounter:
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

    def __init__(self, map,  player, encounterType=BOGEY,):
        self.player = player
        self.enemies = []
        self.map = Map(20, 20, 'a.txt', False)
        print(Style.BRIGHT + Fore.BLACK)
        # you should consider moving all of this mess.
        if encounterType == Encounter.GOBLIN:
            self.enemies.append(Enemy(Enemy.GOBLIN_NAMES, 15, 15, 10, 8, 10, Fore.RED + chr(60) + Fore.BLACK, False))
        if encounterType == Encounter.ORC:
            self.enemies.append(Enemy(Enemy.ORC_NAMES, 1, 1, 1, 1, 1, chr(536), False))
        if encounterType == Encounter.OGRES:
            self.enemies.append(Enemy(Enemy.OGRE_NAMES, 1, 1, 1, 1, 1, chr(789), False))
        if encounterType == Encounter.DRAGON:
            self.enemies.append(Enemy(Enemy.DRAGON_NAMES, 1, 1, 1, 1, 1, chr(4789), False))
        if encounterType == Encounter.THIEVES:
            self.enemies.append(Enemy(Enemy.THIEF_NAMES, 1, 1, 1, 1, 1, chr(439), False))
        if encounterType == Encounter.GIANT_ASS_SPIDER:
            self.enemies.append(Enemy(Enemy.BUG_BEAR_NAMES, 1, 1, 1, 1, 1, chr(9000), False))
        if encounterType == Encounter.BUG_BEAR:
            self.enemies.append(Enemy(Enemy.HOBGOBLIN_NAMES, 1, 1, 1, 1, 1, chr(769), False))
        if encounterType == Encounter.BOGEY:
            self.enemies.append(Enemy(Enemy.BOGEY_NAMES, 15, 5, 5, 5, 5, Fore.RED + chr(987) + Fore.BLACK, False))
        if encounterType == Encounter.PIXIE:
            self.enemies.append(Enemy(Enemy.PIXIE_NAMES, 1, 1, 1, 1, 1, chr(1111111), False))
        if encounterType == Encounter.GHOST_KNIGHT:
            self.enemies.append(Enemy(Enemy.GHOST_KNIGHT_NAMES, 1, 1, 1, 1, 1, chr(10002), False))
        if encounterType == Encounter.FLYING_SABERTOOTH_BATS:
            self.enemies.append(Enemy(Enemy.FLYING_SABERTOOTH_BAT_NAMES, 1, 1, 1, 1, 1, chr(597), False))
        if encounterType == Encounter.RABID_RED_EYED_FAIRIES:
            self.enemies.append(Enemy(Enemy.RABBID_RED_EYED_FARIE_NAMES, 1, 1, 1, 1, 1, chr(73), False))
        if encounterType == Encounter.MILITANT_CENTAURS:
            self.enemies.append(Enemy(Enemy.MILLITANT_CENTAUR_NAMES, 1, 1, 1, 1, 1, chr(576), False))
        if encounterType == Encounter.WELL_EDUCATED_CYCLOPS:
            self.enemies.append(Enemy(Enemy.WELL_EDUCATED_CYCLOPS_NAMES, 1, 1, 1, 1, 1, chr(9402), False))
        if encounterType == Encounter.LONELY_SIRENS:
            self.enemies.append(Enemy(Enemy.LONLEY_SIREN_NAMES, 1, 1, 1, 1, 1, chr(7395), False))
        if encounterType == Encounter.LONG_HAIRED_WOOLLY_MAMMOTHS_WITH_ATTITUDE:
            self.enemies.append(Enemy(Enemy.LONG_HARIED_WOOLY_MAMMOTH_WITH_ATTITUDE_NAMES, 1, 1, 1, 1, 1,
                                      chr(124365879), False))
        if encounterType == Encounter.CYBORG_BADGER:
            self.enemies.append(Enemy(Enemy.CYBORG_BADGER_NAMES, 1, 1, 1, 1, 1, chr(123456789), False))
            self.placeGuys()

    def placeGuys(self):
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
                    new = Fore.BLUE + "P" + Fore.BLACK
                for enemy in self.enemies:
                    if enemy.row == rowCounter and enemy.col == colCounter:
                        new = Fore.RED + enemy.symbol + Fore.RESET + Fore.BLACK

                m += new
                colCounter += 1
            print(m)

            rowCounter += 1

    def handleMovement(self, unit):
        valid = False
        while not valid:
            if isinstance(unit, Enemy):
                destination = unit.getTargetDestination(self.player)
            else:
                destination = unit.getTargetDestination()
            valid = self.map.validateMove(destination)
            if not valid:
                if unit == Enemy:
                    print(unit.name + " forfeited this turn!")
                else:
                    print("You cant go there! Pick another direction")
            else:
                guyAtDestination = self.getGuyColAndRow(destination[0], destination[1])
                if not guyAtDestination:
                    unit.col = destination[0]
                    unit.row = destination[1]
                else:
                    unit.attack(guyAtDestination)

    def getGuyColAndRow(self, col, row):
        if self.player.col == col and self.player.row == row:
            return self.player
        for enemy in self.enemies:
            if enemy.row == row and enemy.col == col:
                return enemy
        return False

    def run(self):
        self.placeGuys()
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
