def count_subpeptides(n):
    return n * (n - 1)

n = int(input("n: "))
print(count_subpeptides(n))