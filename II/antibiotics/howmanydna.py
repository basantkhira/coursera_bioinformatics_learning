from collections import defaultdict

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


if __name__ == "__main__":
    codon_count = code_to_count()
    peptide = input("Peptide: ").strip()
    total = count_dna_encodings(peptide, codon_count)
    print(f"Number of DNA strings encoding {peptide}: {total}")