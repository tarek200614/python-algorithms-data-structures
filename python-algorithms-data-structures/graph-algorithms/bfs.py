"""Breadth-First Search (BFS) algorithm implementation.

BFS is a graph traversal algorithm that explores vertices level by level,
starting from a source vertex. It visits all neighbors of a vertex before
moving to the next level of vertices.

BFS is commonly used for:
    - Finding the shortest path in an unweighted graph.
    - Level-order traversal of trees.
    - Finding connected components.

Time Complexity: O(V + E) where V = vertices, E = edges.
Space Complexity: O(V) for the queue and visited set.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

from collections import deque
from typing import Dict, Hashable, List, Optional, Set

# Type alias for a graph representation (adjacency list).
Graph = Dict[Hashable, List[Hashable]]


def bfs_traverse(graph: Graph, start: Hashable) -> List[Hashable]:
    """Traverse a graph using BFS and return the traversal order.

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
    queue: deque = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        # Explore all neighbors of the current vertex.
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_shortest_path(graph: Graph, start: Hashable, target: Hashable) -> Optional[List[Hashable]]:
    """Find the shortest path between two vertices in an unweighted graph.

    Args:
        graph: An adjacency list representation of the graph.
        start: The starting vertex.
        target: The target vertex.

    Returns:
        A list of vertices representing the shortest path from start to
        target, or None if no path exists.

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

    visited: Set[Hashable] = {start}
    # parent map to reconstruct the path.
    parent: Dict[Hashable, Hashable] = {}
    queue: deque = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)

                if neighbor == target:
                    # Reconstruct the path by following parent pointers.
                    path: List[Hashable] = [target]
                    current = target
                    while current != start:
                        current = parent[current]
                        path.append(current)
                    path.reverse()
                    return path

    # No path found.
    return None


def bfs_shortest_distances(graph: Graph, start: Hashable) -> Dict[Hashable, int]:
    """Compute the shortest distance from a start vertex to all others.

    Args:
        graph: An adjacency list representation of the graph.
        start: The starting vertex.

    Returns:
        A dictionary mapping each reachable vertex to its distance (number
        of edges) from the start vertex.

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

    distances: Dict[Hashable, int] = {start: 0}
    queue: deque = deque([start])

    while queue:
        vertex = queue.popleft()
        current_distance = distances[vertex]

        for neighbor in graph.get(vertex, []):
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    return distances


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use the BFS functions."""
    print("=== Breadth-First Search (BFS) Example ===\n")

    # Define a sample undirected graph using an adjacency list.
    graph: Graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Graph (adjacency list):")
    for vertex, neighbors in graph.items():
        print(f"  {vertex}: {neighbors}")
    print()

    # --- Traversal ---
    print("--- Traversal ---")
    order = bfs_traverse(graph, "A")
    print(f"BFS traversal from 'A': {order}")
    print()

    # --- Shortest path ---
    print("--- Shortest Path ---")
    path = bfs_shortest_path(graph, "A", "F")
    print(f"Shortest path from 'A' to 'F': {path}")
    print()

    # --- Shortest distances ---
    print("--- Shortest Distances ---")
    distances = bfs_shortest_distances(graph, "A")
    print(f"Shortest distances from 'A': {distances}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()