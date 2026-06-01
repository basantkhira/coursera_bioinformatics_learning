#Clump Finding Problem
from frequent import FrequencyTable

def main():
    with open("E_coli.txt") as f:
        g = f.read().strip()

    k = int(input("k:"))
    L = int(input("L:"))
    t = int(input("t:"))

    result = FindClumps(g, k, L, t)

    with open("result.txt", "w") as f:
        for p in result:
            f.write("\n".join(result))
    
    count = 0
    for p in result:
        count += 1
    print(f"Number of patterns: {count}")

def FindClumps(g, k, L, t):
    patterns = set()
    n = len(g)

    window = g[0:L]
    freqMap = FrequencyTable(window, k)
    
    for s in freqMap:
        if freqMap[s] >= t:
            patterns.add(s)

        # sliding
    for i in range(1, n - L + 1):

        # pattern خرج
        firstPattern = g[i-1:i-1+k]
        freqMap[firstPattern] -= 1

        # pattern دخل
        lastPattern = g[i+L-k:i+L]
        freqMap[lastPattern] += 1

        # check
        if freqMap[lastPattern] >= t:
            patterns.add(lastPattern)

    return patterns

if __name__ == "__main__":    main()