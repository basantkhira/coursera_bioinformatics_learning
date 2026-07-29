def reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(pattern))

def shared_kmers(k, s1, s2):
    # Build a dictionary: kmer -> list of starting positions in s2
    kmer_positions = {}
    for j in range(len(s2) - k + 1):
        kmer = s2[j:j+k]
        kmer_positions.setdefault(kmer, []).append(j)

    result = []
    for i in range(len(s1) - k + 1):
        kmer = s1[i:i+k]
        rc = reverse_complement(kmer)
        # direct matches
        if kmer in kmer_positions:
            for j in kmer_positions[kmer]:
                result.append((i, j))
        # reverse complement matches (avoid double-counting when kmer == rc, i.e. palindrome)
        if rc != kmer and rc in kmer_positions:
            for j in kmer_positions[rc]:
                result.append((i, j))
    return result

# Read input
k = int(input().strip())
s1 = input().strip()
s2 = input().strip()

pairs = shared_kmers(k, s1, s2)

for x, y in pairs:
    print(f'({x}, {y})')

print("done")