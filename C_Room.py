from helpers import *


class Room:

    def __init__(self):
        self.lastDoorLocation = 0, 0
        self.lastSide = 0

    def controlRooms(self, numberOfRooms, cols, rows, map):
        rowOffset = 0
        colOffset = 0
        x = cols
        y = rows
        randomPos = (random.randint(40, y - 40), random.randint(40, x - 50))
        randomSizes = (random.randint(10, 40), random.randint(8, 15))
        self.buildRoom((15, 15), (15, 15), 0, map)
        if numberOfRooms > 1:
            door = 1
        else:
            door = 0
        self.addDoors(door, (15, 15), (15, 15), 0, map)
        numberOfRooms -= 1
        while numberOfRooms > 0:
            if numberOfRooms > 1:
                numberOfDoors = 1
            else:
                numberOfDoors = 0
            randomOne = (random.randint(7, 20))
            randomTwo = (random.randint(8, 10))
            if self.lastSide == 1:
                rowOffset = -1
                colOffset = -1
            if self.lastSide == 2:
                rowOffset = 1
                colOffset = -1
            if self.lastSide == 3:
                rowOffset = 1
                colOffset = 1
            if self.lastSide == 4:
                rowOffset = -1
                colOffset = 1
            positions = (self.lastDoorLocation[0] + rowOffset, self.lastDoorLocation[1] + colOffset)
            try:
                self.buildRoom(positions, (8, 10), self.lastSide, map)
                self.addDoors(numberOfDoors, positions, (8, 10), self.lastSide, map)
            except:
                print("Control rooms fucked up.... dumbass")
            numberOfRooms -= 1

    def buildRoom(self, position, size, original, map):
        wall = "#"
        x = position[0]
        y = position[1]
        sizeX = size[0]
        sizeY = size[1]
        # confirm room fits in map
        # build rectangle
        if original == 0 or original == 2:
            while sizeY > 0:
                try:
                    map[x + sizeY - 1][y] = wall  # Left Side
                    map[x + sizeY - 1][y + sizeX - 1] = wall  # Right Side
                    sizeY -= 1
                except:
                    print("Error in 10/2 Top")
                    sizeY -= 1
            sizeY = size[1]
            while sizeX > 0:
                try:
                    map[x][y+sizeX - 1] = wall  # Top Side
                    map[x + sizeY - 1][y + sizeX - 1] = wall  # Bottom Side
                    sizeX -= 1
                except:
                    print("Error in 10/2 Bottom")
                    sizeX -= 1
            sizeX = size[0]
        if original == 1:
            sizeY = size[1] - 1
            while sizeY > 0:
                try:
                    map[x - sizeY][y + 2] = wall  # Right Side
                    map[x - sizeY][y - sizeX + 3] = wall  # Left Side
                    sizeY -= 1
                except:
                    print("Error in 1 Top")
                    sizeY -= 1
            sizeY = size[1]
            while sizeX > 0:
                try:
                    map[x][y-sizeX + 3] = wall  # Bottom Side
                    map[x - sizeY + 1][y - sizeX + 3] = wall  # Top Side
                    sizeX -= 1
                except:
                    print("Error in 1 Bottom")
                    sizeX -= 1
            sizeX = size[0]
        if original == 3:
            while sizeX > 0:
                try:
                    map[x - sizeX - 1][y - 2] = wall  # Left Side
                    map[x - sizeX - 1][y - sizeY - 1] = wall  # Right Side
                    sizeX -= 1
                except:
                    print("Error in 3 Top")
                    sizeX -= 1
            sizeX = size[0]
            while sizeY > 0:
                try:
                    map[x - 2][y-sizeY - 1] = wall  # Top Side
                    map[x - sizeX - 1][y - sizeY - 1] = wall  # Bottom Side
                    sizeY -= 1
                except:
                    print("Error in 3 Bottom")
                    sizeY -= 1
            sizeX = size[0]  # Top Left Corner
        if original == 4:
            while sizeX > 0:
                try:
                    map[x + sizeX - 1][y] = wall  # Left Side
                    map[x + sizeX - 1][y + sizeY - 1] = wall  # Right Side
                    sizeX -= 1
                except:
                    print("Error in 4 Top")
                    sizeX -= 1
            sizeY = size[1]
            sizeX = size[0]
            while sizeY > 0:
                try:
                    map[x][y+sizeY - 1] = wall  # Top Side
                    map[x + sizeX - 1][y + sizeY - 1] = wall  # Bottom Side
                    sizeY -= 1
                except:
                    print("Error in 4 Bottom")
                    sizeY -= 1
        x = position[0]
        y = position[1]
        sizeX = size[0]
        sizeY = size[1]

    def addDoors(self, numberOfDoors, positionOfRoom, sizeOfRoom, original, map):
        side = 0
        debug = True
        x = positionOfRoom[0]
        y = positionOfRoom[1]
        sizeX = sizeOfRoom[0] - 1
        sizeY = sizeOfRoom[1] - 1
        xValue = sizeX
        yValue = sizeY
        print(self.lastSide, self.lastDoorLocation, x, y, sizeX, sizeY)
        while numberOfDoors > 0:
            if not debug:
                side = random.randint(1, 4)
                while side == self.lastSide:
                    side = random.randint(1, 4)
                try:
                    if side == 1:  # North
                        topColLoc = random.randint(y + 1, y + yValue - 1)
                        map[x][topColLoc] = '-'
                        self.lastDoorLocation = x, topColLoc
                    if side == 2:  # South
                        bottomColLoc = random.randint(y + 1, y + yValue - 1)
                        map[x + xValue][bottomColLoc] = '_'
                        self.lastDoorLocation = x + xValue, bottomColLoc
                    if side == 3:  # East
                        rightRowLoc = random.randint(x + 1, x + xValue - 1)
                        map[rightRowLoc][y + yValue] = ']'
                        self.lastDoorLocation = rightRowLoc, y + yValue
                    if side == 4:  # West
                        leftRowLoc = random.randint(x + 1, x + xValue - 1)
                        map[leftRowLoc][y] = '['
                        self.lastDoorLocation = leftRowLoc, y
                except:
                    print("ERROR: No value for XY", side)
            else:
                side = 3
                rightRowLoc = x + 1
                map[rightRowLoc][y + yValue] = ']'
                self.lastDoorLocation = rightRowLoc, y + yValue
            numberOfDoors -= 1
            self.lastSide = side
            print(self.lastSide, self.lastDoorLocation, x, y, sizeX, sizeY)
            print('Next room:')
