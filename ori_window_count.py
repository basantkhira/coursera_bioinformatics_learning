# counting nuclotides 
import requests

def main():
    response = requests.get("https://bioinformaticsalgorithms.com/data/realdatasets/Replication/Vibrio_cholerae.txt")
    DNA = response.text
    A,T,C,G = 0,0,0,0
    for i in range(len(DNA)):
        if DNA[i] == "A":
            A += 1
        elif DNA[i] == "T":
            T += 1
        elif DNA[i] == "C":
            C += 1
        elif DNA[i] == "G":
            G += 1
    print(f"A: {A}, T: {T}, C: {C}, G: {G}")

if __name__ == "__main__":    main()