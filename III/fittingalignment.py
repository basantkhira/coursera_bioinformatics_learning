"""
Fitting Alignment Problem
Find a highest-scoring alignment of a smaller string (v) within a larger string (w).
The alignment can start and end anywhere in w, but must include all of v.
Uses dynamic programming (similar to Smith-Waterman, but different traceback).
"""
def create_BLOSUM26():
    matrix_data = {
    'A': {'A': 4, 'C': 0, 'D': -2, 'E': -1, 'F': -2, 'G': 0, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1, 'T': 0, 'V': 0, 'W': -3, 'Y': -2}, 
    'C': {'A': 0, 'C': 9, 'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1, 'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'Y': -2}, 
    'D': {'A': -2, 'C': -3, 'D': 6, 'E': 2, 'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1, 'P': -1, 'Q': 0, 'R': -2, 'S': 0, 'T': -1, 'V': -3, 'W': -4, 'Y': -3}, 
    'E': {'A': -1, 'C': -4, 'D': 2, 'E': 5, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -3, 'M': -2, 'N': 0, 'P': -1, 'Q': 2, 'R': 0, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'Y': -2}, 
    'F': {'A': -2, 'C': -2, 'D': -3, 'E': -3, 'F': 6, 'G': -3, 'H': -1, 'I': 0, 'K': -3, 'L': 0, 'M': 0, 'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1, 'Y': 3}, 
    'G': {'A': 0, 'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6, 'H': -2, 'I': -4, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': -2, 'Q': -2, 'R': -2, 'S': 0, 'T': -2, 'V': -3, 'W': -2, 'Y': -3}, 
    'H': {'A': -2, 'C': -3, 'D': -1, 'E': 0, 'F': -1, 'G': -2, 'H': 8, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': 1, 'P': -2, 'Q': 0, 'R': 0, 'S': -1, 'T': -2, 'V': -3, 'W': -2, 'Y': 2}, 
    'I': {'A': -1, 'C': -1, 'D': -3, 'E': -3, 'F': 0, 'G': -4, 'H': -3, 'I': 4, 'K': -3, 'L': 2, 'M': 1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3, 'W': -3, 'Y': -1}, 
    'K': {'A': -1, 'C': -3, 'D': -1, 'E': 1, 'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5, 'L': -2, 'M': -1, 'N': 0, 'P': -1, 'Q': 1, 'R': 2, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'Y': -2}, 
    'L': {'A': -1, 'C': -1, 'D': -4, 'E': -3, 'F': 0, 'G': -4, 'H': -3, 'I': 2, 'K': -2, 'L': 4, 'M': 2, 'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1, 'W': -2, 'Y': -1}, 
    'M': {'A': -1, 'C': -1, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 1, 'K': -1, 'L': 2, 'M': 5, 'N': -2, 'P': -2, 'Q': 0, 'R': -1, 'S': -1, 'T': -1, 'V': 1, 'W': -1, 'Y': -1}, 
    'N': {'A': -2, 'C': -3, 'D': 1, 'E': 0, 'F': -3, 'G': 0, 'H': 1, 'I': -3, 'K': 0, 'L': -3, 'M': -2, 'N': 6, 'P': -2, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -3, 'W': -4, 'Y': -2}, 
    'P': {'A': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': -2, 'P': 7, 'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'Y': -3}, 
    'Q': {'A': -1, 'C': -3, 'D': 0, 'E': 2, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -2, 'M': 0, 'N': 0, 'P': -1, 'Q': 5, 'R': 1, 'S': 0, 'T': -1, 'V': -2, 'W': -2, 'Y': -1}, 
    'R': {'A': -1, 'C': -3, 'D': -2, 'E': 0, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 2, 'L': -2, 'M': -1, 'N': 0, 'P': -2, 'Q': 1, 'R': 5, 'S': -1, 'T': -1, 'V': -3, 'W': -3, 'Y': -2}, 
    'S': {'A': 1, 'C': -1, 'D': 0, 'E': 0, 'F': -2, 'G': 0, 'H': -1, 'I': -2, 'K': 0, 'L': -2, 'M': -1, 'N': 1, 'P': -1, 'Q': 0, 'R': -1, 'S': 4, 'T': 1, 'V': -2, 'W': -3, 'Y': -2}, 
    'T': {'A': 0, 'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0, 'P': -1, 'Q': -1, 'R': -1, 'S': 1, 'T': 5, 'V': 0, 'W': -2, 'Y': -2}, 
    'V': {'A': 0, 'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3, 'K': -2, 'L': 1, 'M': 1, 'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0, 'V': 4, 'W': -3, 'Y': -1}, 
    'W': {'A': -3, 'C': -2, 'D': -4, 'E': -3, 'F': 1, 'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2, 'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'Y': 2}, 
    'Y': {'A': -2, 'C': -2, 'D': -3, 'E': -2, 'F': 3, 'G': -3, 'H': 2, 'I': -1, 'K': -2, 'L': -1, 'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2, 'Y': 7}}
    
    BLOSUM26_flat = {}
    for aa1 in matrix_data:
        for aa2 in matrix_data[aa1]:
            BLOSUM26_flat[(aa1, aa2)] = matrix_data[aa1][aa2]
    
    return BLOSUM26_flat

def fitting_alignment(v, w, match,mismatch, gap_penalty=-1):
    
    n = len(v)
    m = len(w)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i * gap_penalty
        
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #match_score = score_matrix.get((v[i-1], w[j-1]), gap_penalty)
            if v[i-1] == w[j-1]:
                score = match
            else:
                score = mismatch
            # Three options
            diagonal = dp[i-1][j-1] + score
            up = dp[i-1][j] + gap_penalty        # Gap in w
            left = dp[i][j-1] + gap_penalty      # Gap in v
            
            # Take maximum
            dp[i][j] = max(diagonal, up, left)
    
    # Find the maximum score in the last row (v fully aligned)
    # We want max score where all of v is used
    max_score = -float('inf')
    max_j = 0
    for j in range(m + 1):
        if dp[n][j] > max_score:
            max_score = dp[n][j]
            max_j = j
    
    # Traceback from (n, max_j) to (0, ?)
    aligned_v = ""
    aligned_w = ""
    i = n
    j = max_j
    
    while i > 0:
        #match_score = score_matrix.get((v[i-1], w[j-1] if j > 0 else '-'), gap_penalty)
        if v[i-1] == w[j-1]:
            score = match
        else:
            score = mismatch
        
        if j > 0:
            diagonal = dp[i-1][j-1] + score
        else:
            diagonal = -float('inf')
        
        up = dp[i-1][j] + gap_penalty if i > 0 else -float('inf')
        left = dp[i][j-1] + gap_penalty if j > 0 else -float('inf')
        
        # Prefer diagonal > up > left
        if j > 0 and dp[i][j] == diagonal:
            aligned_v = v[i-1] + aligned_v
            aligned_w = w[j-1] + aligned_w
            i -= 1
            j -= 1
        elif dp[i][j] == up:
            aligned_v = v[i-1] + aligned_v
            aligned_w = "-" + aligned_w
            i -= 1
        elif j > 0 and dp[i][j] == left:
            aligned_v = "-" + aligned_v
            aligned_w = w[j-1] + aligned_w
            j -= 1
        else:
            # Reached beginning
            break
    
    
    
    return max_score, aligned_v, aligned_w

if __name__ == "__main__":
    line1 = input().split()
    match = int(line1[0])
    mismatch = -int(line1[1])
    gap_penalty = -int(line1[2])
    
    # Read input
    v = input().strip()
    w = input().strip()

    score_matrix = create_BLOSUM26()

    # Compute fitting alignment
    max_score, aligned_v, aligned_w = fitting_alignment(v, w, match,mismatch, gap_penalty)

    # Output
    print(max_score)
    print(aligned_v)
    print(aligned_w)