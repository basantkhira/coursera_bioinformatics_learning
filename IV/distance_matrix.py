import sys
from collections import defaultdict

#converting the input into a distance matrix
def solve(input_text):
    lines = input_text.strip().split('\n')
    n = int(lines[0])
    
    graph = defaultdict(list)
    max_node = n - 1
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        left, rest = line.split('->')
        b, c = rest.split(':')
        a = int(left)
        b = int(b)
        c = int(c)
        graph[a].append((b, c))
        max_node = max(max_node, a, b)
    
 # clculating the distance of each node from every other node and storing it in a distance matrix
    def distances_from(source):
        dist = {source: 0}
        stack = [source]
        while stack:
            u = stack.pop()
            for v, w in graph[u]:
                if v not in dist:
                    dist[v] = dist[u] + w
                    stack.append(v)
        return dist
    # building the distance matrix
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        d = distances_from(i)
        for j in range(n):
            matrix[i][j] = d[j]
    
    out_lines = []
    for row in matrix:
        out_lines.append('\t'.join(map(str, row)))
    return '\n'.join(out_lines)


if __name__ == '__main__':
    input_text = sys.stdin.read()
    result = solve(input_text)
    with open('output.txt', 'w') as f:
        f.write(result)
    print("Done")