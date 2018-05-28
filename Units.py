from helpers import *
from colorama import Fore
from C_Item import *


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
        self.equippedItems = []
        self.backpack = []
        # may want a weapon at some point...

    def getAttackRoll(self):
        for l in range(1):
            r = random.randint(self.damage, self.attackSkill)
        return r

    def attack(self, victim):
        attackRoll = self.getAttackRoll()
        defenseRoll = self.defend()
        if attackRoll > defenseRoll:
            victim.receiveDamage(attackRoll-defenseRoll, self)

    def defend(self):
        for k in range(1):
            defenseRoll = random.randint(0, self.armor)
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

    def equipItem(self, item):
        hands = []
        usedHands = 0
        armor = []
        misc = []
        # check current equipped items
        for equippedItem in self.equippedItems:
            if isinstance(equippedItem, Weapon):
                if equippedItem.size == Weapon.LARGE:
                    usedHands += 2
                else:
                    usedHands += 1
                hands.append(equippedItem)
            elif isinstance(equippedItem, Armor):
                armor.append(equippedItem)

            elif isinstance(equippedItem, Item):
                misc.append(equippedItem)
            else:
                print("error non item held in inventory.")
        # handle weapons
        if isinstance(item, Weapon):
            if usedHands > 0:
                if item.size == Weapon.LARGE:
                    for weapon in hands:
                        self.unequipItem(weapon)
                else:
                    if usedHands == 2:
                        unequipedItem = chooseItemFromNamedList(hands, "What would you like to unequip?")
                        self.unequipItem(unequipedItem)
            self.equippedItems.append(item)
        # handle armor
        elif isinstance(item, Armor):
            if armor.__len__() == 0:
                self.equippedItems.append(item)
            else:
                unequip = chooseItemFromNamedList(armor, "What item would you like to unequip?")
                self.unequipItem(unequip)
                self.equippedItems.append(item)
        elif isinstance(item, Item):
            if misc.__len__() < 4:
                self.equippedItems.append(item)
            else:
                unequip = chooseItemFromNamedList(misc, "What item would you like to unequip?")
                self.unequipItem(unequip)
            pass

    def unequipItem(self, item):
        c = getInt("Would you like to put " + item.name + " in your backpack(1) or on the ground (2)?", 2)
        if c == 1:
            self.backpack.append(item)
        else:
            print("You have discarded an item.")
        self.equippedItems.remove(item)

    def equipFromBackpack(self):
        item = chooseItemFromNamedList(self.backpack,
                                       "You are rummaging through your backpack. What would you like to equip?")
        self.equipItem(item)
        self.backpack.remove(item)


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
        direction = getInt(Fore.CYAN + "Which direction do you want to go? North:1, East:2, South:3, West:4" +
                           Fore.BLACK, 4, 1)
        t = translateDirectionToDXAndDY(direction)
        return self.col + t[0], self.row + t[1]


u = Player()
greatSword = Weapon(Weapon.BLADE, Weapon.LARGE)
sword = Weapon(Weapon.BLADE, Weapon.MEDIUM)
mace = Weapon(Weapon.HAMMER, Weapon.SMALL)
plate = Armor(Armor.PLATE, Armor.HEAVY)
chain = Armor(Armor.PLATE, Armor.LIGHT)
i1 = Item("A", 1, 1)
i2 = Item("B", 1, 1)
i3 = Item("C", 1, 1)
i4 = Item("D", 1, 1)
i5 = Item("E", 1, 1)
u.backpack.append(greatSword)
u.backpack.append(sword)
u.backpack.append(mace)
u.backpack.append(plate)
u.backpack.append(chain)
u.backpack.append(i1)
u.backpack.append(i2)
u.backpack.append(i3)
u.backpack.append(i4)
u.backpack.append(i5)

for p in range(1):
    m = ""
    for i in u.equippedItems:
        m += i.name + ", "
    print(m)
    u.equipFromBackpack()


