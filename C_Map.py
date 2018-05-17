import random
from colorama import Fore, Style


class Map:
    WATER = '`'

    OVERWORLD_CHARACTERS = [' ']
    MINIMAP_CHARACTERS = [' ']
    NON_TRAVERSABLE_CHARACTERS = ['#']

    def __init__(self, rows, cols, encounter=True, fileName=False, loadFile=False):
        self.grid = []
        self.nonTraversableSquares = False
        self.mapName = ""
        self.cardinalPoints = ['north', 'south', 'east', 'west']
        if loadFile:
            self.loadMap(fileName)
        else:

            self.generateMap(rows, cols, encounter)
        # fills self.grid

    def getRandomBorder(self, size):
        # gets a random border
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
        if size == 3:
            finishSide = random.choice(self.cardinalPoints)
        if size == 2:
            if startSide == 'north':
                possibleFinish = ['east', 'west']
            if startSide == 'south':
                possibleFinish = ['east', 'west']
            if startSide == 'east':
                possibleFinish = ['north', 'south']
            if startSide == 'west':
                possibleFinish = ['north', 'south']
            finishSide = random.choice(possibleFinish)
        if size == 1:
            if startSide == 'north':
                possibleFinish = ['east', 'north', 'west']
            if startSide == 'south':
                possibleFinish = ['east', 'west', 'south']
            if startSide == 'east':
                possibleFinish = ['north', 'east', 'south']
            if startSide == 'west':
                possibleFinish = ['north', 'south', 'west']
            finishSide = random.choice(possibleFinish)
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
            # self.makeTerrain(self.getRandomBorder(2), Fore.WHITE + '^' + Fore.BLACK, 2)
            # self.makeTerrain(self.getRandomSpot(), Fore.YELLOW + '_' + Fore.BLACK, 3)
            self.makeTerrain(self.getRandomBorder(2), Fore.BLUE + '~' + Fore.BLACK, 2)
            self.placeBorder((9, 29))
        else:
            # Print the rooms
            self.buildRoom((18, 9), (140, 14))
            self.placeBorder((19, 19))

    def placeBorder(self, type):
        row = 0
        col = 0
        numberOfRows = type[0]
        numberOfCols = type[1]
        for i in range(numberOfCols):
            self.grid[row][col] = '-'
            col += 1
        col = 0
        for p in range(numberOfRows):
            self.grid[row][col] = '|'
            row += 1
        row = 0
        for k in range(numberOfCols):
            row = numberOfRows
            self.grid[row][col] = '-'
            col += 1
        col = 0
        row = 0
        for o in range(numberOfRows):
            col = numberOfCols
            self.grid[row][col] = '|'
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
        try:
            if random.randint(1, 8) == 1 and symbol[5] == '~':
                symbol = bridgeSymbol
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
                            self.fillInBridges(newRow, newCol, bridgeSymbol)
                        else:
                            pass
                    else:
                        self.grid[newRow+py*i][newCol+px*i] = symbol
                        self.grid[newRow+py*i][newCol-i*px] = symbol
        except:
                pass

    def fillInBridges(self, bridgeStartRow, bridgeStartCol, bridgeSymbol):
        for row in self.grid:
            for col in row:
                if col == "=":
                    lookingLeft = True
                    lookingRight = False
                    lookingUp = False
                    lookingDown = False
                    leftCounter = 0
                    rightCounter = 0
                    upCounter = 0
                    downCounter = 0
                    # Checking the directions!
                    while lookingLeft:
                        check = self.grid[bridgeStartRow][bridgeStartCol-leftCounter]
                        if check == '~' or '=':
                            leftCounter += 1
                        if check != '~' or '=':
                            lookingLeft = False
                            lookingRight = True
                    while lookingRight:
                        check = self.grid[bridgeStartRow][bridgeStartCol+rightCounter]
                        if check == "~" or '=':
                            rightCounter += 1
                        if check != '~' or '=':
                            lookingRight = False
                            lookingUp = True
                    while lookingUp:
                        check = self.grid[bridgeStartRow-upCounter][bridgeStartCol]
                        if check == "~" or '=':
                            upCounter += 1
                        if check != '~' or '=':
                            lookingUp = False
                            lookingDown = True
                    while lookingDown:
                        check = self.grid[bridgeStartRow][bridgeStartCol-downCounter]
                        if check == "~" or '=':
                            downCounter += 1
                        if check != '~' or '=':
                            lookingDown = False
                    leftToRight = leftCounter + rightCounter
                    upToDown = upCounter + downCounter
                    # Print the bridge
                    if upToDown > leftToRight:
                        while leftCounter > 0:
                            leftCounter -= 1
                            self.grid[bridgeStartRow][bridgeStartCol-leftCounter] = bridgeSymbol
                        while rightCounter > 0:
                            rightCounter -= 1
                            self.grid[bridgeStartRow][bridgeStartCol+rightCounter] = bridgeSymbol
                    if upToDown <= leftToRight:
                        while upCounter > 0:
                            upCounter -= 1
                            self.grid[bridgeStartRow-upCounter][bridgeStartCol] = bridgeSymbol
                        while downCounter > 0:
                            downCounter -= 1
                            self.grid[bridgeStartCol+downCounter][bridgeStartCol] = bridgeSymbol

    def buildRoom(self, position, size):
        wall = '#'
        x = position[0]
        y = position[1]
        sizeX = size[0] - 1
        sizeY = size[1] - 1
        try:
            self.grid[x][y] = wall
            while sizeX > 0 or sizeY > 0:
                self.grid[x - sizeX][y] = wall
                self.grid[x][y - sizeY] = wall
                sizeX -= 1
                sizeY -= 1
            sizeY = size[1]
            sizeX = size[0]
            while sizeX > 0:
                self.grid[x - sizeX+1][y-sizeY+1] = wall
                sizeX -= 1
            sizeX = size[0]
            sizeY = size[1]
            while sizeY > 0:
                self.grid[x - sizeX+1][y-sizeY+1] = wall
                sizeY -= 1
        except:
            print('Error In the Room function')

    def buildRoomOld(self, position, size, doors):
        doorSymbol = ']'
        wall = "#"
        x = position[0]
        y = position[1]
        sx = size[0]
        sy = size[1]
        # confirm room fits in map
        # build rectangle
        for ix in range(sx):
            self.grid[ix+x][y] = wall
            self.grid[ix+x][y+sy] = wall
        for iy in range(sy):
            self.grid[x][iy+1+y] = wall
            self.grid[x+sy][iy+1+y] = wall
        # add doors
        for door in range(doors):
            possibleRemainingDoors = self.cardinalPoints
            for door in range(doors-1):
                if possibleRemainingDoors.__len__() > 0:
                    d = random.choice(possibleRemainingDoors)
                    # place door on chosen wall
                    if d == 'north' or True:
                        doorY = y
                        doorX = random.randint(x+1, sx+x-1)
                        self.grid[doorY][doorX] = doorSymbol
                    if d == 'south':
                        doorY = random.randint(y+1, sy + y-1)
                        doorX = x
                        self.grid[doorY][doorX] = doorSymbol
                    if d == 'east':
                        pass
                    if d == 'west':
                        pass
                    possibleRemainingDoors.remove(d)

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
        except:
            pass
        if newCol < 0 or newCol > cols-1 or newRow < 0 or newRow > rows-1 or not traversable:
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
                if targetCol < 0 or targetRow < 0 or targetRow > self.grid.__len__() - 1 or targetCol >\
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
