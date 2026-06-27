"""
input : seq 1 and seq 2
output : score , lcs
"""

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
    result = [] # forming the subsequent
    while i > 0 and j > 0:
        if backtrack[i][j] == "↘":
            result.append(v[i - 1])  # match 
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            i -= 1                    # came from above
        else:
            j -= 1                    # came from left
    return "".join(reversed(result))  # built backwards so reverse
 

if __name__ == "__main__":
    
    v = input("sequence 1 : ").strip().upper()
    w = input("sequence 2 :  ").strip().upper()

    backtrack, s = lcs_backtrack(v, w)
    lcs          = output_lcs(backtrack, v, len(v), len(w))

    print(f"LCS length     : {s[len(v)][len(w)]}")
    print(f"LCS            : {lcs}")