from __future__ import absolute_import


def solver_a(grid_list):
    def bfs_search(row, col, grid, target, depth):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 1
        if target < grid[row][col]:
            return 1
        if depth > 0:
            return 0
        perimeters = bfs_search(row, col - 1, grid, target, depth + 1) + \
            bfs_search(row - 1, col, grid, target, depth + 1) + \
            bfs_search(row, col + 1, grid, target, depth + 1) + \
            bfs_search(row + 1, col, grid, target, depth + 1)
        return perimeters

    lowest_list = []
    for row in range(len(grid_list)):
        for col in range(len(grid_list[row])):
            if bfs_search(row, col, grid_list, grid_list[row][col], 0) == 4:
                lowest_list.append(grid_list[row][col] + 1)

    return sum(lowest_list)


def solver_b(grid_list):
    visited = []

    def bfs_search(row, col, grid, basins):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if (row, col) in visited:
            return
        if grid[row][col] == 9:
            return
        visited.append((row, col))
        basins.append(grid[row][col])
        bfs_search(row, col - 1, grid, basins)
        bfs_search(row - 1, col, grid, basins)
        bfs_search(row, col + 1, grid, basins)
        bfs_search(row + 1, col, grid, basins)
        return len(basins)

    basins_list = []
    for row in range(len(grid_list)):
        for col in range(len(grid_list[row])):
            result = bfs_search(row, col, grid_list, [])
            if result:
                basins_list.append(result)
    basins_list = sorted(basins_list)
    return basins_list[-1] * basins_list[-2] * basins_list[-3]


def generate_list(string=None):
    row_list = []
    if string is None:
        with open('day9-inputs.txt', 'r') as f:
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
    grid_list = generate_list()

    print(solver_a(grid_list))
    print(solver_b(grid_list))


if __name__ == '__main__':
    main()
