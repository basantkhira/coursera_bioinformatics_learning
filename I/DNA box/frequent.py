# count the frequency of each k-mer in the text and return the most frequent k-mers
from collections import defaultdict

def main():
    text = input("Text:")
    k = int(input("k:"))
    freq = FrequencyTable(text, k) 
    result = highest_freq(freq)
    print (result)

def FrequencyTable(text, k):
    freqMap = defaultdict(int)

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        freqMap[pattern] += 1

    return freqMap


#find the highest values in the freq
def highest_freq(freq):
    result = []
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    max = sorted_freq[0][1]
    for pattern,value in sorted_freq:
        if value == max:
            result.append(pattern)
    return result


if __name__ == "__main__":
    main()  

