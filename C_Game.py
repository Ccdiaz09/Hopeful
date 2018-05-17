from C_World import*


class Game:
    def __init__(self, savedFiles=False):

        self.player = Guy()  # when we start saving players this will need to change.
        if savedFiles:
            # not implemented
            self.loadSavedFiles(savedFiles)
        else:
            map = Map(100, 100, 'worldMap.txt')
        self.world = World(map, self.player)
        self.encounterA = Encounter(Map(20, 20, "encounterMap"), self.player)

    def loadSavedFiles(self, files):

        # populate self.grid of new Map
        self.map = Map(0, 0, files[0], True)
        # load guy

        pass

    def run(self):
        while 1:
            engaged = False

            if not engaged:
                    if not self.world.run():
                        engaged = True
                        print("Start Encounter")
                    if engaged:
                        self.encounterA.run()
                        print("End Encounter")


savedFiles = ["Map.txt", 23, 655]
g = Game()
g.run()
