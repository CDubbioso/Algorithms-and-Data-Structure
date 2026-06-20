import numpy as np

def bus_schedule_problem(price_matrix):
    """
    We are given a price matrix with the cost of traveling between bus stops.
    The first bus stop is always 0 and the last bus stop is always n-1.
    The cost of traveling from bus stop i to bus stop j is given by price_matrix[i][j].
    The cost of traveling from bus stop i to bus stop j is 0 if i == j.
    The goal is to find the minimum cost to travel from the first bus stop to the last bus stop.
    Example:
    [[0, 5, 10, 15],
     [0, 0, 7, 13],
     [0, 0, 0, 4],
     [0, 0, 0, 0]]
    The minimum cost to travel from bus stop 0 to bus stop 3 is 14 (stop 0 -> stop 2 -> stop 3).
    This function calculates the minimum cost to travel from the first bus stop to the last bus stop using dynamic programming.
    :param price_matrix: A matrix representing the cost of traveling between bus stops, where price_matrix[i][j] 
    is the cost to travel from bus stop i to bus stop j.
    :return: The minimum cost to travel from the first bus stop to the last bus stop
    :rtype: int
    """
    n = len(price_matrix[0])
    
    rows = [list(row) for row in price_matrix]

    dp = [float("inf")] * n     # dp[i] = min cost to reach stop i
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            cost = rows[j][i]
            if cost > 0:
                candidate = dp[j] + cost
                if candidate < dp[i]:
                    dp[i] = candidate
    return dp[n - 1]