# branch and bound algorithm
from theoretical_spectrum import cyclic_spectrum, linear_spectrum, masstable,full_masstable
from spectrum_to_peptide import masses_to_peptides

def is_consistent(peptide, spectrum, mass_table):
    
    pep_spectrum = linear_spectrum(peptide, mass_table)
    target = list(spectrum)  # copy so we can remove matches
    for mass in pep_spectrum:
        if mass in target:
            target.remove(mass)
        else:
            return False  # this mass is not in the spectrum → ban it
    return True


def cyclopeptide_sequencing(spectrum, mass_table):
    parent_mass = max(spectrum)
    alphabet = list(mass_table.keys())

    candidates = [""]      
    final_peptides = []

    while candidates:
        
        candidates = [peptide + aa
                      for peptide in candidates
                      for aa in alphabet]

        next_candidates = []
        for peptide in candidates:
            pep_mass = sum(mass_table[aa] for aa in peptide)

            if pep_mass == parent_mass:
                if cyclic_spectrum(peptide, mass_table) == sorted(spectrum):
                    masses = "-".join(str(mass_table[aa]) for aa in peptide)
                    if masses not in final_peptides:
                        final_peptides.append(masses)

            elif pep_mass < parent_mass:
                if is_consistent(peptide, spectrum, mass_table):
                    next_candidates.append(peptide)
            

        candidates = next_candidates

    return final_peptides


if __name__ == "__main__":
    spectrum = list(map(int, input("Spectrum: ").strip().split()))
    mass_table = masstable()
    full_table =full_masstable

    results = cyclopeptide_sequencing(spectrum, mass_table)

    if results:
        for mass_string in results:
            variants = masses_to_peptides(mass_string, full_table)
            print(" ".join(results))
    else:
        print("No peptide found.")