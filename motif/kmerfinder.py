# find most frequent k-mers with mismatches in a genome and its reverse complement
from collections import defaultdict
from hamming import hamming 
from reverse import reverse

def main():     
    genome = input("genome: ").strip()
    k = int(input("k: "))
    mismatch = int(input("mismatch: ")) 

    freqmap = defaultdict(int)
    n = int(len(genome))
    
    # forward starnd 
    for i  in range (n - k +1):
        pattern = genome[i:i+k]
        neighborhood = Neighbors(pattern,mismatch)
        for neighbor in neighborhood:
            freqmap[neighbor] += 1
    
    #extra for the reserved addition problem
    reversed_strand = reverse(genome)
    m = int(len(reversed_strand))
    for i in range(m - k +1):
        pattern = reversed_strand[i:i+k]
        neighborhood = Neighbors(pattern,mismatch)
        for neighbor in neighborhood:
            freqmap[neighbor] += 1 

    # find most frequent patterns
    max_freq = max(freqmap.values())
    patterns = {key for key, value in freqmap.items() if value == max_freq}
    
    print(len(patterns))
    with open("output.txt","w") as f:
        f.write( " ".join(patterns))
    
# if consumed all mismatches return the pattern itself else explore the possible other options     
def Neighbors(pattern,mismatch):
     #base case 
     if mismatch == 0:
          return {pattern} 
     if len(pattern) == 1:
          return {"A","C","G","T"} 
     
     # recursive case 
     neighborhood = set()
     suffix = pattern[1:]
     suffixNeighbors = Neighbors(suffix,mismatch)  
     for neighbor in suffixNeighbors:
        if hamming(suffix,neighbor) < mismatch:
            for x in "ACGT":
                neighborhood.add(x + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)
     return neighborhood
 
          
if __name__ == "__main__" :  main()
          