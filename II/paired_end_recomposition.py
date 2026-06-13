import sys
from collections import defaultdict


def build_paired_debruijn(paired_reads):
    graph = defaultdict(list)
    for read1, read2 in paired_reads:
        left  = (read1[:-1], read2[:-1])   # (k-1)-mer prefixes
        right = (read1[1:],  read2[1:])    # (k-1)-mer suffixes
        graph[left].append(right)
    return graph


def eulerian_path(graph):
    in_deg  = defaultdict(int)
    out_deg = defaultdict(int)
    all_nodes = set()
    for node, neighbors in graph.items():
        out_deg[node] += len(neighbors)
        all_nodes.add(node)
        for nb in neighbors:
            in_deg[nb] += 1
            all_nodes.add(nb)

    # True path start: out - in == 1; if none exists it's a circuit
    start = None
    for node in all_nodes:
        if out_deg[node] - in_deg[node] == 1:
            start = node
            break

    is_circuit = (start is None)
    if is_circuit:
        for node in all_nodes:
            if out_deg[node] > 0:
                start = node
                break

    # Hierholzer's algorithm
    adj = defaultdict(list)
    for node, neighbors in graph.items():
        adj[node].extend(neighbors)

    stack, path = [start], []
    while stack:
        v = stack[-1]
        if adj[v]:
            stack.append(adj[v].pop())
        else:
            path.append(stack.pop())

    path.reverse()
    return path, is_circuit


def path_to_genome(path, k, d):
    # Walk the paired-node path to rebuild two parallel strings
    top    = path[0][0]
    bottom = path[0][1]
    for node in path[1:]:
        top    += node[0][-1]
        bottom += node[1][-1]

    # top covers genome[0 .. ], bottom covers genome[k+d .. ]
    # Their shared region must agree
    offset  = k + d
    overlap = len(top) - offset
    if overlap <= 0:
        return None
    if top[offset:] != bottom[:overlap]:
        return None

    return top + bottom[overlap:]


def reconstruct(paired_reads, k, d):
    graph = build_paired_debruijn(paired_reads)
    path, is_circuit = eulerian_path(graph)

    result = path_to_genome(path, k, d)
    if result:
        return result

    # For Eulerian circuits the start is arbitrary — try every rotation
    if is_circuit and len(path) > 1:
        n = len(path) - 1
        for i in range(1, n):
            rotated = path[i:n] + path[1:i+1]
            result  = path_to_genome(rotated, k, d)
            if result:
                return result

    return None


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    d = int(data[1])
    paired_reads = []
    for token in data[2:]:
        if '|' in token:
            a, b = token.split('|', 1)
            paired_reads.append((a, b))
    print(reconstruct(paired_reads, k, d))


if __name__ == "__main__":
    main()