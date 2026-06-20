def floor_is_lava(grid, position, final_position, n, dp):
    """
    Calculates the probability of reaching the final_position from the given position
    in exactly n steps, moving only to adjacent (up, down, left, right) non-lava cells.
    Parameters:
    -----------
    grid : List[List[int]]
        A 2D list representing the map. A value of 1 indicates a safe cell,
        and 0 indicates a lava cell that cannot be stepped on.
    position : Tuple[int, int]
        The starting coordinates (x, y) in the grid.
    final_position : Tuple[int, int]
        The target coordinates (fx, fy) in the grid to reach in exactly n steps.
    n : int
        The exact number of steps allowed to reach the final position.
    dp : dict
        A memoization dictionary to cache subproblem results for optimization.
        Keys are tuples of the form (x, y, steps_remaining), and values are 
        computed probabilities for those states.
    Returns:
    --------
    float
        The probability of reaching the final_position from position in exactly n steps,
        moving only to adjacent safe cells with equal probability in each direction.
    Notes:
    ------
    - If a move would go out of bounds or onto lava, it contributes 0 to the probability.
    - At each step, the function tries all four directions (up/down/left/right) with equal probability (0.25).
    - If n == 0, the function returns 1.0 only if the current position is the final position,
      otherwise returns 0.0.
    """
    # Base Case: final position
    if n == 0:
        if position == final_position:
            return 1.0
        else:
            return 0.0
    
    x, y = position

    if (x, y, n) in dp:
        return dp[(x, y, n)]
    
    rows = len(grid)
    cols = len(grid[0])

    # Base Case: invalid cell 
    if x < 0 or x >= rows or y<0 or y>=cols or grid[x][y] == 0:
        return 0.0

    directions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    total_prob = 0 

    for move in directions:
        prob = 0.25 * floor_is_lava(grid, move, final_position, n-1, dp)
        total_prob += prob

    dp[(x, y, n)] = total_prob

    return total_prob