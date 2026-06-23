from LeaderboardCyclopeptideSequencing import leaderboard_cyclopeptide_sequencing
from convolution import spectral_convolution, spectral_spectral_convolution_top_element


def convolution_cyclopeptide_sequencing(spectrum, M):
    counts = spectral_convolution(spectrum)
    top_masses = spectral_spectral_convolution_top_element(counts,M)
    ## mass itself is the key, no chr() needed for the real spectrum 
    mass_table = {mass: mass for mass in top_masses}
    
    return mass_table


if __name__ == "__main__":
    M = int(input("M: ").strip())
    N = int(input("N: ").strip())
    spectrum = list(map(float, input("Spectrum: ").strip().split()))
    
    mass_table = convolution_cyclopeptide_sequencing(spectrum,M)

    result,best_score = leaderboard_cyclopeptide_sequencing(spectrum, mass_table, N)
    
    print(f"\nBest score: {best_score}")
    print(f"Number of top peptides: {len(result)}\n")
    for peptide in result:
        masses = "-".join(str(ord(aa)) for aa in peptide)
        print(masses, end=" ")