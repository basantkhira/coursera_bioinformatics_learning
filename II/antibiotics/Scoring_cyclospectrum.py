from theoretical_spectrum import cyclic_spectrum, masstable,linear_spectrum
#using linear for leaderboard sake

def score(peptide, spectrum, mass_table):
    pep_spectrum = cyclic_spectrum(peptide, mass_table)

    target = list(spectrum)  
    count = 0
    for mass in pep_spectrum:
        if mass in target:
            target.remove(mass)
            count += 1
    return count

def linear_score(peptide, spectrum, mass_table):

    pep_spectrum = linear_spectrum(peptide, mass_table)
    target = list(spectrum)
    count = 0
    for mass in pep_spectrum:
        if mass in target:
            target.remove(mass)
            count += 1
    return count


if __name__ == "__main__":
    mass_table = masstable()

    peptide = input("Peptide: ").strip()
    spectrum = list(map(int, input("Spectrum: ").strip().split()))

    result = score(peptide, spectrum, mass_table)
    print(f"\nScore({peptide}, Spectrum) = {result}")