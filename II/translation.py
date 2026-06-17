def genetic_code():
    with open("genetic_code.txt","r") as g:
        array = {}
        for line in g:
            codon,acid = line.split(" ") 
            array[codon] = acid.strip()
    return array
    
def translate(RNA,array):
    
    codons = [RNA[i:i+3] for i in range(0,len(RNA)-2,3)]
    
    protein = ""
    
    for codon in codons:
        if codon in array:
            protein += array[codon]
    return protein

def main():
    string = input("RNA: ").strip()
    array = genetic_code()
    protein = translate(string,array)
    print(protein)
    
if __name__ == "__main__":
    main()