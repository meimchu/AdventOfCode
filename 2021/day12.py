from __future__ import absolute_import


def solver_a(path_list):
    path_dict = get_adjacency_list(path_list)
    all_paths = []

    def recursive_dfs(current, paths, visited):
        paths.append(current)
        if current.islower() or current == 'start':
            visited.append(current)
        for path in path_dict[current]:
            if path == 'end':
                paths.append(path)
                all_paths.append(paths)
            elif path in visited:
                continue
            else:
                recursive_dfs(path, paths[:], visited[:])

    recursive_dfs('start', [], [])

    return len(all_paths)


def solver_b(path_list):
    path_dict = get_adjacency_list(path_list)
    all_paths = []

    def recursive_dfs(current, paths, visited_dict):
        paths.append(current)

        if current.islower() or current == 'start':
            if current not in visited_dict:
                visited_dict[current] = 0
            visited_dict[current] += 1
        for path in path_dict[current]:
            if path == 'end':
                paths.append(path)
                if paths not in all_paths:
                    all_paths.append(paths)
            elif path == 'start':
                continue
            elif 2 in visited_dict.values():
                if path not in visited_dict:
                    recursive_dfs(path, paths[:], visited_dict.copy())
            else:
                recursive_dfs(path, paths[:], visited_dict.copy())

    recursive_dfs('start', [], {})

    return len(all_paths)


def get_adjacency_list(path_list):
    path_dict = {}
    for start, end in path_list:
        if start not in path_dict:
            path_dict[start] = []
        path_dict[start].append(end)
        if end not in path_dict:
            path_dict[end] = []
        path_dict[end].append(start)
    del path_dict['end']
    # print(path_dict)

    return path_dict


def generate_list(string=None):
    row_list = []
    if string is None:
        with open('day12-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                line = line.split('-')
                row_list.append((line[0], line[1]))
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            line = line.split('-')
            row_list.append((line[0], line[1]))

    return row_list


def main():
    path_list = generate_list()

    print(solver_a(path_list))
    print(solver_b(path_list))


if __name__ == '__main__':
    main()
