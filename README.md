# 🐍 Python Algorithms & Data Structures

<div align="center">

<h3>A Modern Collection of Algorithms & Data Structures in Python</h3>

<p>
Clean • Documented • Beginner-Friendly • Interview Ready • Production Quality
</p>

<p>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-blue?style=for-the-badge)
![Type Hints](https://img.shields.io/badge/Type%20Hints-Enabled-success?style=for-the-badge)
![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen?style=for-the-badge)
![Algorithms](https://img.shields.io/badge/Algorithms-Classic-orange?style=for-the-badge)

</p>

<p>

A carefully crafted educational repository containing **classic algorithms and data structures** implemented in modern Python with clean architecture, detailed documentation, complexity analysis, and beginner-friendly explanations.

Designed for students, self-learners, coding interview preparation, university coursework, and developers who want to strengthen their understanding of Computer Science fundamentals.

</p>

</div>

---

# 📚 Table of Contents

- [Overview](#-overview)
- [Why This Repository?](#-why-this-repository)
- [Features](#-features)
- [Repository Structure](#-repository-structure)
- [Algorithms Included](#-algorithms-included)
- [Algorithm Categories](#-algorithm-categories)
- [Project Highlights](#-project-highlights)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Repository Architecture](#-repository-architecture)
- [Complexity Cheat Sheet](#-complexity-cheat-sheet)
- [Learning Roadmap](#-learning-roadmap)
- [Technologies](#-technologies)
- [Coding Standards](#-coding-standards)
- [Future Roadmap](#-future-roadmap)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

# 📖 Overview

Algorithms and Data Structures are among the most important concepts in Computer Science.

Whether you're preparing for coding interviews, studying at university, building software professionally, or simply learning Python, understanding these concepts is essential.

This repository provides a structured collection of classic algorithms implemented with a strong focus on:

- readability
- correctness
- maintainability
- documentation
- educational value

Every implementation is written from scratch without unnecessary dependencies, allowing readers to fully understand how each algorithm works internally.

Unlike repositories that only provide code, this project explains the theory behind every algorithm, discusses its complexity, demonstrates practical usage, and includes visual documentation wherever appropriate.

---

# 🎯 Why This Repository?

Many algorithm repositories suffer from one or more of these problems:

- difficult to understand
- poor documentation
- inconsistent coding style
- missing complexity analysis
- little explanation of algorithm behavior

This project solves those problems by providing:

✅ Production-quality Python code

✅ Detailed documentation

✅ Clear comments

✅ Type hints

✅ Input validation

✅ Independent executable examples

✅ Consistent project organization

✅ Professional GitHub structure

The goal is not only to provide working implementations but also to serve as a long-term learning resource.

---

# ✨ Features

| Feature | Description |
|----------|-------------|
| 📘 Educational | Every algorithm is explained with detailed documentation and examples |
| 🐍 Modern Python | Written using Python 3.8+ best practices |
| 📐 Type Safe | Comprehensive type hints throughout the project |
| 📚 Fully Documented | Rich docstrings, Markdown guides, and SVG diagrams |
| 🛡 Robust | Input validation and meaningful error handling |
| 🚀 Ready to Run | Every algorithm can be executed independently |
| 📊 Complexity Analysis | Time and space complexity included everywhere |
| 🧩 Modular | Each algorithm is organized into its own folder |
| 🎯 Beginner Friendly | Designed for learners with extensive explanations |
| 💼 Portfolio Ready | Repository structure suitable for GitHub portfolios |

---

# 📁 Repository Structure

```text
python-algorithms-data-structures/
│
├── README.md
├── LICENSE
│
├── assets/
│   ├── diagrams/
│   ├── icons/
│   └── screenshots/
│
├── docs/
│   ├── project-structure.txt
│   └── complexity-cheatsheet.md
│
├── hash-table/
│   ├── hash_table.py
│   ├── README.md
│   └── screenshots/
│
├── tower-of-hanoi/
│   ├── tower_of_hanoi.py
│   ├── README.md
│   └── screenshots/
│
├── graph-algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   └── README.md
│
├── recursion/
│   ├── fibonacci.py
│   ├── parentheses_generator.py
│   └── README.md
│
└── sorting/
    ├── bubble_sort.py
    ├── insertion_sort.py
    └── README.md
```

---

# 🏗 Repository Architecture

```
Algorithms
│
├── Data Structures
│     └── Hash Table
│
├── Graph Algorithms
│     ├── BFS
│     ├── DFS
│     └── Dijkstra
│
├── Recursion
│     ├── Fibonacci
│     └── Parentheses Generator
│
└── Sorting
      ├── Bubble Sort
      └── Insertion Sort
```

Every algorithm is isolated in its own module, making the repository easy to navigate, extend, and maintain.

Additional documentation is stored in the **docs** directory, while visual resources are located inside **assets**.

---

# 🧠 Algorithms Included

| Category | Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|-----------|------------|-----------------|-----------------|
| Data Structure | Hash Table | ⭐⭐⭐ | O(1) Average | O(n) |
| Recursion | Tower of Hanoi | ⭐⭐ | O(2ⁿ) | O(n) |
| Graph | Breadth-First Search | ⭐⭐ | O(V + E) | O(V) |
| Graph | Depth-First Search | ⭐⭐ | O(V + E) | O(V) |
| Graph | Dijkstra | ⭐⭐⭐⭐ | O((V + E) log V) | O(V + E) |
| Recursion | Fibonacci | ⭐ | O(n) → O(2ⁿ) | O(1) → O(n) |
| Backtracking | Parentheses Generator | ⭐⭐⭐ | O(4ⁿ / √n) | O(n) |
| Sorting | Bubble Sort | ⭐ | O(n²) | O(1) |
| Sorting | Insertion Sort | ⭐⭐ | O(n²) | O(1) |

---

# 📂 Algorithm Categories

## 📦 Data Structures

### Hash Table

Implementation using **Separate Chaining** with automatic resizing based on load factor.

Features:

- Insert
- Search
- Delete
- Resize
- Collision Handling

---

## 🔄 Recursive Algorithms

### Tower of Hanoi

Recursive puzzle demonstrating divide-and-conquer principles.

### Fibonacci

Includes multiple implementations:

- Recursive
- Memoized
- Iterative

allowing performance comparisons.

### Parentheses Generator

Classic backtracking problem demonstrating recursive tree exploration.

---

## 🌐 Graph Algorithms

### Breadth-First Search (BFS)

Used for:

- shortest path in unweighted graphs
- level-order traversal
- graph exploration

---

### Depth-First Search (DFS)

Used for:

- graph traversal
- connected components
- cycle detection
- topological concepts

---

### Dijkstra's Algorithm

Computes shortest paths in weighted graphs using a priority queue.

Ideal for:

- routing
- maps
- networking
- path planning

---

## 🔃 Sorting Algorithms

### Bubble Sort

Simple comparison-based sorting algorithm primarily used for educational purposes.

### Insertion Sort

Efficient for:

- nearly sorted data
- small datasets
- incremental sorting

---

# 🚀 Project Highlights

✔ Clean Architecture

✔ PEP 8 Compliant

✔ Fully Documented

✔ Independent Modules

✔ Beginner Friendly

✔ Production Quality

✔ Type Hints

✔ Complexity Analysis

✔ Error Handling

✔ SVG Documentation

---

# 📥 Installation

## Requirements

- Python 3.8+
- No external dependencies

Clone the repository:

```bash
git clone https://github.com/your-username/python-algorithms-data-structures.git

cd python-algorithms-data-structures
```

Verify your installation:

```bash
python --version
```

Expected output:

```text
Python 3.8+
```

---

# ⚡ Quick Start

Run any algorithm independently.

```bash
python hash-table/hash_table.py
```

```bash
python tower-of-hanoi/tower_of_hanoi.py
```

```bash
python graph-algorithms/bfs.py
```

```bash
python graph-algorithms/dfs.py
```

```bash
python graph-algorithms/dijkstra.py
```

```bash
python recursion/fibonacci.py
```

```bash
python recursion/parentheses_generator.py
```

```bash
python sorting/bubble_sort.py
```

```bash
python sorting/insertion_sort.py
```

---

# 💻 Example Usage

```python
from hash_table import HashTable

table = HashTable()

table.insert("language", "Python")

table.insert("year", 1991)

print(table.get("language"))

print(table.get("year"))
```

Output

```text
Python

1991
```

---

# 📊 Complexity Cheat Sheet

| Algorithm | Best | Average | Worst | Space |
|------------|------|---------|--------|--------|
| Hash Table (Insert/Search/Delete) | O(1) | O(1) | O(n) | O(n) |
| Tower of Hanoi | O(2ⁿ) | O(2ⁿ) | O(2ⁿ) | O(n) |
| Breadth-First Search (BFS) | O(V + E) | O(V + E) | O(V + E) | O(V) |
| Depth-First Search (DFS) | O(V + E) | O(V + E) | O(V + E) | O(V) |
| Dijkstra's Algorithm | O((V + E) log V) | O((V + E) log V) | O((V + E) log V) | O(V + E) |
| Fibonacci (Iterative) | O(n) | O(n) | O(n) | O(1) |
| Fibonacci (Memoization) | O(n) | O(n) | O(n) | O(n) |
| Fibonacci (Recursive) | O(2ⁿ) | O(2ⁿ) | O(2ⁿ) | O(n) |
| Parentheses Generator | O(4ⁿ / √n) | O(4ⁿ / √n) | O(4ⁿ / √n) | O(n) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

---

# 📈 Learning Roadmap

If you're new to algorithms, following the topics in the right order will help you build a solid understanding of Computer Science fundamentals.

### Phase 1 — Foundations

- Python basics
- Variables and data types
- Functions
- Loops
- Lists
- Dictionaries

---

### Phase 2 — Algorithm Analysis

Learn to measure performance using:

- Time Complexity
- Space Complexity
- Big-O Notation

Understand the difference between:

- Constant Time
- Linear Time
- Logarithmic Time
- Quadratic Time
- Exponential Time

---

### Phase 3 — Recursion

Study:

- Recursive thinking
- Base cases
- Recursive trees
- Stack frames

Practice with:

- Fibonacci
- Tower of Hanoi
- Parentheses Generator

---

### Phase 4 — Data Structures

Learn:

- Hash Tables
- Collision Resolution
- Load Factor
- Dynamic Resizing

---

### Phase 5 — Graph Algorithms

Continue with:

- Graph representation
- BFS
- DFS
- Shortest Path
- Weighted Graphs

---

### Phase 6 — Sorting

Understand:

- Stable vs Unstable Sorting
- In-place Algorithms
- Comparison-based Sorting
- Best, Average, Worst Cases

Practice:

- Bubble Sort
- Insertion Sort

---

### Phase 7 — Continue Your Journey

Recommended next topics:

- Merge Sort
- Quick Sort
- Heap Sort
- Binary Search
- Binary Search Trees
- AVL Trees
- Red-Black Trees
- Trie
- Heap
- Segment Tree
- Fenwick Tree
- Union Find (Disjoint Set)
- Dynamic Programming
- Greedy Algorithms
- Topological Sorting
- Bellman-Ford
- Floyd-Warshall
- Prim's Algorithm
- Kruskal's Algorithm
- A* Search
- KMP String Matching
- Rabin-Karp
- Boyer-Moore

---

# 🛠 Technologies

| Category | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| Documentation | Markdown |
| Diagrams | SVG |
| Version Control | Git |
| Repository Hosting | GitHub |
| Coding Standard | PEP 8 |
| Type Checking | Python Type Hints |
| Development Style | Modular Programming |

---

# 📐 Coding Standards

Every implementation in this repository follows a consistent development philosophy.

## Code Quality

- Clean and readable code
- Meaningful variable names
- Modular functions
- Separation of responsibilities

## Documentation

Every algorithm includes:

- Detailed docstrings
- Usage examples
- Complexity analysis
- Theory explanation

## Error Handling

Programs validate inputs whenever appropriate and raise meaningful exceptions instead of failing silently.

## Python Best Practices

- PEP 8 formatting
- Type hints
- Standard library only
- No unnecessary dependencies

---

# 🎯 Skills You'll Gain

Working through this repository will help you develop practical skills in:

- Designing efficient algorithms
- Understanding computational complexity
- Choosing appropriate data structures
- Writing clean Python code
- Debugging recursive algorithms
- Solving graph problems
- Implementing search techniques
- Building reusable software components
- Improving problem-solving abilities
- Preparing for technical interviews

---

# 🗺 Future Roadmap

This repository is intended to grow over time.

Planned additions include:

### Sorting

- Merge Sort
- Quick Sort
- Heap Sort
- Counting Sort
- Radix Sort
- Shell Sort

### Trees

- Binary Search Tree
- AVL Tree
- Red-Black Tree
- B Tree
- B+ Tree

### Heaps

- Min Heap
- Max Heap
- Priority Queue

### Graph Algorithms

- Bellman-Ford
- Floyd-Warshall
- Prim
- Kruskal
- Topological Sort
- Strongly Connected Components
- Minimum Spanning Tree
- A* Pathfinding

### Dynamic Programming

- Knapsack
- Longest Common Subsequence
- Coin Change
- Matrix Chain Multiplication

### Advanced Data Structures

- Trie
- Segment Tree
- Fenwick Tree
- Bloom Filter
- Union Find

### String Algorithms

- KMP
- Rabin-Karp
- Boyer-Moore
- Z Algorithm

---

# 🤝 Contributing

Contributions are welcome and appreciated.

If you'd like to improve this repository:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit with descriptive messages.
5. Open a Pull Request.

Please ensure that new contributions:

- follow PEP 8
- include documentation
- include complexity analysis
- include usage examples
- maintain the existing project structure

---

# 💡 Support

If you find this project useful:

⭐ Star the repository

🍴 Fork the repository

🐛 Report bugs through GitHub Issues

💬 Suggest new algorithms or improvements

Sharing the project with others also helps it grow and benefits the learning community.

---

# 👨‍💻 Author

**MEGHARI Abderrahmane Tarek**

Computer Science & AI Student passionate about:

- Artificial Intelligence
- Software Engineering
- Algorithms & Data Structures
- Open Source
- Python Development

**Connect with me**

- GitHub: `https://github.com/tarek200614`
- LinkedIn: `https://www.linkedin.com/in/abderrahmane-tarek-meghari`
- Email: `meghariabderrhmanetarek@gmail.com`



---

# 📄 License

This project is distributed under the **MIT License**.

You are free to:

- Use
- Modify
- Study
- Distribute

the source code, provided that the original license is included.

For complete details, see the [LICENSE](LICENSE) file.

---

# 🙏 Acknowledgements

This repository was created as an educational resource inspired by fundamental Computer Science concepts taught in universities, technical interviews, and open-source communities.

Special thanks to everyone who contributes to the Python ecosystem and the open-source community for making learning accessible to developers around the world.

---

<div align="center">

## ⭐ Enjoyed this project?

If this repository helped you learn something new, consider supporting it by giving it a **Star** on GitHub.

It helps other learners discover the project and motivates future improvements.

**Happy Coding! 🚀**

Made with ❤️ using **Python** and a passion for learning Computer Science.

</div>
