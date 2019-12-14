from math import sqrt, pow


class LineObject():
    def __init__(self, from_pos, to_pos):
        self.startPos = from_pos
        self.endPos = to_pos
        self.distance = self.GetDistance(from_pos, to_pos)
        self.slope = self.GetSlope(from_pos, to_pos)

    def GetDistance(self, from_pos, to_pos):
        x1 = from_pos[0]
        y1 = from_pos[1]
        x2 = to_pos[0]
        y2 = to_pos[1]
        self.distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
        return self.distance

    def GetSlope(self, from_pos, to_pos):
        x1 = from_pos[0]
        y1 = from_pos[1]
        x2 = to_pos[0]
        y2 = to_pos[1]
        try:
            self.slope = (x2 - x1) / (y2 - y1)
        except ZeroDivisionError:
            return 0
        return self.slope

    @property
    def Distance(self):
        return self.distance

    @property
    def StartPos(self):
        return self.startPos

    @property
    def EndPos(self):
        return self.endPos

    @property
    def Slope(self):
        return self.slope


class WireObject():
    START_POS = (0, 0)
    X_MOVE, Y_MOVE = range(2)

    def __init__(self):
        self.posX = WireObject.START_POS[0]
        self.posY = WireObject.START_POS[-1]
        self.history = [(self.posX, self.posY)]
        self.intersectList = []
        self.steps = []

    def Move(self, x=0, y=0):
        if x:
            self.steps.append(abs(x))
        else:
            self.steps.append(abs(y))
        self.posY += y
        self.posX += x
        self.GetIntersect(self.history[-1], (self.posX, self.posY))
        self.history.append(self.Position)
        return self.Position

    def _getIntersect(self, posA, posB, posC, posD):
        if (posA[0] == posB[0]):
            tmp = posA
            posA = posC
            posC = tmp
            tmp = posB
            posB = posD
            posD = tmp

        if (posC[0] == posD[0]):
            if (posA[0] == posB[0]):
                return None

            if (posA[0] > posB[0]):
                tmp = posA
                posA = posB
                posB = tmp

            if (posC[1] > posD[1]):
                tmp = posC
                posC = posD
                posD = tmp

            if (posC[0] > posA[0] and posC[0] < posB[0] and posA[1] > posC[1] and posA[1] < posD[1]):
                return (posC[0], posA[1])

        return None

    def GetIntersect(self, from_pos, to_pos):
        # Loop through previous positions and play through it to find if there
        # is any line that intersects
        for count, histPos in enumerate(self.history):
            if count < 0:
                continue

            intersect = self._getIntersect(
                from_pos, to_pos, self.history[count - 1], histPos)
            if intersect:
                self.intersectList.append(intersect)
        return self.intersectList

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
        return (self.posX, self.posY)

    def GetSteps(self, stop=None):
        if stop:
            return sum(self.steps[:stop])
        return sum(self.steps)


class MoveMachine(object):
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'

    def __init__(self,):
        self.allWires = []
        self.intersectList = []

    def AddWire(self):
        self.wireObj = WireObject()
        self.allWires.append(self.wireObj)
        self.intersectList = []
        self.stepsList = []
        return self.wireObj

    def MoveWire(self, wireObj, direction, movement):
        if direction == MoveMachine.RIGHT:
            wireObj.Move(movement, 0)
        if direction == MoveMachine.LEFT:
            wireObj.Move(-movement, 0)
        if direction == MoveMachine.UP:
            wireObj.Move(0, movement)
        if direction == MoveMachine.DOWN:
            wireObj.Move(0, -movement)
        return wireObj.Position

    def MoveWireByData(self, wireObj, data):
        for i in data:
            direction = i[0]
            move = int(i.replace(direction, ''))
            self.MoveWire(wireObj, direction, move)
        return wireObj

    def _getIntersect(self, posA, posB, posC, posD):
        line1x = posB[0] - posA[0]
        line1y = posB[1] - posA[1]

        line2x = posD[0] - posC[0]
        line2y = posD[1] - posC[1]

        x = None
        y = None

        if line1x and line2y:
            if line2y > 0:
                yRange = range(posC[1], posD[1] + 1)
            else:
                yRange = range(posD[1], posC[1] + 1)
            if posA[1] in yRange:
                if line1x > 0:
                    xRange = range(posA[0], posB[0] + 1)
                else:
                    xRange = range(posB[0], posA[0 + 1])
                if posC[0] in xRange:
                    x = posD[0]
                    y = posB[1]
        if line1y and line2x:
            if line2x > 0:
                xRange = range(posC[0], posD[0] + 1)
            else:
                xRange = range(posD[0], posC[0] + 1)
            if posA[0] in xRange:
                if line1y > 0:
                    yRange = range(posA[1], posB[1] + 1)
                else:
                    yRange = range(posB[1], posA[1] + 1)
                if posC[1] in yRange:
                    x = posB[0]
                    y = posD[1]

        if x and y:
            return (x, y)
        return None

    def GetIntersects(self, wireObj):
        wireAsteps = 0
        wireBsteps = 0

        for allWire in self.allWires:
            if allWire != wireObj:
                for count, thisWireHistPos in enumerate(wireObj.History):
                    if count < 0:
                        continue

                    from_pos = wireObj.History[count - 1]
                    to_pos = thisWireHistPos

                    for i, histPos in enumerate(allWire.History):
                        if i < 0:
                            continue
                        intersect = self._getIntersect(
                            from_pos, to_pos, allWire.History[i - 1], histPos)

                        if intersect:
                            self.intersectList.append(intersect)

                            wireAsteps = wireObj.GetSteps(count - 1)
                            wireAsteps += self._getDistanceBetweenTwoPoints(
                                from_pos, intersect)
                            wireBsteps = allWire.GetSteps(i - 1)
                            wireBsteps += self._getDistanceBetweenTwoPoints(
                                allWire.History[i - 1], intersect)
                            self.stepsList.append(int(wireAsteps + wireBsteps))
        return self.intersectList

    def _getDistanceBetweenTwoPoints(self, from_pos, to_pos):
        x1 = from_pos[0]
        y1 = from_pos[1]
        x2 = to_pos[0]
        y2 = to_pos[1]
        distance = sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))
        return distance

    def Wires(self):
        return self.allWires

    def DistanceToStart(self, x, y):
        return int(abs(x) + abs(y))

    def GetShortestDistanceToStart(self):
        distances = []
        if not self.intersectList:
            for wireObj in self.allWires:
                self.GetIntersects(wireObj)
        for intersect in self.intersectList:
            distances.append(self.DistanceToStart(intersect[0], intersect[1]))
        if not distances:
            return 0
        return sorted(distances)[0]

    def GetShortestDistanceFromStepsToStart(self):
        stepDict = {}
        if not self.intersectList:
            for wireObj in self.allWires:
                self.GetIntersects(wireObj)
        for steps, intersect in zip(self.stepsList, self.intersectList):
            stepDict[steps] = intersect
        if not stepDict:
            return 0
        return sorted(self.stepsList)[0]


def SolveA(dataSet):
    machine = MoveMachine()
    for data in dataSet:
        wire = machine.AddWire()
        machine.MoveWireByData(wire, data)
    return machine.GetShortestDistanceToStart()


def SolveB(dataSet):
    machine = MoveMachine()
    for data in dataSet:
        wire = machine.AddWire()
        machine.MoveWireByData(wire, data)
    return machine.GetShortestDistanceFromStepsToStart()


def main():
    dataSet = []

    with open('day3-inputs.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            dataSet.append([i.replace('\n', '') for i in line.split(',')])
        f.close()
    print SolveA(dataSet)
    print SolveB(dataSet)
    print 'Solved.'


if __name__ == '__main__':
    main()
