from aoc_timer import time_it


class GroupAnswers():
    def __init__(self, groupDict):
        self._groupDict = groupDict
        self._groupAnswers = set()
        self._fullGroupAnswers = set()

        self.groupAnswers()

    @property
    def groupDict(self):
        return self._groupDict

    def groupAnswers(self):
        for key, value in self.groupDict.iteritems():
            prevFullGroupAnswers = self._fullGroupAnswers.copy()
            self._groupAnswers.update(set(value))
            fullGroupAnswers = set(value)
            if key == 0:
                prevFullGroupAnswers = fullGroupAnswers.copy()
            self._fullGroupAnswers = set(
                prevFullGroupAnswers).intersection(fullGroupAnswers)
        return self._groupAnswers

    def groupAnswersCount(self):
        return len(self._groupAnswers)

    def fullGroupAnswers(self):
        return self._fullGroupAnswers

    def fullGroupAnswersCount(self):
        return len(self._fullGroupAnswers)


@time_it
def SolverA(groupDictList):
    totalAnswers = 0
    for groupDict in groupDictList:
        groupObj = GroupAnswers(groupDict)
        totalAnswers += groupObj.groupAnswersCount()

    return totalAnswers


@time_it
def SolverB(groupDictList):
    totalAnswers = 0
    for groupDict in groupDictList:
        groupObj = GroupAnswers(groupDict)
        totalAnswers += groupObj.fullGroupAnswersCount()

    return totalAnswers


def parse(textData):
    groupDictList = []
    groupDict = {}
    count = 0
    lineRows = textData.count('\n')
    for lineCount, line in enumerate(textData.splitlines()):
        if line != '':
            groupDict[count] = line
            count += 1
            if lineCount == lineRows:
                groupDictList.append(groupDict)
        else:
            groupDictList.append(groupDict)
            groupDict = {}
            count = 0

    return(groupDictList)


def main():
    groupDictList = []
    lines = ''
    with open('day6-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        groupDictList = parse(lines)

    print(SolverA(groupDictList))
    print(SolverB(groupDictList))


if __name__ == '__main__':
    main()
