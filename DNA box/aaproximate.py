# find all approxamit occurance of pattern 
# pattern,genome,mismatch .. stating positions


from hamming import hamming

pattern = input("pattern: ")
genome = input("genome: ").strip()
mismatch = int(input("mismatch: ")) 

positions = []
for i in range(len(genome)-len(pattern)+1):
    text = genome[i:i+len(pattern)]
    if hamming(text,pattern) <= mismatch:
        positions.append(i)
        
for p in positions:
    print(p,end=" ")
