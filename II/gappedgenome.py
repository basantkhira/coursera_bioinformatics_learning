import sys


def StringSpelledByPatterns(patterns):
    string = patterns[0]
    for pattern in patterns[1:]:
        string += pattern[-1]
    return string


def StringSpelledByGappedPatterns(patterns, k, d):
    pattern1 =[]
    pattern2 = []
    for pair in patterns:
        pattern1.append(pair.split("|")[0])
        pattern2.append(pair.split("|")[1])
        

    prefix_string = StringSpelledByPatterns(pattern1)
    suffix_string = StringSpelledByPatterns(pattern2)

    for i in range(k + d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - (k + d)]:
            return "there is no string spelled by the gapped patterns"

    return prefix_string + suffix_string[-(k + d):]


def main():
    k     = int(input("k: "))
    d     = int(input("d: "))
    pairs = input("text: ").split(" ")
    print(StringSpelledByGappedPatterns(pairs, k, d))
    print("Done")


if __name__ == "__main__":
    main()
