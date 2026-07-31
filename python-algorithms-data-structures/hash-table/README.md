# 🗂️ Hash Table

<div align="center">

![Hash Table](https://img.shields.io/badge/Data%20Structure-Hash%20Table-blueviolet?style=for-the-badge)
![Complexity](https://img.shields.io/badge/Average-O(1)-success?style=for-the-badge)

</div>

---

## 📌 Purpose

A **hash table** (also called a hash map) is a data structure that maps
**keys** to **values** using a **hash function**. It provides near-constant-time
average-case performance for insertions, lookups, and deletions, making it
one of the most widely used data structures in computer science.

This implementation uses **separate chaining** (linked lists per bucket)
to handle collisions and **automatic resizing** to maintain efficiency as
the number of entries grows.

---

## 📚 Theory

### How Hash Tables Work

1. **Hash Function:** A function that takes a key and produces an integer
   (the hash code). Python's built-in `hash()` function is used.

2. **Index Mapping:** The hash code is mapped to a bucket index using the
   modulo operation: `index = hash(key) % capacity`.

3. **Storage:** Each bucket holds a linked list of key-value pairs. If
   multiple keys map to the same bucket (a **collision**), they are stored
   in the same linked list.

4. **Load Factor:** The ratio `size / capacity`. When it exceeds a threshold
   (default 0.75), the table **resizes** (doubles capacity) and re-hashes
   all entries to keep operations efficient.

### Collision Resolution: Separate Chaining

When two different keys hash to the same bucket index, a **collision** occurs.
This implementation resolves collisions using **separate chaining**:

- Each bucket is the head of a linked list.
- On insert, if the bucket is occupied, the new node is prepended to the chain.
- On lookup, the chain is traversed to find the matching key.

---

## 🔧 Algorithm Explanation

### Insert (key, value)

```
1. Compute index = hash(key) % capacity
2. Traverse the linked list at that index
3. If key exists → update its value
4. If key doesn't exist → prepend a new node to the list
5. Increment size
6. If load factor ≥ threshold → resize (double capacity)
```

### Get (key)

```
1. Compute index = hash(key) % capacity
2. Traverse the linked list at that index
3. If key found → return its value
4. If key not found → return default (or None)
```

### Delete (key)

```
1. Compute index = hash(key) % capacity
2. Traverse the linked list at that index
3. If key found → remove the node from the list, decrement size
4. If key not found → return False
```

---

## ⏱️ Time Complexity

| Operation | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Insert | O(1) | O(1) | O(n) |
| Search | O(1) | O(1) | O(n) |
| Delete | O(1) | O(1) | O(n) |

- **Best/Average case:** When the hash function distributes keys uniformly,
  each bucket has O(1) elements.
- **Worst case:** When all keys hash to the same bucket, the linked list
  has n elements, degrading to O(n).

---

## 💾 Space Complexity

**O(n)** — where n is the number of key-value pairs stored. The bucket
array also uses O(capacity) space, but capacity is proportional to n due
to automatic resizing.

---

## 📝 Example

```python
from hash_table import HashTable

# Create a hash table
table = HashTable(initial_capacity=4)

# Insert key-value pairs
table.insert("name", "Alice")
table.insert("age", 30)
table["city"] = "Lagos"  # dict-like syntax

# Retrieve values
print(table.get("name"))   # Output: Alice
print(table["age"])        # Output: 30

# Check membership
print("city" in table)     # Output: True

# Delete a key
table.delete("city")
print("city" in table)     # Output: False

# Iterate over items
for key, value in table.items():
    print(f"{key}: {value}")
```

---

## ▶️ How to Run

```bash
# Navigate to the hash-table directory
cd hash-table

# Run the example
python hash_table.py
```

### Expected Output

```
=== Hash Table Example ===

Table size: 4
Name: Alice
Age: 30
Updated age: 31
'city' in table: True
'phone' in table: False

All items:
  name: Alice
  age: 31
  city: Lagos
  email: alice@example.com

Deleted 'city': True
'city' in table after delete: False

Capacity: 8
Size: 3
Load factor: 0.38

=== End of Example ===
```

---

## 📊 Diagram

See the hash table diagram: [`../assets/diagrams/hash-table.svg`](../assets/diagrams/hash-table.svg)

---

[← Back to Root](../README.md)