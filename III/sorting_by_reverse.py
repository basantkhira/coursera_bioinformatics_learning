def greedy_sorting(P):
    P = list(P)
    n = len(P)
    approx = 0

    for k in range(1, n + 1):
        # find element k or -k in P[k-1:]
        if P[k-1] != k:
            # find position of k or -k
            for i in range(k, n + 1):
                if abs(P[i-1]) == k:
                    P[k-1:i] = [-x for x in reversed(P[k-1:i])]
                    approx += 1
                    with open('output.txt', 'a') as f:
                        f.write(' '.join(('+'+str(x) if x>0 else str(x)) for x in P) + '\n')
                    
                    break

        if P[k-1] == -k:
            P[k-1] = k
            approx += 1
            with open('output.txt', 'a') as f:
                        f.write(' '.join(('+'+str(x) if x>0 else str(x)) for x in P) + '\n')
            

    return approx


if __name__ == "__main__":
    line = input().strip().split(" ")
    P = []
    for x in line:
        if x.startswith('+'):
            P.append(int(x[1:]))
        else:
            P.append(int(x))
    result = greedy_sorting(P)
    print('Approximate number of reversals: ' + str(result))