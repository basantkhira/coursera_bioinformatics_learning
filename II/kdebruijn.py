# from k-mers
def main():
    patterns = input("patterns: ").split(" ")
    
    graph = de_bruijn(patterns)
    
    with open("output3.txt", "w") as f:
        for node, neighbors in sorted(graph.items()):
            line = f"{node} : {' '.join(neighbors)}"
            f.write(line + "\n")
            
            
def de_bruijn(patterns):
    edges = {}
    
    for pattern in patterns:
        prefix = pattern[:-1]   # first k-1 characters
        suffix = pattern[1:]    # last k-1 characters
        
        if prefix not in edges:
            edges[prefix] = []
        edges[prefix].append(suffix)
    
    return edges

if __name__ == "__main__":
    main()