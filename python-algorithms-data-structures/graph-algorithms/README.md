# 🌐 Graph Algorithms

<div align="center">

![Graph Algorithms](https://img.shields.io/badge/Topic-Graph%20Algorithms-blue?style=for-the-badge)
![Complexity](https://img.shields.io/badge/Time-O(V+E)-success?style=for-the-badge)

</div>

---

## 📌 Purpose

This folder contains three fundamental **graph algorithms**:

| Algorithm | File | Purpose |
|---|---|---|
| **BFS** | [`bfs.py`](bfs.py) | Level-order traversal, shortest path in unweighted graphs |
| **DFS** | [`dfs.py`](dfs.py) | Deep traversal, cycle detection, topological sort |
| **Dijkstra** | [`dijkstra.py`](dijkstra.py) | Shortest path in weighted graphs (non-negative weights) |

---

## 📚 Theory

### Graph Representation

All algorithms use an **adjacency list** representation:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    ...
}
```

For weighted graphs (Dijkstra), each entry is a list of `(neighbor, weight)` tuples:

```python
graph = {
    "A": [("B", 4), ("C", 2)],
    ...
}
```

### BFS (Breadth-First Search)

Explores vertices **level by level** using a **queue** (FIFO). Visits all
neighbors of a vertex before moving deeper. Guarantees the shortest path
in **unweighted** graphs.

### DFS (Depth-First Search)

Explores as **deep as possible** along each branch before backtracking,
using a **stack** (LIFO) or recursion. Useful for cycle detection,
topological sorting, and finding connected components.

### Dijkstra's Algorithm

Finds the **shortest path** from a source to all vertices in a **weighted**
graph with non-negative weights. Uses a **priority queue** (min-heap) to
always process the vertex with the smallest known distance.

---

## 🔧 Algorithm Explanations

### BFS

```
1. Enqueue the start vertex, mark as visited
2. While queue is not empty:
   a. Dequeue a vertex
   b. For each unvisited neighbor:
      - Mark as visited
      - Enqueue it
```

### DFS

```
1. Push start vertex onto stack, mark as visited
2. While stack is not empty:
   a. Pop a vertex
   b. For each unvisited neighbor:
      - Mark as visited
      - Push onto stack
```

### Dijkstra

```
1. Set distance to source = 0, all others = infinity
2. Push (0, source) onto priority queue
3. While queue is not empty:
   a. Pop vertex with smallest distance
   b. For each neighbor:
      - If new distance < current distance:
        - Update distance
        - Push (new_distance, neighbor) onto queue
```

---

## ⏱️ Time Complexity

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V + E) |

---

## 💾 Space Complexity

- **BFS/DFS:** O(V) for the visited set and queue/stack.
- **Dijkstra:** O(V + E) for distances, priority queue, and graph storage.

---

## 📝 Example

```python
from bfs import bfs_traverse, bfs_shortest_path
from dfs import dfs_traverse_recursive, dfs_detect_cycle
from dijkstra import dijkstra, dijkstra_shortest_path

graph = {
    "A": ["B", "C"], "B": ["A", "D", "E"],
    "C": ["A", "F"], "D": ["B"], "E": ["B", "F"], "F": ["C", "E"],
}

print(bfs_traverse(graph, "A"))          # ['A', 'B', 'C', 'D', 'E', 'F']
print(bfs_shortest_path(graph, "A", "F")) # ['A', 'C', 'F']
print(dfs_traverse_recursive(graph, "A")) # ['A', 'B', 'D', 'E', 'F', 'C']

weighted = {"A": [("B", 4), ("C", 2)], "B": [("C", 1), ("D", 5)],
            "C": [("B", 1), ("D", 8), ("E", 10)], "D": [("E", 2)], "E": []}
print(dijkstra(weighted, "A"))  # {'A': 0, 'B': 3, 'C': 2, 'D': 8, 'E': 10}
```

---

## ▶️ How to Run

```bash
cd graph-algorithms
python bfs.py
python dfs.py
python dijkstra.py
```

---

## 📊 Diagrams

- BFS: [`../assets/diagrams/bfs.svg`](../assets/diagrams/bfs.svg)
- DFS: [`../assets/diagrams/dfs.svg`](../assets/diagrams/dfs.svg)
- Dijkstra: [`../assets/diagrams/dijkstra.svg`](../assets/diagrams/dijkstra.svg)

## 📸 Screenshots

- ![BFS Demo](screenshots/bfs_demo.png)
- ![DFS Demo](screenshots/dfs_demo.png)
- ![Dijkstra Demo](screenshots/dijkstra_demo.png)

---

[← Back to Root](../README.md)
