import numpy as np

def coin_row(coins):
    """
    Given a list of coin values in a row, compute the maximum value you can
    collect without taking adjacent coins. Use dynamic programming.

    Example:
        coins = [5, 1, 2, 10, 6, 2]
        Take coins 5 + 10 + 2 = 17

    :param coins: List of coin values (non-negative integers)
    :return: Maximum value collectible (int)
    :rtype: int
    """
    F = [0, coins[0]] + [0] * (len(coins) - 1)  # base case

    for i in range(1, len(coins)):
        F[i+1] = max((coins[i] + F[i-1]), F[i])
    
    return F[len(coins)], F

print(coin_row([5, 1, 2, 10, 6, 2]))
print([0, 5] + [0] * (6 - 1))

def fibonacci(n):
    """
    Compute the nth Fibonacci number using dynamic programming.

    Example:
        n = 5
        F(5) = 5

    :param n: The index of the Fibonacci number to compute (non-negative integer)
    :return: The nth Fibonacci number (int)
    :rtype: int
    """
    # base case
    if n <= 1:
        return n

    F = [0, 1] * ([0] * (n-1))  # store Fibonacci numbers

    for i in range(2, n + 1):
        F[i] = F[i-1] + F[i-2]

    return F[n]


def change_making(coins, amount):
    """
    Given a list of coin denominations and a target amount, compute the minimum
    number of coins needed to make that amount. Use dynamic programming.

    Example:
        coins = [1, 3, 4]
        amount = 6
        Minimum coins needed: 2 (3 + 3)

    :param coins: List of coin denominations (positive integers)
    :param amount: Target amount to make change for (non-negative integer)
    :return: Minimum number of coins needed (int), or -1 if not possible
    :rtype: int
    """
    lst = [0] # F[0] = 0, base case

    for val in range(1, amount+1):
        j = 0   # index for coins
        tempMin = float('inf')  # temporary minimum, initialized to infinity

        while j < len(coins) and val >= coins[j]:   # while the coin is less than or equal to the value
            tempMin = min(tempMin, lst[val - coins[j]]) # find the minimum number of coins needed for the remaining amount
            j += 1  # move to next coin

        lst.append(tempMin + 1)     # add 1 to account for the coin just used
    
    return lst[amount]

# print(change_making([1, 3, 4], 6))


def coin_collecting_robot(grid):
    """
    Given a 2D grid of coin values, compute the maximum value a robot can collect
    starting from the top-left corner (0,0) to the bottom-right corner (m-1,n-1),
    moving only right or down. Use dynamic programming.
    """
    F = np.zeros((len(grid)+1, len(grid[0])+1), dtype=int)  # store maximum values

    for i in range(1, len(F)):
        for j in range(1, len(F[0])):
            F[i][j] = max(F[i-1][j], F[i][j-1]) + grid[i-1][j-1]  # max of top or left cell + current cell value


    return F[len(grid)][len(grid[0])]

table = [
    [0,0,0,0,1,0],
    [0,1,0,1,0,0],
    [0,0,0,1,0,1],
    [0,0,1,0,0,1],
    [1,0,0,0,1,0],
]
# print(coin_collecting_robot(table))



# -------------------------------------------------------------------



def knapsack_bottom_up(weights, values, capacity):
    F = np.zeros((len(values)+1, capacity+1), dtype=int)  # store maximum values
    for i in range(1, len(values)+1):
        for j in range(1, capacity + 1):
            if j - weights[i-1] >= 0:
                F[i][j] = max(F[i-1][j], F[i-1][j-weights[i-1]] + values[i-1])
            else:
                F[i][j] = F[i-1][j]
    
    return F[len(values)][capacity]

# print(knapsack_bottom_up([2, 1, 3, 2], [12, 10, 20, 15], 5))
# [[ 0  0  0  0  0  0]
#  [ 0  0 12 12 12 12]
#  [ 0 10 12 22 22 22]
#  [ 0 10 12 22 30 32]
#  [ 0 10 15 25 30 37]]

def knapsack_top_down(weights, values, capacity):
    """
    Given weights, values, and a capacity, compute the maximum value achievable
    using the 0/1 knapsack problem. Use recursion + memoization.

    Example:
        weights = [1, 2, 3], values = [6, 10, 12], capacity = 5
        Take items 1 and 2 (weights 2+3=5) for total value = 10+12=22
    
    :param weights: List of item weights (positive integers)
    :param values: List of item values (positive integers)  
    :param capacity: Maximum weight capacity (positive integer)
    :return: Maximum value achievable (int)
    :rtype: int
    """
    memo = {}   # store computed results for subproblems
    
    def bt(i, j):
        # i : index
        # j : temporary weight capacity
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if j - weights[i-1] >= 0:       # if the current weight can be included
            memo[(i, j)] = max(bt(i-1, j), values[i-1] + bt(i-1, j-weights[i-1]))   # store the maximum value
        else:   # if the current weight cannot be included
            memo[(i, j)] = bt(i-1, j)

        return memo[(i, j)]     # return solution for the current subproblem
    
    return bt(len(values), capacity)    # return the maximum value achievable for the full problem

# print(knapsack_top_down([2, 1, 3, 2], [12, 10, 20, 15], 5))


def subset_sum(S, d):
    """
    Given a list of numbers S and a target d, find if there exists a subset S' such that 
    the sum of the numbers in S' is equal to d. 
    Return True whether it exist a solution, False otherwise. 
    """
    # memo = {}

    def dp(i, k):
        if k == 0: 
            return True
        elif i == 0 or k < 0:
            return False
        
        # if (i,k) in memo:
        #     return memo[(i,k)]
        
        return dp(i-1, k) or dp(i-1, k-S[i-1])
    
    return dp(len(S), d)

# print(subset_sum([1, 2, 5, 6, 8], 9))


def bus_trip(costs, n):
    """
    Given a matrix of prices where costs(i,j) is the cost of going from i to j,
    find the cheapest itinerary from 0 to n. 
    """
    dp = [float("inf")] * len(costs[0]) # store minimum price to reach station i from 0
    dp[0] = 0

    for i in range(len(costs)):
        for j in range(len(costs[0])):
            price = costs[j][i]
            if price > 0:
                candidate = dp[j] + price
                if candidate < dp[i]:
                    dp[i] = candidate

    return dp[n]

price_matrix = [
    [0, 5, 10, 15],
     [0, 0, 7, 13],
     [0, 0, 0, 4],
     [0, 0, 0, 0]
]
# print(bus_trip(price_matrix, 3))


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# Design a top-down dynamic programming algorithm which solves the (worst-case) problem in linear time. 
# Note that for a unconnected (acyclic) graph any node can be the root. 
# You may assume that the initial call to your function will be made with a  fixed root node. 
def vertex_cover(G, root):
    """
    :param G: An adjacency list representation of a graph.
    :type G: Dict[str, List[str]]
    
    :param root: The root of the (sub)tree
    :type root: str

    :return: The size of a minimal vertex cover.  
    :rtype: int 
    """
    memo = {node: None for node in G.keys()} 

    def bt(node, parent):
        children = [n for n in G[node] if n != parent]

        cover_in = 1
        cover_out= 0

        for child in children:
            child_in, child_out = bt(child, node)   # recurse: get child's pair
            cover_in += min(child_in, child_out)    # parent covers edge -> child free
            cover_out += child_in                   # parent doesn't -> child forced in

        return (cover_in, cover_out)

    return min(bt(root, None))


G = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C', 'E', 'F'],
    'E': ['D'],
    'F': ['D', 'G'],
    'G': ['F'],
}
root = 'A'
# print(vertex_cover(G, root))

