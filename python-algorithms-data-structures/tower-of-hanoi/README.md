# 🗼 Tower of Hanoi

<div align="center">

![Tower of Hanoi](https://img.shields.io/badge/Problem-Tower%20of%20Hanoi-orange?style=for-the-badge)
![Complexity](https://img.shields.io/badge/Time-O(2ⁿ)-red?style=for-the-badge)

</div>

---

## 📌 Purpose

The **Tower of Hanoi** is a classic mathematical puzzle that demonstrates
the power of **recursion**. Given three rods and *n* disks of different
sizes, the goal is to move all disks from the source rod to the destination
rod following these rules:

1. **Only one disk** may be moved at a time.
2. A move consists of taking the **top disk** from one rod and placing it on another.
3. **No disk** may be placed on top of a smaller disk.

---

## 📚 Theory

### The Recursive Insight

To move *n* disks from the source rod to the destination rod:

1. Move the top *n-1* disks from the **source** to the **auxiliary** rod.
2. Move the **largest disk** from the **source** to the **destination** rod.
3. Move the *n-1* disks from the **auxiliary** to the **destination** rod.

The base case is *n = 0* (nothing to move).

### Minimum Number of Moves

The minimum number of moves required is: **2ⁿ - 1**

| Disks (n) | Minimum Moves |
|---|---|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 5 | 31 |
| 10 | 1,023 |
| 20 | 1,048,575 |

---

## 🔧 Algorithm Explanation

```
function hanoi(n, source, auxiliary, destination):
    if n == 0:
        return
    hanoi(n-1, source, destination, auxiliary)   # Step 1
    move disk n from source to destination        # Step 2
    hanoi(n-1, auxiliary, source, destination)   # Step 3
```

- **Step 1:** Move n-1 disks from source to auxiliary (using destination as temp).
- **Step 2:** Move the largest disk directly to the destination.
- **Step 3:** Move n-1 disks from auxiliary to destination (using source as temp).

---

## ⏱️ Time Complexity

**O(2ⁿ)** — The number of moves is exactly 2ⁿ - 1, which is exponential.

---

## 💾 Space Complexity

**O(n)** — The maximum recursion depth is *n* (one stack frame per disk level).

---

## 📝 Example

```python
from tower_of_hanoi import hanoi_recursive, hanoi_count_moves

# Solve for 3 disks
moves = hanoi_recursive(3, source="A", auxiliary="B", destination="C")

for i, move in enumerate(moves, 1):
    print(f"{i}. {move}")

print(f"\nTotal moves: {len(moves)}")
print(f"Minimum moves: {hanoi_count_moves(3)}")
```

### Output

```
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. Move disk 3 from A to C
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

Total moves: 7
Minimum moves: 7
```

---

## ▶️ How to Run

```bash
cd tower-of-hanoi
python tower_of_hanoi.py
```

---

## 📊 Diagram

See the Tower of Hanoi diagram: [`../assets/diagrams/tower-of-hanoi.svg`](../assets/diagrams/tower-of-hanoi.svg)

## 📸 Screenshot

![Tower of Hanoi Demo](screenshots/tower_of_hanoi_demo.png)

---

[← Back to Root](../README.md)
