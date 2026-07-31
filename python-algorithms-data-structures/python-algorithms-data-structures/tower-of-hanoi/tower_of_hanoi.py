"""Tower of Hanoi solver using recursion.

The Tower of Hanoi is a classic mathematical puzzle. Given three rods and
*n* disks of different sizes, the goal is to move all disks from the source
rod to the destination rod, obeying these rules:

1. Only one disk may be moved at a time.
2. A move consists of taking the top disk from one rod and placing it on
   another rod.
3. No disk may be placed on top of a smaller disk.

Time Complexity: O(2^n) — the number of moves is exactly 2^n - 1.
Space Complexity: O(n) for the recursion stack.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from typing import List, Optional


def hanoi_recursive(n: int, source: str = "A", auxiliary: str = "B", destination: str = "C") -> List[str]:
    """Return a list of move instructions for the Tower of Hanoi.

    This is a pure function that does not modify any state. It returns a
    list of strings, each describing one move.

    Args:
        n: The number of disks. Must be non-negative.
        source: The name of the source rod.
        auxiliary: The name of the auxiliary rod.
        destination: The name of the destination rod.

    Returns:
        A list of move instruction strings.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    moves: List[str] = []

    def _solve(disks: int, src: str, aux: str, dst: str) -> None:
        """Recursive helper that generates move instructions."""
        if disks == 0:
            return
        # Step 1: Move n-1 disks from source to auxiliary.
        _solve(disks - 1, src, dst, aux)
        # Step 2: Move the largest disk from source to destination.
        moves.append(f"Move disk {disks} from {src} to {dst}")
        # Step 3: Move n-1 disks from auxiliary to destination.
        _solve(disks - 1, aux, src, dst)

    _solve(n, source, auxiliary, destination)
    return moves


def hanoi_count_moves(n: int) -> int:
    """Return the minimum number of moves required to solve the puzzle.

    The formula is 2^n - 1.

    Args:
        n: The number of disks. Must be non-negative.

    Returns:
        The minimum number of moves.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    return (1 << n) - 1  # Equivalent to 2**n - 1


def hanoi_iterative(n: int) -> List[str]:
    """Solve the Tower of Hanoi iteratively and return move instructions.

    Args:
        n: The number of disks. Must be non-negative.

    Returns:
        A list of move instruction strings.

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

    # Rods represented as stacks. Disk 1 is smallest, disk n is largest.
    # Disks stored bottom-to-top; largest at index 0.
    rods: List[List[int]] = [list(range(n, 0, -1)), [], []]
    rod_names = ["A", "B", "C"]
    moves: List[str] = []
    total_moves = (1 << n) - 1

    # For even n, the cycle is A->B, A->C, B->C
    # For odd n, the cycle is A->C, A->B, B->C
    if n % 2 == 0:
        cycle = [(0, 1), (0, 2), (1, 2)]
    else:
        cycle = [(0, 2), (0, 1), (1, 2)]

    move_num = 0
    while move_num < total_moves:
        for src, dst in cycle:
            if move_num >= total_moves:
                break
            # Try to make a legal move between src and dst.
            if _try_move(rods, src, dst, rod_names, moves):
                move_num += 1
            elif _try_move(rods, dst, src, rod_names, moves):
                move_num += 1

    return moves


def _try_move(rods: List[List[int]], src: int, dst: int, names: List[str], moves: List[str]) -> bool:
    """Attempt a legal move between two rods.

    Returns:
        True if a move was made, False if the move was not legal.
    """
    if not rods[src]:
        return False
    disk = rods[src][-1]
    if rods[dst] and rods[dst][-1] < disk:
        return False
    rods[src].pop()
    rods[dst].append(disk)
    moves.append(f"Move disk {disk} from {names[src]} to {names[dst]}")
    return True


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the Tower of Hanoi functions."""
    print("=== Tower of Hanoi Example ===\n")

    n = 3
    print(f"Solving Tower of Hanoi with {n} disks\n")

    # --- Recursive approach ---
    print("--- Recursive Approach ---\n")
    moves = hanoi_recursive(n)
    for i, move in enumerate(moves, 1):
        print(f"  {i}. {move}")
    print(f"\nTotal moves: {len(moves)}")
    print(f"Minimum moves required: {hanoi_count_moves(n)}")

    # --- Iterative approach ---
    print("\n--- Iterative Approach ---\n")
    iter_moves = hanoi_iterative(n)
    for i, move in enumerate(iter_moves, 1):
        print(f"  {i}. {move}")
    print(f"\nTotal moves: {len(iter_moves)}")

    # Verify both approaches produce the same number of moves.
    print(f"\nRecursive and iterative match: {len(moves) == len(iter_moves)}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()