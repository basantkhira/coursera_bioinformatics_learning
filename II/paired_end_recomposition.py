from collections import defaultdict
from Eulerianpath import eulerian_path
from gappedgenome import StringSpelledByGappedPatterns
import requests

def main():
    k     = int(input("k: "))
    d     = int(input("d: "))
    pairs = list()
    with open ("reads.txt","r") as f:
        for line in f:
            pairs.append(line)
    #pairs = text.split(" ")
    graph = build_paired_debruijn(pairs)
    print(graph)
    path = eulerian_path(graph)
    string = StringSpelledByGappedPatterns(path,k,d)
    print(string)



def build_paired_debruijn(paired_reads):
    graph = defaultdict(list)
    
    for read in paired_reads:
        read1, read2 = read.split("|") 
        left  = (read1[:-1], read2[:-1])   # (k-1)-mer prefixes
        right = (read1[1:],  read2[1:])    # (k-1)-mer suffixes
        graph[left].append(right)
    return graph


if __name__ == "__main__":
    main()