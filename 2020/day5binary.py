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

    def search(self, rowOrCol):
        if rowOrCol == self.ROW:
            pattern = self.rowPattern.replace('F', '0')
            pattern = pattern.replace('B', '1')
        else:
            pattern = self.colPattern.replace('L', '0')
            pattern = pattern.replace('R', '1')

        return int(pattern, 2)

    def search_row(self):
        return self.search(self.ROW)

    def search_col(self):
        return self.search(self.COL)

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
