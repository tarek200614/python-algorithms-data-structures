"""Dijkstra's shortest path algorithm implementation.

Dijkstra's algorithm finds the shortest paths from a source vertex to all
other vertices in a weighted graph with non-negative edge weights.

The algorithm maintains a set of vertices whose shortest distances from
the source are known, and repeatedly selects the unvisited vertex with
the smallest known distance, updating the distances of its neighbors.

Time Complexity: O((V + E) log V) with a binary heap (priority queue).
Space Complexity: O(V + E) for the distance array, priority queue, and graph.

Author: python-algorithms-data-structures contributors
License: MIT
"""

from __future__ import annotations

import heapq
from typing import Dict, Hashable, List, Optional, Tuple

# Type alias for a weighted graph.
# Keys are vertices, values are lists of (neighbor, weight) tuples.
WeightedGraph = Dict[Hashable, List[Tuple[Hashable, float]]]


def _validate_graph(graph: WeightedGraph, start: Hashable) -> None:
    """Validate the graph and start vertex.

    Args:
        graph: A weighted adjacency list.
        start: The source vertex.

    Raises:
        TypeError: If the graph is not a dict.
        ValueError: If the graph is empty, the start vertex is not in the
            graph, or any edge has a negative weight.
    """
    if not isinstance(graph, dict):
        raise TypeError("graph must be a dictionary (adjacency list)")
    if not graph:
        raise ValueError("graph must not be empty")
    if start not in graph:
        raise ValueError(f"start vertex {start!r} is not in the graph")

    # Validate that all edge weights are non-negative.
    for vertex, edges in graph.items():
        for neighbor, weight in edges:
            if weight < 0:
                raise ValueError(
                    f"Edge ({vertex} -> {neighbor}) has negative weight {weight}. "
                    "Dijkstra's algorithm requires non-negative weights."
                )


def dijkstra(graph: WeightedGraph, start: Hashable) -> Dict[Hashable, float]:
    """Compute shortest distances from a source vertex to all others.

    Uses a min-heap (priority queue) for efficient extraction of the
    minimum-distance vertex.

    Args:
        graph: A weighted adjacency list. Weights must be non-negative.
        start: The source vertex.

    Returns:
        A dictionary mapping each reachable vertex to its shortest distance
        from the source. Unreachable vertices are not included.

    Raises:
        ValueError: If the graph is empty or the start vertex is not in the graph.
        TypeError: If the graph is not a dict.
    """
    _validate_graph(graph, start)

    # Initialize distances: 0 for the start, infinity for all others.
    distances: Dict[Hashable, float] = {start: 0}
    # Priority queue stores (distance, vertex) tuples.
    pq: List[Tuple[float, Hashable]] = [(0, start)]
    # Track visited vertices to avoid reprocessing.
    visited: set = set()

    while pq:
        current_dist, current = heapq.heappop(pq)

        # Skip if we've already processed this vertex with a shorter distance.
        if current in visited:
            continue
        visited.add(current)

        # If the popped distance is greater than the recorded distance, skip.
        if current_dist > distances.get(current, float("inf")):
            continue

        # Relax all edges from the current vertex.
        for neighbor, weight in graph.get(current, []):
            new_dist = current_dist + weight

            # If we found a shorter path to the neighbor, update it.
            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


def dijkstra_shortest_path(
    graph: WeightedGraph, start: Hashable, target: Hashable
) -> Tuple[Optional[List[Hashable]], float]:
    """Find the shortest path and distance between two vertices.

    Args:
        graph: A weighted adjacency list with non-negative weights.
        start: The source vertex.
        target: The target vertex.

    Returns:
        A tuple (path, distance) where:
        - path is a list of vertices from start to target, or None if no
          path exists.
        - distance is the total path weight, or float('inf') if no path exists.

    Raises:
        ValueError: If the graph is empty, or start/target vertices are not
            in the graph.
        TypeError: If the graph is not a dict.
    """
    _validate_graph(graph, start)
    if target not in graph:
        raise ValueError(f"target vertex {target!r} is not in the graph")

    distances: Dict[Hashable, float] = {start: 0}
    # Track the predecessor of each vertex for path reconstruction.
    predecessors: Dict[Hashable, Optional[Hashable]] = {start: None}
    pq: List[Tuple[float, Hashable]] = [(0, start)]
    visited: set = set()

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        # Early termination: we found the target.
        if current == target:
            break

        if current_dist > distances.get(current, float("inf")):
            continue

        for neighbor, weight in graph.get(current, []):
            new_dist = current_dist + weight

            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                predecessors[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    # Reconstruct the path from start to target.
    if target not in distances:
        return None, float("inf")

    path: List[Hashable] = []
    current: Optional[Hashable] = target
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    path.reverse()

    return path, distances[target]


# ----------------------------------------------------------------------
# Usage example
# ----------------------------------------------------------------------
def _example_usage() -> None:
    """Demonstrate how to use Dijkstra's algorithm functions."""
    print("=== Dijkstra's Algorithm Example ===\n")

    # Define a sample weighted graph using an adjacency list.
    # Each entry is (neighbor, weight).
    graph: WeightedGraph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("B", 1), ("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": [],
    }

    print("Graph (weighted adjacency list):")
    for vertex, edges in graph.items():
        edges_str = ", ".join(f"({n}, w={w})" for n, w in edges)
        print(f"  {vertex}: [{edges_str}]")
    print()

    # --- Shortest distances from A ---
    print("--- Shortest Distances from 'A' ---")
    distances = dijkstra(graph, "A")
    for vertex, dist in sorted(distances.items(), key=lambda x: x[1]):
        print(f"  Distance to {vertex}: {dist}")
    print()

    # --- Shortest path from A to E ---
    print("--- Shortest Path from 'A' to 'E' ---")
    path, distance = dijkstra_shortest_path(graph, "A", "E")
    print(f"  Path: {' -> '.join(path) if path else 'No path'}")
    print(f"  Total distance: {distance}")

    print("\n=== End of Example ===")


if __name__ == "__main__":
    _example_usage()