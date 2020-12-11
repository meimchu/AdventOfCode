from aoc_timer import time_it


class ExpenseObject():
    def __init__(self, expenseList, target):
        self._expenseList = sorted(expenseList)
        self._reversedExpenseList = sorted(expenseList, reverse=True)
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
    def reversedExpenseList(self):
        return self._reversedExpenseList

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
def solver_a(expenseList):
    exp = ExpenseObject(expenseList, 2020)
    expLength = exp.expenseListLength
    expList = exp.expenseList
    reversedExpList = exp.reversedExpenseList
    expTarget = exp.target

    inputLocA = 0
    inputLocB = 0
    while inputLocA < expLength:
        inputA = reversedExpList[inputLocA]
        if inputA >= expTarget:
            continue

        while inputLocB < expLength:
            inputB = expList[inputLocB]
            if (inputA + inputB) > expTarget:
                break
            elif (inputA + inputB) == expTarget:
                return (inputA * inputB)
            inputLocB += 1

        inputLocA += 1
        inputLocB = 0
    return None


@time_it
def solver_b(expenseList):
    exp = ExpenseObject(expenseList, 2020)
    expLength = exp.expenseListLength
    expList = exp.expenseList
    reversedExpList = exp.reversedExpenseList
    expTarget = exp.target

    inputLocA = 0
    inputLocB = 0
    inputLocC = 0
    while inputLocA < expLength:
        inputA = reversedExpList[inputLocA]
        msg = str(inputA)
        if inputA >= expTarget:
            continue

        while inputLocB < expLength:
            inputB = expList[inputLocB]
            msg = msg + ' ' + str(inputB)
            if (inputA + inputB) > expTarget:
                break

            while inputLocC < expLength:
                inputC = expList[inputLocC]
                msg = msg + ' ' + str(inputC)
                if (inputA + inputB + inputC) > expTarget:
                    break
                elif (inputA + inputB + inputC) == expTarget:
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
            if line not in expenseList:
                expenseList.append(int(line))

    print(solver_a(expenseList))
    print(solver_b(expenseList))
    print('Solved.')


if __name__ == '__main__':
    main()
