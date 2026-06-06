#countn(tetx,pattern)
pattern = input("pattern: ")
genome = input("genome: ").strip()
mismatch = int(input("mismatch: ")) 

from hamming import hamming

patterns =[]
for i in range(len(genome)-len(pattern)+1):
    text = genome[i:i+len(pattern)]
    if hamming(text,pattern) <= mismatch:
        patterns.append(text)

print(len(patterns))
