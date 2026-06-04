import random 
from greedy_motifs import build_profile, find_score
from most_probable import most_probable_kmer

def main():
    dna = input("dna: ").strip().split(" ")
    k = int(input("k: ").strip())
    t = int(input("t: ").strip())
    result = random_motif_search(dna, k, t)
    print(" ".join(result))


def random_motif_search(Dna, k, t):
    
    motifs = []
    for i in range(t):
        random_index = random.randint(0, len(Dna[i]) - k)
        motifs.append(Dna[i][random_index:random_index + k])
    Bestmotifs = motifs
    while True:
        profile = build_profile(motifs)
        motifs = []
        for i in range(t): 
            motif = most_probable_kmer(profile, Dna[i], k)
            motifs.append(motif)
        if find_score(motifs) < find_score(Bestmotifs):
            Bestmotifs = motifs
        else:            return Bestmotifs
            
if __name__ == "__main__":    main()