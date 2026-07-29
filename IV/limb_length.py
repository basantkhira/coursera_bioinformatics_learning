import sys

def limb_length(n, j, D):
    best = float('inf')
    for i in range(n):
        if i == j:
            continue
        for k in range(n):
            if k == j or k == i:
                continue
            val = (D[i][j] + D[j][k] - D[i][k]) // 2
            if val < best:
                best = val
    return best

def solve(input_text):
    lines = input_text.strip().split('\n')
    n = int(lines[0])
    j = int(lines[1])
    D = []
    for line in lines[2:2+n]:
        row = list(map(int, line.split()))
        D.append(row)
    return limb_length(n, j, D)

if __name__ == '__main__':
    input_text = sys.stdin.read()
    print(solve(input_text))