import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    H, W = NMI()
    S = [SI() for _ in range(H)]
    l, r, u, d = W, 0, H, 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                l = min(l, w)
                r = max(r, w+1)
                u = min(u, h)
                d = max(d, h+1)
    ans = S[u:d]
    ans = [row[l:r] for row in ans]
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
