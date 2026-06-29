import numpy as np

# Brute Force and Backtracking Practice Exercises


# Exercise 1: 
# Subset Sum
# Given a list of positive integers and a target value, find all subsets
# that sum exactly to the target. Use backtracking to prune branches early.
#
# Examples:
#   subset_sum([3, 1, 4, 2, 2], 5) -> [[3, 2], [3, 2], [1, 4], [1, 2, 2]]
#   subset_sum([1, 2, 3], 7)       -> []
#   subset_sum([2, 4, 6], 6)       -> [[2, 4], [6]]

def subset_sum(nums: list[int], target: int) -> list[list[int]]:
    result = []

    def bt(start, partial, current_sum):
        if current_sum == target:
            result.append(partial[:])
            return 
        if current_sum > target:
            return
        
        for i in range(start, len(nums)):
            partial.append(nums[i])
            bt(i+1, partial, current_sum + nums[i])
            partial.pop()

    bt(0, [], 0)
    return result
    
# print(subset_sum([3, 1, 4, 2, 2], 5))

# ---------------------------------------------------------------------------------------------------

# Exercise 2: 
# Sudoku Solver
# Fill a 9x9 sudoku board (0 represents an empty cell) using backtracking.
# At each empty cell, try digits 1-9, check validity (no repeats in row,
# column, or 3x3 box), recurse, and backtrack if stuck.
# Modify the board in-place and return True if solved, False if unsolvable.
#
# Example board (0 = empty):
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]
# solve_sudoku(board) -> True, board filled in correctly

def solve_sudoku(board: list[list[int]]) -> bool:
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for num in range(1, len(board)+1):
                    if sudoku_constraint(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    
    return True            


def sudoku_constraint(board, row, col, num):
    if num in board[row] or any(num == board[i][col] for i in range(len(board))):   # check row and column
        return False
    
    # check 3x3 box
    sqrt = int(len(board) ** 0.5)
    row_start = (row // sqrt) * sqrt
    col_start = (col // sqrt) * sqrt
    for r in range(row_start, row_start + sqrt):
        for c in range(col_start, col_start + sqrt):
            if board[r][c] == num:
                return False
    
    return True

# -----------------------------------------------------------------------------------

# Exercise 3: 
# Word Search
# Given a 2D grid of characters and a target word, determine whether the word
# exists in the grid. The word can be constructed from letters of sequentially
# adjacent cells (horizontally or vertically). The same cell may not be used twice.
# Use backtracking: mark a cell as visited when you step into it, unmark on backtrack.
#
# Examples:
#   grid = [["A","B","C","E"],
#           ["S","F","C","S"],
#           ["A","D","E","E"]]
#   word_search(grid, "ABCCED") -> True
#   word_search(grid, "SEE")    -> True
#   word_search(grid, "ABCB")   -> False  (can't reuse B)

def word_search(grid: list[list[str]], word: str) -> bool:
    visited = set()
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c, index):
        # Base case: impossible case, out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        # Base case: letter already visited 
        if (r, c) in visited:
            return False
        # Base case: letter doesn't match
        if grid[r][c] != word[index]:
            return False
        
        # is complete word found
        if index == len(word) - 1:
            return True
        
        visited.add((r, c))
        # explore neighbors
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for dr, dc in directions:
            if dfs(r+dr, c+dc, index+1):
                return True
        visited.remove((r,c))   # backtrack
        return False

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    
    return False

# word = "BASA"
# grd = [["A","B","C","E"],
#        ["S","F","C","S"],
#        ["A","D","E","E"]]
# print(word_search(grd, word))  # True



# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------



def knapsack_exhaustive(weights, values, target):
    lst = []

    def bt(i, capacity, accumulated):
        if i >= len(weights):
            return 0
        
        skip = bt(i+1, capacity, accumulated)

        take = 0
        lst.append(values[i])
        if capacity - weights[i] >= 0: 
            capacity -= weights[i]
            accumulated += weights[i]
            take = values[i] + bt(i+1, capacity, accumulated)
            

        return max(skip, take)

    return bt(0, target, 0)

weight = [8, 3, 4, 5]
value = [42, 14, 40, 27]
# print(knapsack_exhaustive(weight, value, 12))


def TSP_exhaustive(graph, route, total_distance):

    n = len(graph)
    r = len(route)

    # Base case
    if r == n:
        total_distance += graph[route[-1][0]]
        route.append(route[0])
        return total_distance, route
    
    best_route = None
    best_distance = float('inf')
    for i in range(n):
        if i not in route:
            current_distance = graph[-1][i]
            total_distance += current_distance
            route.append(i)

            dist, tot_route = TSP_exhaustive(graph, route, total_distance)

            if dist < best_distance:
                best_distance = dist
                best_route = tot_route
            
            total_distance -= current_distance
            route.pop()
    
    return best_distance, best_route


def hamiltonian_cycle(graph, start):
    def bt(s, p_partial):
        if len(p_partial) == len(graph) and start in graph[p_partial[-1]]:
            p_partial.append(start)
            return p_partial
        
        for neigh in graph[s]:
            if neigh not in p_partial:
                p_partial.append(neigh)
                solution = bt(neigh, p_partial)
            
                if solution:
                    return solution
                p_partial.pop()
        return False

    return bt(start, [start])

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E', 'F'],
    'D': ['B', 'F'],    
    'E': ['A', 'C', 'F'],
    'F': ['E', 'C', 'D']
}
# print(hamiltonian_cycle(graph, 'A'))


def TSP_backtracking(graph, start):
    def bt(s, partial_path, partial_cost):
        if len(partial_path)==len(graph) and start in graph[partial_path[-1]]:
            return partial_path + [start], partial_cost + graph[partial_path[-1]][start]
        
        best_cost = float('inf')
        best_path = None

        for neighbour in graph[s]:
            if neighbour not in partial_path:
                partial_path.append(neighbour)
                partial_cost += graph[s][neighbour]
                path, cost = bt(neighbour, partial_path, partial_cost)

                if cost < best_cost:
                    best_path = path
                    best_cost = cost

                partial_cost -= graph[s][neighbour]
                partial_path.pop()
        
        return best_path, best_cost

    return bt(start, [start], 0)

graph = {
    'A': {'B': 2, 'C': 5, 'D': 7},
    'B': {'A': 2, 'C': 8, 'D': 3},
    'C': {'A': 5, 'B': 8, 'D': 1},
    'D': {'A': 7, 'B': 3, 'C': 1},
}
# print(TSP_backtracking(graph, 'A'))



def alphametic(w1, w2, w3, mapping, letters, digits):

    def bt(index, mapping, used):
        if index == len(letters): 
            if check_mapping(w1, w2, w3, mapping, letters):
                return mapping
            else:
                return None
        
        letter = letters[index]
        for i in digits:
            if i not in used:
                
                if (letter == w1[0] or letter == w2[0] or letter == w3[0]) and i == 0:
                    continue
                
                mapping[letter] = i
                used.add(i)
                partial_mapping = bt(index+1, mapping, used)

                if partial_mapping:
                    return partial_mapping
                
                used.remove(i)
                del mapping[letter]

        return None
    
    return bt(0, mapping, set())

def check_mapping(w1, w2, w3, mapping, letters):
    
    if len(letters) != len(mapping):
        return None
    
    count_string_1 = 0
    i = 0
    for letter in w1[::-1]:
        count_string_1 += (mapping[letter] * (10 ** i))
        i += 1

    count_string_2 = 0
    i = 0
    for letter in w2[::-1]:
        count_string_2 += (mapping[letter] * (10 ** i))
        i += 1

    count_string_3 = 0
    i = 0
    for letter in w3[::-1]:
        count_string_3 += (mapping[letter] * (10 ** i))
        i += 1

    if count_string_1 + count_string_2 == count_string_3:
        return True
    return False


result = alphametic(
  'SEND', 'MORE', 'MONEY', 
  dict(), 
  ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'], 
  [0, 1, 2, 5, 6, 7, 8, 9])
print(result)
