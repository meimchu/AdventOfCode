from itertools import product


class IntcodeObject(object):
    ADD = 1
    MULT = 2
    END = 99

    def __init__(self):
        self.intcodes = [self.ADD, self.MULT, self.END]

    def AllIntCodes(self, intcode):
        return self.intcodes

    def _validateIntcode(self):
        if self.intcode not in self.intcodes:
            raise RuntimeError(
                'Intcode needs to be one of the following option %s.' % self.intcodes)

    def _validateInputs(self):
        if not isinstance(self.a, int) and not isinstance(self.b, int):
            raise RuntimeError('a and b inputs both need to be integers.')

    def Operation(self, intcode, a, b):
        self.intcode = intcode
        self.a = a
        self.b = b

        self._validateIntcode()
        self._validateInputs()

        if intcode is self.ADD:
            return a + b
        if intcode is self.MULT:
            return a * b
        if intcode is self.END:
            return None


class IntcodeListObject(object):
    def __init__(self, intList):
        self.intList = intList

        self.Validate(self.intList)
        self.intcodeOp = IntcodeObject()

    def Validate(self, intcodeList):
        if not isinstance(intcodeList, list):
            raise RuntimeError('Need a list input.')
        for i in intcodeList:
            if not isinstance(i, int):
                raise RuntimeError('List needs to be integers only.')

    def _validateRun(self, stop):
        if not isinstance(stop, int):
            raise RuntimeError('Stop needs to be an integer.')

    def OverrideNounVerb(self, intcode, a, b):
        self.intList = intcode
        self.intList[1] = a
        self.intList[2] = b
        self.Validate(self.intList)

    def _operation(self, outputList, intcode, a, b, c):
        valueA = outputList[a]
        valueB = outputList[b]
        result = self.intcodeOp.Operation(intcode, valueA, valueB)
        if result:
            outputList[c] = result
            return result
        return None

    def Run(self):
        outputList = []
        outputList.extend(self.intList)
        i = 0
        listLen = len(self.intList)

        while i < listLen:
            intcodeOp = outputList[i]
            if intcodeOp == self.intcodeOp.END:
                break
            posA = self.intList[i+1]
            posB = self.intList[i+2]
            posC = self.intList[i+3]
            self._operation(outputList, intcodeOp, posA, posB, posC)
            i += 4

        return outputList


def SolveA(intcodes):
    intcodeObj = IntcodeListObject(intcodes)
    return intcodeObj.Run()


def SolveB(intcodes):
    intcodeObj = IntcodeListObject(intcodes)
    for noun, verb in product(range(100), range(100)):
        intcodeObj.OverrideNounVerb(intcodes, noun, verb)
        if intcodeObj.Run()[0] == 19690720:
            return 100 * noun + verb


def main():
    intcodes = []

    with open('day2-intcodes-data.txt', 'r') as f:
        lines = f.readline()
        intcodes = [int(i) for i in lines.split(',')]
        f.close()
    print SolveA(intcodes)
    print SolveB(intcodes)
    print 'Solved.'


if __name__ == '__main__':
    main()
