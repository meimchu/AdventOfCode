from aoc_timer import time_it


class SeatFinder():
    TOTAL_ROWS = range(128)
    TOTAL_COLS = range(8)
    ROW, COL = range(2)

    def __init__(self, pattern):
        self._pattern = pattern
        self._rowPattern = pattern[:7]
        self._colPattern = pattern[7:]

    @property
    def rowPattern(self):
        return self._rowPattern

    @property
    def colPattern(self):
        return self._colPattern

    def search(self, x, rowOrCol):
        lowHigh = [0, len(x)]
        if rowOrCol == self.ROW:
            pattern = self.rowPattern
            lowKeyWord = 'F'
            highKeyWord = 'B'
        else:
            pattern = self.colPattern
            lowKeyWord = 'L'
            highKeyWord = 'R'

        for row in pattern:
            mid = (lowHigh[0] + lowHigh[-1]) // 2
            if row == lowKeyWord:
                lowHigh[-1] = mid
            elif row == highKeyWord:
                lowHigh[0] = mid
        return lowHigh[0]

    def search_row(self):
        return self.search(self.TOTAL_ROWS, self.ROW)

    def search_col(self):
        return self.search(self.TOTAL_COLS, self.COL)

    def seat_id(self):
        return (self.search_row() * 8 + self.search_col())


@time_it
def SolverA(seatList):
    largestSeatId = 0
    for seat in seatList:
        seatObj = SeatFinder(seat)
        if seatObj.seat_id() > largestSeatId:
            largestSeatId = seatObj.seat_id()

    return largestSeatId


@time_it
def SolverB(seatList):
    seats = set()
    for seat in seatList:
        seatObj = SeatFinder(seat)
        seats.add(seatObj.seat_id())

    it = iter(seats)
    x = next(it)
    while True:
        try:
            y = next(it)
            if y != x + 1:
                return x + 1
            x = y
        except StopIteration:
            break
    return None


def main():
    seatList = []
    with open('day5-inputs.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            seatList.append(line)

    print(SolverA(seatList))
    print(SolverB(seatList))


if __name__ == '__main__':
    main()
