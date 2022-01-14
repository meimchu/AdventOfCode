from __future__ import absolute_import


def solver_a(action_list):
    forward = 0
    depth = 0
    vertical_actions = ['up', 'down']
    horizontal_actions = ['forward']

    for action, amount in action_list:
        if action in vertical_actions:
            if action == 'up':
                depth -= amount
            else:
                depth += amount
        else:
            forward += amount
    return forward * depth


def solver_b(action_list):
    forward = 0
    depth = 0
    aim = 0
    vertical_actions = ['up', 'down']
    horizontal_actions = ['forward']

    for action, amount in action_list:
        if action in vertical_actions:
            if action == 'up':
                aim -= amount
            else:
                aim += amount
        else:
            forward += amount
            depth += aim * amount
    return forward * depth


def generate_list(string=None):
    action_list = []

    if string is None:
        with open('day2-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                action, amount = line.split(' ')
                action_list.append((action, int(amount)))
    else:
        for line in string.split('\n'):
            action, amount = line.split(' ')
            action_list.append((action, int(amount)))

    return action_list


def main():
    action_list = generate_list()

    print(solver_a(action_list))
    print(solver_b(action_list))


if __name__ == '__main__':
    main()
