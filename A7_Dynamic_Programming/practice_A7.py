import numpy as np

# ==============================================================================
# Exercise 1 — Coin Change
# ==============================================================================

def coin_change_bottom_up(coins, amount):
    """
    Given a list of coin denominations and a target amount, return the minimum
    number of coins needed to make up that amount. You have an unlimited supply
    of each denomination. If it is impossible, return -1.

    Example:
        coins = [1, 5, 6, 9], amount = 11
        Optimal: 9 + 1 + 1 = 3 coins  -> return 3

        coins = [2], amount = 3
        Impossible                     -> return -1

    :param coins: List of coin denominations (positive integers)
    :param amount: Target amount (non-negative integer)
    :return: Minimum number of coins, or -1 if impossible
    :rtype: int
    """
    storage = {}

    for i in range(amount + 1):
        if amount in storage:
            return storage[amount], storage
        if i == 0:
            storage[i] = 0
        else:
            for c in coins:
                if i - c in storage:
                    if i not in storage:
                        storage[i] = storage[i - c] + 1
                    else:
                        storage[i] = min(storage[i], storage[i - c] + 1)

    if amount in storage:
        return storage[amount], storage
                        
    return -1, storage

# print(coin_change_bottom_up([1, 5, 6, 9], 11))
# print(coin_change_bottom_up([2], 3))

def coin_change_top_down(coins, amount):
    """
    Same problem as coin_change_bottom_up — solve it with recursion + memoization.

    :param coins: List of coin denominations (positive integers)
    :param amount: Target amount (non-negative integer)
    :param memo: Memoization dictionary (leave as None on first call)
    :return: Minimum number of coins, or -1 if impossible
    :rtype: int
    """
    solutions = {
        0: 0
    }

    def dp(new_amount):
        # Base case
        if new_amount == 0:
            return 0
        if new_amount < 0:
            return -1
        
        # check memoization 
        if new_amount in solutions: 
            return solutions[new_amount]      

        # recursive case
        for coin in coins:
            result = dp(new_amount - coin)
            if new_amount not in solutions:
                if result != -1:
                    solutions[new_amount] = result + 1
                else:
                    solutions[new_amount] = -1
            else:
                if result != -1:
                    solutions[new_amount] = min(solutions[new_amount], result + 1)
        
        return solutions[new_amount]
                
    return dp(amount)

# print(coin_change_top_down([1, 5, 6, 9], 11))
# print(coin_change_top_down([2], 3))

# ==============================================================================
# Exercise 2 — Longest Increasing Subsequence
# ==============================================================================

def lis_bottom_up(arr):
    """
    Given a list of integers, return the length of the longest strictly
    increasing subsequence (elements do not need to be contiguous).

    Example:
        arr = [10, 9, 2, 5, 3, 7, 101, 18]
        One LIS: [2, 3, 7, 18]  -> return 4

    :param arr: List of integers
    :return: Length of the longest strictly increasing subsequence
    :rtype: int
    """
    storage = [1] * len(arr)  # store lenghts 

    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                storage[i] = max(storage[i], storage[j] + 1)
    
    return max(storage)
                
# print(lis_bottom_up([10, 9, 2, 5, 3, 7, 101, 18]))

def lis_top_down(arr, index=0, prev_val=float('-inf')):
    """
    Same problem as lis_bottom_up — solve it with recursion + memoization.

    Top-down approach:
        At each index decide: skip arr[index] or take it (only if arr[index] > prev_val).
        State: (index, prev_val) — memoize on this pair.
        Base case: index == len(arr) -> return 0.
        Recurrence:
            skip = lis(index + 1, prev_val)
            take = 1 + lis(index + 1, arr[index])   if arr[index] > prev_val
            return max(skip, take)

    :param arr: List of integers
    :param index: Current position in arr (leave as 0 on first call)
    :param prev_val: Value of the last taken element (leave as -inf on first call)
    :param memo: Memoization dictionary (leave as None on first call)
    :return: Length of the longest strictly increasing subsequence
    :rtype: int
    """
    memo = {}  # (index, prev_val) -> length

    def dp(index, prev_val):
        # Base case
        if index == len(arr):
            return 0
        
        # check memoization 
        if (index, prev_val) in memo:
            return memo[(index, prev_val)]

        # recursive case
        skip = dp(index + 1, prev_val)
        take = 0
        if arr[index] > prev_val:
            take = 1 + dp(index + 1, arr[index])
        
        memo[(index, prev_val)] = max(skip, take)
        return memo[(index, prev_val)]
    
    return dp(index, prev_val)

# print(lis_top_down([10, 9, 2, 5, 3, 7, 101, 18]))   

# ==============================================================================
# Exercise 3 — Grid Minimum Path
# ==============================================================================

def grid_min_path_bottom_up(grid):
    """
    Given an n x m grid of non-negative integers, find the minimum-cost path
    from (0, 0) to (n-1, m-1) moving only RIGHT or DOWN.

    Example:
        grid = [[1, 3, 1],
                [1, 5, 1],
                [4, 2, 1]]
        Optimal path: 1->3->1->1->1 = 7  -> return 7

    Bottom-up approach:
        Build a 2D dp table of the same size as grid.
        dp[i][j] = minimum cost to reach cell (i, j).
        Base case:  dp[0][0] = grid[0][0].
                    First row:    dp[0][j] = dp[0][j-1] + grid[0][j].
                    First column: dp[i][0] = dp[i-1][0] + grid[i][0].
        Recurrence: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).
        Answer:     dp[n-1][m-1].

    :param grid: 2D list of non-negative integers (n x m)
    :return: Minimum cost to travel from (0, 0) to (n-1, m-1)
    :rtype: int
    """
    pass


def grid_min_path_top_down(grid, i=None, j=None, memo=None):
    """
    Same problem as grid_min_path_bottom_up — solve it with recursion + memoization.

    Top-down approach:
        Define cost(i, j) = minimum cost to reach (i, j) from (0, 0).
        Base case:  cost(0, 0) = grid[0][0].
                    cost(i, 0) = cost(i-1, 0) + grid[i][0]   (only from above).
                    cost(0, j) = cost(0, j-1) + grid[0][j]   (only from left).
        Recurrence: cost(i, j) = grid[i][j] + min(cost(i-1, j), cost(i, j-1)).
        Memoize on (i, j).
        On the first call pass i = n-1, j = m-1 (you compute top-down toward (0,0)).

    :param grid: 2D list of non-negative integers (n x m)
    :param i: Row index (leave as None on first call — will default to n-1)
    :param j: Column index (leave as None on first call — will default to m-1)
    :param memo: Memoization dictionary (leave as None on first call)
    :return: Minimum cost to travel from (0, 0) to (n-1, m-1)
    :rtype: int
    """
    pass


# ==============================================================================
# Exercise 4 — Partition Equal Subset Sum
# ==============================================================================

def can_partition_bottom_up(nums):
    """
    Given a list of positive integers, determine whether it can be split into
    two subsets with equal sum.

    Example:
        nums = [1, 5, 11, 5]  -> True   ({1,5,5} and {11})
        nums = [1, 2, 3, 5]   -> False

    Bottom-up approach:
        If total sum is odd, return False immediately.
        target = total // 2.
        dp is a boolean array of size (target + 1).
        dp[j] = True if some subset of the items seen so far sums to j.
        Base case: dp[0] = True.
        For each item, iterate j from target down to item (right-to-left,
        like 0/1 knapsack) and set dp[j] |= dp[j - item].
        Answer: dp[target].

    :param nums: List of positive integers
    :return: True if the list can be split into two equal-sum subsets
    :rtype: bool
    """
    pass


def can_partition_top_down(nums, index=0, remaining=None, memo=None):
    """
    Same problem as can_partition_bottom_up — solve it with recursion + memoization.

    Top-down approach:
        If total sum is odd, return False immediately.
        target = total // 2.
        Define reachable(index, remaining) = True if some subset of
        nums[index:] sums exactly to `remaining`.
        Base case:  remaining == 0 -> True.
                    index == len(nums) -> False.
        Recurrence: skip nums[index] OR take it (if nums[index] <= remaining).
        Memoize on (index, remaining).
        First call: reachable(0, target).

    :param nums: List of positive integers
    :param index: Current position in nums (leave as 0 on first call)
    :param remaining: Remaining sum to hit (leave as None — defaults to total//2)
    :param memo: Memoization dictionary (leave as None on first call)
    :return: True if the list can be split into two equal-sum subsets
    :rtype: bool
    """
    pass


# ==============================================================================
# Exercise 5 — Weighted Job Scheduling
# ==============================================================================

def weighted_jobs_bottom_up(jobs):
    """
    Given a list of jobs (start, end, profit), find the maximum total profit
    from a set of non-overlapping jobs.

    Example:
        jobs = [(1,3,50), (2,5,20), (4,6,100), (6,7,200)]
        Optimal: (1,3,50) + (4,6,100) + (6,7,200) = 350  -> return 350

    Bottom-up approach:
        1. Sort jobs by end time.
        2. Build an array of end times for binary search.
        3. dp[i] = max profit considering jobs[0..i-1] (dp[0] = 0).
        4. For each job i (1-indexed):
               skip: dp[i] = dp[i-1]
               take: find last job j whose end <= jobs[i-1].start using
                     binary search, then dp[i] = profit_i + dp[j].
               dp[i] = max(skip, take).
        Answer: dp[n].

    Hint: use the bisect module for binary search.

    :param jobs: List of (start, end, profit) tuples
    :return: Maximum profit from non-overlapping jobs
    :rtype: int
    """
    pass


def weighted_jobs_top_down(jobs, index=None, memo=None):
    """
    Same problem as weighted_jobs_bottom_up — solve it with recursion + memoization.

    Top-down approach:
        1. Sort jobs by end time.
        2. Define best(index) = max profit using jobs[index:].
        3. Base case: index == len(jobs) -> return 0.
        4. Recurrence:
               skip = best(index + 1)
               find the first job k >= index+1 whose start >= jobs[index].end
               (binary search on start times, or scan forward).
               take = jobs[index].profit + best(k)
               return max(skip, take).
        Memoize on index.
        First call: best(0) after sorting.

    :param jobs: List of (start, end, profit) tuples
    :param index: Current job index (leave as None on first call — defaults to 0)
    :param memo: Memoization dictionary (leave as None on first call)
    :return: Maximum profit from non-overlapping jobs
    :rtype: int
    """
    pass
