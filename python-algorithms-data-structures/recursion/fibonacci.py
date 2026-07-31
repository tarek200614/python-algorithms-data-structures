"""Fibonacci sequence implementations using multiple approaches.

The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n >= 2

This module provides three implementations:
    1. Naive recursive (exponential time — for educational purposes).
    2. Memoized recursive (top-down dynamic programming).
    3. Iterative (bottom-up dynamic programming, most efficient).

Time Complexity:
    - Naive recursive: O(2^n)
    - Memoized: O(n)
    - Iterative: O(n)

Space Complexity:
    - Naive recursive: O(n) for the call stack
    - Memoized: O(n) for the memo + call stack
    - Iterative: O(1) (constant space, only storing two values)

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from functools import lru_cache
from typing import List


def fibonacci_recursive(n: int) -> int:
    """Compute the n-th Fibonacci number using naive recursion.

    This is the simplest but least efficient approach. It recomputes
    the same subproblems many times, leading to exponential time.

    Args:
        n: The index in the Fibonacci sequence. Must be non-negative.

    Returns:
        The n-th Fibonacci number (F(0) = 0, F(1) = 1).

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """Compute the n-th Fibonacci number using memoized recursion.

    Uses Python's functools.lru_cache to store previously computed
    results, avoiding redundant calculations.

    Args:
        n: The index in the Fibonacci sequence. Must be non-negative.

    Returns:
        The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Compute the n-th Fibonacci number using an iterative approach.

    This is the most efficient approach, using O(1) space by only
    keeping track of the two most recent values.

    Args:
        n: The index in the Fibonacci sequence. Must be non-negative.

    Returns:
        The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    prev2 = 0  # F(0)
    prev1 = 1  # F(1)

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


def fibonacci_sequence(n: int) -> List[int]:
    """Generate the first n Fibonacci numbers as a list.

    Args:
        n: The number of Fibonacci numbers to generate. Must be non-negative.

    Returns:
        A list of the first n Fibonacci numbers: [F(0), F(1), ..., F(n-1)].

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []

    sequence: List[int] = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the Fibonacci functions."""
    print("=== Fibonacci Example ===\n")

    n = 10
    print(f"Computing Fibonacci numbers up to F({n})\n")

    # --- Iterative (recommended) ---
    print("--- Iterative Approach ---")
    for i in range(n + 1):
        print(f"  F({i}) = {fibonacci_iterative(i)}")

    # --- Memoized ---
    print("\n--- Memoized Approach ---")
    print(f"  F({n}) = {fibonacci_memoized(n)}")

    # --- Sequence ---
    print("\n--- Full Sequence ---")
    seq = fibonacci_sequence(n)
    print(f"  First {n} Fibonacci numbers: {seq}")

    # --- Naive recursive (only for small n) ---
    print("\n--- Naive Recursive (small n only) ---")
    print(f"  F(10) = {fibonacci_recursive(10)}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()