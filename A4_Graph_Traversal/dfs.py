def dfs_contains_cycles(graph):
    visited = set()
    current_exploring = set()

    def dfs(node):
        current_exploring.add(node)
        for neighbour in graph[node]:
            if neighbour in current_exploring:
                return True
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
                
        current_exploring.remove(node)
        visited.add(node)
        return False
            
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


# Tests
graph1 = {'a': {'b', 'c'}, 'b': set(), 'c': set()}
print(dfs_contains_cycles(graph1))   # False

graph2 = {'a': {'b'}, 'b': {'c'}, 'c': {'a'}}
print(dfs_contains_cycles(graph2))   # True

graph3 = {'a': {'b'}, 'b': {'c'}, 'c': set()}
print(dfs_contains_cycles(graph3))   # False
