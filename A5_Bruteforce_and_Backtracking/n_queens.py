def rec_nQueens(size, queens=[]):
    """
    Recursively computes all solutions for the n-Queens puzzle.

    :param size: The size of the puzzle
    :type size: int
    :param queens: The currently placed queens, e.g. [4,2] represent
    that on row 0 there is a queen on the 4th index and on row 1 
    there is a queen on the 2nd index. 
    :type queens: list[int]
    
    :return: the (partial) list of queen posisitons
    :rtype: list[int]
    """
    if len(queens) == size:
        return [queens]
    
    solution = []
    for i in range(size):
        if constraint(queens, i): 
            new_queens = queens + [i]
            solution.extend(rec_nQueens(size, new_queens))

    return solution

def constraint(queens, col):
    """
    The constraints for the n-queens problem.
    
    :param queens: The currently placed queens.
    :type queens: list[int]
    :param col: The column that the next queen would be placed
    :type col: int
    
    :return: If the puzzle constraint is satisfied or not
    :rtype: bool
    """
    if queens == []:
        return True 
    
    new_row = len(queens)

    for row, c in enumerate(queens):
        if col == c:
            return False
        if abs(row - new_row) == abs(c - col):
            return False
    
    return True

# print(rec_nQueens(1), [0])  # [0]
print(rec_nQueens(4, [1]))  # [1, 3, 0, 2]
# print(rec_nQueens(8, [1]))  # [0, 4, 7, 5, 2, 6, 1, 3]
# print(rec_nQueens(2, [1]))  # None (no solution exists)
# print(rec_nQueens(3, [1]))  # None (no solution exists)