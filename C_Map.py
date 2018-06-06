from colorama import Fore, Style
from C_Room import *


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
        room = Room()
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
            room.controlRooms(3, cols, rows, self.grid)
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
