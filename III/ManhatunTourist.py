def manhattan_tourist(n, m, down, right):
    # Initialize score table
    s = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill first column (can only go Down)
    for i in range(1, n + 1):
        s[i][0] = s[i-1][0] + down[i-1][0]

    # Fill first row (can only go Right)
    for j in range(1, m + 1):
        s[0][j] = s[0][j-1] + right[0][j-1]

    # Fill rest of the table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            from_down  = s[i-1][j] + down[i-1][j]
            from_right = s[i][j-1] + right[i][j-1]
            s[i][j]    = max(from_down, from_right)

    return s[n][m], s


def read_matrices():
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line.strip())

    # Split by '-'
    separator = lines.index("-")
    down_lines  = lines[:separator]
    right_lines = lines[separator + 1:]

    down  = [list(map(int, row.split())) for row in down_lines  if row]
    right = [list(map(int, row.split())) for row in right_lines if row]

    return down, right



if __name__ == "__main__":
    n,m= list(map(int,(input("n m: ").strip().split(" "))))
    down , right = read_matrices()
    
    score, s = manhattan_tourist(n, m, down, right)
    print(score)
    