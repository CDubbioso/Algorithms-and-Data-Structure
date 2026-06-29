def bfs_connected(graph):
    queue = []
    visited = set()

    for v in range(len(graph)):
        for e in range(len(graph[0])):
            if v == e:
                continue
            
            if graph[v][e]:
                continue
            else:
                return False
            
    return True


graph = [
  [False, True, True],
  [True, False, True],
  [True, True, False]
] # connected graph
 
print(bfs_connected(graph))

def dfe_contains_cycles(graph):
    pass