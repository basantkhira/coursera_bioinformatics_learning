#string composition problem 
# inpit : k and string >>>>>>> output : all possible k-mer any order 

k = int(input("k: ").strip())
string = input("string: ").strip()
result = list()

for s in range(len(string)-k+1) :
    kmer = string[s:s+k]
    result.append(kmer)

with open("output.txt", "w") as f:
    for line in result:
        f.write(line + " ")

print("done")    
     