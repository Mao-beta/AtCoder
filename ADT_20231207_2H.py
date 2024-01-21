import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W, N = NMI()
    RCA = EI(N)

    ARCI = [[a, r, c, i] for i, (r, c, a) in enumerate(RCA)]
    ARCI.sort()

    ans = [0] * N
    H2M = [0] * (H+1)
    W2M = [0] * (W+1)
    prev_a = ARCI[-1][0]
    hwrs = []
    for a, h, w, i in ARCI[::-1]:
        if prev_a != a:
            for ph, pw, pr in hwrs:
                H2M[ph] = max(H2M[ph], pr)
                W2M[pw] = max(W2M[pw], pr)

            hwrs = []

        res = 0
        res = max(res, H2M[h]+1)
        res = max(res, W2M[w]+1)
        ans[i] = res-1
        hwrs.append([h, w, res])
        prev_a = a

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
