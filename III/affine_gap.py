def affine_alignment(s1, s2, match, mismatch, sigma, eps):
    
    n, m = len(s1), len(s2)
    NEG = float('-inf')

    mid = [[NEG]*(m+1) for _ in range(n+1)]
    low = [[NEG]*(m+1) for _ in range(n+1)]  
    upp = [[NEG]*(m+1) for _ in range(n+1)]  
    
    mid[0][0] = 0
    for i in range(1, n+1):
        low[i][0] = -sigma - (i-1)*eps
        mid[i][0] = low[i][0]
    for j in range(1, m+1):
        upp[0][j] = -sigma - (j-1)*eps
        mid[0][j] = upp[0][j]

    back_mid = [[None]*(m+1) for _ in range(n+1)]
    back_low = [[None]*(m+1) for _ in range(n+1)]
    back_upp = [[None]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            open_l = mid[i-1][j] - sigma
            ext_l = low[i-1][j] - eps
            low[i][j] = max(open_l, ext_l)
            back_low[i][j] = 'M' if open_l >= ext_l else 'L'

            open_u = mid[i][j-1] - sigma
            ext_u = upp[i][j-1] - eps
            upp[i][j] = max(open_u, ext_u)
            back_upp[i][j] = 'M' if open_u >= ext_u else 'U'

            s = match if s1[i-1] == s2[j-1] else -mismatch
            diag = mid[i-1][j-1] + s
            best = max(diag, low[i][j], upp[i][j])
            mid[i][j] = best
            back_mid[i][j] = 'D' if best == diag else ('L' if best == low[i][j] else 'U')

    score = mid[n][m]
    a1, a2 = [], []
    i, j = n, m
    state = 'M'
    while i > 0 or j > 0:
        if state == 'M':
            if i == 0: state = 'U'; continue
            if j == 0: state = 'L'; continue
            move = back_mid[i][j]
            if move == 'D':
                a1.append(s1[i-1]); a2.append(s2[j-1]); i -= 1; j -= 1; state = 'M'
            else:
                state = move
        elif state == 'L':
            a1.append(s1[i-1]); a2.append('-')
            move = back_low[i][j]; i -= 1
            state = 'M' if move == 'M' else 'L'
        else:
            a1.append('-'); a2.append(s2[j-1])
            move = back_upp[i][j]; j -= 1
            state = 'M' if move == 'M' else 'U'

    a1.reverse(); a2.reverse()
    return score, ''.join(a1), ''.join(a2)



if __name__ == "__main__":
    
    line = input("input").split()
    match = int(line[0])
    mismatch = int(line[1])
    sigma = int(line[2])
    eps = int(line[3])
        
    s1 = input("seq1: ").strip()
    s2 = input("seq2: ").strip()
    
    score, a1 , a2 = affine_alignment(s1, s2, match, mismatch, sigma, eps)
    
    print(score)
    print(a1)
    print(a2)
