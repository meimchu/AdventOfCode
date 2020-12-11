from aoc_timer import time_it
from itertools import groupby
from operator import itemgetter


@time_it
def solver_a(device_list):
    device_list.append(0)
    device_list.sort()
    device_list.append(device_list[-1]+3)

    device_dict = {}

    for x, y in zip(device_list, device_list[1:]):
        if y - x <= 3:
            try:
                count = device_dict[y - x]
                device_dict[y - x] = count + 1
            except KeyError:
                device_dict[y - x] = 1

    skip_one = device_dict[1]
    skip_three = device_dict[3]
    return (skip_one * skip_three)


@time_it
def solver_b(device_list):
    """Using this visualization, it helps to realize that for example, having
    2 consecutive numbers generate  only 1 path. 3 consecutive numbers could
    generate 2 paths. 4 consecutive numbers generate 4 possible paths... etc.

    Visualized here:
    https://www.reddit.com/r/adventofcode/comments/kanaht/2020_day_10_part_2_graphical_visulisation_of/
    """
    device_list.append(0)
    device_list.sort()
    device_list.append(device_list[-1]+3)
    gap_list = []
    gap_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    possibilities_dict = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13}

    # Find consecutive numbers in the device_list and add them.
    for k, g in groupby(enumerate(device_list), lambda(i, x): i - x):
        gap_list.append(map(itemgetter(1), g))

    # Create a dictionary that tally how many consecutive numbers happened.
    for gap in gap_list:
        difference = gap[-1] - gap[0]
        gap_dict[difference] += 1

    path_sums = 1
    for k, v in gap_dict.iteritems():
        if k >= 1 and v > 0:
            path_sums *= possibilities_dict[k] ** v

    return path_sums


def parse(textData):
    device_list = []
    for line in textData.splitlines():
        device_list.append(int(line))
    return device_list


def main():
    device_list = []
    lines = ''
    with open('day10-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        device_list = parse(lines)

    print(solver_a(device_list))
    print(solver_b(device_list))


if __name__ == '__main__':
    main()
