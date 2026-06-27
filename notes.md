# Algorithm Templates — General Skeletons

Python-style pseudocode for every paradigm we covered. Each template has placeholder
functions (`is_goal`, `get_candidates`, …) you swap out for the specific problem.

---

## 1. Graph Traversal

### DFS — recursive (the default)
```python
def dfs(v, graph, visited):
    visited.add(v)
    for w in graph[v]:
        if w not in visited:
            dfs(w, graph, visited)
```
Call with `visited = set()`. Reach for iterative only on very deep graphs (recursion limit).

### DFS — iterative (explicit stack)
```python
def dfs_iter(start, graph):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()          # pop = LIFO -> depth-first
        if v not in visited:
            visited.add(v)
            for w in graph[v]:
                if w not in visited:
                    stack.append(w)
    return visited
```

### BFS — queue (layer by layer)
```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])
    while queue:
        v = queue.popleft()      # popleft = FIFO -> breadth-first
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return visited
```
DFS and BFS are the *same* skeleton — stack vs queue is the only real difference.

---

## 2. Graph Applications

### Connectivity (is the whole graph reachable from one vertex?)
```python
def is_connected(graph):
    start = next(iter(graph))
    visited = set()
    dfs(start, graph, visited)
    return len(visited) == len(graph)
```

### Cycle detection — UNDIRECTED (track where you came from)
```python
def has_cycle_undirected(v, graph, visited, parent):
    visited.add(v)
    for w in graph[v]:
        if w not in visited:
            if has_cycle_undirected(w, graph, visited, v):
                return True
        elif w != parent:        # visited neighbour that isn't the edge we arrived on
            return True
    return False
```

### Cycle detection — DIRECTED (track the active recursion chain)
```python
def has_cycle_directed(v, graph, visited, path):
    visited.add(v)
    path.add(v)                  # currently on the stack
    for w in graph[v]:
        if w not in visited:
            if has_cycle_directed(w, graph, visited, path):
                return True
        elif w in path:          # back-edge into the active chain = cycle
            return True
    path.remove(v)               # leaving the chain -> undo
    return False
```

---

## 3. State-Space / Game Tree (minimax with memoization)

For combinatorial games: "is the current state a WIN for the player to move?"
A state is a win if *any* move leads to a losing state for the opponent.
```python
def is_winning(state, memo):
    if state in memo:
        return memo[state]
    if is_terminal(state):                 # no moves left
        result = False                     # player to move has already lost
    else:
        result = False
        for move in get_moves(state):
            next_state = apply(state, move)
            if not is_winning(next_state, memo):   # opponent loses -> we win
                result = True
                break
        memo[state] = result
    return result
```
Use a *canonical* state representation (e.g. sorted tuple) as the memo key.

---

## 4. Exhaustive Search (generate-and-test / brute force)

Build every candidate, test each, keep the valid/best one. No early pruning.
```python
def exhaustive_search(problem):
    best = None
    for candidate in generate_all_candidates(problem):   # all permutations / subsets / ...
        if is_valid(candidate):
            if best is None or better(candidate, best):
                best = candidate
    return best
```
Odometer-style recursive generation (e.g. the combination lock):
```python
def generate(position, current, problem):
    if position == length(problem):
        test(current)                       # complete candidate
        return
    for value in choices(position):
        current[position] = value
        generate(position + 1, current, problem)
```

---

## 5. Backtracking (exhaustive search + pruning)

The inner `is_promising` check is what makes it backtracking, not brute force.

### Find ANY solution (existence)
```python
def backtrack(state):
    if is_complete(state):
        return state                        # found one
    for choice in get_candidates(state):
        if is_promising(state, choice):     # PRUNE here
            make_choice(state, choice)
            result = backtrack(state)
            if result is not None:
                return result
            undo_choice(state, choice)      # needed if state is mutable
    return None
```

### Find ALL solutions
```python
def backtrack_all(state, solutions):
    if is_complete(state):
        solutions.append(copy(state))       # COPY — state keeps mutating
        return
    for choice in get_candidates(state):
        if is_promising(state, choice):
            make_choice(state, choice)
            backtrack_all(state, solutions)
            undo_choice(state, choice)
```
Notes: copy the state when storing it. `undo_choice` is required when building a
path/solution; it's optional for pure existence checks that never need the path back.

---

## 6. Recursion Paradigms (by how the subproblem shrinks)

### Decrease by one — factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Decrease by constant factor — binary search
```python
def binary_search(arr, target, lo, hi):
    if lo > hi:
        return -1                           # not found
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, lo, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, hi)
```

### Divide and conquer — merge sort
```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)               # O(n) combine step

def merge(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:]); result.extend(b[j:])
    return result
```

### Decrease by variable size — Euclid's GCD
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

---

## 7. Greedy

Sort by a heuristic, then take items in that order if they fit.
```python
def greedy(items, capacity):
    items = sorted(items, key=lambda x: heuristic(x), reverse=True)  # best first
    chosen, total = [], 0
    for item in items:
        if fits(item, total, capacity):
            chosen.append(item)
            total += size(item)
        # else: skip and continue (don't break) unless the problem says otherwise
    return chosen
```
Watch tie-breaking: `sort(key=lambda x: x[0], reverse=True)` reverses only the key, so
ties keep stable input order — `sort(reverse=True)` would reverse the whole tuple.

---

## 8. Dynamic Programming

### Top-down (recursion + memo)
```python
def solve(state, memo):
    if state in memo:
        return memo[state]
    if is_base_case(state):
        return base_value(state)
    result = combine(solve(subproblem_a(state), memo),
                     solve(subproblem_b(state), memo))   # the recurrence
    memo[state] = result
    return result
```

### Bottom-up 1D (tabulation)
```python
def solve_1d(n):
    dp = [0] * (n + 1)
    dp[0] = base_value                      # seed base case(s)
    for i in range(1, n + 1):
        dp[i] = best_over(dp[i - k] + cost(i, k) for k in choices(i))
    return dp[n]
```
Examples: bus schedule, rod cutting.

### Bottom-up 2D (tabulation)
```python
def solve_2d(A, B):
    rows, cols = len(A) + 1, len(B) + 1
    dp = [[0] * cols for _ in range(rows)]
    # seed first row / first column as base cases
    for i in range(1, rows):
        for j in range(1, cols):
            if match(A, B, i, j):
                dp[i][j] = dp[i - 1][j - 1] + 1               # recurrence A
            else:
                dp[i][j] = best(dp[i - 1][j], dp[i][j - 1])   # recurrence B
    return dp[rows - 1][cols - 1]
```
Same skeleton for LCS, edit distance, 0/1 knapsack — only the recurrence changes.

---

## Quick chooser

| You need to…                                   | Reach for          |
|------------------------------------------------|--------------------|
| Visit/explore all reachable nodes              | DFS / BFS          |
| Shortest path in unweighted graph              | BFS                |
| Detect a cycle                                  | DFS + parent/path  |
| Find any/all configs satisfying constraints     | Backtracking       |
| Try literally everything, small input          | Exhaustive search  |
| Optimal play in a two-player game              | Minimax + memo     |
| Fast "good enough" by local best choice         | Greedy             |
| Overlapping subproblems + optimal substructure  | Dynamic programming|
| Optimal & sub-results reused, top-down feel      | DP (memoization)   |
| Optimal & you can order the subproblems          | DP (tabulation)    |