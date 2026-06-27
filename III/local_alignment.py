from matrix_source import create_pam250
"""
Local Alignment Problem (Smith-Waterman Algorithm)
Find the highest-scoring local alignment of two sequences using PAM250 matrix.
"""

def local_alignment(seq1, seq2, scoring_matrix, gap_penalty):
    n = len(seq1)
    m = len(seq2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_score = 0
    max_i, max_j = 0, 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Score for match/mismatch
            score = scoring_matrix.get((seq1[i-1], seq2[j-1]), -5)
            
            # Three options
            diagonal = dp[i-1][j-1] + score
            up = dp[i-1][j] + gap_penalty
            left = dp[i][j-1] + gap_penalty
            
            # Take maximum (or 0 to stop local alignment)
            dp[i][j] = max(0, diagonal, up, left)
            
            # Track maximum score and its position
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_i, max_j = i, j
    
    # Traceback from max position
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = max_i, max_j
    
    while i > 0 and j > 0:
        score = scoring_matrix.get((seq1[i-1], seq2[j-1]), -5)
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
        
        # Stop when score reaches 0
        if dp[i][j] == 0:
            break
    
    return max_score, aligned_seq1, aligned_seq2

if __name__ == "__main__":
    seq1 = input().strip()
    seq2 = input().strip()

    pam250 = create_pam250()

    max_score, aligned_seq1, aligned_seq2 = local_alignment(seq1, seq2, pam250, gap_penalty=-5)
    
    print(f"\n{max_score}")
    print(aligned_seq1)
    print(aligned_seq2)