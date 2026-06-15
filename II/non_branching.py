def main():
    
    graph = {}

    with open("input.txt", "r") as f:
        for line in f:   
            line = line.strip()     
            node, *neighbors = line.split(":")      
            graph[node] = [neighbor for neighbor in neighbors[0].split()]

    print("Graph:", graph)
    paths = maximal_non_branching_paths(graph)
    for path in paths:
        print(" ".join(path))
    

    
    
def maximal_non_branching_paths(graph):
    
    # Calculate in-degree and out-degree for each node
    in_degree = {v: 0 for v in graph}
    out_degree = {v: len(graph[v]) for v in graph}
    
    for v in graph:
        for w in graph[v]:
            if w not in in_degree:
                in_degree[w] = 0
                out_degree[w] = len(graph.get(w, []))
            in_degree[w] += 1
    
    def is_1_in_1_out(node):
        return in_degree.get(node, 0) == 1 and out_degree.get(node, 0) == 1
    
    paths = []
    visited_edges = set()
    
    # Find non-branching paths starting from non-1-in-1-out nodes
    for v in graph:
        if not is_1_in_1_out(v):
            if out_degree.get(v, 0) > 0:
                for w in graph[v]:
                    path = [v, w]
                    visited_edges.add((v, w))
                    
                    current = w
                    while is_1_in_1_out(current):
                        next_node = graph[current][0]
                        visited_edges.add((current, next_node))
                        path.append(next_node)
                        current = next_node
                    
                    paths.append(path)
    
    # Find isolated cycles (nodes not yet visited) where every node is 1-in-1-out
    for start in graph:
        # Check if this node is 1-in-1-out and has unvisited edges
        if is_1_in_1_out(start):
            if any((start, w) not in visited_edges for w in graph[start]):
                # Trace the cycle
                cycle = [start]
                visited_edges.add((start, graph[start][0]))
                current = graph[start][0]
                
                while current != start:
                    cycle.append(current)
                    next_node = graph[current][0]
                    visited_edges.add((current, next_node))
                    current = next_node
                
                cycle.append(start)  # close the cycle
                paths.append(cycle)
    
    return paths

if __name__ == "__main__":
    main()