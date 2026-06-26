def lcs_backtrack(v, w):
    n = len(v)
    m = len(w)

    # Initialize score table
    s = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the table
    backtrack = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = 1 if v[i-1] == w[j-1] else 0

            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + match)

            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = "→"
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i][j] = "↘"

    return backtrack, s

def output_lcs(backtrack, v, i, j):
    """Iterative reconstruction — no recursion depth issues."""
    result = []
    while i > 0 and j > 0:
        if backtrack[i][j] == "↘":
            result.append(v[i - 1])  # match — take the character
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            i -= 1                    # came from above — skip
        else:
            j -= 1                    # came from left  — skip
    return "".join(reversed(result))  # built backwards so reverse
 

def print_table(s, backtrack, v, w):
    n, m = len(v), len(w)
    print("\nScore + Backtrack Table:")
    print("        " + "   ".join(f" {c}" for c in w))
    for i in range(n + 1):
        row_label = f"  {v[i-1] if i > 0 else ' '}  "
        row = ""
        for j in range(m + 1):
            arrow = backtrack[i][j] if backtrack[i][j] else " "
            row += f" {s[i][j]}{arrow} "
        print(row_label + row)

if __name__ == "__main__":
    #input    
    print("=" * 45)
    print("       LCS Backtrack")
    print("=" * 45)

    v = input("\nEnter sequence 1 : ").strip().upper()
    w = input("Enter sequence 2 :  ").strip().upper()

    backtrack, s = lcs_backtrack(v, w)
    lcs          = output_lcs(backtrack, v, len(v), len(w))

    print_table(s, backtrack, v, w)

    print(f"\nSequence 1     : {v}")
    print(f"Sequence 2     : {w}")
    print(f"LCS length     : {s[len(v)][len(w)]}")
    print(f"LCS            : {lcs}")