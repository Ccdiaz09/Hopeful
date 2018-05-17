from helpers import *
from colorama import Fore, Back, Style


class Guy:
    def __init__(self):
        # self.name = input("Hello! What's your name?")
        self.name = "you"
        self.isDead = False
        self.hp = 80
        self.attackSkill = 10
        self.damage = 3
        self.defenseSkill = 5
        self.armor = 1
        self.col = 1
        self.row = 1
        # may want a weapon at some point...

    def getTargetDestination(self):
        direction = getInt(Fore.CYAN + "Which direction do you want to go? North:1, East:2, South:3, West:4" +
                           Fore.BLACK, 4, 1)
        t = self.translateDirectionToDXandDY(direction)
        return self.col + t[0], self.row + t[1]
#

    def translateDirectionToDXandDY(self, direction):
        if direction == 1:
            return 0, -1
        if direction == 2:
            return 1, 0
        if direction == 3:
            return 0, 1
        if direction == 4:
            return -1, 0
        # d = translate...
        # d[0] = x component
        # d[1] = y component

    def getRoll(self, n):
        successes = 0
        for i in range(n):
            r = random.randint(self.damage, self.attackSkill)
            if r > 4:
                successes += 1
        return successes

    def attack(self, victim):
        attackRoll = self.getRoll(self.attackSkill)
        defenseRoll = self.defend(self)
        if attackRoll > defenseRoll:
            victim.receiveDamage(attackRoll-defenseRoll, self)

    def defend(self, attacker):
        defenseRoll = self.getRoll(self.defenseSkill)
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
'''
class Player(Guy):
    def __init__(self):
        self.hitPoints = 50
        self.attackSkill = 5
        self.damage = 3
        self.defense = 5
        self.armor = 6
        self.col = 0
        self.row = 0
'''


class Enemy(Guy):
    GOBLIN_NAMES = ["Goblin Jeff", "Goblin Joe"]
    ORC_NAMES = ["fuck", "you"]
    OGRE_NAMES = ["fucker", "jeff"]
    DRAGON_NAMES = ["ya boi sherman", "fredrick", "Puff the magic dragon"]
    THIEF_NAMES = ["mofo i aint tellin u my name", "dat dude"]
    BUG_BEAR_NAMES = ["john", "connor", "yogi bear"]
    HOBGOBLIN_NAMES = ["arthur"]
    BOGEY_NAMES = ["Bogey Boggart", "Bogey Slurher"]
    PIXIE_NAMES = ["Gem", "Sapphire", "Ruby", "Pearl", "Diamond"]
    GHOST_KNIGHT_NAMES = ["john", "sir bendict"]
    FLYING_SABERTOOTH_BAT_NAMES = ["wookie", "seth"]
    RABBID_RED_EYED_FARIE_NAMES = ["figure this out later"]
    MILLITANT_CENTAUR_NAMES = ["figure this out later"]
    WELL_EDUCATED_CYCLOPS_NAMES = ["figure this out later"]
    LONLEY_SIREN_NAMES = ["figure this out later"]
    LONG_HARIED_WOOLY_MAMMOTH_WITH_ATTITUDE_NAMES = ["figure this out later"]
    CYBORG_BADGER_NAMES = ["figure this out later"]

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

    def aiPick(self):
        pass

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
            change = self.translateDirectionToDXandDY(direction)  # this was wrong.
            return self.col + change[0], self.row + change[1]

