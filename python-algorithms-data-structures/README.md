# 🐍 Python Algorithms & Data Structures

A curated, professional collection of classic algorithms and data structures implemented in clean, well-documented Python — built for learning, interviewing, and reference.

---

## 📖 Description

This repository contains from-scratch, dependency-free Python implementations of foundational computer science algorithms and data structures. Each module is self-contained, thoroughly documented, and includes complexity analysis, example usage, and expected output — making it suitable both as a study resource and as a portfolio piece.

---

## ✨ Features

- Clean, PEP 8–compliant Python code with type hints
- Docstrings and beginner-friendly inline comments on every function
- Time and space complexity documented for every algorithm
- Independent, runnable example usage in every file
- Dedicated README per module with theory and step-by-step explanations
- Custom SVG diagrams and icons (no external image dependencies)
- Zero third-party dependencies — pure Python standard library

---

## 🗂️ Repository Structure

```text
python-algorithms-data-structures/
│
├── README.md
├── LICENSE
│
├── assets/
│   ├── icons/
│   ├── screenshots/
│   └── diagrams/
│
├── docs/
│   ├── project-structure.txt
│   └── complexity-cheatsheet.md
│
├── hash-table/
├── tower-of-hanoi/
├── graph-algorithms/
├── recursion/
└── sorting/
```

See [`docs/project-structure.txt`](docs/project-structure.txt) for the full annotated tree.

---

## 🧮 Algorithm List

| Category | Module | Files |
|---|---|---|
| Data Structures | Hash Table | `hash-table/hash_table.py` |
| Recursion | Tower of Hanoi | `tower-of-hanoi/tower_of_hanoi.py` |
| Graph Algorithms | Breadth-First Search | `graph-algorithms/bfs.py` |
| Graph Algorithms | Depth-First Search | `graph-algorithms/dfs.py` |
| Graph Algorithms | Dijkstra's Algorithm | `graph-algorithms/dijkstra.py` |
| Recursion | Fibonacci (naive + memoized) | `recursion/fibonacci.py` |
| Recursion | Parentheses Generator | `recursion/parentheses_generator.py` |
| Sorting | Bubble Sort | `sorting/bubble_sort.py` |
| Sorting | Insertion Sort | `sorting/insertion_sort.py` |

---

## ⏱️ Complexity Overview

| Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space |
|---|---|---|---|---|
| Hash Table (avg case) | O(1) | O(1) | O(n) | O(n) |
| Tower of Hanoi | O(2^n) | O(2^n) | O(2^n) | O(n) |
| BFS | O(V + E) | O(V + E) | O(V + E) | O(V) |
| DFS | O(V + E) | O(V + E) | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V+E) log V) | O((V+E) log V) | O((V+E) log V) | O(V) |
| Fibonacci (memoized) | O(n) | O(n) | O(n) | O(n) |
| Parentheses Generator | O(4^n / √n) | O(4^n / √n) | O(4^n / √n) | O(n) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

A full reference is available in [`docs/complexity-cheatsheet.md`](docs/complexity-cheatsheet.md).

---

## 🛠️ Technologies

- **Language:** Python 3.10+
- **Standard Library Only:** no external dependencies
- **Documentation:** Markdown
- **Diagrams:** hand-authored SVG

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/python-algorithms-data-structures.git
cd python-algorithms-data-structures
```

No package installation is required — every script runs with a standard Python 3 interpreter.

---

## ▶️ Usage

Each algorithm can be run independently:

```bash
python3 sorting/bubble_sort.py
python3 graph-algorithms/dijkstra.py
python3 recursion/fibonacci.py
```

Every file includes an example usage block under `if __name__ == "__main__":` that demonstrates the algorithm with sample data and prints the result.

---

## 🎓 Learning Outcomes

By studying and running this repository, you will:

- Understand the mechanics and trade-offs of classic sorting algorithms
- Learn how graph traversal (BFS/DFS) and shortest-path algorithms (Dijkstra) work
- Practice recursive problem-solving through Tower of Hanoi and Fibonacci
- Understand hash table internals, including collision handling
- Build intuition for Big-O time and space complexity analysis

---

## 👤 Author

Maintained as a personal algorithms & data structures reference/portfolio project.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
