from non_branching import maximal_non_branching_paths
from genomepath import pathtogenome
from kdebruijn import de_bruijn

def main():
    graph = de_bruijn(input("input: "))
    result = maximal_non_branching_paths(graph)
    print()
    for r in result:
        print(pathtogenome(r),end=" ")

    
if __name__ == "__main__":
    main()

