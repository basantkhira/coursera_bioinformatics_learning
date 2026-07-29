def cycle_to_chromosome(nodes):
    chromosome = [0] * (len(nodes) // 2)
    for j in range(len(nodes) // 2):
        if nodes[2*j] < nodes[2*j + 1]:
            chromosome[j] = nodes[2*j + 1] // 2
        else:
            chromosome[j] = -nodes[2*j] // 2
    return chromosome

def black_partner(x):
    return x + 1 if x % 2 == 1 else x - 1

def build_cycles(edges, num_nodes):
    colored = {}
    for a, b in edges:
        colored[a] = b
        colored[b] = a

    visited = set()
    cycles = []
    for start in range(1, num_nodes + 1):
        if start in visited:
            continue
        cycle = []
        node = start
        use_black = True
        while True:
            cycle.append(node)
            visited.add(node)
            if use_black:
                nxt = black_partner(node)
            else:
                nxt = colored[node]
            use_black = not use_black
            if nxt == start:
                break
            node = nxt
        cycles.append(cycle)
    return cycles

def graph_to_genome(edges):
    num_nodes = max(max(a, b) for a, b in edges)
    cycles = build_cycles(edges, num_nodes)
    P = []
    for cycle in cycles:
        chromosome = cycle_to_chromosome(cycle)
        P.append(chromosome)
    return P

if __name__ == "__main__":
    line = input().strip()
    edges = []
    parts = line.split('), (')
    for part in parts:
        part = part.strip('()')
        a, b = part.split(',')
        edges.append((int(a.strip()), int(b.strip())))

    P = graph_to_genome(edges)

    output = ''
    for chromosome in P:
        output += '(' + ' '.join(f'+{x}' if x > 0 else str(x) for x in chromosome) + ')'
    print(output)