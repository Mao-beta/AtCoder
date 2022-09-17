import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    H, W = NMI()
    S = [NLI() for _ in range(H)]
    N = NI()
    RC = [NLI() for _ in range(N)]
    RC = [[x-1, y-1] for x, y in RC]

    for r, c in RC:
        S[r][c] = 0
        for h in range(r, 0, -1):
            S[h][c], S[h-1][c] = S[h-1][c], S[h][c]

    for s in S:
        print(*s)


if __name__ == "__main__":
    main()
