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
        print(stack)
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(grph[vertex] - visited)
    return visited


# {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs(graph, 'A'))
