import random
from collections import defaultdict
from Euleriancycle import eulerian_cycle
def main():
    graph = {}

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            node, neighbors = line.split(": ")
            graph[int(node)] = list(map(int, neighbors.split(" ")))
    
    Path = eulerian_path(graph)
    result = " ".join(map(str, Path))
    
    with open("output.txt", "w") as f:
        f.write(result)

def find_start_end(graph):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for node, neighbors in graph.items():
        out_degree[node] += len(neighbors)
        for neighbor in neighbors:
            in_degree[neighbor] += 1
    
    # collect all nodes
    all_nodes = set(in_degree.keys()) | set(out_degree.keys())
    
    start = end = None
    for node in all_nodes:
        diff = out_degree[node] - in_degree[node]
        if diff == 1:       # one more out than in → start
            start = node
        elif diff == -1:    # one more in than out → end
            end = node
    
    return start, end

def eulerian_path(graph):
    adj = defaultdict(list)
    for node, neighbors in graph.items():
        adj[node].extend(neighbors)
    
    start, end = find_start_end(graph)
    
    # Add a virtual edge from end → start to make it a cycle
    adj[end].append(start)
    
    # Run Eulerian cycle
    cycle = eulerian_cycle(adj)

    # Remove the virtual edge (find where start→end appears and cut there)
    for i in range(len(cycle) - 1):
        if cycle[i] == end and cycle[i+1] == start:
            path = cycle[i+1:] + cycle[1:i+1]
    
    return path

if __name__ == "__main__":
    main()
