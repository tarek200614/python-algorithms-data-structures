"""Hash Table implementation using separate chaining for collision resolution.

A hash table (hash map) maps keys to values using a hash function. This
implementation uses separate chaining (linked lists per bucket) and
automatically resizes when the load factor exceeds a threshold.

Time Complexity (average):
    - Insert: O(1)
    - Search: O(1)
    - Delete: O(1)

Time Complexity (worst):
    - Insert: O(n)
    - Search: O(n)
    - Delete: O(n)

Space Complexity: O(n)

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from typing import Any, Iterator, List, Optional, Tuple


class _Node:
    """A node in a linked list used for separate chaining."""

    __slots__ = ("key", "value", "next")

    def __init__(self, key: Any, value: Any, next_node: Optional["_Node"] = None) -> None:
        """Initialize a new node.

        Args:
            key: The key stored in the node.
            value: The value associated with the key.
            next_node: Reference to the next node in the chain (or None).
        """
        self.key = key
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the node."""
        return f"_Node(key={self.key!r}, value={self.value!r})"


# A unique sentinel object to distinguish "key not found" from a stored None.
_SENTINEL: Any = object()


class HashTable:
    """A hash table with separate chaining and automatic resizing.

    The table starts with a small number of buckets and doubles its capacity
    when the load factor exceeds a configurable threshold (default 0.75).

    Attributes:
        _capacity: The current number of buckets.
        _size: The number of stored key-value pairs.
        _buckets: The list of bucket heads (each a _Node or None).
        _load_factor_threshold: The load factor that triggers a resize.
    """

    def __init__(self, initial_capacity: int = 8, load_factor_threshold: float = 0.75) -> None:
        """Initialize an empty hash table.

        Args:
            initial_capacity: The starting number of buckets. Must be >= 1.
            load_factor_threshold: The load factor that triggers resizing.
                Must be greater than 0.

        Raises:
            ValueError: If initial_capacity is less than 1 or load factor
                threshold is not positive.
        """
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be at least 1")
        if load_factor_threshold <= 0:
            raise ValueError("load_factor_threshold must be positive")

        self._capacity: int = initial_capacity
        self._size: int = 0
        self._buckets: List[Optional[_Node]] = [None] * self._capacity
        self._load_factor_threshold: float = load_factor_threshold

    # ------------------------------------------------------------------
    # Public properties
    # ------------------------------------------------------------------
    @property
    def size(self) -> int:
        """Return the number of key-value pairs stored in the table."""
        return self._size

    @property
    def capacity(self) -> int:
        """Return the current number of buckets."""
        return self._capacity

    @property
    def load_factor(self) -> float:
        """Return the current load factor (size / capacity)."""
        return self._size / self._capacity

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _hash(self, key: Any) -> int:
        """Compute the bucket index for a given key.

        Uses Python's built-in hash() and maps it to the current capacity.

        Args:
            key: The key to hash.

        Returns:
            An integer index in the range [0, capacity).
        """
        # abs() guards against negative hash values returned by hash().
        return abs(hash(key)) % self._capacity

    def _resize(self, new_capacity: int) -> None:
        """Resize the internal bucket array to a new capacity.

        All existing entries are re-hashed and re-inserted into the new
        bucket array.

        Args:
            new_capacity: The new number of buckets. Must be >= 1.
        """
        if new_capacity < 1:
            raise ValueError("new_capacity must be at least 1")

        old_buckets = self._buckets
        self._capacity = new_capacity
        self._buckets = [None] * self._capacity
        self._size = 0  # Reset; insert() will increment it again

        # Re-insert every key-value pair into the new buckets.
        for head in old_buckets:
            current = head
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next

    def _maybe_resize(self) -> None:
        """Double the capacity if the load factor exceeds the threshold."""
        if self.load_factor >= self._load_factor_threshold:
            self._resize(self._capacity * 2)

    # ------------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------------
    def insert(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair in the hash table.

        If the key already exists, its value is updated. Otherwise a new
        entry is created. The table may resize automatically if the load
        factor exceeds the threshold.

        Args:
            key: The key to insert. Must be hashable.
            value: The value to associate with the key.

        Raises:
            TypeError: If the key is not hashable.
        """
        try:
            index = self._hash(key)
        except TypeError as exc:
            raise TypeError(f"Key {key!r} is not hashable") from exc

        bucket = self._buckets[index]

        # Check if the key already exists in the chain; update if so.
        current = bucket
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Key not found: insert a new node at the head of the chain.
        new_node = _Node(key, value, bucket)
        self._buckets[index] = new_node
        self._size += 1

        # Resize if needed to keep operations efficient.
        self._maybe_resize()

    def get(self, key: Any, default: Any = None) -> Any:
        """Retrieve the value associated with a key.

        Args:
            key: The key to look up.
            default: The value to return if the key is not found.

        Returns:
            The value associated with the key, or `default` if not found.

        Raises:
            TypeError: If the key is not hashable.
        """
        try:
            index = self._hash(key)
        except TypeError as exc:
            raise TypeError(f"Key {key!r} is not hashable") from exc

        current = self._buckets[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return default

    def delete(self, key: Any) -> bool:
        """Remove a key-value pair from the hash table.

        Args:
            key: The key to remove.

        Returns:
            True if the key was found and removed, False otherwise.

        Raises:
            TypeError: If the key is not hashable.
        """
        try:
            index = self._hash(key)
        except TypeError as exc:
            raise TypeError(f"Key {key!r} is not hashable") from exc

        current = self._buckets[index]
        prev: Optional[_Node] = None

        while current is not None:
            if current.key == key:
                # Remove the node from the linked list.
                if prev is None:
                    # The node is the head of the chain.
                    self._buckets[index] = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return True
            prev = current
            current = current.next

        return False

    def contains(self, key: Any) -> bool:
        """Check whether a key exists in the hash table.

        Args:
            key: The key to check.

        Returns:
            True if the key exists, False otherwise.
        """
        return self.get(key, _SENTINEL) is not _SENTINEL

    def keys(self) -> Iterator[Any]:
        """Iterate over all keys in the hash table.

        Yields:
            Each stored key. Order is not guaranteed.
        """
        for bucket in self._buckets:
            current = bucket
            while current is not None:
                yield current.key
                current = current.next

    def values(self) -> Iterator[Any]:
        """Iterate over all values in the hash table.

        Yields:
            Each stored value. Order is not guaranteed.
        """
        for bucket in self._buckets:
            current = bucket
            while current is not None:
                yield current.value
                current = current.next

    def items(self) -> Iterator[Tuple[Any, Any]]:
        """Iterate over all (key, value) pairs in the hash table.

        Yields:
            Tuples of (key, value). Order is not guaranteed.
        """
        for bucket in self._buckets:
            current = bucket
            while current is not None:
                yield (current.key, current.value)
                current = current.next

    def clear(self) -> None:
        """Remove all key-value pairs from the hash table."""
        self._buckets = [None] * self._capacity
        self._size = 0

    # ------------------------------------------------------------------
    # Dunder methods for dict-like usage
    # ------------------------------------------------------------------
    def __setitem__(self, key: Any, value: Any) -> None:
        """Support `table[key] = value` syntax."""
        self.insert(key, value)

    def __getitem__(self, key: Any) -> Any:
        """Support `value = table[key]` syntax.

        Raises:
            KeyError: If the key is not found.
        """
        result = self.get(key, _SENTINEL)
        if result is _SENTINEL:
            raise KeyError(key)
        return result

    def __delitem__(self, key: Any) -> None:
        """Support `del table[key]` syntax.

        Raises:
            KeyError: If the key is not found.
        """
        if not self.delete(key):
            raise KeyError(key)

    def __contains__(self, key: Any) -> bool:
        """Support `key in table` syntax."""
        return self.contains(key)

    def __len__(self) -> int:
        """Return the number of stored pairs."""
        return self._size

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        items_str = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"HashTable({{{items_str}}})"

    def __iter__(self) -> Iterator[Any]:
        """Iterate over keys (like a dict)."""
        return self.keys()


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the HashTable class."""
    print("=== Hash Table Example ===\n")

    # Create a new hash table.
    table = HashTable(initial_capacity=4)

    # Insert some key-value pairs.
    table.insert("name", "Alice")
    table.insert("age", 30)
    table.insert("city", "Lagos")
    table["email"] = "alice@example.com"  # dict-like syntax

    print(f"Table size: {len(table)}")
    print(f"Name: {table.get('name')}")
    print(f"Age: {table['age']}")  # dict-like access

    # Update an existing key.
    table.insert("age", 31)
    print(f"Updated age: {table['age']}")

    # Check membership.
    print(f"'city' in table: {'city' in table}")
    print(f"'phone' in table: {'phone' in table}")

    # Iterate over items.
    print("\nAll items:")
    for key, value in table.items():
        print(f"  {key}: {value}")

    # Delete a key.
    deleted = table.delete("city")
    print(f"\nDeleted 'city': {deleted}")
    print(f"'city' in table after delete: {'city' in table}")

    # Show the load factor and capacity (may have resized).
    print(f"\nCapacity: {table.capacity}")
    print(f"Size: {table.size}")
    print(f"Load factor: {table.load_factor:.2f}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()