from C_Encounter import *


class World(Encounter):
    def __init__(self, map, player):
        super().__init__(map, player, False)

    def run(self):
        # world run commands...
        r = random.randint(1, 1)
        print(r)
        super().run()
        if r == 1:
            return False
        return True
