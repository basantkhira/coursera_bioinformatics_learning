import math

def longest_path_dag(start, end, edges):
    # Build adjacency list
    graph = {}
    nodes = set()

    for u, v, w in edges:
        nodes.add(u)
        nodes.add(v)
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    # Topological order = nodes in increasing order
    topo_order = sorted(nodes)

    # DP table: longest distance from start to each node
    dist      = {node: -math.inf for node in nodes}
    prev      = {node: None      for node in nodes}  # for traceback
    dist[start] = 0

    # Fill in topological order
    for u in topo_order:
        if dist[u] == -math.inf:
            continue                        # not reachable from start
        if u not in graph:
            continue
        for v, w in graph[u]:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u                 # track which node we came from

    # Traceback path from end to start
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()

    # Validate path starts at start
    if path[0] != start:
        return -1, []                       # no path from start to end

    return dist[end], path


if __name__ == "__main__":
    start = int(input("\nEnter start node: "))
    end   = int(input("Enter end node  : "))

    edges = []
    while True:
        line = input().strip()
        if line.upper() == "END":
            break
        u, v, w = map(int, line.split())
        edges.append((u, v, w))

    length, path = longest_path_dag(start, end, edges)

    print(f"\nLongest path length : {length}")
    print(f"Path                : {' '.join(map(str, path))}")