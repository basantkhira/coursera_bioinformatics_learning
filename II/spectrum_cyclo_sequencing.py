from theoretical_spectrum import cyclic_spectrum,linear_spectrum,masstable

def score(peptide, spectrum, mass_table, cyclic=True):
    
    if cyclic:
        pep_spectrum = cyclic_spectrum(peptide, mass_table)
    else:
        pep_spectrum = linear_spectrum(peptide, mass_table)

    # Count matches (handle duplicates correctly)
    target = list(spectrum)
    count = 0
    for mass in pep_spectrum:
        if mass in target:
            target.remove(mass)
            count += 1
    return count


def trim(leaderboard, spectrum, n, mass_table):
    if not leaderboard:
        return leaderboard

    scores = [(peptide, score(peptide, spectrum, mass_table, cyclic=False))
              for peptide in leaderboard]
    scores.sort(key=lambda x: x[1], reverse=True)

    # Keep top N, but include ties at the cutoff
    cutoff_score = scores[min(n, len(scores)) - 1][1]
    return [p for p, s in scores if s >= cutoff_score]


def cyclopeptide_sequencing(spectrum, mass_table, N=1000):

    parent_mass = max(spectrum)
    alphabet = list(mass_table.keys())

    leaderboard = [""]   # start with empty peptide
    leader_peptide = ""
    leader_score = 0

    while leaderboard:
        # Expand each peptide by one amino acid
        leaderboard = [peptide + aa
                       for peptide in leaderboard
                       for aa in alphabet]

        next_board = []
        for peptide in leaderboard:
            pep_mass = sum(mass_table[aa] for aa in peptide)

            if pep_mass == parent_mass:
                s = score(peptide, spectrum, mass_table, cyclic=True)
                if s > leader_score:
                    leader_score = s
                    leader_peptide = peptide
                next_board.append(peptide)

            elif pep_mass < parent_mass:
                next_board.append(peptide)
        

        leaderboard = trim(next_board, spectrum, N, mass_table)

    return leader_peptide, leader_score


if __name__ == "__main__":
    spectrum = list(map(int, input("Spectrum: ").strip().split()))
    mass_table = masstable()

    peptide, s = cyclopeptide_sequencing(spectrum, mass_table, N=1000)

    if peptide:
        masses = "-".join(str(mass_table[aa]) for aa in peptide)
        print(f"Best peptide : {peptide}")
        print(f"As masses    : {masses}")
        print(f"Score        : {s}")
    else:
        print("No peptide found.")