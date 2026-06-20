#brute force approch 
from theoretical_spectrum import cyclic_spectrum , masstable

def bf_cyclopeptide_sequencing(spectrum):
    parent_mass = max(spectrum)
    results = []

    aa_masses = masstable().values()

    # BFS: generate all peptides whose mass == parent_mass
    queue = [[]]
    while queue:
        peptide = queue.pop(0)
        current_mass = sum(peptide)
        for mass in aa_masses:
            new_peptide = peptide + [mass]
            new_mass = current_mass + mass
            if new_mass == parent_mass:
                if cyclic_spectrum(new_peptide) == spectrum:
                    results.append(new_peptide)
            elif new_mass < parent_mass:
                queue.append(new_peptide)

    return results
