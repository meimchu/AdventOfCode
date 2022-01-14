from __future__ import absolute_import


def solver_a(fish_list, days):
    fish_list = fish_list.copy()
    for day in range(days):
        add_fishes = 0
        for i, fish in enumerate(fish_list):
            if fish == 0:
                add_fishes += 1
                fish_list[i] = 7
            fish_list[i] -= 1

        for _ in range(add_fishes):
            fish_list.append(8)

    return len(fish_list)


def solver_b(fish_list, days):
    fish_dict = [fish_list.count(x) for x in range(9)]

    for _ in range(days):
        fish_dict = fish_dict[1:] + [fish_dict[0]]
        fish_dict[6] += fish_dict[8]

    return sum(fish_dict)


def generate_list(string=None):
    fish_list = []
    if string is None:
        with open('day6-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                for x in line.split(','):
                    fish_list.append(int(x))
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            for x in line.split(','):
                fish_list.append(int(x))

    return fish_list


def main():
    fish_list = generate_list()

    print(solver_a(fish_list, 80))
    print(solver_b(fish_list, 256))


if __name__ == '__main__':
    main()
