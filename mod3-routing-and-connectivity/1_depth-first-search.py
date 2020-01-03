graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


def dfs(grph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(grph[vertex] - visited)
    return visited


def dfs_paths(grph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for nxt in grph[start] - set(path):
        yield from dfs_paths(grph, nxt, goal, path + [nxt])


# {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs(graph, 'A'))

# [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
print(list(dfs_paths(graph, 'C', 'F')))
