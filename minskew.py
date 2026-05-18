# to detect ori 

from skew import skeww
import requests

def main ():
    genome = input("genome: ").strip()
    print(min_skew(genome))

def min_skew(genome):
    result = []
    skew = skeww(genome)
    min_value = min(skew)
    for i in range(len(skew)):
        if skew[i] == min_value:
            result.append(i)
    return result


if __name__ == "__main__":    main()
    