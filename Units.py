from helpers import *
from colorama import Fore


class Guy:
    def __init__(self):
        self.name = "you"
        self.isDead = False
        self.hp = 110
        self.attackSkill = 10
        self.damage = 3
        self.defenseSkill = 5
        self.armor = 1
        self.col = 1
        self.row = 1
        self.lvlUp = False
        # may want a weapon at some point...

    def getAttackRoll(self):
        global r
        for i in range(1):
            r = random.randint(self.damage, self.attackSkill)
        return r

    def attack(self, victim):
        attackRoll = self.getAttackRoll()
        defenseRoll = self.defend()
        if attackRoll > defenseRoll:
            victim.receiveDamage(attackRoll-defenseRoll, self)

    def defend(self):
        global defenseRoll
        for i in range(1):
            defenseRoll = random.randint(0,self.armor)
        return defenseRoll

    def receiveDamage(self, damage, attacker):
        self.hp -= damage
        # may be added to later with armor and such....
        if self.hp < 0:
            print(Fore.GREEN + self.name + " died." + Fore.BLACK)
            return True
        else:
            print(Fore.GREEN + self.name, " took ", damage, "damage", "from ", attacker.name, "!", " Health is now at"
                  , self.hp, Fore.BLACK)
        return False

    def getTargetDestination(self, player):
        print("invalid use of get target destination")


class Enemy(Guy):
    GOBLIN_NAMES = ["Goblin Jeff", "Goblin Joe"]
    ORC_NAMES = ["fuck", "you"]
    OGRE_NAMES = ["fucker", "jeff"]
    DRAGON_NAMES = ["ya boi sherman", "fredrick", "Puff the magic dragon"]
    THIEF_NAMES = ["mofo i aint tellin u my name", "dat dude"]
    GIANT_ASS_SPIDER_NAMES = ["I Dont Know How To Name A Spider"]
    BUG_BEAR_NAMES = ["john", "connor", "yogi bear"]
    HOBGOBLIN_NAMES = ["arthur"]
    BOGEY_NAMES = ["Bogey Boggart", "Bogey Slurher", 'Golem']
    PIXIE_NAMES = ["Gem", "Sapphire", "Ruby", "Pearl", "Diamond"]
    GHOST_KNIGHT_NAMES = ["john", "sir bendict"]
    FLYING_SABERTOOTH_BAT_NAMES = ["wookie", "seth"]
    RABBID_RED_EYED_FARIE_NAMES = ["figure this out later"]
    MILLITANT_CENTAUR_NAMES = ["figure this out later"]
    WELL_EDUCATED_CYCLOPS_NAMES = ["figure this out later"]
    LONLEY_SIREN_NAMES = ["figure this out later"]
    LONG_HARIED_WOOLY_MAMMOTH_WITH_ATTITUDE_NAMES = ["figure this out later"]
    CYBORG_BADGER_NAMES = ["figure this out later"]
    STAG_WOLF_NAMES = ['Spot', 'Sparky', 'Lucky', 'Desmond', 'Gunner', 'Hodor', 'Bob', 'Bilbo Baggins']

    def __init__(self, nameList, hp, attackSkill, damage, defense, armor, symbol, visionRange):
        super().__init__()
        self.name = random.choice(nameList)
        self.hp = hp
        self.attackSkill = attackSkill
        self.damage = damage
        self.defense = defense
        self.armor = armor
        self.symbol = symbol
        self.aggro = False
        self.visionRange = 5

    def lookForPlayer(self, player):
        # make sure the player is within two spaces to the enemy
        dx = abs(player.col - self.col)
        dy = abs(player.row - self.row)
        if dx+dy < self.visionRange:
            self.aggro = True

    def moveTowardPlayer(self, player):
        distanceX = player.col - self.col
        distanceY = player.row - self.row
        dx = 0
        dy = 0
        if distanceX > 0:
            dx = 1
        if distanceX < 0:
            dx = -1
        if distanceY > 0:
            dy = 1
        if distanceY < 0:
            dy = -1
        return self.col + dx, self.row + dy

    def getTargetDestination(self, player):
        if self.aggro:
            return self.moveTowardPlayer(player)
        else:
            # wander
            direction = random.randint(1, 4)
            change = translateDirectionToDXAndDY(direction)
            return self.col + change[0], self.row + change[1]


def translateDirectionToDXAndDY(direction):
    if direction == 1:
        return 0, -1
    if direction == 2:
        return 1, 0
    if direction == 3:
        return 0, 1
    if direction == 4:
        return -1, 0


class Player(Guy):
    def __init__(self):
        super().__init__()
        # character creation

    def getTargetDestination(self, player="useless"):
        direction = getInt(Fore.CYAN + "Which direction do you want to go? North:1, East:2, South:3, West:4" + Fore.BLACK, 4, 1)
        t = translateDirectionToDXAndDY(direction)
        return self.col + t[0], self.row + t[1]