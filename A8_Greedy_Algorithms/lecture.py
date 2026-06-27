import numpy as np

def coin_problem(coins, amount):
    """
    Given an infinite amount of coins with value d1, d2, ..., dn cents, and 
    an amount to be paid of n (n >= 0) cents. All d_i are > 0 and different. 
    What's the minimal number of coins required to pay the amount of n in cents.

    param coins : list coins
    type coins: List[int]

    param amount : total amount to make change
    type amount: int

    return : number of coins used 
    """
    count = 0
    coins.sort(reverse=True)
    used = []
    
    while amount > 0:
        took_one = False
        for c in coins:
            if c <= amount:
                amount -= c
                count += 1
                took_one = True
                used.append(c)
                break
        if not took_one:
            return f'There is no perfect change.'
    
    return count, used


coin = [4, 6, 9]    
# print(coin_problem(coin, 8))


def TSP_greedy(graph, start):
    """
    Given n cities with a distance between each pair of city, find a shortest path that visists
    each city exactly once, and returning to the initial city, 

    param graph : dictionary where each key refers to a node and 
        as values a dictionary with key=neighbour, value=cost to reach neighbour
    type graph : Dict{ Dict{} }

    return path
    """
    visited = set()
    visited.add(start)
    path = [start]
    cost = 0

    while len(path) < len(graph):
        current = path[-1]
        shortest = float('inf')
        for neighbour in graph[current].keys():
            if neighbour not in visited and graph[current][neighbour] < shortest:
                shortest = graph[current][neighbour]
                best = neighbour
        path.append(best)
        visited.add(best)
        cost += shortest
    
    cost += graph[start][path[-1]]
    path.append(start)


    return path, cost


graph = {
    'A': {'B': 2, 'C': 5, 'D': 7},
    'B': {'A': 2, 'C': 8, 'D': 3},
    'C': {'A': 5, 'B': 8, 'D': 1},
    'D': {'A': 7, 'B': 3, 'C': 1},
}
# print(TSP_greedy(graph, 'A'))


def knapsack_greedy(weights, values, target):
    """
    
    """
    # you could select the element based on the ratio: value/weight
    v_w = [(values[i]/weights[i]) for i in range(len(weights))]

    # sort from most valuable to least
    index = []
    while len(index) < len(weights):
        current_ratio = float('-inf')
        current_index = None
        for i in range(len(values)):
            if i not in index:
                if v_w[i] > current_ratio:
                    current_ratio = v_w[i]
                    current_index = i
            
        index.append(current_index)

    store = []
    for i in index:
        if target - weight[i] == 0:
            store.append((value[i], weight[i]))
            return store
        elif target - weight[i] > 0:
            store.append((value[i], weight[i]))
            target -= weight[i]
        else:
            continue

    return store

weight = [8, 3, 4, 5]
value = [42, 14, 40, 27]
# print(knapsack_greedy(weight, value, 12))


def dijkstra(start: str, graph: dict[str, list[tuple[str, int]]]):
    visited = set()
    distance = {node : float('inf') for node in graph}  # dict[str, int]  --> distance to reach node
    distance[start] = 0

    while len(visited) < len(graph):
        current_distance = float('inf')
        current_node = None

        # select node with the smallest current distance to reach it
        for node in graph:
            if node not in visited and distance[node] < current_distance:
                current_distance = distance[node]
                current_node = node
        
        # if the graph is not connected 
        if current_node is None:
            break

        visited.add(current_node)

        # update neighbours distance
        for neighbour, cost in graph[current_node]:
            if neighbour in visited:
                continue
            current_cost = cost + distance[current_node]
            if current_cost < distance[neighbour]:
                distance[neighbour] = current_cost
        
    return distance

graph = {
    'A': [('B', 2), ('C', 9)],
    'B': [('A', 2), ('F', 2), ('D', 4)],
    'C': [('A', 9), ('D', 2), ('G', 2), ('E', 4)],
    'D': [('B', 4), ('C', 2), ('H', 6)],
    'E': [('C', 4), ('G', 4)],
    'F': [('B', 2), ('H', 7)],
    'G': [('C', 2), ('H', 5), ('E', 4)],
    'H': [('F', 7), ('D', 6), ('G', 5)],
}
# print(dijkstra('A', graph))


def map_colouring_problem(adj_list, available_colours):
    """
    :param adj_list: An adjacency list representation of a graph.
    :type adj_list: Dict[str, Set[str]]
    
    :param available_colours: Set of possible colours.
    :type available_colours: Set[str]
    
    :return: An assignment, associating vertices to colours, 
        or the boolean False, if no assignment is possible.
    :rtype: Dict[str,str] or bool 
    """
    colours = list(available_colours)
    visited = set()
    solution = {node: None for node in adj_list.keys()}
    # solution[(adj_list.keys())[0]] = colours[0]
    # visited.add((adj_list.keys())[0])

    while len(visited) < len(adj_list):
        current_node = None
        
        # select node
        for node in adj_list.keys():
            if node not in visited:
                current_node = node
                break
        
        visited.add(current_node)

        # select colour
        found = False
        for colour in colours:
            for neighbour in adj_list[current_node]:
                if colour == solution[neighbour]:
                    break
            else:
                # possible colour
                solution[current_node] = colour
                found = True
        if not found: return False
            
    return solution if found else False

def check_assignment(graph, assignment):
    """
    :param graph: An adjacency list represention of a graph. 
    :type graph: Dict[str, Set[str]]
    
    :param assignment: A dictionary representation of a graph colouring, 
        with vertices as keys and colours as values.
    :type assignment: Dict[str,str]
    
    :return: Whether or not the assignment is valid. 
    :rtype: bool 
    """
    if not assignment:
        return False
    for node in graph.keys():               # for every node in the graph
        for neighbour in graph[node]:       # check each neighbour
            if assignment[neighbour] == assignment[node]:       # check if neighbours have the same colour as the node
                return False
    
    # else if every neighbour have a different colour, return True
    return True

adj_list = {
    'Ze': {'So', 'NB'},
    'NB': {'Ze', 'Li', 'So', 'Ge'},
    'So': {'Ze', 'NB', 'Ut', 'Ge', 'NH'},
    'Li': {'NB', 'Ge'}, 
    'Ut': {'So', 'NH', 'Ge', 'Fl'}, 
    'Ge': {'Li', 'NB', 'So', 'Ut', 'Fl', 'Ov'}, 
    'NH': {'So', 'Ut', 'Fl', 'Fr'}, 
    'Fl': {'NH', 'Ut', 'Ge', 'Ov', 'Fr'}, 
    'Ov': {'Ge', 'Fl', 'Fr', 'Dr'},
    'Dr': {'Ov', 'Fr', 'Gr'}, 
    'Fr': {'NH','Fl', 'Ov', 'Dr', 'Gr'},
    'Gr': {'Fr', 'Dr'}
}
colours = {'re', 'gr', 'bl', 'ye'}
print(map_colouring_problem(adj_list, colours))
print(check_assignment(adj_list, map_colouring_problem(adj_list, colours)))

