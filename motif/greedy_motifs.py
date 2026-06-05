from most_probable import most_probable_kmer

def main():
    dna = input("dna: ").strip().split(" ")
    k = int(input("k: ").strip())
    t = int(input("t: ").strip())
    result = greedy(dna, k, t)
    print(" ".join(result))
    
    
def greedy(dna,k,t):
    Bestmotifs = best_motifs(dna, k)
    first = dna[0]
    for i in range(len(first) - k + 1):
        Motif1 = first[i:i+k]
        Motifs = [Motif1]
        for j in range(1, t): 
            Profile = build_profile(Motifs)
            Motifj = most_probable_kmer(Profile, dna[j], k)
            Motifs.append(Motifj)
        if score(Motifs) < score(Bestmotifs):
            Bestmotifs = Motifs
    return Bestmotifs
        
        
def best_motifs(dna, k):
    best_motifs = []
    for string in dna:
        best_motif = string[:k]
        best_motifs.append(best_motif)
    return best_motifs

"""modificatin: apply laplace's rule of succession to avoid zero probabilities in the profile matrix."""
def build_profile(motifs):
    profile = {}
    n = len(motifs)
    k = len(motifs[0])
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            if i not in profile:
                profile[i] = {'A': 1, 'C': 1, 'G': 1, 'T': 1} # to avoid zero
            profile[i][nucleotide] += 1
    # normalize
    for i in profile:
        for nuc in profile[i]:
            profile[i][nuc] /= (n + 4) # add 4 for the pseudocounts
    return profile

def score(motifs):
    score = 0
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        consensus = max(set(column), key=column.count)  
        score += sum(1 for nuc in column if nuc != consensus)    
    return score

if __name__ == "__main__":  main()