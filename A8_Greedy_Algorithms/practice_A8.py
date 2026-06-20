# ==============================================================================
# Exercise 1 — Activity Selection (interval scheduling)
# ==============================================================================

def activity_selection(activities):
    """
    Given a list of activities, each defined by (start, end), select the maximum
    number of non-overlapping activities. Two activities overlap if one starts
    before the other ends.

    Example:
        activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
        Optimal selection: (1,4), (5,7), (8,11)  -> return 3

    Greedy insight: always pick the activity that finishes earliest — it leaves
    the most room for future activities. Sort by end time, then greedily take
    each activity whose start >= the end of the last selected one.

    :param activities: List of (start, end) tuples
    :return: Maximum number of non-overlapping activities
    :rtype: int
    """
    pass


# ==============================================================================
# Exercise 2 — Huffman Encoding (greedy tree construction)
# ==============================================================================

def huffman_lengths(frequencies):
    """
    Given a dictionary mapping characters to their frequencies, compute the
    optimal (minimum total bits) prefix-free code length for each character
    using Huffman's algorithm. Return a dictionary mapping each character to
    its code length (depth in the Huffman tree).

    Example:
        frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        One valid result: {'f': 1, 'c': 3, 'd': 3, 'a': 4, 'b': 4, 'e': 3}
        (exact lengths may differ by arrangement of equal-weight nodes)

    Greedy insight: always merge the two nodes with the lowest frequency.
    Use a min-heap (heapq). Each node stores (frequency, label, children).
    After building the tree, traverse it to assign depths.

    Hint: import heapq. Push (freq, char) tuples. Pop two minimums, merge into
    a new node with combined frequency, push back. Repeat until one node left.

    :param frequencies: dict mapping character -> frequency (positive int)
    :return: dict mapping character -> code length (int)
    :rtype: dict[str, int]
    """
    pass


# ==============================================================================
# Exercise 3 — Fractional Knapsack (greedy, items are divisible)
# ==============================================================================

def fractional_knapsack(weights, values, capacity):
    """
    Unlike the 0/1 knapsack, here you may take any fraction of an item.
    Given weights, values, and a capacity, return the maximum value achievable.

    Example:
        weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
        Take all of item 0 (10 kg, 60 val) + all of item 1 (20 kg, 100 val)
        + 2/3 of item 2 (20 kg, 80 val) -> total value = 240.0

    Greedy insight: sort by value-to-weight ratio (descending). Take as much of
    the best-ratio item as possible before moving on. Because items are divisible,
    this greedy choice is globally optimal (unlike 0/1 knapsack).

    :param weights: List of item weights (positive numbers)
    :param values: List of item values (positive numbers)
    :param capacity: Maximum weight capacity (positive number)
    :return: Maximum value (float)
    :rtype: float
    """
    pass


# ==============================================================================
# Exercise 4 — Prim's Algorithm (greedy MST, alternative to Kruskal)
# ==============================================================================

def prim(adj_list):
    """
    Find a Minimum Spanning Tree of an undirected weighted graph using Prim's
    algorithm. Return the total weight of the MST.

    The graph is given as an adjacency list:
        adj_list[u] = [(v, weight), ...]

    Example:
        adj_list = {
            'A': [('B', 2), ('C', 3)],
            'B': [('A', 2), ('C', 1), ('D', 4)],
            'C': [('A', 3), ('B', 1), ('D', 5)],
            'D': [('B', 4), ('C', 5)],
        }
        MST edges: B-C(1), A-B(2), B-D(4) -> total weight = 7

    Greedy insight: grow the MST one vertex at a time. Start from any vertex.
    At each step, pick the cheapest edge that connects a vertex already in the
    MST to one outside it (like Dijkstra but tracking edge weight, not total
    path distance).

    Hint: use a min-heap of (weight, neighbor) tuples. Keep a visited set.

    :param adj_list: dict[str, list[tuple[str, int]]]
    :return: Total weight of the MST
    :rtype: int
    """
    pass


# ==============================================================================
# Exercise 5 — Task Scheduling to Minimise Lateness (deadline scheduling)
# ==============================================================================

def minimize_lateness(jobs):
    """
    You have a single machine and a list of jobs. Each job i has a processing
    time t_i and a deadline d_i. Jobs must be scheduled one at a time with no
    gaps. The lateness of job i is max(0, finish_time_i - d_i). Schedule all
    jobs to minimise the maximum lateness across all jobs.

    Return the maximum lateness of the optimal schedule.

    Example:
        jobs = [(3, 6), (2, 8), (1, 9), (4, 9), (3, 14), (2, 15)]
               # (processing_time, deadline)
        Sorted by deadline: same order. Schedule finishes at times 3,5,6,10,13,15.
        Latenesses: max(0,3-6)=0, max(0,5-8)=0, max(0,6-9)=0,
                    max(0,10-9)=1, max(0,13-14)=0, max(0,15-15)=0
        Maximum lateness = 1  -> return 1

    Greedy insight: schedule jobs in order of earliest deadline first (EDF).
    This is provably optimal for minimising maximum lateness.

    :param jobs: List of (processing_time, deadline) tuples
    :return: Minimum possible maximum lateness
    :rtype: int
    """
    pass
