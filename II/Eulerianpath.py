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
    is_circuit = (start is None)
    
    if is_circuit:
        # pick any node that has outgoing edges as start
        for node in adj:
            if adj[node]:
                start = node
                break
    else:
        # convert path → circuit with a virtual edge
        adj[end].append(start)

    # Hierholzer
    stack, cycle = [start], []
    while stack:
        v = stack[-1]
        if adj[v]:
            stack.append(adj[v].pop())
        else:
            cycle.append(stack.pop())
    cycle.reverse()

    if is_circuit:
        return cycle

    # cut the virtual edge (end → start) out of the cycle
    for i in range(len(cycle) - 1):
        if cycle[i] == end and cycle[i + 1] == start:
            path = cycle[i + 1:] + cycle[1:i + 1]
            return path, False

    return cycle  

if __name__ == "__main__":
    main()
