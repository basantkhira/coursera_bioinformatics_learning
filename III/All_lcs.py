def lcs_backtrack_all(v, w):
    n = len(v)
    m = len(w)

    s         = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[set() for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = 1 if v[i-1] == w[j-1] else 0

            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + match)

            # Store ALL directions that achieve the maximum
            if s[i][j] == s[i-1][j]:
                backtrack[i][j].add("↓")
            if s[i][j] == s[i][j-1]:
                backtrack[i][j].add("→")
            if s[i][j] == s[i-1][j-1] + match and match == 1:
                backtrack[i][j].add("↘")

    return backtrack, s


def output_all_lcs(backtrack, v, i, j):
    """Iteratively find ALL LCS using a stack to handle branching."""
    if i == 0 or j == 0:
        return {""}

    # Stack holds (i, j, current_string_built_so_far)
    stack   = [(i, j, "")]
    results = set()

    while stack:
        ci, cj, current = stack.pop()

        # Base case
        if ci == 0 or cj == 0:
            results.add(current[::-1])   # built backwards so reverse
            continue

        # Branch into every valid direction
        for arrow in backtrack[ci][cj]:
            if arrow == "↘":
                stack.append((ci - 1, cj - 1, current + v[ci - 1]))
            elif arrow == "↓":
                stack.append((ci - 1, cj, current))
            elif arrow == "→":
                stack.append((ci, cj - 1, current))

    return results


def print_table(s, backtrack, v, w):
    n, m = len(v), len(w)
    print("\nScore + Backtrack Table:")
    print("        " + "   ".join(f"  {c}" for c in w))
    for i in range(n + 1):
        row_label = f"  {v[i-1] if i > 0 else ' '}  "
        row = ""
        for j in range(m + 1):
            arrows = "".join(sorted(backtrack[i][j])) if backtrack[i][j] else " "
            row += f" {s[i][j]}{arrows} "
        print(row_label + row)


# ─────────────────────────────────────────────
# Input
# ─────────────────────────────────────────────
print("=" * 45)
print("       All LCS")
print("=" * 45)

v = input("\nEnter sequence 1: ").strip().upper()
w = input("Enter sequence 2: ").strip().upper()

# ─────────────────────────────────────────────
# Run
# ─────────────────────────────────────────────
backtrack, s = lcs_backtrack_all(v, w)
all_lcs      = output_all_lcs(backtrack, v, len(v), len(w))

print_table(s, backtrack, v, w)

print(f"\nSequence 1   : {v}")
print(f"Sequence 2   : {w}")
print(f"LCS length   : {s[len(v)][len(w)]}")
print(f"Total LCS    : {len(all_lcs)}")
print(f"\nAll LCS:")
for i, lcs in enumerate(sorted(all_lcs), 1):
    print(f"  {i}. {lcs}")