"""Insertion Sort algorithm implementation.

Insertion Sort is a simple, intuitive sorting algorithm that builds the
sorted list one element at a time. It works similarly to how you might
sort playing cards in your hand: you pick up one card at a time and insert
it into its correct position among the already-sorted cards.

The algorithm divides the list into a "sorted" portion (left side) and an
"unsorted" portion (right side). It takes each element from the unsorted
portion and inserts it into the correct position in the sorted portion by
shifting larger elements one position to the right.

Time Complexity:
    - Best case: O(n) — when the list is already sorted.
    - Average case: O(n^2)
    - Worst case: O(n^2) — when the list is sorted in reverse order.

Space Complexity: O(1) — it is an in-place sorting algorithm.
Stability: Insertion sort is a stable sort.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from typing import List, TypeVar

# Type variable for comparable elements.
T = TypeVar("T")


def insertion_sort(arr: List[T]) -> List[T]:
    """Sort a list using the insertion sort algorithm.

    The algorithm iterates through the list, taking one element at a time
    and inserting it into its correct position in the already-sorted
    portion of the list (to the left of the current element).

    Args:
        arr: The list to sort. Elements must be comparable.

    Returns:
        The sorted list (sorted in place; the same list object is returned
        for convenience).

    Raises:
        TypeError: If arr is not a list or elements are not comparable.

    Example:
        >>> insertion_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if not isinstance(arr, list):
        raise TypeError(f"Expected a list, got {type(arr).__name__}")

    n = len(arr)

    # An empty list or single-element list is already sorted.
    if n <= 1:
        return arr

    # Start from the second element (index 1).
    # The first element (index 0) is trivially "sorted".
    for i in range(1, n):
        # The element to be inserted into the sorted portion.
        key = arr[i]

        # Index of the last element in the sorted portion.
        j = i - 1

        # Shift elements of the sorted portion that are greater than key
        # one position to the right.
        try:
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
        except TypeError as exc:
            raise TypeError(f"Elements are not comparable: {exc}") from exc

        # Insert the key at its correct position.
        arr[j + 1] = key

    return arr


def insertion_sort_verbose(arr: List[T]) -> List[T]:
    """Sort a list using insertion sort and print each step.

    This is an educational version that shows how the algorithm works
    step by step.

    Args:
        arr: The list to sort.

    Returns:
        The sorted list.
    """
    if not isinstance(arr, list):
        raise TypeError(f"Expected a list, got {type(arr).__name__}")

    n = len(arr)
    if n <= 1:
        return arr

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"Step {i}: {arr} (inserted {key} at position {j + 1})")

    return arr


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the insertion sort functions."""
    print("=== Insertion Sort Example ===\n")

    # --- Basic insertion sort ---
    print("--- Basic Insertion Sort ---")
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"  Original: {data}")
    sorted_data = insertion_sort(data.copy())
    print(f"  Sorted:   {sorted_data}")
    print()

    # --- Already sorted (best case) ---
    print("--- Already Sorted (Best Case) ---")
    data = [1, 2, 3, 4, 5]
    print(f"  Original: {data}")
    sorted_data = insertion_sort(data.copy())
    print(f"  Sorted:   {sorted_data}")
    print()

    # --- Reverse sorted (worst case) ---
    print("--- Reverse Sorted (Worst Case) ---")
    data = [5, 4, 3, 2, 1]
    print(f"  Original: {data}")
    sorted_data = insertion_sort(data.copy())
    print(f"  Sorted:   {sorted_data}")
    print()

    # --- Verbose version ---
    print("--- Verbose Version ---")
    data = [5, 2, 4, 6, 1, 3]
    print(f"  Original: {data}")
    insertion_sort_verbose(data.copy())
    print()

    # --- Edge cases ---
    print("--- Edge Cases ---")
    print(f"  Empty list: {insertion_sort([])}")
    print(f"  Single element: {insertion_sort([42])}")
    print(f"  Duplicates: {insertion_sort([3, 1, 3, 1, 3])}")
    print(f"  Strings: {insertion_sort(['banana', 'apple', 'cherry'])}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()