# cyclic count : n * (n - 1)
# linear count:
def count_subpeptides(n):
    return n * (n + 1) // 2 + 1

n = int(input("n: "))
print(count_subpeptides(n))
