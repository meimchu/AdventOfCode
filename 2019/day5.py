class IntcodeObject():
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    END = 99

    def __init__(self):
        self.intcodes = [self.ADD, self.MULT,
                         self.INPUT, self.OUTPUT, self.END]

    def AllIntCodes(self):
        return self.intcodes

    def _validateIntcode(self, intcode=None):
        invalid = False
        if intcode:
            if intcode not in self.intcodes:
                invalid = True
        else:
            if self.intcode not in self.intcodes:
                invalid = True

        if invalid:
            raise RuntimeError(
                'Intcode needs to be one of the following option %s.' % self.intcodes)
        else:
            return True

    def _validateInputs(self):
        if not isinstance(self.a, int) and not isinstance(self.b, int):
            raise RuntimeError('a and b inputs both need to be integers.')

    def ValidateIntcode(self, intcode):
        return self._validateIntcode(intcode)

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
        if intcode is self.INPUT:
            return a
        if intcode is self.OUTPUT:
            print 'Diagnostic:', a
            return a
        if intcode is self.END:
            return None


class IntcodeListObject():
    POSITION = 0
    IMMEDIATE = 1

    def __init__(self, intList, initial_input):
        self.intList = intList

        self.Validate(self.intList)
        self.intcodeOp = IntcodeObject()

        self.initial_input = initial_input

    def Validate(self, intcodeList):
        if not isinstance(intcodeList, list):
            raise RuntimeError('Need a list input.')
        for i in intcodeList:
            if not isinstance(i, int):
                raise RuntimeError('List needs to be integers only.')

    def _validateRun(self, stop):
        if not isinstance(stop, int):
            raise RuntimeError('Stop needs to be an integer.')

    def _operation(self, outputList, intcode, a, b, c):
        if intcode == self.intcodeOp.INPUT:
            valueA = self.initial_input
        else:
            valueA = outputList[a]
        if b:
            valueB = outputList[b]
        else:
            valueB = 0
        result = self.intcodeOp.Operation(intcode, valueA, valueB)
        if result >= 0:
            if intcode != self.intcodeOp.OUTPUT:
                outputList[c] = result
            return result
        return None

    def _checkIntcode(self, intcode):
        if intcode in self.intcodeOp.AllIntCodes():
            return (0, 0, intcode)
        intcodeStr = str(intcode)
        if len(intcodeStr) == 4:
            return (int(intcodeStr[0]), int(intcodeStr[1]), int(intcodeStr[2:]))
        elif len(intcodeStr) == 3:
            return (0, int(intcodeStr[0]), int(intcodeStr[2:]))
        else:
            return (0, 0, intcode)

    def Run(self, startAt=None):
        outputList = []
        outputList.extend(self.intList)
        i = 0
        if startAt:
            i = startAt
        listLen = len(outputList)
        while i < listLen:
            intcodeOp = outputList[i]
            execB, execA, opcode = self._checkIntcode(intcodeOp)

            if opcode == self.intcodeOp.END:
                break
            elif opcode in [self.intcodeOp.ADD, self.intcodeOp.MULT]:
                if execA == self.POSITION:
                    posA = self.intList[i+1]
                elif execA == self.IMMEDIATE:
                    posA = i+1
                if execB == self.POSITION:
                    posB = self.intList[i+2]
                elif execB == self.IMMEDIATE:
                    posB = i+2
                posC = self.intList[i+3]
                self._operation(outputList, opcode, posA, posB, posC)
                i += 4
            elif opcode in [self.intcodeOp.INPUT, self.intcodeOp.OUTPUT]:
                if execA == self.POSITION:
                    posA = self.intList[i+1]
                elif execA == self.IMMEDIATE:
                    posA = i+1
                posB = None
                posC = self.intList[i+1]
                result = self._operation(outputList, opcode, posA, posB, posC)
                if opcode == self.intcodeOp.OUTPUT and result != 0:
                    print 'ABORT! None zero diagnostic result...'
                    return result
                i += 2
            else:
                self.intcodeOp._validateIntcode(opcode)
                break

        return outputList


def SolveA(intcodes):
    num = input('Initial input:')
    intcodeObj = IntcodeListObject(intcodes, num)
    result = intcodeObj.Run()
    return result


def main():
    intcodes = []

    with open('day5-inputs.txt', 'r') as f:
        lines = f.readline()
        intcodes = [int(i) for i in lines.split(',')]
        f.close()
    # intcodes = [1002, 4, 3, 4, 33]
    # intcodes = [1101, 100, -1, 4, 0]
    # intcodes = [3, 2, 50, 99]
    print SolveA(intcodes)
    print 'Solved.'


if __name__ == '__main__':
    main()
