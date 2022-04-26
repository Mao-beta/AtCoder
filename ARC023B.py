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
    H, W, D = NMI()
    G = [NLI() for _ in range(H)]
    ans = 0
    for s in range(D+1):
        for h in range(s+1):
            if h >= H: break
            w = s - h
            if w < 0 or w >= W:
                continue
            if D % 2 == s % 2:
                ans = max(ans, G[h][w])
    print(ans)


if __name__ == "__main__":
    main()
