from theoretical_spectrum import full_masstable 

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


if __name__ == "__main__":
    mass_table = full_masstable()
    string = input("Enter mass string (e.g. 99-128-113-163): ").strip().split(" ")
    peptides =[]
    for st in string:
        peptide = masses_to_peptides(st, mass_table)
        peptides.append(peptide)
    print(f"Possible peptides ({len(peptides)} total):")
    for p in peptides:
        print(p)