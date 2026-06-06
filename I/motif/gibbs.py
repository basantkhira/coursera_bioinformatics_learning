import random 
from greedy_motifs import build_profile, score

def main():
    dna = input("dna: ").strip().split(" ")
    k = int(input("k: ").strip())
    t = int(input("t: ").strip())
    n = int(input("n: ").strip())
    best_motifs,best_score = run_gibbs_sampler(dna,k,t,n,runs=20)
    print(" ".join(best_motifs))
    print("Best Score:", best_score)


def gibbs_sampler(dna, k, t, n):
    # Step 1: Random initialization
    motifs = [random.choice([seq[i:i+k] for i in range(len(seq) - k + 1)])
              for seq in dna]
    
    best_motifs = motifs[:]
    best_score = score(best_motifs)
    
    # Step 2: n iterations
    for _ in range(n):
        # Pick a random string i to remove
        i = random.randint(0, t - 1)
        
        # Build profile from all motifs EXCEPT i
        motifsI = motifs[:i] + motifs[i+1:]
        profile = build_profile(motifsI)
        
        # Randomly pick a new k-mer for string i weighted by profile
        motifs[i] = profile_random_kmer(dna[i], k, profile)
        # Update best if improved
        current_score = score(motifs)
        if current_score < best_score:
            best_motifs = motifs[:]
            best_score = current_score
    
    return best_motifs, best_score


def run_gibbs_sampler(dna, k, t, n, runs):
    best_motifs = None
    best_score = float('inf')
    
    for _ in range(runs):
        motifs, score = gibbs_sampler(dna, k, t, n)
        if score < best_score:
            best_score = score
            best_motifs = motifs
    
    return best_motifs, best_score


def profile_random_kmer(sequence, k, profile):
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    probs = [profile_probability(kmer, profile) for kmer in kmers]
    return random.choices(kmers, weights=probs)[0]

def profile_probability(kmer, profile):
    prob = 1.0
    for j, nuc in enumerate(kmer):
        prob *= profile[j][nuc]
    return prob
    
if __name__ == "__main__":   
    main()