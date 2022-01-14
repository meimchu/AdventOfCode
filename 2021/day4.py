from __future__ import absolute_import


def solver_a(grid_list):
    input_list = grid_list[0]
    grid_list = grid_list[1:]
    checked = -99
    found_solution = None

    for i in range(len(input_list)):
        if not grid_list:
            break

        # Get current step
        current_input = input_list[i]

        # Loop through all the boards
        for board in grid_list:
            for row in range(len(board)):
                if current_input in board[row]:
                    for col in range(len(board[row])):
                        if board[row][col] == current_input:
                            board[row][col] = checked
                            break

                    # Check if row is winning
                    if board[row] == [checked] * len(board[0]):
                        found_solution = board
                        break

                    # Check if col is winning
                    col_vals = []
                    for r in range(len(board)):
                        col_vals.append(board[r][col])
                    if col_vals == [checked] * len(board[0]):
                        found_solution = board
                        break

            if found_solution:
                break
        if found_solution:
            break

    solution_sum = 0
    for row in range(len(found_solution)):
        for col in range(len(found_solution[row])):
            if found_solution[row][col] != checked:
                solution_sum += found_solution[row][col]

    return solution_sum * current_input


def solver_b(grid_list):
    input_list = grid_list[0]
    grid_list = grid_list[1:]
    checked = -99

    for i in range(len(input_list)):
        if not grid_list:
            break

        # Get current step
        current_input = input_list[i]

        # Loop through all the boards
        boards_to_remove = []
        for j, board in enumerate(grid_list):
            for row in range(len(board)):
                if current_input in board[row]:
                    for col in range(len(board[row])):
                        if board[row][col] == current_input:
                            board[row][col] = checked
                            break

                    # Check if row is winning
                    if board[row] == [checked] * len(board[0]):
                        boards_to_remove.append(j)
                        break

                    # Check if col is winning
                    col_vals = []
                    for r in range(len(board)):
                        col_vals.append(board[r][col])
                    if col_vals == [checked] * len(board[0]):
                        boards_to_remove.append(j)
                        break

        if boards_to_remove:
            boards_to_remove.reverse()
            for b in boards_to_remove:
                grid_list.pop(b)

    solution_sum = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != checked:
                solution_sum += board[row][col]

    return solution_sum * current_input


def generate_list(string=None):
    grid_list = []
    board = []

    count = 0
    if string is None:
        with open('day4-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                line = line.replace('  ', ' ')
                if count == 0:
                    input_line = [int(i) for i in line.split(',')]
                    grid_list.append(input_line)
                elif line == '':
                    if board:
                        grid_list.append(board)
                    board = []
                else:
                    grid_line = [int(i) for i in line.split(' ')]
                    board.append(grid_line)
                count += 1
            grid_list.append(board)
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            line = line.replace('  ', ' ')
            if count == 0:
                input_line = [int(i) for i in line.split(',')]
                grid_list.append(input_line)
            elif line == '':
                if board:
                    grid_list.append(board)
                board = []
            else:
                grid_line = [int(i) for i in line.split(' ')]
                board.append(grid_line)
            count += 1
        grid_list.append(board)

    return grid_list


def main():
    grid_list = generate_list()

    print(solver_a(grid_list))
    print(solver_b(grid_list))


if __name__ == '__main__':
    main()
