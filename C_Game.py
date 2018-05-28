from C_World import*


class Game:
    def __init__(self, savedFiles=False):
        self.player = Player()  # when we start saving players this will need to change.
        if savedFiles:
            # not implemented
            self.loadSavedFiles(savedFiles)
        self.world = World(Map(10, 30, False, 'The Main World Map', False), self.player)

    def loadSavedFiles(self, files):
        # get text data
        # populate self.grid of new Map
        # load guy
        pass

    def levelUpPlayer(self):
        if Encounter.encounterCounter == 3 and Encounter.encounterCounter <= 4:
            self.player.lvlUp = True
            print("You Leveled up!!")
            Encounter.encounterLevel += 1
        if Encounter.encounterCounter == 4:
            print("Congrats!!! You beat the game!! You are a great contributor to society! You should be proud!")
            ifReset = getInt(Fore.GREEN + "Would you like to play again? 1 = Yes, 2 = No" + Fore.BLACK, 2, 1)
            if ifReset == 1:
                print(Fore.GREEN, "Ok then! Let's give it another go!", Fore.BLACK)
                self.reset()
            else:
                print(Fore.CYAN, "Ok then! Goodbye!", Fore.BLACK)
                sys.exit()
        if self.player.lvlUp:
            Encounter.encounterCounter = 0
            self.player.lvlUp = False
            self.player.hp += 50
            self.player.attackSkill += 7
            self.player.damage += 3
            self.player.armor += 2
            self.player.defenseSkill += 2

    def reset(self):
        self.world = World(Map(10, 30, False, False,  'The Main World Map', False), self.player)
        self.player.hp = 110
        self.player.attackSkill = 10
        self.player.damage = 3
        self.player.defenseSkill = 5
        self.player.armor = 1
        self.player.row = 0
        self.player.col = 0
        Encounter.encounterLevel = 0
        Encounter.encounterCounter = 0
        self.run()

    def run(self):
        print(Style.BRIGHT, Fore.RED + 'H' + Fore.YELLOW + 'e' + Fore.GREEN + 'l' + Fore.BLUE + 'l' + Fore.MAGENTA
              + 'o' + Fore.LIGHTMAGENTA_EX + '!!!', Fore.BLACK, ' Good Luck!')
        while self.player.hp > 0:
            self.levelUpPlayer()
            engaged = False
            if not self.world.run():
                self.player.col = 0
                self.player.row = 0
                engaged = True
                print(Fore.RED, "Start Encounter", Fore.BLACK)
                self.world.determineEncounter().run()
            if engaged:
                print(Fore.BLUE, "End Encounter", Fore.BLACK)
                Encounter.encounterCounter += 1
                self.player.col = self.world.lastWorldLocationCol
                self.player.row = self.world.lastWorldLocationRow
        else:
            print(Fore.RED, "Uh oh! You lost too much HP You died!")
            ifReset = getInt(Fore.GREEN + "Would you like to play again? 1 = Yes, 2 = No" + Fore.BLACK, 2, 1)
            if ifReset == 1:
                print(Fore.CYAN + "Ok then! Let's give it another go!" + Fore.BLACK)
                self.reset()
            else:
                print(Fore.GREEN + "Ok then! Goodbye!" + Fore.BLACK)
                sys.exit()


g = Game()
g.run()
