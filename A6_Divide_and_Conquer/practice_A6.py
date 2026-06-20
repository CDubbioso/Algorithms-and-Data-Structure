# Divide and Conquer Practice Exercises


# Exercise 1: 
# Power Function
# Implement pow(base, exp) using divide and conquer.
# Key insight: base^exp = base^(exp//2) * base^(exp//2), with an extra *base if exp is odd.
# Target time complexity: O(log n)
#
# Examples:
#   pow(2, 10) -> 1024
#   pow(3, 5)  -> 243
#   pow(5, 0)  -> 1

def pow(base: int, exp: int) -> int:
    if exp == 0 or base == 1:
        return 1
    if exp == 1:
        return base
    
    half = pow(base, (exp//2))
    
    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half
    
# print(pow(2, 10)) # 1024
# print(pow(3, 5))  # 243
# print(pow(5, 0))  # 1

# -----------------------------------------------------------------------------------

# Exercise 2: 
# Find Maximum Subarray Sum (Kadane's D&C version)
# Given a list of integers, find the contiguous subarray with the largest sum.
# Use divide and conquer: split the array in half, recursively solve left and right,
# then compute the maximum subarray that crosses the midpoint.
# Target time complexity: O(n log n)
#
# Examples:
#   max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])   -> 6  (subarray [4, -1, 2, 1])
#   max_subarray([1, 2, 3, 4])                      -> 10
#   max_subarray([-1, -2, -3])                      -> -1

def max_subarray(nums: list[int]) -> tuple[int, list[int]]:
    mid = len(nums) // 2
    
    if len(nums) == 1:
        return nums[0], nums[:]

    left = nums[:mid]
    right = nums[mid:]
    
    new_sum_left = 0
    sum_left = float('-inf')
    best_l = mid
    for i in range(mid-1, -1, -1):
        new_sum_left += left[i]
        if new_sum_left >= sum_left:
            sum_left = new_sum_left
            best_l = i
    
    new_sum_right = 0 
    sum_right = float('-inf')
    best_r = -1
    for i in range(mid, len(nums)):
        new_sum_right += right[i-mid]
        if new_sum_right >= sum_right:
            sum_right = new_sum_right
            best_r = i - mid
    
    cross_sum = sum_left + sum_right
    cross_list = left[best_l:] + right[:best_r+1]

    left_sum, left_list = max_subarray(left)
    right_sum, right_list = max_subarray(right)

    return max((cross_sum, cross_list), (left_sum, left_list), (right_sum, right_list), key=lambda x: x[0])

# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6

# -----------------------------------------------------------------------------------

# Exercise 3: 
# Count Inversions
# An inversion is a pair (i, j) where i < j but nums[i] > nums[j].
# Count the total number of inversions in the list using a modified merge sort.
# Target time complexity: O(n log n)
#
# Examples:
#   count_inversions([2, 4, 1, 3, 5]) -> 3   (pairs: (2,1), (4,1), (4,3))
#   count_inversions([1, 2, 3, 4, 5]) -> 0   (already sorted)
#   count_inversions([5, 4, 3, 2, 1]) -> 10  (every pair is inverted)

def count_inversions(nums: list[int]) -> int:
    count = 0
    list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
                list.append((nums[i], nums[j]))
    return count, list

# print(count_inversions([2, 4, 1, 3, 5])) 