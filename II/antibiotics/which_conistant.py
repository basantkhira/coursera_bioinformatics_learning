from theoretical_spectrum import linear_spectrum, cyclic_spectrum, masstable

def is_consistent(peptide, spectrum, mass_table):
    pep_spectrum = linear_spectrum(peptide, mass_table)
    target = list(spectrum)
    for mass in pep_spectrum:
        if mass in target:
            target.remove(mass)
        else:
            return False
    return True


def check_peptides(peptides, spectrum, mass_table):
    results = []
    for peptide in peptides:
       results.append((peptide, is_consistent(peptide, spectrum, mass_table)))
    return results


if __name__ == "__main__":
    mass_table = masstable()
    spectrum = list(map(int, input("Target spectrum: ").strip().split(" ")))
    
    
    peptides =  input("peptides: ").strip().split(" ")
    results = check_peptides(peptides, spectrum, mass_table)

    for peptide, consistent in results:
        status = "✓ consistent" if consistent else "✗ not consistent"
        print(f"{peptide}: {status}")
