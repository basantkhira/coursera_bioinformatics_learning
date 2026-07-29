from breakpointdistance import colored_edges,parse_genome
from breakpointD import graph_to_genome

def parse_edges(line):
    line = line.strip()
    edges = []
    parts = line.split('), (')
    for part in parts:
        part = part.strip('()')
        a, b = part.split(',')
        edges.append((int(a.strip()), int(b.strip())))
    return edges

def two_break_on_genome_graph(edges, i1, i2, i3, i4):
    new_edges = []
    for (a, b) in edges:
        if (a == i1 and b == i2) or (a == i2 and b == i1):
            continue
        if (a == i3 and b == i4) or (a == i4 and b == i3):
            continue
        new_edges.append((a, b))
    new_edges.append((i1, i3))
    new_edges.append((i2, i4))
    return new_edges

def two_break_on_genome(P, i1, i2, i3, i4):
    edges = colored_edges(P)
    edges = two_break_on_genome_graph(edges, i1, i2, i3, i4)
    P_new = graph_to_genome(edges)
    return P_new

def format_genome(P):
    output = ''
    for chromosome in P:
        output += '(' + ' '.join(f'+{x}' if x > 0 else str(x) for x in chromosome) + ')'
    return output
 
 
def find_nontrivial_cycle(red_edges, blue_edges):
    red_adj = {}
    for a, b in red_edges:
        red_adj[a] = b
        red_adj[b] = a
    blue_adj = {}
    for a, b in blue_edges:
        blue_adj[a] = b
        blue_adj[b] = a
 
    nodes = set(red_adj.keys()) | set(blue_adj.keys())
    visited = set()
 
    for start in nodes:
        if start in visited:
            continue
        cycle_nodes = [start]
        visited.add(start)
        current = start
        use_red = True
        while True:
            nxt = red_adj[current] if use_red else blue_adj[current]
            use_red = not use_red
            if nxt == start:
                break
            cycle_nodes.append(nxt)
            visited.add(nxt)
            current = nxt
 
        if len(cycle_nodes) > 2:
            i2 = cycle_nodes[1]
            i3 = cycle_nodes[2]
            i1 = red_adj[i2]
            i4 = red_adj[i3]
            return (i1, i2, i3, i4)
 
    return None
 
 
def two_break_sorting(P, Q):
    results = [P]
    blue_edges = colored_edges(Q)
    red_edges = colored_edges(P)
 
    while True:
        cyc = find_nontrivial_cycle(red_edges, blue_edges)
        if cyc is None:
            break
        i1, i2, i3, i4 = cyc
        P = two_break_on_genome(P, i1, i2, i4, i3)
        results.append(P)
        red_edges = colored_edges(P)
 
    return results
 
 
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
 
    P = parse_genome(line1)
    Q = parse_genome(line2)
 
    scenario = two_break_sorting(P, Q)
    for genome in scenario:
        print(format_genome(genome))