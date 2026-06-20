def cut_rod(price):
    """
    Given a list of prices where price[i] is the price of a rod of length i+1,
    return the maximum price obtainable by cutting up the rod and selling the pieces.
    Use dynamic programming to speed up the solution.
    Use tabulation (bottom-up) or memoization (top-down) to solve this problem.
    
    Arguments:
    price -- List[int], where price[i] = price of rod length i+1
    Returns:
    int -- Maximum price obtainable
    """
    dp = [0]        # optimal value for each lenght

    for i in range(1, len(price)+1):
        max_value = 0
        for j in range(1, i+1):     # try evry cut 
            max_value = max(price[j - 1] + dp[i - j], max_value)

        dp.append(max_value)

    return dp[len(price)]