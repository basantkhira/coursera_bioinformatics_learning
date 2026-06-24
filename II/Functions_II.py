"""ALL FUNCTIONS OF BIOINFORMATICS II """
from collections import defaultdict
from collections import Counter



"""TRANSLATION\PEPTIDE """

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def dna_to_rna(dna):
    return dna.replace('T', 'U')

def peptide_encoding(text, peptide, array):
    k = 3 * len(peptide)
    substrings = []

    for i in range(len(text) - k + 1):
        segment = text[i:i+k]

        # forward strand: transcribe and translate directly
        if translate(dna_to_rna(segment), array) == peptide:
            substrings.append(segment)

        # reverse strand: the gene could be on the complementary strand
        rev_comp = reverse_complement(segment)
        if translate(dna_to_rna(rev_comp), array) == peptide:
            substrings.append(segment)

    return substrings

def genetic_code():
    with open("genetic_code.txt","r") as g:
        array = {}
        for line in g:
            codon,acid = line.split(" ") 
            array[codon] = acid.strip()
    return array
    
def translate(RNA,array):
    
    codons = [RNA[i:i+3] for i in range(0,len(RNA)-2,3)]
    
    protein = ""
    
    for codon in codons:
        if codon in array:
            protein += array[codon]
    return protein




"""SPECTRUM"""

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

def masstable():
    mass_table = {}
    seen_masses = set()
    with open("masstable.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            acid, mass = line.split()
            mass = int(mass)
            if mass not in seen_masses:
                mass_table[acid] = mass
                seen_masses.add(mass)
    return mass_table

def full_masstable():
    mass_table = {}
    with open("masstable.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            acid, mass = line.split()
            mass_table[acid] = int(mass)
    return mass_table

def cyclic_spectrum(peptide,mass_table):
    
    n = len(peptide)
    prefix_mass = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_mass[i] = prefix_mass[i - 1] + mass_table[peptide[i - 1]]
    
    # add for cyclic peptide
    peptide_mass = prefix_mass[n]
    
    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))


    return sorted(spectrum)


def linear_spectrum(peptide, mass_table):
    n = len(peptide)
    prefix_mass = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_mass[i] = prefix_mass[i - 1] + mass_table[peptide[i - 1]]

    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)


def masses_to_peptides(string, mass_table):
    
    reverse = {}
    for aa, mass in mass_table.items():
        if mass not in reverse:
            reverse[mass] = []
        reverse[mass].append(aa)

    masses = list(map(int, string.split("-")))

    # Build all possible peptides
    candidates = [""]
    for mass in masses:
        if mass not in reverse:
            print(f"Warning: mass {mass} not found in mass table!")
            return []

        options = reverse[mass]
        new_candidates = []
        for current in candidates:
            for aa in options:
                if len(options) > 1:
                    new_candidates.append(current + aa + "*")
                else:
                    new_candidates.append(current + aa)
        candidates = new_candidates

    return candidates

"""CYCLOPEPTIDE SEQUENCING PROBLEM WITH DIFFERENT ALGORITHMIC APPROCHES"""


"""BF""" 
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


"""CONVOLUTION"""


def spectral_convolution(spectrum):
    result = []
    n = len(spectrum)

    for i in range(n):
        for j in range(n):
            diff = spectrum[j] - spectrum[i]
            if diff > 0:
                result.append(diff)

    return Counter(result)

def spectral_spectral_convolution_top_element(counts,M):
    filtered = {mass: cnt for mass, cnt in counts.items() if 57 <= mass <= 200}
    if not filtered:
        return []
    
    sorted_elements = sorted(filtered.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    if M >= len(sorted_elements):
        return [mass for mass, cnt in sorted_elements]
    
    threshold = sorted_elements[M - 1][1]  
    return [mass for mass, cnt in sorted_elements if cnt >= threshold]
    
def convolution_cyclopeptide_sequencing(spectrum, M):
    counts = spectral_convolution(spectrum)
    top_masses = spectral_spectral_convolution_top_element(counts,M)

    mass_table = {chr(mass): mass for mass in top_masses}
    
    return mass_table





""" LEADERBOARD\LEADERPEPTIDE"""

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


def leaderpeptide_cyclopeptide_sequencing(spectrum, mass_table, N):
    parent_mass = max(spectrum)
    alphabet = list(mass_table.keys())

    leaderboard = [""]
    leader_peptide = ""  # single peptide, not a list
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
                    leader_peptide = peptide  # just replace, no list
                next_leaderboard.append(peptide)
            elif pep_mass < parent_mass:
                next_leaderboard.append(peptide) 
                
        leaderboard = trim(next_leaderboard, spectrum, N, mass_table)

    return leader_peptide, leader_score


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

"""BRANCH AND BOUND"""

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





""" SOME CODES MADE FOR FINAL QUIZ """

def code_to_count():

    result = defaultdict(list)

    with open("genetic_code.txt", "r") as file:
        for line in file:
            codon, aa = line.split(" ")
            result[aa.strip()].append(codon.strip())

    # Convert to counts
    codon_count = {aa: len(codons) for aa, codons in result.items()}
    return codon_count

def count_dna_encodings(peptide, codon_count):
    result = 1
    for aa in peptide:
        result *= codon_count[aa]
    return result

def count_peptides_with_mass(m):

    aa_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    
    dp = [0] * (m + 1)
    dp[0] = 1  # empty peptide has mass 0
    
    for mass in range(1, m + 1):
        for aa in aa_masses:
            if mass - aa >= 0:
                dp[mass] += dp[mass - aa]
    
    return dp[m]


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
