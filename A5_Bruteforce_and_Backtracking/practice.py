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
        # impossible case, out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        # Base case: letter already visited or letter doesn't match 
        if (r, c) in visited or grid[r][c] != word[index]:
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