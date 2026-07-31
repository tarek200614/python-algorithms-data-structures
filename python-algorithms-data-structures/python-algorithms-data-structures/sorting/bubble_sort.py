"""Bubble Sort algorithm implementation.

Bubble Sort is one of the simplest sorting algorithms. It repeatedly steps
through the list, compares adjacent elements, and swaps them if they are in
the wrong order. The pass through the list is repeated until no swaps are
needed, indicating that the list is sorted.

The name "bubble sort" comes from the way larger elements "bubble" to the
end of the list with each pass, like bubbles rising to the surface.

Time Complexity:
    - Best case: O(n) — when the list is already sorted (with optimization).
    - Average case: O(n^2)
    - Worst case: O(n^2) — when the list is sorted in reverse order.

Space Complexity: O(1) — it is an in-place sorting algorithm.
Stability: Bubble sort is a stable sort.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from typing import List, TypeVar

# Type variable for comparable elements.
T = TypeVar("T")


def bubble_sort(arr: List[T]) -> List[T]:
    """Sort a list using the bubble sort algorithm.

    This implementation includes an optimization: if no swaps are made
    during a pass, the list is already sorted and the algorithm terminates
    early. This gives O(n) best-case performance.

    Args:
        arr: The list to sort. Elements must be comparable.

    Returns:
        The sorted list (sorted in place; the same list object is returned
        for convenience).

    Raises:
        TypeError: If arr is not a list or elements are not comparable.

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if not isinstance(arr, list):
        raise TypeError(f"Expected a list, got {type(arr).__name__}")

    n = len(arr)

    # An empty list or single-element list is already sorted.
    if n <= 1:
        return arr

    # Outer loop: we need at most n-1 passes.
    for i in range(n - 1):
        swapped = False

        # Inner loop: compare adjacent elements.
        # After pass i, the last i elements are already in their final positions,
        # so we don't need to check them.
        for j in range(n - 1 - i):
            # Validate that elements are comparable.
            try:
                if arr[j] > arr[j + 1]:
                    # Swap the elements.
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            except TypeError as exc:
                raise TypeError(
                    f"Elements at index {j} and {j + 1} are not comparable: {exc}"
                ) from exc

        # Optimization: if no swaps were made, the list is already sorted.
        if not swapped:
            break

    return arr


def bubble_sort_verbose(arr: List[T]) -> List[T]:
    """Sort a list using bubble sort and print each pass.

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

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        print(f"Pass {i + 1}: {arr}")
        if not swapped:
            print("  (no swaps, already sorted)")
            break

    return arr


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the bubble sort functions."""
    print("=== Bubble Sort Example ===\n")

    # --- Basic bubble sort ---
    print("--- Basic Bubble Sort ---")
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"  Original: {data}")
    sorted_data = bubble_sort(data.copy())
    print(f"  Sorted:   {sorted_data}")
    print()

    # --- Already sorted (best case) ---
    print("--- Already Sorted (Best Case) ---")
    data = [1, 2, 3, 4, 5]
    print(f"  Original: {data}")
    sorted_data = bubble_sort(data.copy())
    print(f"  Sorted:   {sorted_data}")
    print()

    # --- Reverse sorted (worst case) ---
    print("--- Reverse Sorted (Worst Case) ---")
    data = [5, 4, 3, 2, 1]
    print(f"  Original: {data}")
    sorted_data = bubble_sort(data.copy())
    print(f"  Sorted:   {sorted_data}")
    print()

    # --- Verbose version ---
    print("--- Verbose Version ---")
    data = [5, 1, 4, 2, 8]
    print(f"  Original: {data}")
    bubble_sort_verbose(data.copy())
    print()

    # --- Edge cases ---
    print("--- Edge Cases ---")
    print(f"  Empty list: {bubble_sort([])}")
    print(f"  Single element: {bubble_sort([42])}")
    print(f"  Duplicates: {bubble_sort([3, 1, 3, 1, 3])}")
    print(f"  Strings: {bubble_sort(['banana', 'apple', 'cherry'])}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()