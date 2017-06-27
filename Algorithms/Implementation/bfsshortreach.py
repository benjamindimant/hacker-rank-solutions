import sys

def build_graph(n, m):
    node_edges = [[]]
    for i in range(n):
        node_edges.append([])
    for i in range(m):
        node, edge = map(int, input().strip().split(' '))
        node_edges[node].append(edge) # Graph is undirected
        node_edges[edge].append(node)
    return node_edges

def compute_distances(root, node_edges):
    distances = {root: 0}
    queue = [root]
    while (queue):
        element = queue.pop(0)
        for neighbor in node_edges[element]:
            if neighbor not in distances:
                distances[neighbor] = distances[element] + 6
                queue.append(neighbor)
    return distances


def print_distances(root, n, distances):
    for i in range(1, n + 1):
        if i in distances:
            if (i != root):
                print(distances[i], end = " "),
        else:
            print(-1, end = " "),
    print()

q = int(input())
for i in range(q):
    n, m = map(int, input().strip().split(' '))
    node_edges = build_graph(n, m)
    root = int(input())
    distances = compute_distances(root, node_edges)
    print_distances(root, n, distances)
