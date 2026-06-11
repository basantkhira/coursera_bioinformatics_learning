from Eulerianpath import eulerian_path
from genomepath import pathtogenome
from kdebruijn import de_bruijn

def main():
    patterns = input("string: ").split(" ")
    graph = de_bruijn(patterns)
    path = eulerian_path(graph)
    dna = pathtogenome(path)
    print(dna)
    
if __name__ == "__main__":
    main()