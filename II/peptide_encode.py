from translation import genetic_code , translate

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


if __name__ == "__main__":
    array = genetic_code()
    #text = input("Genome: ").strip()
    text =""
    with open("Bacillus_brevis.txt","r") as f :
        for line in f :
            text += line.strip().replace("\n","")
            
    peptide = input("Peptide: ").strip()

    result = peptide_encoding(text, peptide, array)
    with open("output.txt","w") as r:
        r.writelines(result)
    #print('\n'.join(result))