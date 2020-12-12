from aoc_timer import time_it
import copy


class GameConsole():
    def __init__(self, code):
        self._code = code
        self._current = 0
        self._accumulator = 0
        self._length = len(code)
        self._loop = {}
        self._max_loop = 2
        self.ended_by_loop = False
        self.ended_by_end = False

    @property
    def code(self):
        return self._code

    @property
    def current(self):
        return self._current

    @property
    def accumulator(self):
        return self._accumulator

    @property
    def length(self):
        return self._length

    @property
    def loop(self):
        return self._loop

    @property
    def max_loop(self):
        return self._max_loop

    def loop_count(self, cmd=None):
        if cmd is not None:
            try:
                return self.loop[cmd]
            except KeyError:
                self.loop[cmd] = 0
                return 0
        return self._loop

    def loop_count_add(self, cmd=None):
        loop_value = self.loop_count(cmd)
        loop_value += 1
        self.loop[cmd] = loop_value

    def continue_game(self):
        for k, v in self.loop.iteritems():
            if v == self.max_loop:
                k2, v2 = self.get_line(k)
                if k2 == 'acc':
                    self.accumulator -= v2
                self.ended_by_loop = True
                return False
        if self.current == self.length:
            self.ended_by_end = True
            return False
        return True

    def nop(self):
        self.loop_count_add(self.current)
        self.current += 1

    def jmp(self, value):
        self.loop_count_add(self.current)
        self.current += value

    def acc(self, value):
        self.loop_count_add(self.current)
        self.current += 1
        self.accumulator += value

    def get_line(self, line=None):
        if line is None:
            line = self.current
        cmd, value = self.code[line].split(' ')
        return cmd, int(value)

    def step(self):
        cmd, value = self.get_line()
        if self.continue_game():
            if cmd == 'jmp':
                self.jmp(value)
            elif cmd == 'nop':
                self.nop()
            elif cmd == 'acc':
                self.acc(value)
        else:
            return False


@time_it
def solver_a(command_list):
    game = GameConsole(command_list)
    while True:
        if game.continue_game():
            game.step()
        else:
            break

    return game.accumulator


@time_it
def solver_b(command_list):
    original_command_list = copy.copy(command_list)
    change_cmd_dict = {}
    inverse_dict = {'jmp': 'nop', 'nop': 'jmp'}

    for change_cmd in inverse_dict:
        cmd_appearance_line_list = []
        for count, line in enumerate(command_list):
            if change_cmd in line:
                cmd_appearance_line_list.append(count)
            change_cmd_dict[change_cmd] = cmd_appearance_line_list

    for k, v in change_cmd_dict.items():
        for line in v:
            command_list[line] = command_list[line].replace(k, inverse_dict[k])

            game = GameConsole(command_list)
            while True:
                if game.continue_game():
                    game.step()
                else:
                    break
            if game.ended_by_end:
                return game.accumulator

            # Restore command list back to original.
            command_list = copy.copy(original_command_list)


def parse(textData):
    command_list = []
    for line in textData.splitlines():
        command_list.append(line)
    return command_list


def main():
    command_list = []
    lines = ''
    with open('day8-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        command_list = parse(lines)

    print(solver_a(command_list))
    print(solver_b(command_list))


if __name__ == '__main__':
    main()
