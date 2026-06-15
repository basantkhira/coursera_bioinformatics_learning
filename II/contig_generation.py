from non_branching import maximal_non_branching_paths
from kdebruijn import de_bruijn

def main():
    graph = de_bruijn(input("input"))
    result = maximal_non_branching_paths(graph)
    for r in result:
        print(" ".join(r))
    
if __name__ == "__main__":
    main()
    

