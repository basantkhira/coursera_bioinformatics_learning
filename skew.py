def main():
    genome = input("genome: ")
    skew = skeww(genome)
    for value in skew:
        print(value,end=" ")

def skeww(genome):     
    skew = []
    value = 0
    skew.append(value)

    for nuclotide in genome:
        match nuclotide:
            case "A"| "T":
                value = value 
            case "C":
                value -= 1
            case "G":  
                value += 1

        skew.append(value)
    return skew
    
if __name__ == "__main__":
    main()