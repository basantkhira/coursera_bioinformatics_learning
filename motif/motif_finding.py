#output : (k,m)motif 
from kmerfinder import Neighbors
from hamming import hamming 

def main ():
    #input : k, mismatch, collection of dna strings
    k = int(input("K: "))
    m = int(input("M: "))
    genome = input("genome: ").strip().split()
    print(motif(genome, k, m))

#Brute force approach(EXahustive search)
def motif(dna,k,m):
    patterns = set()
    first = dna[0]
    for s in range(len(first) - k + 1):
        pattern = first[s:s+k]
        neighborhood = Neighbors(pattern,m)
        for neighbor in neighborhood:     
            if all(any(hamming(neighbor, string[i:i+k]) <= m 
                   for i in range(len(string) - k + 1)) for string in dna): 
                patterns.add(neighbor)                    
    return patterns

if __name__ == "__main__":    main()