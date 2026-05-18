pattern = "ATA"
'''
with open("text.txt") as f:    
    genome = f.read().replace("\n", "").strip()
'''
genome = input("Genome: ")
locations = []
dna_len = len(genome)
for i in range(dna_len-len(pattern)+1):
    if genome[i:i+len(pattern)] == pattern:
        locations.append(str(i))

print(" ".join(locations))