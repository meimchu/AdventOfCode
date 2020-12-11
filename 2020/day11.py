from aoc_timer import time_it
import itertools
import copy


class SeatMap():
    OCCUPIED_SEAT = '#'
    EMPTY_SEAT = 'L'
    FLOOR = '.'

    def __init__(self, seat_map, part_b=False):
        self._seat_map = seat_map
        self._column = len(seat_map)
        self._row = len(seat_map[0])
        self._part_b = part_b

    @property
    def part_b(self):
        return self._part_b

    @property
    def seat_map(self):
        return self._seat_map

    @property
    def column(self):
        return self._column

    @property
    def row(self):
        return self._row

    def get_seat(self, row, col):
        try:
            return self.seat_map[col][row]
        except IndexError:
            return None

    def get_adj_seat(self, row, col):
        adj_seat_list = []
        adj_map = list(itertools.product(range(-1, 2), repeat=2))
        adj_map.remove((0, 0))
        for x, y in adj_map:
            adj_row = row + x
            adj_col = col + y
            if adj_row >= 0 and adj_col >= 0:
                adj_seat = self.get_seat(adj_row, adj_col)
                if adj_seat is not None:
                    if not self.part_b:
                        # Do Part A
                        adj_seat_list.append(adj_seat)
                    else:
                        # Do Part B
                        if adj_seat == self.FLOOR:
                            visible_seat = self.extend_vision(
                                row, col, adj_row, adj_col)
                            if visible_seat is not None:
                                adj_seat_list.append(visible_seat)
                        else:
                            adj_seat_list.append(adj_seat)

        return adj_seat_list

    def extend_vision(self, row, col, adj_row, adj_col):
        # Find the (x, y) direction it is heading from original seat location.
        x = adj_row - row
        y = adj_col - col

        while True:
            adj_row += x
            adj_col += y
            if adj_row >= 0 and adj_col >= 0:
                visible_seat = self.get_seat(adj_row, adj_col)
                if visible_seat != self.FLOOR:
                    return visible_seat
                elif visible_seat is None:
                    break
            else:
                return None
        return None

    def apply_rule(self, row, col):
        seat = self.get_seat(row, col)
        adj_seats = self.get_adj_seat(row, col)
        if seat == self.EMPTY_SEAT:
            if self.OCCUPIED_SEAT not in adj_seats:
                return True
        elif seat == self.OCCUPIED_SEAT:
            comfort = 4
            if self.part_b:
                # Do Part B
                comfort = 5
            if adj_seats.count(self.OCCUPIED_SEAT) >= comfort:
                return True

        return False

    def apply_rules(self):
        change_seats = []
        for col in range(self.column):
            for row in range(self.row):
                if self.apply_rule(row, col):
                    change_seats.append((row, col))
        if change_seats:
            self.change_seat_map(change_seats)
            return True
        else:
            return False

    def change_seat_map(self, seat_list):
        for seat in seat_list:
            row, col = seat
            rows = self.seat_map[col]
            if self.get_seat(row, col) == self.OCCUPIED_SEAT:
                rows = rows[0:row] + self.EMPTY_SEAT + rows[row + 1:]
            elif self.get_seat(row, col) == self.EMPTY_SEAT:
                rows = rows[0:row] + self.OCCUPIED_SEAT + rows[row + 1:]
            self.seat_map[col] = rows


@time_it
def solver_a(seat_map):
    seat_map_obj = SeatMap(seat_map)
    while True:
        if seat_map_obj.apply_rules():
            current_map = seat_map_obj.seat_map
        else:
            break

    occupied = 0
    for col in range(seat_map_obj.column):
        for row in range(seat_map_obj.row):
            if seat_map_obj.get_seat(row, col) == seat_map_obj.OCCUPIED_SEAT:
                occupied += 1

    return occupied


@time_it
def solver_b(seat_map):
    seat_map_obj = SeatMap(seat_map, part_b=True)
    while True:
        if seat_map_obj.apply_rules():
            current_map = seat_map_obj.seat_map
        else:
            break

    occupied = 0
    for col in range(seat_map_obj.column):
        for row in range(seat_map_obj.row):
            if seat_map_obj.get_seat(row, col) == seat_map_obj.OCCUPIED_SEAT:
                occupied += 1

    return occupied


def parse(textData):
    seat_map = []
    for line in textData.splitlines():
        seat_map.append(line)
    return seat_map


def main():
    seat_map = []
    lines = ''
    with open('day11-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        seat_map = parse(lines)
    seat_map2 = copy.copy(seat_map)
    print(solver_a(seat_map))
    print(solver_b(seat_map2))


if __name__ == '__main__':
    main()
