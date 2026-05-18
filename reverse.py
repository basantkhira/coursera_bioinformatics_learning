
def main():
    template = input("DNA: ")
    reversed_strand = reverse(template)
    print("reverse: \n", reversed_strand)

def reverse(template):
    new_template = "" 
    for letter in template:
        match letter:
            case "A":
                new_template += "T"
            case "T":
                new_template += "A"
            case "C":
                new_template += "G"
            case "G":
                new_template += "C"
    return new_template[::-1]

if __name__ == "__main__":
    main()
