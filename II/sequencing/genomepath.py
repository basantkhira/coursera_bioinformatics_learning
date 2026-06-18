def main():
    path = input("path: ").split(" ")
    print(pathtogenome(path))

def pathtogenome(path):
    string = path[0]
    leng = len (path[0])
    for p in path[1:] :
        string += p[leng-1:]
    return string  

if __name__ == "__main__":
    main()
        