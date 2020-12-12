import copy


class MapSystem():
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'
    MOVES = [NORTH, SOUTH, EAST, WEST]

    LEFT = 'L'
    RIGHT = 'R'
    FORWARD = 'F'
    DIRECTIONS = [LEFT, RIGHT, FORWARD]

    def __init__(self, direction_list, part_b=False):
        self._direction_list = direction_list
        self._length = len(direction_list)
        self._direction = 'E'
        self._direction_degree = 0
        self._position = (0, 0)
        self._current = 0

        self._part_b = part_b
        self._waypoint_position = (10, 1)

    @property
    def part_b(self):
        return self._part_b

    @property
    def direction_list(self):
        return self._direction_list

    @property
    def length(self):
        return self._length

    @property
    def current(self):
        return self._current

    @property
    def direction(self):
        return self._direction

    @property
    def direction_degree(self):
        return self._direction_degree

    @property
    def position(self):
        return self._position

    @property
    def waypoint_position(self):
        return self._waypoint_position

    def get_line(self, line=None):
        if line is None:
            line = self.current
        cmd = self.direction_list[line][:1]
        value = int(self.direction_list[line][1:])
        return cmd, value

    def continue_ferry(self):
        if self.current == self.length:
            self.current = self.length - 1
            return False
        return True

    def step(self):
        if self.continue_ferry():
            cmd, value = self.get_line()
            if cmd in self.DIRECTIONS:
                self.apply_direction(cmd, value)
            elif cmd in self.MOVES:
                self.apply_move(cmd, value)
            self.current += 1
        return False

    def apply_move(self, cmd, value):
        if not self.part_b:
            x, y = self.position
            if cmd == self.FORWARD:
                cmd = self.direction
            if cmd == self.NORTH:
                y += value
            elif cmd == self.SOUTH:
                y -= value
            elif cmd == self.EAST:
                x += value
            elif cmd == self.WEST:
                x -= value

            self.position = (x, y)
        else:
            ship_x, ship_y = self.position
            x, y = self.waypoint_position
            if cmd == self.NORTH:
                y += value
            elif cmd == self.SOUTH:
                y -= value
            elif cmd == self.EAST:
                x += value
            elif cmd == self.WEST:
                x -= value
            elif cmd == self.FORWARD:
                x *= value
                y *= value

            if cmd in self.MOVES:
                self.waypoint_position = (x, y)
            else:
                self.position = (ship_x + x, ship_y + y)
                self.waypoint_position = (x, y)

    def apply_direction(self, cmd, value):
        if not self.part_b:
            changed_direction = False
            if cmd == self.LEFT:
                self.direction_degree += value
                changed_direction = True
            elif cmd == self.RIGHT:
                self.direction_degree -= value
                changed_direction = True
            elif cmd == self.FORWARD:
                self.apply_move(self.direction, value)

            if changed_direction:
                cycles = self.direction_degree // 90
                mod = cycles % 4
                if mod == 0:
                    self.direction = self.EAST
                elif mod == 1:
                    self.direction = self.NORTH
                elif mod == 2:
                    self.direction = self.WEST
                elif mod == 3:
                    self.direction = self.SOUTH
        else:
            x, y = self.waypoint_position
            if cmd == self.LEFT:
                for _ in range(value // 90):
                    x, y = -y, x
            elif cmd == self.RIGHT:
                for _ in range(value // 90):
                    x, y = y, -x
            elif cmd == self.FORWARD:
                self.apply_move(self.FORWARD, value)
            self.waypoint_position = (x, y)

    def get_distance(self):
        return abs(self.position[0]) + abs(self.position[-1])


def solver_a(direction_list):
    ferry = MapSystem(direction_list)
    while True:
        if ferry.continue_ferry():
            ferry.step()
        else:
            break

    return ferry.get_distance()


def solver_b(direction_list):
    ferry = MapSystem(direction_list, part_b=True)
    while True:
        if ferry.continue_ferry():
            ferry.step()
        else:
            break

    return ferry.get_distance()


def parse(textData):
    direction_list = []
    for line in textData.splitlines():
        direction_list.append(line)
    return direction_list


def main():
    direction_list = []
    lines = ''
    with open('day12-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        direction_list = parse(lines)

    direction_list2 = copy.copy(direction_list)
    print(solver_a(direction_list))
    print(solver_b(direction_list2))


if __name__ == '__main__':
    main()
