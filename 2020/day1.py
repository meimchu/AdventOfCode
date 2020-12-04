from aoc_timer import time_it

class ExpenseObject():
    def __init__(self, expenseList, target):
        self._expenseList = expenseList
        self._target = target

        self._inputLocA = 0
        self._inputLocB = 0

    @property
    def target(self):
        return self._target

    @property
    def expenseList(self):
        return self._expenseList

    @property
    def expenseListLength(self):
        return len(self._expenseList)

    @property
    def inputLocA(self):
        return self._inputLocA

    @inputLocA.setter
    def inputLocA(self, a):
        self._inputLocA = a

    @property
    def inputLocB(self):
        return self._inputLocB

    @inputLocB.setter
    def inputLocB(self, b):
        self._inputLocB = b


@time_it
def SolverA(expenseList):
    exp = ExpenseObject(expenseList, 2020)
    expLength = exp.expenseListLength
    expList = exp.expenseList
    expTarget = exp.target

    inputLocA = 0
    inputLocB = 0
    while inputLocA < expLength:
        inputA = expList[inputLocA]

        while inputLocB < expLength:
            inputB = expList[inputLocB]
            if (inputA + inputB) == expTarget:
                return (inputA * inputB)
            inputLocB += 1

        inputLocA += 1
        inputLocB = 0
    return None

@time_it
def SolverB(expenseList):
    exp = ExpenseObject(expenseList, 2020)
    expLength = exp.expenseListLength
    expList = exp.expenseList
    expTarget = exp.target

    inputLocA = 0
    inputLocB = 0
    inputLocC = 0
    while inputLocA < expLength:
        inputA = expList[inputLocA]

        while inputLocB < expLength:
            inputB = expList[inputLocB]

            while inputLocC < expLength:
                inputC = expList[inputLocC]
                if (inputA + inputB + inputC) == expTarget:
                    return (inputA * inputB * inputC)

                inputLocC += 1

            inputLocB += 1
            inputLocC = 0

        inputLocA += 1
        inputLocB = 0
    return None


def main():
    expenseList = []
    with open('day1-inputs.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            expenseList.append(int(line))

    print(SolverA(expenseList))
    print(SolverB(expenseList))
    print('Solved.')


if __name__ == '__main__':
    main()
