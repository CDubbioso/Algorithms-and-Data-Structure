def maze_solver(maze):
    """
    Starting in the top left corner (0,0) determine whether there is a path,
    moving horizontally and vertically, to exit the labyrinth in the bottom-right corner.
    
    :param maze: A 2D list representing a maze, with 0 for paths and 1 for walls
    :type maze: list[list[int]]
    :return: True/False whether there is a way to exit the labyrinth
    """
    visited = set()
    return solve(maze, 0, 0, visited)

def solve(maze, row, col, visited):
    r = len(maze)
    c = len(maze[0])

    # contraints
    if row >= r or col >= c or row < 0 or col < 0:
        return False
    if maze[row][col] == 1:
        return False
    if (row, col) in visited:
        # visited 
        return False

    # base case
    if row == r-1 and col == c-1:
        return True
    
    visited.add((row,col))

    return solve(maze, row, col+1, visited) or solve(maze, row+1, col, visited) or solve(maze, row-1, col, visited) or solve(maze, row, col-1, visited)
    # if solve(maze, row, col+1, visited) or solve(maze, row+1, col, visited) or solve(maze, row-1, col, visited) or solve(maze, row, col-1, visited):
    #     return True
    # visited.remove((row, col))  # backtrack: undo the choice
    # return False

# Simple path exists
print(maze_solver([[0,0],[0,0]]))  # True
# Wall blocking
print(maze_solver([[0,1],[1,0]]))  # False
# Requires going up/left
print(maze_solver([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]))  # True
# Start is wall
print(maze_solver([[1,0],[0,0]]))  # False