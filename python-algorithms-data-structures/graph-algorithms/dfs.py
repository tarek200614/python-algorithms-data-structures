"""Depth-First Search (DFS) algorithm implementation.

DFS is a graph traversal algorithm that explores as far as possible along
each branch before backtracking. It uses a stack (either explicit or via
recursion) to keep track of vertices to visit.

DFS is commonly used for:
    - Detecting cycles in a graph.
    - Topological sorting of a directed acyclic graph (DAG).
    - Finding connected components.
    - Solving mazes and puzzles.

Time Complexity: O(V + E) where V = vertices, E = edges.
Space Complexity: O(V) for the recursion stack and visited set.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from typing import Dict, Hashable, List, Optional, Set

# Type alias for a graph representation (adjacency list).
Graph = Dict[Hashable, List[Hashable]]


def dfs_traverse_recursive(graph: Graph, start: Hashable) -> List[Hashable]:
    """Traverse a graph using recursive DFS and return the traversal order.

    Args:
        graph: An adjacency list representation of the graph.
        start: The starting vertex for the traversal.

    Returns:
        A list of vertices in the order they were visited.

    Raises:
        ValueError: If the graph is empty or the start vertex is not in the graph.
        TypeError: If the graph is not a dict.
    """
    if not isinstance(graph, dict):
        raise TypeError("graph must be a dictionary (adjacency list)")
    if not graph:
        raise ValueError("graph must not be empty")
    if start not in graph:
        raise ValueError(f"start vertex {start!r} is not in the graph")

    visited: Set[Hashable] = set()
    order: List[Hashable] = []

    def _dfs(vertex: Hashable) -> None:
        """Recursive helper that visits a vertex and its neighbors."""
        visited.add(vertex)
        order.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order


def dfs_traverse_iterative(graph: Graph, start: Hashable) -> List[Hashable]:
    """Traverse a graph using iterative DFS and return the traversal order.

    This version uses an explicit stack instead of recursion, which avoids
    potential stack overflow for very deep graphs.

    Args:
        graph: An adjacency list representation of the graph.
        start: The starting vertex for the traversal.

    Returns:
        A list of vertices in the order they were visited.

    Raises:
        ValueError: If the graph is empty or the start vertex is not in the graph.
        TypeError: If the graph is not a dict.
    """
    if not isinstance(graph, dict):
        raise TypeError("graph must be a dictionary (adjacency list)")
    if not graph:
        raise ValueError("graph must not be empty")
    if start not in graph:
        raise ValueError(f"start vertex {start!r} is not in the graph")

    visited: Set[Hashable] = set()
    order: List[Hashable] = []
    stack: List[Hashable] = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)

            # Push neighbors in reverse order so they are visited in the
            # same order as the recursive version (left-to-right).
            neighbors = graph.get(vertex, [])
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def dfs_find_path(graph: Graph, start: Hashable, target: Hashable) -> Optional[List[Hashable]]:
    """Find a path from start to target using DFS.

    Note: DFS does not guarantee the shortest path. For the shortest path
    in an unweighted graph, use BFS instead.

    Args:
        graph: An adjacency list representation of the graph.
        start: The starting vertex.
        target: The target vertex.

    Returns:
        A list of vertices representing a path from start to target, or
        None if no path exists.

    Raises:
        ValueError: If the graph is empty, or start/target vertices are not
            in the graph.
        TypeError: If the graph is not a dict.
    """
    if not isinstance(graph, dict):
        raise TypeError("graph must be a dictionary (adjacency list)")
    if not graph:
        raise ValueError("graph must not be empty")
    if start not in graph:
        raise ValueError(f"start vertex {start!r} is not in the graph")
    if target not in graph:
        raise ValueError(f"target vertex {target!r} is not in the graph")

    if start == target:
        return [start]

    visited: Set[Hashable] = set()
    path: List[Hashable] = []

    def _dfs(vertex: Hashable) -> bool:
        """Recursive helper that searches for the target.

        Returns:
            True if the target was found, False otherwise.
        """
        visited.add(vertex)
        path.append(vertex)

        if vertex == target:
            return True

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if _dfs(neighbor):
                    return True

        # Backtrack: target not found along this path.
        path.pop()
        return False

    found = _dfs(start)
    return path if found else None


def dfs_detect_cycle(graph: Graph) -> bool:
    """Detect whether a directed graph contains a cycle using DFS.

    Uses a three-color marking scheme:
    - WHITE: vertex has not been visited.
    - GRAY: vertex is currently being processed (in the current DFS path).
    - BLACK: vertex and all its descendants have been fully processed.

    A cycle exists if we encounter a GRAY vertex during DFS.

    Args:
        graph: An adjacency list representation of a directed graph.

    Returns:
        True if the graph contains a cycle, False otherwise.

    Raises:
        TypeError: If the graph is not a dict.
    """
    if not isinstance(graph, dict):
        raise TypeError("graph must be a dictionary (adjacency list)")
    if not graph:
        return False

    # WHITE = not visited, GRAY = in progress, BLACK = done
    color: Dict[Hashable, str] = {v: "WHITE" for v in graph}

    def _has_cycle(vertex: Hashable) -> bool:
        """Recursive helper that checks for cycles from a vertex.

        Returns:
            True if a cycle is detected, False otherwise.
        """
        color[vertex] = "GRAY"

        for neighbor in graph.get(vertex, []):
            if neighbor not in color:
                # Neighbor is not a key in the graph; skip it.
                continue
            if color[neighbor] == "GRAY":
                # Found a back edge: cycle detected.
                return True
            if color[neighbor] == "WHITE":
                if _has_cycle(neighbor):
                    return True

        color[vertex] = "BLACK"
        return False

    for vertex in graph:
        if color.get(vertex) == "WHITE":
            if _has_cycle(vertex):
                return True

    return False


def dfs_topological_sort(graph: Graph) -> Optional[List[Hashable]]:
    """Perform a topological sort on a directed acyclic graph (DAG).

    A topological sort orders vertices such that for every directed edge
    (u, v), vertex u comes before vertex v in the ordering.

    Args:
        graph: An adjacency list representation of a directed graph.

    Returns:
        A list of vertices in topological order, or None if the graph
        contains a cycle (and thus no valid topological sort exists).

    Raises:
        TypeError: If the graph is not a dict.
    """
    if not isinstance(graph, dict):
        raise TypeError("graph must be a dictionary (adjacency list)")
    if not graph:
        return []

    # First check for cycles; if there's a cycle, topological sort is impossible.
    if dfs_detect_cycle(graph):
        return None

    visited: Set[Hashable] = set()
    result: List[Hashable] = []

    def _dfs(vertex: Hashable) -> None:
        """Recursive helper that visits a vertex and its neighbors."""
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                _dfs(neighbor)

        # Add vertex to result after all its descendants are processed.
        # We prepend (insert at 0) to get the correct topological order.
        result.insert(0, vertex)

    for vertex in graph:
        if vertex not in visited:
            _dfs(vertex)

    return result


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the DFS functions."""
    print("=== Depth-First Search (DFS) Example ===\n")

    # Define a sample directed graph using an adjacency list.
    graph: Graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    print("Graph (adjacency list):")
    for vertex, neighbors in graph.items():
        print(f"  {vertex}: {neighbors}")
    print()

    # --- Recursive traversal ---
    print("--- Recursive Traversal ---")
    order = dfs_traverse_recursive(graph, "A")
    print(f"DFS (recursive) from 'A': {order}")
    print()

    # --- Iterative traversal ---
    print("--- Iterative Traversal ---")
    order = dfs_traverse_iterative(graph, "A")
    print(f"DFS (iterative) from 'A': {order}")
    print()

    # --- Find a path ---
    print("--- Find Path ---")
    path = dfs_find_path(graph, "A", "F")
    print(f"Path from 'A' to 'F': {path}")
    print()

    # --- Cycle detection ---
    print("--- Cycle Detection ---")
    has_cycle = dfs_detect_cycle(graph)
    print(f"Graph has cycle: {has_cycle}")

    cyclic_graph: Graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
    }
    has_cycle = dfs_detect_cycle(cyclic_graph)
    print(f"Cyclic graph has cycle: {has_cycle}")
    print()

    # --- Topological sort ---
    print("--- Topological Sort ---")
    dag: Graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["E"],
        "E": [],
    }
    topo = dfs_topological_sort(dag)
    print(f"Topological sort: {topo}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()