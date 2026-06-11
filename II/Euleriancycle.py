import random
from collections import defaultdict

def main():
    graph = {}

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            node, neighbors = line.split(": ")
            graph[int(node)] = list(map(int, neighbors.split(" ")))
    
    cycle = eulerian_cycle(graph)
    result = " ".join(map(str, cycle))
    
    with open("output.txt", "w") as f:
        f.write(result)


def eulerian_cycle(graph):
    # copy adjacency list with edge counts to manipulate 
    adj = defaultdict(list)
    for node, neighbors in graph.items():
        adj[node].extend(neighbors)
    
    # Start from any node (ex. node[0])
    start = list(adj.keys())[0]
    cycle = [start]
    
    # Step 1: randomly walk until stuck (first partial cycle)
    current = start
    while adj[current]:
        next_node = adj[current].pop(random.randint(0, len(adj[current]) - 1))
        cycle.append(next_node)
        current = next_node
    
    # Step 2: while unexplored edges exist
    while any(adj[node] for node in cycle):
        # Find a node in cycle that still has unexplored edges
        for i, node in enumerate(cycle):
            if adj[node]:
                new_start_idx = i
                break
        
        # Re-form cycle starting from new_start
        # cycle' = cycle[new_start_idx:] + cycle[1:new_start_idx+1]
        cycle = cycle[new_start_idx:] + cycle[1:new_start_idx + 1]
        
        # Continue walking from new_start
        current = cycle[-1]  # which is new_start again
        while adj[current]:
            next_node = adj[current].pop(random.randint(0, len(adj[current]) - 1))
            cycle.append(next_node)
            current = next_node
    
    return cycle

if __name__ == "__main__":
    main()
