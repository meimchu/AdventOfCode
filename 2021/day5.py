from __future__ import absolute_import


def solver_a(move_list):
    coord_dict = {}
    for moves in move_list:
        x1, y1, x2, y2 = moves
        if x1 == x2:
            distance = y2 - y1
            move = 1
            if distance > 0:
                move = -1
            while distance != 0:
                if (x1, y1 + distance) not in coord_dict:
                    coord_dict[x1, y1 + distance] = 0
                coord_dict[x1, y1 + distance] += 1
                distance += move
            if (x1, y1) not in coord_dict:
                coord_dict[(x1, y1)] = 0
            coord_dict[(x1, y1)] += 1

        elif y1 == y2:
            distance = x2 - x1
            move = 1
            if distance > 0:
                move = -1
            while distance != 0:
                if (x1 + distance, y1) not in coord_dict:
                    coord_dict[x1 + distance, y1] = 0
                coord_dict[x1 + distance, y1] += 1
                distance += move
            if (x1, y1) not in coord_dict:
                coord_dict[(x1, y1)] = 0
            coord_dict[(x1, y1)] += 1

    # for row in range(10):
    #     row_line = ''
    #     for col in range(10):
    #         if (row, col) in coord_dict:
    #             row_line += str(coord_dict[(row, col)])
    #         else:
    #             row_line += '.'
    #     print(row_line)

    over_one_sum = 0
    for k, v in coord_dict.items():
        if v > 1:
            over_one_sum += 1

    return over_one_sum


def solver_b(move_list):
    coord_dict = {}
    for moves in move_list:
        x1, y1, x2, y2 = moves
        if x1 == x2:
            distance = y2 - y1
            move = 1
            if distance > 0:
                move = -1
            while distance != 0:
                if (x1, y1 + distance) not in coord_dict:
                    coord_dict[x1, y1 + distance] = 0
                coord_dict[x1, y1 + distance] += 1
                distance += move
            if (x1, y1) not in coord_dict:
                coord_dict[(x1, y1)] = 0
            coord_dict[(x1, y1)] += 1

        elif y1 == y2:
            distance = x2 - x1
            move = 1
            if distance > 0:
                move = -1
            while distance != 0:
                if (x1 + distance, y1) not in coord_dict:
                    coord_dict[x1 + distance, y1] = 0
                coord_dict[x1 + distance, y1] += 1
                distance += move
            if (x1, y1) not in coord_dict:
                coord_dict[(x1, y1)] = 0
            coord_dict[(x1, y1)] += 1
        elif abs(x2 - x1) == abs(y2 - y1):
            x_distance = x2 - x1
            y_distance = y2 - y1
            x_move = 1
            y_move = 1
            if x_distance > 0:
                x_move = -1
            if y_distance > 0:
                y_move = -1
            while x_distance != 0:
                if (x1 + x_distance, y1 + y_distance) not in coord_dict:
                    coord_dict[x1 + x_distance, y1 + y_distance] = 0
                coord_dict[x1 + x_distance, y1 + y_distance] += 1
                x_distance += x_move
                y_distance += y_move
            if (x1, y1) not in coord_dict:
                coord_dict[(x1, y1)] = 0
            coord_dict[(x1, y1)] += 1

    # for row in range(10):
    #     row_line = ''
    #     for col in range(10):
    #         if (row, col) in coord_dict:
    #             row_line += str(coord_dict[(row, col)])
    #         else:
    #             row_line += '.'
    #     print(row_line)

    over_one_sum = 0
    for k, v in coord_dict.items():
        if v > 1:
            over_one_sum += 1

    return over_one_sum


def generate_list(string=None):
    move_list = []
    if string is None:
        with open('day5-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                line = line.replace(' ', '')
                coords = line.split('->')
                x1, y1 = coords[0].split(',')
                x2, y2 = coords[-1].split(',')
                move_list.append([int(x1), int(y1), int(x2), int(y2)])
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            line = line.replace(' ', '')
            coords = line.split('->')
            x1, y1 = coords[0].split(',')
            x2, y2 = coords[-1].split(',')
            move_list.append([int(x1), int(y1), int(x2), int(y2)])

    return move_list


def main():
    move_list = generate_list()

    print(solver_a(move_list))
    print(solver_b(move_list))


if __name__ == '__main__':
    main()
