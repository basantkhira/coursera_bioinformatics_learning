#brute force approch 
from theoretical_spectrum import cyclic_spectrum , masstable

def bf_cyclopeptide_sequencing(spectrum):
    parent_mass = max(spectrum)
    mass_table = masstable()
    alphabet = list(mass_table.keys())
    results = []

    # BFS: generate all peptides whose mass == parent_mass
    queue = [""]
    while queue:
        peptide = queue.pop(0)
        current_mass = sum(mass_table[aa] for aa in peptide)
        for aa in alphabet:
            new_peptide = peptide + aa
            new_mass = current_mass + mass_table[aa]
            
            if new_mass == parent_mass:
                if cyclic_spectrum(new_peptide,mass_table) == spectrum:
                    results.append(new_peptide)
            elif new_mass < parent_mass:
                queue.append(new_peptide)

    return results



if __name__ == "__main__":
    spectrum = list(map(int, input("Spectrum: ").strip().split()))
    results = bf_cyclopeptide_sequencing(sorted(spectrum))

    print(f"\nFound {len(results)} peptide(s):")
    for peptide in results:
        print(peptide)
