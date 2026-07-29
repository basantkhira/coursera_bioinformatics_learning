def chromosome_to_cycle(chromosome):
    nodes = [0] * (2 * len(chromosome))
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            nodes[2*j] = 2*i - 1
            nodes[2*j + 1] = 2*i
        else:
            nodes[2*j] = -2*i
            nodes[2*j + 1] = -2*i - 1
    return nodes

def colored_edges(P):
    edges = []
    for chromosome in P:
        nodes = chromosome_to_cycle(chromosome)
        n = len(chromosome)
        for j in range(n):
            a = nodes[2*j + 1]
            b = nodes[(2*j + 2) % (2*n)]
            edges.append((a, b))
    return edges

def parse_genome(line):
    line = line.strip()
    chromosomes = []
    parts = line.replace('(', ' (').strip().split('(')
    for part in parts:
        part = part.strip()
        if not part:
            continue
        part = part.rstrip(')')
        chromosome = [int(x) for x in part.split()]
        chromosomes.append(chromosome)
    return chromosomes

def two_break_distance(P, Q):
    edges_P = colored_edges(P)
    edges_Q = colored_edges(Q)
    
    # total number of synteny blocks
    n = sum(len(chromosome) for chromosome in P)
    
    # build adjacency using combined red+blue edges
    adj = {}
    for a, b in edges_P + edges_Q:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    
    visited = set()
    cycles = 0
    for node in adj:
        if node not in visited:
            cycles += 1
            stack = [node]
            visited.add(node)
            while stack:
                curr = stack.pop()
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
    
    return n - cycles

if __name__ == "__main__":
    # Read input
    line1 = input().strip()
    line2 = input().strip()

    P = parse_genome(line1)
    Q = parse_genome(line2)

    result = two_break_distance(P, Q)
    print(result)