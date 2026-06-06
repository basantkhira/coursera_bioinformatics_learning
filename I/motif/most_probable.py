def main():

    with open ("profile.txt",'r') as p:
        profile = [line.strip() for line in p]
    profile = [list(map(float, row.split(" "))) for row in profile]
    k = int(input("k: "))
    string = input("string: ").strip()
    
    print(most_probable_kmer(profile, string, k))

def most_probable_kmer(profile, string, k):
    # value of each 
    # higher first one 
    score = 0 
    pattern = None
    result = {}
    for i in range(len(string) - k + 1):
        pattern = string[i:i+k]
        score = find_score(profile,pattern)
        result.update({pattern:score})
    
    # Sort dictionary by values (descending)
    max_value = max(result, key = result.get)
    return(max_value)
            
        
# edits for importing issues 
def find_score(profile, pattern):
    score = 1
    for i in range(len(pattern)):
        if pattern[i] == "A":
            score *= float(profile[i][pattern[i]])
        elif pattern[i] == "C":
            score *= float(profile[i][pattern[i]])
        elif pattern[i] == "G":
            score *= float(profile[i][pattern[i]])
        elif pattern[i] == "T":
            score *= float(profile[i][pattern[i]])
    return score

if __name__ == "__main__":
    main()
    