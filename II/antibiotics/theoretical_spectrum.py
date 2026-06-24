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


if __name__ == "__main__":

    peptide = input("Peptide: ").strip()
    mass_table = masstable()
    spectrum = cyclic_spectrum(peptide,mass_table)
    with open("output.txt","w") as file:
        file.write(' '.join(map(str, spectrum)))
    print("Done")
    
