class Item:
    WEAPON = 1
    ARMOR = 2
    MISC = 3
    SMALL = 4
    MEDIUM = 5
    LARGE = 6

    def __init__(self, name, cost, itemType, size=SMALL):
        self.name = name
        self.cost = cost
        self.itemType = itemType
        self.size = size


class Weapon(Item):
    BLADE = 1
    HAMMER = 2
    AXE = 3
    SMALL = 4
    MEDIUM = 5
    LARGE = 6

    def __init__(self, type, size):
        super().__init__(self.getName(size, type), 1, Item.WEAPON, size)
        self.damage = 1
        self.accuracy = 1

    def getName(self, size, type):
        if size == Weapon.LARGE:
            if type == Weapon.BLADE:
                name = "Great Sword"
            if type == Weapon.AXE:
                name = "Giant Axe"
            if type == Weapon.HAMMER:
                name = "Maul"
        if size == Weapon.MEDIUM:
            if type == Weapon.BLADE:
                name = "Longsword"
            if type == Weapon.AXE:
                name = "Battle Axe"
            if type == Weapon.HAMMER:
                name = "War Hammer"
        if size == Weapon.SMALL:
            if type == Weapon.BLADE:
                name = "Dagger"
            if type == Weapon.AXE:
                name = "Hatchet"
            if type == Weapon.HAMMER:
                name = "Cudgel"
        return name


class Armor(Item):
    CLOTH = 1
    LEATHER = 2
    PLATE = 3
    LIGHT = 1
    HEAVY = 2

    def __init__(self, type, size):
        super().__init__(self.getName(size, type), 1, type, size)

    def getName(self, size, type):
        if size == Armor.LIGHT:
            if type == Armor.CLOTH:
                name = "Silk Armor"
            if type == Armor.LEATHER:
                name = "Leather Armor"
            if type == Armor.PLATE:
                name = "Chain Mail"
        if size == Armor.HEAVY:
            if type == Armor.CLOTH:
                name = "Padded Armor"
            if type == Armor.LEATHER:
                name = "Studded Leather"
            if type == Armor.PLATE:
                name = "Plate Mail"
        return name
