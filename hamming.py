# detect mismatch between the patterns 
def main():
    text1 = input("text1: ").strip()
    text2 = input("text2: ").strip()
    print(hamming(text1, text2))

def hamming(text1,text2):
    count = 0 
    for i in range (len(text1)):
        if text1[i] != text2[i]:
            count +=1 
    return count 

if __name__ == "__main__":    main()
