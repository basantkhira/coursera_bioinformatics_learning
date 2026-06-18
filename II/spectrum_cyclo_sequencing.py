from theoretical_spectrum import cyclic_spectrum, linear_spectrum, masstable


def is_consistent(peptide, spectrum, mass_table):
    """
    Check if a linear peptide is consistent with the spectrum.
    Every mass in the peptide's linear spectrum must appear in the target spectrum.
    """
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

    candidates = [""]       # start with empty peptide
    final_peptides = []

    while candidates:
        # Expand — add one amino acid to every candidate
        candidates = [peptide + aa
                      for peptide in candidates
                      for aa in alphabet]

        next_candidates = []
        for peptide in candidates:
            pep_mass = sum(mass_table[aa] for aa in peptide)

            if pep_mass == parent_mass:
                # Full length — check cyclic spectrum
                if cyclic_spectrum(peptide, mass_table) == sorted(spectrum):
                    masses = "-".join(str(mass_table[aa]) for aa in peptide)
                    if masses not in final_peptides:
                        final_peptides.append(masses)
                # Don't keep it in candidates either way

            elif pep_mass < parent_mass:
                # Still growing — check consistency and keep if consistent
                if is_consistent(peptide, spectrum, mass_table):
                    next_candidates.append(peptide)
                # If inconsistent → silently drop it (the bounding step)

        candidates = next_candidates

    return final_peptides


if __name__ == "__main__":
    spectrum = list(map(int, input("Spectrum: ").strip().split()))
    mass_table = masstable()

    results = cyclopeptide_sequencing(spectrum, mass_table)

    if results:
        for peptide in results:
            print(peptide)
    else:
        print("No peptide found.")