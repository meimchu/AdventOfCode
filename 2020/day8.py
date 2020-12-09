from aoc_timer import time_it
import copy

acc = 0
loop = {}
part_b = False


def execute_command(command_list, command, current):
    global acc
    global loop

    cmd = command[0]
    value = int(command[-1])
    if current not in loop:
        loop[current] = 1
    else:
        loop[current] += 1
    if loop[current] == 2:
        if part_b:
            # print('Recursive and it is Part B')
            acc = 0
            return None
        # print('Not Part B')
        return acc

    if cmd == 'jmp':
        current += value
    elif cmd == 'acc':
        current += 1
        acc += value
    elif cmd == 'nop':
        current += 1
    if current == len(command_list):
        # print('Hit end of list')
        return acc
    cmd, value = command_list[current].split(' ')
    execute_command(command_list, (cmd, int(value)), current)


@time_it
def SolverA(command_list):
    global acc
    global part_b
    acc = 0
    part_b = False
    cmd, value = command_list[0].split(' ')
    execute_command(command_list, (cmd, int(value)), 0)
    return acc


@time_it
def SolverB(command_list):
    global acc
    global part_b
    global loop
    acc = 0
    part_b = True
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
            # print(k, line, command_list)
            cmd, value = command_list[0].split(' ')
            execute_command(command_list, (cmd, int(value)), 0)
            if acc != 0:
                return acc

            # Restore command list back to original.
            command_list = copy.copy(original_command_list)
            acc = 0
            loop = {}


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

    print(SolverA(command_list))
    print(SolverB(command_list))


if __name__ == '__main__':
    main()
