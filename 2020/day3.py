from aoc_timer import time_it


class PuzzleMap():
    def __init__(self, puzzleMap):
        self._puzzleMap = puzzleMap
        self._row = len(self._puzzleMap[0])
        self._column = len(self._puzzleMap)

    @property
    def puzzleMap(self):
        return self._puzzleMap

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column
    
    def drawLine(self, x, y):
        line = self.puzzleMap[y-1]
        line = list(line)
        if x > self.row:
            x = x % self.row
        line[x - 1] = 'O'
        if self.hitTree(x, y):
            line[x - 1] = 'X'
        return ''.join(line)

    def itemAtPosition(self, x, y):
        if x > self.row:
            x = x % self.row
        return self._puzzleMap[y-1][x-1]

    def hitTree(self, x, y):
        item = self.itemAtPosition(x, y)
        if item == '#':
            return True
        return False


@time_it
def SolverA(puzzleMap):
    mapObj = PuzzleMap(puzzleMap)
    posX = 1
    posY = 1
    treeHits = 0
    while posY <= mapObj.column:
        # print(mapObj.drawLine(posX, posY))
        if mapObj.hitTree(posX, posY):
            treeHits += 1
        posX += 3
        posY += 1
    return treeHits

@time_it
def SolverB(puzzleMap):
    mapObj = PuzzleMap(puzzleMap)
    posList = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    totalTreeHits = []
    for x, y in posList:
        posX = 1
        posY = 1
        treeHits = 0
        while posY <= mapObj.column:
            # print(mapObj.drawLine(posX, posY))
            if mapObj.hitTree(posX, posY):
                treeHits += 1
            posX += x
            posY += y
        totalTreeHits.append(treeHits)
    
    treeHitProduct = 1
    for treeHit in totalTreeHits:
        treeHitProduct *= treeHit
    return treeHitProduct

def main():
    puzzleMap = []
    with open('day3-input.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            puzzleMap.append(line)

    print(SolverA(puzzleMap))
    print(SolverB(puzzleMap))


if __name__ == '__main__':
    main()
