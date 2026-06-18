# from string 
def main():
    k = int(input("k: "))
    text = input("Text: ")
    
    graph = de_bruijn(k, text)
    
    with open("output3.txt", "w") as f:
        for node, neighbors in sorted(graph.items()):
            line = f"{node} : {' '.join(neighbors)}"
            f.write(line + "\n")
            
            
def de_bruijn(k, text):
    edges = {}
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prefix = kmer[:-1]   # first k-1 characters
        suffix = kmer[1:]    # last k-1 characters
        
        if prefix not in edges:
            edges[prefix] = []
        edges[prefix].append(suffix)
    
    return edges

if __name__ == "__main__":
    main()