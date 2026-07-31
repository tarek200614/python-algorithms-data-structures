# 📊 Complexity Cheatsheet

A comprehensive reference for Big-O time and space complexity of the
algorithms and data structures in this repository.

---

## 🔢 Big-O Notation

Big-O notation describes the **upper bound** of an algorithm's growth rate
as the input size increases. It helps us compare algorithms and understand
how they scale.

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Naive Fibonacci |
| O(n!) | Factorial | Permutations |

### Growth Rate Comparison (from fastest to slowest)

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### Visual Comparison

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 0 | 1 | 2 |
| 10 | 1 | 3 | 10 | 30 | 100 | 1,024 |
| 100 | 1 | 7 | 100 | 664 | 10,000 | 10³⁰ |
| 1000 | 1 | 10 | 1000 | 9,966 | 1,000,000 | 10³⁰¹ |

---

## 🔀 Sorting Comparison

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|---|---|---|---|---|---|---|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |

### When to Use Which?

- **Bubble Sort:** Educational purposes only; never use in production.
- **Insertion Sort:** Small arrays (n < 50) or nearly-sorted data.
- **Merge Sort:** General-purpose, stable sorting; needs O(n) extra space.
- **Quick Sort:** General-purpose, in-place; worst case is rare with good pivots.
- **Heap Sort:** When O(1) space is required and stability doesn't matter.

---

## 🌐 BFS vs DFS

| Property | BFS | DFS |
|---|---|---|
| **Data Structure** | Queue (FIFO) | Stack (LIFO) / Recursion |
| **Traversal Order** | Level by level | Deep first, then backtrack |
| **Time Complexity** | O(V + E) | O(V + E) |
| **Space Complexity** | O(V) | O(V) |
| **Shortest Path (unweighted)** | ✅ Yes | ❌ No |
| **Cycle Detection** | ✅ Yes | ✅ Yes |
| **Topological Sort** | ✅ Yes (Kahn's) | ✅ Yes |
| **Memory Usage** | Higher (wide graphs) | Lower (deep graphs) |
| **Implementation** | Iterative | Recursive or Iterative |

### When to Use BFS?

- Finding the **shortest path** in unweighted graphs.
- **Level-order traversal** of trees.
- Finding all nodes within *k* edges.
- Web crawlers (explore layer by layer).

### When to Use DFS?

- **Topological sorting**.
- Detecting **cycles** in a graph.
- Finding **connected components**.
- Solving **mazes** and puzzles.
- **Path finding** (any path, not shortest).

---

## 🛣️ Dijkstra's Algorithm

| Property | Value |
|---|---|
| **Purpose** | Shortest path from source to all vertices |
| **Data Structure** | Min-heap (priority queue) |
| **Time Complexity** | O((V + E) log V) |
| **Space Complexity** | O(V + E) |
| **Graph Type** | Weighted, non-negative edges |
| **Optimal?** | Yes (for non-negative weights) |

### Dijkstra vs Other Shortest Path Algorithms

| Algorithm | Time Complexity | Handles Negative Weights? | Use Case |
|---|---|---|---|
| **Dijkstra** | O((V + E) log V) | ❌ No | Non-negative weights |
| Bellman-Ford | O(V · E) | ✅ Yes | Negative weights (no cycles) |
| Floyd-Warshall | O(V³) | ✅ Yes | All-pairs shortest path |
| A* Search | O(b^d) | ❌ No | Heuristic-guided search |

### Dijkstra Limitations

- Cannot handle **negative edge weights** (use Bellman-Ford instead).
- Computes shortest paths from **one source** only (use Floyd-Warshall for all-pairs).
- Does not work for **negative cycles**.

---

## 🗂️ Hash Tables

| Operation | Average Case | Worst Case |
|---|---|---|
| **Insert** | O(1) | O(n) |
| **Search** | O(1) | O(n) |
| **Delete** | O(1) | O(n) |
| **Resize** | O(n) | O(n) |

### Collision Resolution Strategies

| Strategy | Description | Pros | Cons |
|---|---|---|---|
| **Separate Chaining** | Linked list per bucket | Simple, handles high load | Extra memory for pointers |
| **Open Addressing** | Probe for empty slot | Cache-friendly | Clustering, deletion complex |
| - Linear Probing | Next slot | Simple | Primary clustering |
| - Quadratic Probing | Quadratic step | Less clustering | Secondary clustering |
| - Double Hashing | Second hash function | Minimal clustering | More computation |

### Load Factor

```
load_factor = number_of_entries / capacity
```

- **Ideal load factor:** 0.6 – 0.75
- **Resize trigger:** When load factor exceeds threshold (default 0.75)
- **Resize strategy:** Double capacity and re-hash all entries

---

## 🔄 Recursion

### Recursion Complexity

| Algorithm | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| **Fibonacci (naive)** | O(2ⁿ) | O(n) | Exponential; recomputes subproblems |
| **Fibonacci (memoized)** | O(n) | O(n) | Caches results; top-down DP |
| **Fibonacci (iterative)** | O(n) | O(1) | Bottom-up DP; most efficient |
| **Tower of Hanoi** | O(2ⁿ) | O(n) | 2ⁿ - 1 moves |
| **Parentheses Generator** | O(4ⁿ/√n) | O(n) | Catalan number of combinations |

### Recursion vs Iteration

| Property | Recursion | Iteration |
|---|---|---|
| **Code Clarity** | Often cleaner | Can be verbose |
| **Memory** | O(n) call stack | O(1) typically |
| **Speed** | Slower (function call overhead) | Faster |
| **Stack Overflow** | Risk for deep recursion | No risk |
| **Tail Recursion** | Optimizable to O(1) space | N/A |

### Dynamic Programming Approaches

| Approach | Direction | Space Optimization |
|---|---|---|
| **Top-Down (Memoization)** | Recursive, caches results | O(n) for memo |
| **Bottom-Up (Tabulation)** | Iterative, fills table | Can optimize to O(1) |

### Catalan Numbers

The number of valid parentheses combinations for n pairs:

```
C(n) = (2n)! / ((n+1)! · n!)

C(0) = 1
C(1) = 1
C(2) = 2
C(3) = 5
C(4) = 14
C(5) = 42
```

---

## 📋 Quick Reference Summary

| Algorithm | Time | Space |
|---|---|---|
| Hash Table (avg) | O(1) | O(n) |
| Tower of Hanoi | O(2ⁿ) | O(n) |
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V + E) |
| Fibonacci (iterative) | O(n) | O(1) |
| Fibonacci (memoized) | O(n) | O(n) |
| Fibonacci (naive) | O(2ⁿ) | O(n) |
| Parentheses Generator | O(4ⁿ/√n) | O(n) |
| Bubble Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |

---

[← Back to Root](../README.md)