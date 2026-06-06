#median string finding problem 
from hamming import hamming 
from kmerfinder import Neighbors

def main():
    k = int(input("k: ").strip())
    with open("input.txt","r") as f:
        dna = [line.strip() for line in f]
    print(median_string(dna, k))


def median_string(dna, k):
    distance = float('inf')
    patterns = Allstrings(k,dna)
    Median = [] # edit from none 
    for p in patterns:
        if distance > d(p, dna):
             distance = d(p,dna)
             Median.append(p) # edit from = p
    return Median

def d(pattern, Dna):
    k = len(pattern)
    distance = 0
    for string in Dna:
        Hdistance = float('inf')
        for i in range(len(string) - k + 1):
            Npattern = string[i:i+k]
            if Hdistance > hamming(pattern, Npattern):
                Hdistance = hamming(pattern, Npattern)
        distance += Hdistance
    return distance


def Allstrings(k,dna):
    patterns = set()
    for string in dna :
        for i in range(len(string) - k + 1):
            pattern = string[i:i+k]
            neighborhood = Neighbors(pattern, k)
            for neighbor in neighborhood:
                patterns.add(neighbor)
    return patterns 
    
    
if __name__ == "__main__":
    main()