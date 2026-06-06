import random 
from greedy_motifs import build_profile, score
from most_probable import most_probable_kmer

def main():
    dna = input("dna: ").strip().split(" ")
    k = int(input("k: ").strip())
    t = int(input("t: ").strip())
    result = run_multiple_runs(dna, k, t,1000)
    print(" ".join(result))

def random_motif_search(Dna, k, t):
    # random motifs 
    motifs = list()
    for i in range(t):
        r = random_generator(Dna,i,k)
        motifs.append(Dna[i][r : r + k])
    
    Bestmotifs = motifs
    # running 
    while True:
        profile = build_profile(motifs)
        new_motifs = []
        for i in range(t): 
            motif = most_probable_kmer(profile, Dna[i], k)
            new_motifs.append(motif)
        if score(new_motifs) < score(Bestmotifs):
            Bestmotifs = new_motifs
            motifs = new_motifs
        else:            
            return Bestmotifs
            
def run_multiple_runs(Dna, k, t, iterations):
    best_overall_motifs = []
    best_score = float('inf')
    # Step 3: Loop multiple times to find the globally optimal motif
    for _ in range(iterations):
        motifs = random_motif_search(Dna, k, t)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_overall_motifs = motifs
    return best_overall_motifs


def random_generator(Dna,i,k):
    random_index = random.randint(0, len(Dna[i]) - k)
    return random_index

    
if __name__ == "__main__":   
    main()