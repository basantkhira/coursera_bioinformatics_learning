#overlap graph 

def main():
    patterns = input("patterns:").split(" ")
    result = adjacency_list(patterns)
    with open("output2.txt","w") as f:
        f.writelines(r + "\n" for r in result )

def adjacency_list(patterns):
    adlist = list()
    for i, pattern in enumerate(patterns):
        suffix = pattern[1:]       # last k-1 characters
        for j, target in enumerate(patterns):
            if i == j:
                continue           # skip self-edges
            prefix = target[:-1]   # first k-1 characters
            if suffix == prefix:
                adlist.append(f"{pattern} : {target}")
                
    return adlist

if __name__ == "__main__":
    main()