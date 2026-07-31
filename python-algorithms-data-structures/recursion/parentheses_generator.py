"""Generate all valid combinations of well-formed parentheses.

Given n pairs of parentheses, this module generates all valid (well-formed)
combinations. A combination is well-formed if every opening parenthesis '('
has a matching closing parenthesis ')' and they are properly nested.

Example for n = 3:
    ["((()))", "(()())", "(())()", "()(())", "()()()"]

This is a classic backtracking problem. At each step, we can add an opening
parenthesis '(' if we haven't used all n, and we can add a closing
parenthesis ')' if the number of closing parentheses used so far is less
than the number of opening parentheses used.

Time Complexity: O(4^n / sqrt(n)) — the n-th Catalan number.
Space Complexity: O(n) for the recursion stack.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from typing import List


def generate_parentheses(n: int) -> List[str]:
    """Generate all valid combinations of n pairs of parentheses.

    Uses a backtracking approach: at each step, we decide whether to add
    an opening or closing parenthesis, subject to the constraints:
    - We can add '(' if we haven't used all n opening parentheses.
    - We can add ')' if there are more '(' than ')' in the current string.

    Args:
        n: The number of pairs of parentheses. Must be non-negative.

    Returns:
        A list of all valid combinations of well-formed parentheses.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return [""]

    result: List[str] = []

    def _backtrack(current: str, open_count: int, close_count: int) -> None:
        """Recursively build valid parentheses strings.

        Args:
            current: The string built so far.
            open_count: Number of '(' used so far.
            close_count: Number of ')' used so far.
        """
        # Base case: we've used all n pairs.
        if len(current) == 2 * n:
            result.append(current)
            return

        # Choice 1: Add an opening parenthesis if we haven't used all n.
        if open_count < n:
            _backtrack(current + "(", open_count + 1, close_count)

        # Choice 2: Add a closing parenthesis if it won't make the string invalid.
        # We can add ')' only if there are more '(' than ')' so far.
        if close_count < open_count:
            _backtrack(current + ")", open_count, close_count + 1)

    _backtrack("", 0, 0)
    return result


def count_parentheses(n: int) -> int:
    """Count the number of valid parentheses combinations without generating them.

    This uses the Catalan number formula:
        C(n) = (2n)! / ((n+1)! * n!)

    Args:
        n: The number of pairs of parentheses. Must be non-negative.

    Returns:
        The number of valid combinations.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    # Compute C(n) = (2n)! / ((n+1)! * n!)
    # We compute this iteratively to avoid large intermediate factorials.
    result = 1
    for i in range(n):
        result = result * (2 * n - i) // (i + 1)
    result = result // (n + 1)
    return result


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the parentheses generator functions."""
    print("=== Parentheses Generator Example ===\n")

    for n in range(5):
        combinations = generate_parentheses(n)
        count = count_parentheses(n)
        print(f"n = {n}: {len(combinations)} combinations (Catalan number: {count})")
        if combinations:
            for combo in combinations:
                print(f"  {combo}")
        print()

    print("=== End of Example ===")


if __name__ == "__main__":
    _example_usage()