from __future__ import absolute_import


def solver_a(octopus_list, days):
    def perform_step(row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == -99:
            return
        elif grid[row][col] >= 9:
            grid[row][col] = -99
            reset_list_coords.add((row, col))
            perform_step(row, col - 1, grid)
            perform_step(row - 1, col - 1, grid)
            perform_step(row - 1, col, grid)
            perform_step(row - 1, col + 1, grid)
            perform_step(row, col + 1, grid)
            perform_step(row + 1, col + 1, grid)
            perform_step(row + 1, col, grid)
            perform_step(row + 1, col - 1, grid)
        else:
            grid[row][col] += 1

    # print(octopus_list)
    flash_sum = 0
    while days != 0:
        reset_list_coords = set()
        for row in range(len(octopus_list)):
            for col in range(len(octopus_list[row])):
                perform_step(row, col, octopus_list)

        flash_sum += len(reset_list_coords)
        for coord in reset_list_coords:
            row, col = coord
            octopus_list[row][col] = 0

        days -= 1

        # print(octopus_list, days)
    return flash_sum


def solver_b(octopus_list):
    def perform_step(row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == -99:
            return
        elif grid[row][col] >= 9:
            grid[row][col] = -99
            reset_list_coords.add((row, col))
            perform_step(row, col - 1, grid)
            perform_step(row - 1, col - 1, grid)
            perform_step(row - 1, col, grid)
            perform_step(row - 1, col + 1, grid)
            perform_step(row, col + 1, grid)
            perform_step(row + 1, col + 1, grid)
            perform_step(row + 1, col, grid)
            perform_step(row + 1, col - 1, grid)
        else:
            grid[row][col] += 1

    all_coords = len(octopus_list) * len(octopus_list[0])
    days = 1
    while True:
        reset_list_coords = set()
        for row in range(len(octopus_list)):
            for col in range(len(octopus_list[row])):
                perform_step(row, col, octopus_list)

        if len(reset_list_coords) == all_coords:
            break
        for coord in reset_list_coords:
            row, col = coord
            octopus_list[row][col] = 0

        days += 1

    return days


def generate_list(string=None):
    row_list = []
    if string is None:
        with open('day11-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                col_list = []
                for x in line:
                    col_list.append(int(x))
                row_list.append(col_list)
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            col_list = []
            for x in line:
                col_list.append(int(x))
            row_list.append(col_list)

    return row_list


def main():
    octopus_list = generate_list()

    print(solver_a(octopus_list, 100))
    print(solver_b(octopus_list))


if __name__ == '__main__':
    main()
