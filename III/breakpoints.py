def count_breakpoints(perm):
    extended = [0] + perm + [len(perm) + 1]
    breakpoints = 0
    for i in range(len(extended) - 1):
        if extended[i+1] - extended[i] != 1:
            breakpoints += 1
    return breakpoints

# Read input
line = input("permutation: ").strip()
perm = [int(x) for x in line.split()]

print(count_breakpoints(perm))