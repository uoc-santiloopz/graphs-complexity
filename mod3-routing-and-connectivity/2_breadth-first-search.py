from shared.graphs import graph


def bfs(grph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(grph[vertex] - visited)
    return visited


def bfs_paths(grph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for nxt in grph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))


def shortest_path(grph, start, goal):
    try:
        return next(bfs_paths(grph, start, goal))
    except StopIteration:
        return None


# {'D', 'F', 'B', 'C', 'E', 'A'}
print(bfs(graph, 'A'))
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(list(bfs_paths(graph, 'A', 'F')))
# ['A', 'C', 'F']
print(shortest_path(graph, 'A', 'F'))
