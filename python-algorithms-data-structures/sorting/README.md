# 🔢 Sorting Algorithms

<div align="center">

![Sorting](https://img.shields.io/badge/Topic-Sorting-green?style=for-the-badge)
![Complexity](https://img.shields.io/badge/Worst-O(n²)-red?style=for-the-badge)

</div>

---

## 📌 Purpose

This folder contains classic **comparison-based sorting algorithms**.
These are fundamental algorithms every programmer should understand.

| Algorithm | File | Purpose |
|---|---|---|
| **Bubble Sort** | [`bubble_sort.py`](bubble_sort.py) | Simplest sorting algorithm; educational |
| **Insertion Sort** | [`insertion_sort.py`](insertion_sort.py) | Efficient for small/nearly-sorted data |

---

## 📚 Theory

### Bubble Sort

Repeatedly steps through the list, compares adjacent elements, and swaps
them if they're in the wrong order. Larger elements "bubble" to the end.
Includes an optimization: if no swaps occur in a pass, the list is sorted.

### Insertion Sort

Builds the sorted list one element at a time. Takes each element and
inserts it into its correct position among already-sorted elements,
shifting larger elements to the right. Similar to sorting playing cards.

---

## 🔧 Algorithm Explanations

### Bubble Sort

```
for i in range(n-1):
    swapped = False
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            swap(arr[j], arr[j+1])
            swapped = True
    if not swapped:
        break  # already sorted
```

### Insertion Sort

```
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
```

---

## ⏱️ Time Complexity

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |

---

## 💾 Space Complexity

Both algorithms are **in-place** sorting algorithms with **O(1)** auxiliary
space. They do not require additional memory proportional to the input size.

---

## 📝 Example

```python
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

data = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(data.copy()))     # [11, 12, 22, 25, 34, 64, 90]
print(insertion_sort(data.copy()))  # [11, 12, 22, 25, 34, 64, 90]
```

---

## ▶️ How to Run

```bash
cd sorting
python bubble_sort.py
python insertion_sort.py
```

---

## 📊 Diagrams

- Bubble Sort: [`../assets/diagrams/bubble-sort.svg`](../assets/diagrams/bubble-sort.svg)
- Insertion Sort: [`../assets/diagrams/insertion-sort.svg`](../assets/diagrams/insertion-sort.svg)

---

[← Back to Root](../README.md)