from Scoring_cyclospectrum import score,linear_score
#updates for extended mass table

def extended_mass_table():
    extended_list = {}
    for i in range(57,201):
        extended_list[chr(i)] = i
    return(extended_list)

def trim(leaderboard, spectrum, n, mass_table):
    if not leaderboard:
        return leaderboard

    scored = [(peptide, linear_score(peptide, spectrum, mass_table)) for peptide in leaderboard]
    scored.sort(key=lambda x: x[1], reverse=True)

    if len(scored) <= n:
        return [p for p, s in scored]

    cutoff_score = scored[n - 1][1]
    return [p for p, s in scored if s >= cutoff_score]


def expand(leaderboard, alphabet):
    return [peptide + aa for peptide in leaderboard for aa in alphabet]


def leaderboard_cyclopeptide_sequencing(spectrum, mass_table, N):
    parent_mass = max(spectrum)
    alphabet = list(mass_table.keys())

    leaderboard = [""]
    leader_peptides = [""]
    leader_score = 0 
    
    while leaderboard:
        leaderboard = expand(leaderboard, alphabet)

        next_leaderboard = []
        for peptide in leaderboard:
            pep_mass = sum(mass_table[aa] for aa in peptide)

            if pep_mass == parent_mass:
                s = score(peptide, spectrum, mass_table)
                if s > leader_score:
                    leader_score = s
                    leader_peptides.clear()
                    leader_peptides.append(peptide)
                elif s == leader_score:
                    leader_peptides.append(peptide)
                next_leaderboard.append(peptide)
            elif pep_mass < parent_mass:
                next_leaderboard.append(peptide) 
                
        leaderboard = trim(next_leaderboard, spectrum, N, mass_table)

    return leader_peptides,leader_score


if __name__ == "__main__":
    mass_table = extended_mass_table()
    N = int(input("N: ").strip())
    spectrum = list(map(int, input("Spectrum: ").strip().split()))

    result,best_score = leaderboard_cyclopeptide_sequencing(spectrum, mass_table, N)

    print(f"\nBest score: {best_score}")
    print(f"Number of top peptides: {len(result)}\n")
    for peptide in result:
        masses = "-".join(str(mass_table[aa]) for aa in peptide)
        print(masses,end=" ")
    