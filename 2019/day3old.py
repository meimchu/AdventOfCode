class WireObject(object):
    START_POS = [0, 0]

    def __init__(self):
        self.posX = WireObject.START_POS[0]
        self.posY = WireObject.START_POS[-1]
        self.history = [[self.posX, self.posY]]
        self.intersectList = []

    def MoveX(self, x):
        for moveX in range(1, abs(x) + 1):
            pastY = self.Position[-1]
            if x > 0:
                self.posX += 1
            else:
                self.posX -= 1
            if self._checkIntersect(self.Position):
                self.intersectList.append(self.Position)
            self.history.append([self.posX, pastY])
        return self.Position

    def MoveY(self, y):
        for moveY in range(1, abs(y) + 1):
            pastX = self.Position[0]
            if y > 0:
                self.posY += 1
            else:
                self.posY -= 1
            if self._checkIntersect(self.Position):
                self.intersectList.append(self.Position)
            self.history.append([pastX, self.posY])
        return self.Position

    def _checkIntersect(self, position):
        if position in self.history:
            return True
        return False

    @property
    def Intersects(self):
        return self.intersectList

    @property
    def Distance(self):
        x, y = self.Position
        return int(abs(x) + abs(y))

    @property
    def History(self):
        return self.history

    @property
    def Position(self):
        return [self.posX, self.posY]


class MoveMachine(object):
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'

    def __init__(self,):
        self.allWires = []

    def AddWire(self):
        self.wireObj = WireObject()
        self.allWires.append(self.wireObj)
        return self.wireObj

    def MoveWire(self, wireObj, direction, movement):
        if direction == MoveMachine.RIGHT:
            wireObj.MoveX(movement)
        if direction == MoveMachine.LEFT:
            wireObj.MoveX(-movement)
        if direction == MoveMachine.UP:
            wireObj.MoveY(movement)
        if direction == MoveMachine.DOWN:
            wireObj.MoveY(-movement)
        return wireObj.Position

    def MoveWireByData(self, wireObj, data):
        for i in data:
            direction = i[0]
            move = int(i.replace(direction, ''))
            self.MoveWire(wireObj, direction, move)
        return wireObj

    def GetIntersects(self):
        intersects = []
        allWireHistory = []
        if not self.allWires:
            return None
        for wire in self.allWires:
            for history in wire.History:
                if history not in wire.Intersects:
                    if history in allWireHistory and history != WireObject.START_POS:
                        intersects.append(history)
                    allWireHistory.append(history)
        return intersects

    def Wires(self):
        return self.allWires

    def DistanceToStart(self, x, y):
        return int(abs(x) + abs(y))

    def GetShortestDistanceToStart(self):
        distances = []
        for intersect in self.GetIntersects():
            distances.append(self.DistanceToStart(intersect[0], intersect[-1]))
        if not distances:
            return 0
        return sorted(distances)[0]


def SolveA(dataSet):
    machine = MoveMachine()
    for data in dataSet:
        wire = machine.AddWire()
        machine.MoveWireByData(wire, data)
        print 'Wire intersect', wire.Intersects
    return machine.GetShortestDistanceToStart()


def main():
    dataSet = []

    # with open('day3-wires-data.txt', 'r') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         dataSet.append([i.replace('\n', '') for i in line.split(',')])
    #     f.close()
    # dataSet = [["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"], [
    #     "U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]]
    # dataSet = [["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"], [
    # "U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]]
    dataSet = [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
    print SolveA(dataSet)
    # print SolveB(dataSet)
    print 'Solved.'


if __name__ == '__main__':
    main()
