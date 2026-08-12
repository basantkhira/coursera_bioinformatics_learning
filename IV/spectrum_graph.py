# Monoisotopic masses of the 20 standard amino acids
AMINO_ACID_MASS = {
    'G': 57,  'A': 71,  'S': 87,  'P': 97,  'V': 99,
    'T': 101, 'C': 103, 'I': 113, 'N': 114,
    'D': 115, 'K': 128,  'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

def spectrum_graph(spectrum):
    # Include 0 as the starting mass
    masses = sorted(set(spectrum) | {0})
    
    edges = []  # list of (from, to, amino_acid)
    for i in range(len(masses)):
        for j in range(i + 1, len(masses)):
            diff = masses[j] - masses[i]
            for aa, mass in AMINO_ACID_MASS.items():
                if diff == mass:
                    edges.append((masses[i], masses[j], aa))
    return edges


def format_graph(edges):
    lines = []
    for u, v, aa in edges:
        lines.append(f"{u}->{v}: {aa}")
    return "\n".join(lines)

found_peptide = None  # will hold the answer once we find it

def decode_ideal_spectrum(spectrum, edges):
    # Build adjacency list from your existing edges
    graph = {}
    for u, v, aa in edges:
        graph.setdefault(u, []).append((v, aa))

    source = 0
    sink = max(spectrum)
    target_multiset = sorted(spectrum)
    
    #helper function: check the condition of the ideal spectrum of the proposed peptide constructed from the given spectrum 
    def ideal_spectrum(peptide):
        prefix = [0]
        for aa in peptide:
            prefix.append(prefix[-1] + AMINO_ACID_MASS[aa])
        total = prefix[-1]
        n = len(prefix) - 1
        result = []
        for i in range(1, n + 1):          # skip prefix[0] = 0
            result.append(prefix[i])       # prefix masses, i = 1..n (includes total once at i=n)
            if i < n:                      
                result.append(total - prefix[i])   # suffix masses, i = 1..n-1
        return result
    
    
    def dfs(node, path):
        global found_peptide
        if found_peptide is not None:
            return  found_peptide  # early exit if we already found a valid peptide

        if node == sink:
            peptide = ''.join(path)
            if sorted(ideal_spectrum(peptide)) == target_multiset:
                found_peptide = peptide
        else:
            for nxt, aa in graph.get(node, []):
                path.append(aa)
                dfs(nxt, path)
                path.pop()   # backtrack so path is correct for the next branch
                
    dfs(source, [])
    return(found_peptide)

if __name__ == "__main__":
    spectrum = list(map(int, input().split()))
    edges = spectrum_graph(spectrum)
    graph = format_graph(edges)
    print(decode_ideal_spectrum(spectrum, edges))