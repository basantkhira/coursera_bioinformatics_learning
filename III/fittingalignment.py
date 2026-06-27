"""
Fitting Alignment Problem
Find a highest-scoring alignment of a smaller string (v) within a larger string (w).
The alignment can start and end anywhere in w, but must include all of v.
Uses dynamic programming (similar to Smith-Waterman, but different traceback).
"""

def fitting_alignment(v, w, match,mismatch, gap_penalty=-1):
    
    n = len(v)
    m = len(w)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i * gap_penalty
        
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            #match_score = score_matrix.get((v[i-1], w[j-1]), gap_penalty) in case of blosum26 matrix
            if v[i-1] == w[j-1]:
                score = match
            else:
                score = mismatch
                
            diagonal = dp[i-1][j-1] + score
            up = dp[i-1][j] + gap_penalty        
            left = dp[i][j-1] + gap_penalty      
            
            dp[i][j] = max(diagonal, up, left)
    

    max_score = -float('inf')
    max_j = 0
    for j in range(m + 1):
        if dp[n][j] > max_score:
            max_score = dp[n][j]
            max_j = j
    
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
        
        # traceback
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

    # Compute fitting alignment
    max_score, aligned_v, aligned_w = fitting_alignment(v, w, match,mismatch, gap_penalty)

    # Output
    print(max_score)
    print(aligned_v)
    print(aligned_w)