from Euleriancycle import eulerian_cycle 
from collections import defaultdict

def main():
    k = int(input("k: "))
    result = k_universal_circular_string(k) 
    print(f"Universal circular string: {result}")

def universal_de_bruijn(k):    
    graph = defaultdict(list)
    # generate all possible k-mers
    for i in range(2**k):
        kmer = format(i, f'0{k}b')  # converts int to binary string of length k
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    
    return graph


def k_universal_circular_string(k):
    graph = universal_de_bruijn(k)
    cycle = eulerian_cycle(graph)
    result = "".join(node[0] for node in cycle[:-1])  
    
    return result


if __name__ == "__main__":
    main()