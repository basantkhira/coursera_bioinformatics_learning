"""
Global Alignment Problem (Needleman-Wunsch Algorithm)
Find the highest-scoring alignment of two strings using a scoring matrix.
"""

def global_alignment(seq1, seq2, match, mismatch, gap_penalty):    
    n = len(seq1)
    m = len(seq2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize first row and column (all gaps)
    for i in range(n + 1):
        dp[i][0] = i * gap_penalty
    for j in range(m + 1):
        dp[0][j] = j * gap_penalty
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            
            diagonal = dp[i-1][j-1] + score
            up = dp[i-1][j] + gap_penalty
            left = dp[i][j-1] + gap_penalty
            
            dp[i][j] = max(diagonal, up, left)
    
    # Traceback: reconstruct the alignment
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = n, m
    
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            
            diagonal = dp[i-1][j-1] + score
            
            if dp[i][j] == diagonal:
                aligned_seq1 = seq1[i-1] + aligned_seq1
                aligned_seq2 = seq2[j-1] + aligned_seq2
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j] + gap_penalty:
                aligned_seq1 = seq1[i-1] + aligned_seq1
                aligned_seq2 = "-" + aligned_seq2
                i -= 1
            else:
                aligned_seq1 = "-" + aligned_seq1
                aligned_seq2 = seq2[j-1] + aligned_seq2
                j -= 1
        elif i > 0:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            j -= 1
    
    return dp[n][m], aligned_seq1, aligned_seq2


if __name__ == "__main__":

    line1 = input().split()
    match = int(line1[0])
    mismatch = int(line1[1])
    gap_penalty = int(line1[2])

    seq1 = input("seq1: ").strip()
    seq2 = input("seq2: ").strip()
    
    
    score,aligned1,aligned2 = global_alignment(seq1, seq2, match, mismatch, gap_penalty)
    
    print(f"\nAlignment Score: {score}")
    print(f"\nAligned Sequence 1: {aligned1}")
    print(f"Aligned Sequence 2: {aligned2}")
        
    