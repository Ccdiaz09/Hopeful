import random
from colorama import Fore, Style


class Map:
    WATER = '`'

    OVERWORLD_CHARACTERS = [' ']
    MINIMAP_CHARACTERS = [' ']
    NON_TRAVERSABLE_CHARACTERS = ['#']

    def __init__(self, rows, cols, encounter=True, fileName=False, loadFile=False):
        self.lastDoorLocation = (0, 0)
        self.lastSide = 0
        self.grid = []
        self.nonTraversableSquares = False
        self.mapName = ""
        self.cardinalPoints = ['north', 'south', 'east', 'west']
        if loadFile:
            self.loadMap(fileName)
        else:

            self.generateMap(rows, cols, encounter)
        # fills self.grid

    def getRandomBorder(self):
        startSide = random.choice(self.cardinalPoints)
        if startSide == 'north':
            startRow = 0
            startCol = random.randint(0, 29)
        if startSide == 'east':
            startRow = random.randint(0, 9)
            startCol = 29
        if startSide == 'south':
            startRow = 9
            startCol = random.randint(0, 29)
        if startSide == 'west':
            startRow = random.randint(0, 9)
            startCol = 0
        self.cardinalPoints.remove(startSide)
        finishSide = random.choice(self.cardinalPoints)
        if finishSide == 'north':
            endRow = 0
            endCol = random.randint(0, 29)
        if finishSide == 'east':
            endRow = random.randint(0, 9)
            endCol = 29
        if finishSide == 'south':
            endRow = 9
            endCol = random.randint(0, 29)
        if finishSide == 'west':
            endRow = random.randint(0, 9)
            endCol = 0
        self.cardinalPoints = ['north', 'south', 'east', 'west']
        return startRow, startCol, endRow, endCol

    def getRandomSpot(self):
        firstRow = random.randint(0, 9)
        firstCol = random.randint(0, 29)
        endRow = random.randint(0, 9)
        endCol = random.randint(0, 29)
        for i in range(10):
            if firstRow == endRow:
                endRow = random.randint(0, 9)
            if firstCol == endCol:
                endCol = random.randint(0, 29)
        return firstRow, firstCol, endRow, endCol

    def generateMap(self, rows, cols, encounter):
        print(Style.BRIGHT)
        mapChrs = Map.MINIMAP_CHARACTERS
        if not encounter:
            mapChrs = Map.OVERWORLD_CHARACTERS
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(random.choice(mapChrs))
            self.grid.append(row)
        i = random.randint(1, 10)
        if not encounter:
            # Print the terrains
            self.makeTerrain(self.getRandomSpot(), Fore.GREEN + "T" + Fore.BLACK, 3)
            # self.makeTerrain(self.getRandomSpot(), Fore.YELLOW + '_' + Fore.BLACK, 3)
            # self.makeTerrain(self.getRandomBorder(), Fore.WHITE + '^' + Fore.BLACK, 2)
            self.makeTerrain(self.getRandomBorder(), Fore.BLUE + '~' + Fore.BLACK, 2)
            self.makeTerrain(self.getRandomBorder(), Fore.BLUE + '~' + Fore.BLACK, 2)
            self.makeTerrain(self.getRandomBorder(), Fore.BLUE + '~' + Fore.BLACK, 2)
            self.fillInBridges()
            self.placeBorder((rows - 1, cols - 1), ('-', '|'))
        else:
            # Print the rooms
            self.controlRooms(3, cols, rows)
            self.placeBorder((rows - 1, cols - 1), ('#', '#'))

    def placeBorder(self, size, symbol):
        row = 0
        col = 0
        for i in range(size[1]):
            self.grid[row][col] = symbol[0]
            col += 1
        col = 0
        for p in range(size[0]):
            self.grid[row][col] = symbol[1]
            row += 1
        row = 0
        for k in range(size[1]):
            row = size[0]
            self.grid[row][col] = symbol[0]
            col += 1
        col = 0
        row = 0
        for o in range(size[0]):
            col = size[1]
            self.grid[row][col] = symbol[1]
            row += 1

    def makeTerrain(self, startAndStop,  _symbol, width):
        startX = startAndStop[0]
        startY = startAndStop[1]
        finishX = startAndStop[2]
        finishY = startAndStop[3]
        dx = finishX - startX
        dy = finishY - startY
        xProcessed = 0
        yProcessed = 0
        directionX = 1
        if dx < 0:
            directionX = -1
        directionY = 1
        if dy < 0:
            directionY = -1
        while xProcessed < abs(dx) or yProcessed < abs(dy):
            remainingXMoves = abs(dx) - abs(xProcessed)
            remainingYMoves = abs(dy) - abs(yProcessed)
            if remainingXMoves > remainingYMoves:
                xProcessed += 1
                self.placeTerrain(_symbol, xProcessed, yProcessed, directionY, directionX, startX, startY, width, 1, 0)
            else:
                yProcessed += 1
                self.placeTerrain(_symbol, xProcessed, yProcessed, directionY, directionX, startX, startY, width, 1, 0)

    def placeTerrain(self, _symbol, xProcessed, yProcessed, directionY, directionX, startX, startY, width, px, py):
        bridgeSymbol = "="
        symbol = _symbol
    # hello
        try:
            # if random.randint(1, 8) == 1 and symbol[5] == '~':
                # symbol = bridgeSymbol
            newCol = startY+yProcessed*directionY
            newRow = startX + xProcessed*directionX
            if self.grid[newRow][newCol] == bridgeSymbol:
                pass
            else:
                self.grid[newRow][newCol] = symbol
            if random.randint(1, 2) == 1:
                for i in range(width):
                    if self.grid[newRow][newCol] == bridgeSymbol:
                        if _symbol == '[34m~[30m':
                            pass
                            # bad place to put this line.

                            # self.fillInBridges(newRow, newCol, bridgeSymbol)
                        else:
                            pass
                    else:
                        self.grid[newRow+py*i][newCol+px*i] = symbol
                        self.grid[newRow+py*i][newCol-i*px] = symbol
        except:
                pass

    def placeBridges(self, maxNumber):
        #  look for a place that satisfies up and down or left right
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3
        RIVER = '[34m~[30m'

        rowCounter = 0
        bridgesPlaced = 0
        for row in self.grid:
            colCounter = -1
            for col in row:
                colCounter += 1

                if col == RIVER and random.randint(1,6) == 1 and bridgesPlaced < maxNumber:
                    distanceRight = self.getRiversInDirection(1, 0, rowCounter, colCounter, "right")
                    distanceLeft = self.getRiversInDirection(-1, 0, rowCounter, colCounter, "left")
                    distanceUp = self.getRiversInDirection(0, -1, rowCounter, colCounter, "Up")
                    distanceDown = self.getRiversInDirection(0, 1, rowCounter, colCounter, "Down")
                    results = [distanceLeft, distanceRight, distanceUp, distanceDown]
                    min = 100
                    for item in results:
                        if min > item > 1:
                            min = item

                    indexOfMin = 1
                    if not min == 100:
                        indexOfMin = results.index(min)
                        print(results)
                    if results[LEFT] == 0 and results[RIGHT] == 0:
                        print("left and right satisfied")
                        self.grid[rowCounter][colCounter] = '%'
                        bridgesPlaced += 1
                    elif results[UP] == 0 and results[DOWN] == 0:
                        print("up and down satisfied")
                        self.grid[rowCounter][colCounter] = '%'
                        bridgesPlaced += 1
            rowCounter += 1
            print(bridgesPlaced)

    def fillInBridges(self):
        RIVER = '[34m~[30m'
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3
        rowCounter = 0
        for row in self.grid:
            colCounter = -1
            for col in row:
                colCounter += 1
                if col == "=":
                    print("bridgeFound at" + str(colCounter) + " , " + str(rowCounter))

                    distanceRight = self.getRiversInDirection(1, 0, rowCounter, colCounter, "right")
                    distanceLeft = self.getRiversInDirection(-1, 0, rowCounter, colCounter, "left")
                    distanceUp = self.getRiversInDirection(0, -1, rowCounter, colCounter, "Up")
                    distanceDown = self.getRiversInDirection(0, 1, rowCounter, colCounter, "Down")
                    results = [distanceLeft, distanceRight, distanceUp, distanceDown]
                    min = 100
                    for item in results:
                        if min > item > 1:
                            min = item
                    indexOfMin = 1
                    if not min == 100:
                        indexOfMin = results.index(min)
                        print(results)
                    if results[LEFT] == 0 and results[RIGHT] == 0:
                        print("left and right satisfied")
                    elif results[UP] == 0 and results[DOWN] == 0:
                        print("up and down satisfied")
                    else:
                        print("placed at:" + str(colCounter) + "," + str(rowCounter))
                        if indexOfMin == LEFT:
                            self.placeBridgeInDirectionFromRowCol((-1, 0), rowCounter, colCounter)
                        if indexOfMin == RIGHT:
                            self.placeBridgeInDirectionFromRowCol((1, 0), rowCounter, colCounter)
                        if indexOfMin == UP:
                            self.placeBridgeInDirectionFromRowCol((0, -1), rowCounter, colCounter)
                        if indexOfMin == DOWN:
                            self.placeBridgeInDirectionFromRowCol((0, 1), rowCounter, colCounter)
            rowCounter += 1

    def getRiversInDirection(self, dx, dy, rowCounter, colCounter, directionString):
        RIVER = '[34m~[30m'
        ret = 0
        try:
            while self.grid[rowCounter + ret * dy + dy][colCounter + ret * dx + dx] == RIVER:
                ret += 1
                print(directionString)
        except:
            self.grid[rowCounter][colCounter] = RIVER
            print("exception " + directionString)
            return 99
        return ret

    def placeBridgeInDirectionFromRowCol(self,d,row,col):
        self.displayAll()
        RIVER = '[34m~[30m'
        BRIDGE = "!"
        print("direction = " + str(d))
        dx = d[0]
        dy = d[1]
        moveX = 0
        moveY = 0
        currentX = col+dx
        currentY = row+dy
        next = RIVER
        try:
            while next == RIVER:
                moveX += dx
                moveY += dy
                next = self.grid[currentY + moveY + dy][currentX + moveX + dx]
                self.grid[currentY + moveX][currentX + moveX] = BRIDGE
                targetX = moveX + col
                targetY = moveY + row
                next = self.grid[targetY][targetX]
                self.grid[targetY][targetX] = BRIDGE
                print("placed new bridge at ")
        except:
            print("place bridge exception")

    def buildRoom(self, position, size, doors, original):
        wall = "#"
        x = position[0]
        y = position[1]
        sizeX = size[0]
        sizeY = size[1]
        # confirm room fits in map
        # build rectangle
        if original == 10 or original == 2:
            while sizeY > 0:
                try:
                    self.grid[x + sizeY - 1][y] = wall  # Left Side
                    self.grid[x + sizeY - 1][y + sizeX - 1] = wall  # Right Side
                    sizeY -= 1
                except:
                    print("Error in 10/2 Top")
                    sizeY -= 1
            sizeY = size[1]
            while sizeX > 0:
                try:
                    self.grid[x][y+sizeX - 1] = wall  # Top Side
                    self.grid[x + sizeY - 1][y + sizeX - 1] = wall  # Bottom Side
                    sizeX -= 1
                except:
                    print("Error in 10/2 Bottom")
                    sizeX -= 1
            self.grid[self.lastDoorLocation[0] + 1][self.lastDoorLocation[1]] = '0'
            sizeX = size[0]
            self.grid[x][y] = wall  # Top Left Corner
        if original == 1:
            sizeY = size[1] - 1
            while sizeY > 0:
                try:
                    self.grid[x - sizeY][y + 2] = wall  # Right Side
                    self.grid[x - sizeY][y - sizeX + 3] = wall  # Left Side
                    sizeY -= 1
                except:
                    print("Error in 1 Top")
                    sizeY -= 1
            sizeY = size[1]
            while sizeX > 0:
                try:
                    self.grid[x][y-sizeX + 3] = wall  # Bottom Side
                    self.grid[x - sizeY + 1][y - sizeX + 3] = wall  # Top Side
                    sizeX -= 1
                except:
                    print("Error in 1 Bottom")
                    sizeX -= 1
            self.grid[self.lastDoorLocation[0] - 1][self.lastDoorLocation[1]] = '0'
            sizeX = size[0]
        if original == 3:
            while sizeX > 0:
                try:
                    self.grid[x - sizeX - 1][y - 2] = wall  # Left Side
                    self.grid[x - sizeX - 1][y - sizeY - 1] = wall  # Right Side
                    sizeX -= 1
                except:
                    print("Error in 3 Top")
                    sizeX -= 1
            sizeX = size[0]
            while sizeY > 0:
                try:
                    self.grid[x - 2][y-sizeY - 1] = wall  # Top Side
                    self.grid[x - sizeX - 1][y - sizeY - 1] = wall  # Bottom Side
                    sizeY -= 1
                except:
                    print("Error in 3 Bottom")
                    sizeY -= 1
            self.grid[self.lastDoorLocation[0]][self.lastDoorLocation[1] - 1] = '0'
            sizeX = size[0]  # Top Left Corner
        if original == 4:
            while sizeX > 0:
                try:
                    self.grid[x + sizeX - 1][y] = wall  # Left Side
                    self.grid[x + sizeX - 1][y + sizeY - 1] = wall  # Right Side
                    sizeX -= 1
                except:
                    print("Error in 4 Top")
                    sizeX -= 1
            sizeY = size[1]
            sizeX = size[0]
            while sizeY > 0:
                try:
                    self.grid[x][y+sizeY - 1] = wall  # Top Side
                    self.grid[x + sizeX - 1][y + sizeY - 1] = wall  # Bottom Side
                    sizeY -= 1
                except:
                    print("Error in 4 Bottom")
                    sizeY -= 1
            self.grid[self.lastDoorLocation[0]][self.lastDoorLocation[1] + 1] = '0'
            sizeX = size[0]
            self.grid[x][y] = wall  # Top Left Corner
            sizeY = size[1]
        self.addDoors(doors, (x, y), (sizeX, sizeY), original)

    def addDoors(self, numberOfDoors, positionOfRoom, sizeOfRoom, original):
        debug = False
        side = 0
        x = positionOfRoom[0]
        y = positionOfRoom[1]
        sizeX = sizeOfRoom[0] - 1
        sizeY = sizeOfRoom[1] - 1
        xValue = sizeX
        yValue = sizeY
        if original == 3:
            pass
        if original == 1:
            xValue = -sizeX
            yValue = -sizeY
        if original == 2:
            xValue = sizeX
            yValue = -sizeY
        if original == 4:
            xValue = -sizeX
            yValue = sizeY
        while numberOfDoors > 0:
            if not debug:
                while side == self.lastSide:
                    side = random.randint(1, 4)
                try:
                    if side == 1:
                        topRow = random.randint(y + 1, y + xValue - 1)
                        self.lastDoorLocation = x, topRow
                        self.grid[x][topRow] = '!'
                    if side == 2:
                        bottomRow = random.randint(y + 1, y + xValue - 1)
                        self.lastDoorLocation = x + yValue, bottomRow
                        self.grid[x + yValue][bottomRow] = '!'
                    if side == 3:
                        leftCol = random.randint(x + 1, x+yValue - 1)
                        self.lastDoorLocation = leftCol, y
                        self.grid[leftCol][y] = '!'
                    if side == 4:
                        leftCol = random.randint(x + 1, x+yValue - 1)
                        self.grid[leftCol][y + xValue] = '!'
                        self.lastDoorLocation = leftCol, y + xValue
                except:
                    print("ERROR: No value for XY", side)
            else:
                side = 1
                self.lastDoorLocation = x, y+1
                self.grid[x][y + 1] = '!'
            numberOfDoors -= 1
            self.lastSide = side

    def controlRooms(self, numberOfRooms, cols, rows):
        rowOffset = 0
        colOffset = 0
        x = cols
        y = rows
        self.buildRoom((random.randint(40, y - 40), random.randint(40, x - 50)), (random.randint(10, 40),
                                                                                  random.randint(8, 15)), 1, 10)
        numberOfRooms -= 1
        while numberOfRooms > 0:
            if numberOfRooms > 1:
                numberOfDoors = 1
            else:
                numberOfDoors = 0
            if self.lastSide == 1:
                rowOffset = -1
                colOffset = -1
            if self.lastSide == 2:
                rowOffset = 1
                colOffset = -1
            if self.lastSide == 3:
                rowOffset = 3
                colOffset = 1
            if self.lastSide == 4:
                rowOffset = -1
                colOffset = 1
            try:
                self.buildRoom((self.lastDoorLocation[0] + rowOffset, self.lastDoorLocation[1] + colOffset),
                               (random.randint(7, 20), random.randint(8, 10)), numberOfDoors, self.lastSide)
            except:
                print(self.grid)
            numberOfRooms -= 1

    def saveMap(self, fileName):
        if not fileName == False:
            file = open(fileName, "w+")
            for row in self.grid:
                r = ""
                for col in row:
                    r += col
                r += '\n'
                file.write(r)
        else:
            print("save error in C_MAP, no filename defined.")

    def loadMap(self, fileName):
        with open(fileName) as f:
            content = f.readlines()
        content = [x.strip('\n') for x in content]
        for row in content:
            self.grid.append(row)

    def getCharacterAtColRow(self, col, row):
        try:
            character = self.grid[row][col]
        except:
            character = 0
        return character

    def validateMove(self, destination):
        traversable = True
        newRow = destination[1]
        newCol = destination[0]
        cols = self.grid[0].__len__()  # ghetto needs to be changed if non rectangular maps...
        rows = self.grid.__len__()
        c = self.getCharacterAtColRow(newCol, newRow)
        try:
            if c.__len__() > 1:
                q = c[5]

            else:
                q = c
            if q == '~' or q == '^' or q == '#' or q == '|' or q == '-':
                traversable = False
            else:
                pass
        except:
            pass
        if newCol < 0 or newCol > cols - 1 or newRow < 0 or newRow > rows - 1 or not traversable:
            return False
        else:
            return True
        pass

    def displayAll(self):
        # world print all
        for row in self.grid:
            m = ""
            for col in row:
                m += col
            print(m)

    def displayFromVision(self, guy):
        for r in range(3):
            m = ""
            for c in range(3):
                targetCol = guy.col + c
                targetRow = guy.col + r
                if targetCol < 0 or targetRow < 0 or targetRow > self.grid.__len__() - 1 or targetCol > \
                        self.grid[0].__len__() - 1:
                    print("Invalid")
                else:
                    # printing p in the middle
                    if c == 1 and r == 1:
                        m += Fore.BLUE + "P" + Fore.BLACK
                    else:
                        m += self.grid[targetRow][targetCol]
            print(m)
        print("\n")
