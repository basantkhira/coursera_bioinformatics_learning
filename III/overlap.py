"""
Overlap Alignment Problem - FIXED VERSION
Find a highest-scoring overlap alignment between two strings.
"""
def overlap_alignment(v, w, match, mismatch, gap_penalty):
    n = len(v)
    m = len(w)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Free to skip prefix of v (first row = 0)
    # But gaps in w (column 0) cost something
    for i in range(n + 1):
        dp[i][0] = i * gap_penalty
    for j in range(m + 1):
        dp[0][j] = 0  # free prefix skip of v
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = match if v[i-1] == w[j-1] else mismatch
            dp[i][j] = max(
                dp[i-1][j-1] + score,
                dp[i-1][j] + gap_penalty,
                dp[i][j-1] + gap_penalty
            )
    
    # Max score must be at last row OR last column
    max_score = -float('inf')
    max_i, max_j = n, m
    
    for j in range(1, m + 1):          # last row
        if dp[n][j] > max_score:
            max_score = dp[n][j]
            max_i, max_j = n, j
    
    for i in range(1, n + 1):          # last column
        if dp[i][m] > max_score:
            max_score = dp[i][m]
            max_i, max_j = i, m
    
    # Traceback
    aligned_v, aligned_w = "", ""
    i, j = max_i, max_j
    
    while i > 0 and j > 0:
        score = match if v[i-1] == w[j-1] else mismatch
        if dp[i][j] == dp[i-1][j-1] + score:
            aligned_v = v[i-1] + aligned_v
            aligned_w = w[j-1] + aligned_w
            i -= 1; j -= 1
        elif dp[i][j] == dp[i-1][j] + gap_penalty:
            aligned_v = v[i-1] + aligned_v
            aligned_w = "-" + aligned_w
            i -= 1
        else:
            aligned_v = "-" + aligned_v
            aligned_w = w[j-1] + aligned_w
            j -= 1

    
    
    # Remaining v (i > 0) is the free prefix skip — don't include it
    
    return max_score, aligned_v, aligned_w


# Read input - FIXED ORDER
v = input().strip()
w = input().strip()

line1 = input().split()
match = int(line1[0])
mismatch = -int(line1[1])
gap_penalty = -int(line1[2])

# Compute overlap alignment
max_score, aligned_v, aligned_w = overlap_alignment(v, w, match, mismatch, gap_penalty)

# Output
print(max_score)
print(aligned_v)
print(aligned_w)