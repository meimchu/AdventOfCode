from aoc_timer import time_it

solution_a = 0


class PreambleCode():
    def __init__(self, codes, preamble=None):
        self._codes = codes
        self._length = len(codes)
        self._preamble = preamble or 25
        self._current = self.preamble
        self._preamble_counter = (0, self.preamble)
        self._preamble_set = codes[0:self.preamble]
        self._no_match = 0
        self._stop = False
        self._target = 0
        self._total_list = []

    @property
    def total_list(self):
        return self._total_list

    @property
    def target(self):
        return self._target

    @property
    def stop(self):
        return self._stop

    @property
    def no_match(self):
        return self._no_match

    @property
    def length(self):
        return self._length

    @property
    def current(self):
        return self._current

    @property
    def codes(self):
        return self._codes

    @property
    def preamble(self):
        return self._preamble

    @property
    def preamble_set(self):
        front, back = self.preamble_counter
        self._preamble_set = self.codes[front:back]
        return self._preamble_set

    @property
    def preamble_counter(self):
        return self._preamble_counter

    def continue_transmit(self):
        if self.stop:
            return False
        if self.current == self.length:
            return False
        return True

    def no_preamble_match(self):
        success = 0
        total = 0
        self._total_list = []
        for i, x in enumerate(self.preamble_set):
            total += x
            self.total_list.append(x)
            for j, y in enumerate(self.preamble_set):
                if i != j:
                    total += y
                    self.total_list.append(y)
                    if total == self.target:
                        self.stop = True
                        return True
                    if self.codes[self.current] == (x + y):
                        success += 1
                        break

        if success == 0:
            self.no_match = self.codes[self.current]
            self.stop = True
            return True
        return False

    def step(self):
        if self.continue_transmit():
            if self.no_preamble_match():
                return False
            front, back = self.preamble_counter
            front += 1
            back += 1
            self.current += 1
            self.preamble_counter = (front, back)
        else:
            return False


@time_it
def SolverA(preamble_list):
    global solution_a

    preambleObj = PreambleCode(preamble_list)
    while True:
        if preambleObj.continue_transmit():
            preambleObj.step()
        else:
            break
    solution_a = preambleObj.no_match
    return solution_a


@time_it
def SolverB(preamble_list):
    global solution_a

    preambleObj = PreambleCode(preamble_list)
    preambleObj.target = solution_a
    while True:
        if preambleObj.continue_transmit():
            preambleObj.step()
        else:
            break
    weakness_list = sorted(preambleObj.total_list)

    return (weakness_list[0] + weakness_list[-1])


def parse(textData):
    preamble_list = []
    for line in textData.splitlines():
        preamble_list.append(int(line))
    return preamble_list


def main():
    preamble_list = []
    lines = ''
    with open('day9-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        preamble_list = parse(lines)

    print(SolverA(preamble_list))
    print(SolverB(preamble_list))


if __name__ == '__main__':
    main()
