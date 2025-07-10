import numpy as np
from scipy.sparse import csr_matrix

def initialize_matrices(n):
    """Initialize distance and next_node matrices."""
    dist = np.full((n, n), np.inf, dtype=np.float32)
    next_node = np.full((n, n), -1, dtype=np.int32)
    np.fill_diagonal(dist, 0)
    np.fill_diagonal(next_node, np.arange(n, dtype=np.int32))
    return dist, next_node

def populate_matrices(adjacency_matrix, dist, next_node):
    """Populate the distance and next_node matrices from the adjacency matrix."""
    n = adjacency_matrix.shape[0]
    mask = adjacency_matrix != 0
    dist[mask] = adjacency_matrix[mask]
    next_node[mask] = np.arange(n)[:, np.newaxis]

def floyd_warshall(adjacency_matrix):
    """Run the Floyd-Warshall algorithm."""
    n = adjacency_matrix.shape[0]
    dist, next_node = initialize_matrices(n)
    populate_matrices(adjacency_matrix, dist, next_node)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    next_node[i, j] = next_node[i, k]
    return dist, next_node

def get_path(u, v, next_node):
    """Reconstruct the path from node u to node v."""
    if next_node[u, v] == -1:
        return []
    path = []
    while u != v:
        path.append(u)
        u = next_node[u, v]
    path.append(v)
    return path

def get_distance(u, v, dist):
    """Get the distance between nodes u and v from the distance matrix."""
    return dist[u, v]

def optimize_all_pairs_shortest_path(adjacency_matrix):
    """Optimize the all-pairs shortest path algorithm."""
    dist, next_node = floyd_warshall(adjacency_matrix)
    return get_path, get_distance, dist, next_node

def handle_sparse_graph(adjacency_matrix):
    """Handle sparse graph optimization."""
    csr = csr_matrix(adjacency_matrix)
    n = adjacency_matrix.shape[0]
    dist, next_node = initialize_matrices(n)
    for i in range(n):
        for j in csr.indices[csr.indptr[i]:csr.indptr[i + 1]]:
            if adjacency_matrix[i, j] != 0:
                dist[i, j] = adjacency_matrix[i, j]
                next_node[i, j] = j
    return optimize_all_pairs_shortest_path(dist)

# Example usage:
if __name__ == "__main__":
    # Example adjacency matrix for testing
    adjacency_matrix = np.array([
        [0, 3, np.inf, 5],
        [2, 0, np.inf, 4],
        [np.inf, 1, 0, np.inf],
        [np.inf, np.inf, 2, 0]
    ], dtype=np.float32)

    get_path_func, get_distance_func, dist, next_node = optimize_all_pairs_shortest_path(adjacency_matrix)

    print("Distance between nodes 0 and 3:", get_distance_func(0, 3, dist))
    print("Path between nodes 0 and 3:", get_path_func(0, 3, next_node))
    print("Distance between nodes 1 and 2:", get_distance_func(1, 2, dist))
    print("Path between nodes 1 and 2:", get_path_func(1, 2, next_node))
