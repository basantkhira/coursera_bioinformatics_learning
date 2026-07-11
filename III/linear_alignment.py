import sys
import numpy as np
sys.setrecursionlimit(100000)

def column_scores(v_arr, w, match, mismatch, indel, num_cols):
    n = len(v_arr)
    prev = -indel * np.arange(n + 1, dtype=np.int64)
    idx = np.arange(1, n + 1, dtype=np.int64)
    for j in range(1, num_cols + 1):
        wc = ord(w[j - 1])
        s = np.where(v_arr == wc, match, -mismatch)
        B = np.maximum(prev[1:] - indel, prev[:-1] + s)
        curr0 = prev[0] - indel
        E = B + indel * idx
        C = np.maximum.accumulate(np.concatenate(([curr0], E)))
        prev = C - indel * np.arange(n + 1, dtype=np.int64)
    return prev


def middle_edge(v, w, match, mismatch, indel):
    n, m = len(v), len(w)
    mid = (m + 1) // 2

    v_arr = np.frombuffer(v.encode(), dtype=np.uint8)
    v_arr_rev = np.frombuffer(v[::-1].encode(), dtype=np.uint8)
    w_rev = w[::-1]

    fw_mid = column_scores(v_arr, w, match, mismatch, indel, mid)
    fw_mid1 = column_scores(v_arr, w, match, mismatch, indel, mid + 1) if mid + 1 <= m else None

    bw_mid = column_scores(v_arr_rev, w_rev, match, mismatch, indel, m - mid)[::-1]
    bw_mid1 = None
    if mid + 1 <= m:
        bw_mid1 = column_scores(v_arr_rev, w_rev, match, mismatch, indel, m - mid - 1)[::-1]

    totals = fw_mid + bw_mid
    i1 = int(len(totals) - 1 - np.argmax(totals[::-1]))

    source = (i1, mid)
    target = None
    best_score = totals[i1]

    if i1 + 1 <= n and fw_mid[i1] - indel + bw_mid[i1 + 1] == best_score:
        target = (i1 + 1, mid)
    elif fw_mid1 is not None and fw_mid[i1] - indel + bw_mid1[i1] == best_score:
        target = (i1, mid + 1)
    elif fw_mid1 is not None and i1 + 1 <= n:
        target = (i1 + 1, mid + 1)

    return source, target


def linear_space_alignment(v, w, match, mismatch, indel):
    """Returns (aligned_v, aligned_w) using divide-and-conquer."""
    stack = []  
    result = []
    stack.append((v, w, result))

    while stack:
        sv, sw, out = stack.pop()
        n, m = len(sv), len(sw)

        if n == 0:
            out.append(('-' * m, sw))
            continue
        if m == 0:
            out.append((sv, '-' * n))
            continue
        if n == 1 or m == 1:
            # base case: small enough to do directly
            a1, a2 = small_align(sv, sw, match, mismatch, indel)
            out.append((a1, a2))
            continue

        (i1, j1), (i2, j2) = middle_edge(sv, sw, match, mismatch, indel)

        # build the edge alignment piece
        if i2 == i1 + 1 and j2 == j1 + 1:
            edge_v = sv[i1]
            edge_w = sw[j1]
        elif i2 == i1 + 1:
            edge_v = sv[i1]
            edge_w = '-'
        else:
            edge_v = '-'
            edge_w = sw[j1]

        mid_out = []
        stack.append((sv[i2:], sw[j2:], out))
        stack.append(('__EDGE__', edge_v, edge_w, mid_out, out))
        stack.append((sv[:i1], sw[:j1], mid_out))

    pass


def small_align(v, w, match, mismatch, indel):
    n, m = len(v), len(w)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): dp[i][0] = -indel * i
    for j in range(1, m + 1): dp[0][j] = -indel * j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = match if v[i-1] == w[j-1] else -mismatch
            dp[i][j] = max(dp[i-1][j-1] + s, dp[i-1][j] - indel, dp[i][j-1] - indel)
    i, j = n, m
    a1, a2 = [], []
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            s = match if v[i-1] == w[j-1] else -mismatch
            if dp[i][j] == dp[i-1][j-1] + s:
                a1.append(v[i-1]); a2.append(w[j-1]); i -= 1; j -= 1; continue
        if i > 0 and dp[i][j] == dp[i-1][j] - indel:
            a1.append(v[i-1]); a2.append('-'); i -= 1
        else:
            a1.append('-'); a2.append(w[j-1]); j -= 1
    return ''.join(reversed(a1)), ''.join(reversed(a2))


def align(v, w, match, mismatch, indel):
    """Iterative divide-and-conquer alignment."""
    segments = []
    task_stack = [(v, w, segments)]

    while task_stack:
        item = task_stack.pop()
        sv, sw, seg = item

        n, m = len(sv), len(sw)

        if n == 0:
            seg.append(('-' * m, sw))
            continue
        if m == 0:
            seg.append((sv, '-' * n))
            continue
        if n <= 2 or m <= 2:
            seg.append(small_align(sv, sw, match, mismatch, indel))
            continue

        (i1, j1), (i2, j2) = middle_edge(sv, sw, match, mismatch, indel)

        if i2 == i1 + 1 and j2 == j1 + 1:
            ev, ew = sv[i1], sw[j1]
        elif i2 == i1 + 1:
            ev, ew = sv[i1], '-'
        else:
            ev, ew = '-', sw[j1]

        left_seg = []
        right_seg = []

        seg.append(('__COMPOUND__', left_seg, (ev, ew), right_seg))
        task_stack.append((sv[i2:], sw[j2:], right_seg))
        task_stack.append((sv[:i1], sw[:j1], left_seg))

    def flatten(seg):
        av, aw = [], []
        for item in seg:
            if isinstance(item, tuple) and len(item) == 4 and item[0] == '__COMPOUND__':
                _, left_seg, (ev, ew), right_seg = item
                lv, lw = flatten(left_seg)
                rv, rw = flatten(right_seg)
                av.append(lv + ev + rv)
                aw.append(lw + ew + rw)
            else:
                av.append(item[0])
                aw.append(item[1])
        return ''.join(av), ''.join(aw)

    return flatten(segments)


def score_alignment(av, aw, match, mismatch, indel):
    score = 0
    for a, b in zip(av, aw):
        if a == '-' or b == '-':
            score -= indel
        elif a == b:
            score += match
        else:
            score -= mismatch
    return score


if __name__ == "__main__":
      
    line = input("input: ").split()
    match = int(line[0])
    mismatch = int(line[1])
    indel = int(line[2])    
        
    s1 = input("seq1: ").strip()
    s2 = input("seq2: ").strip()
    print("WAIT")

    av, aw = align(s1, s2, match, mismatch, indel)
    sc = score_alignment(av, aw, match, mismatch, indel)
    print(sc)
    print(av)
    print(aw)