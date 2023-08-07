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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W = NMI()
    A = EI(H)
    ans = []
    for h in range(H):
        for w in range(W):
            for dh, dw in zip([1, 0], [0, 1]):
                nh, nw = h+dh, w+dw
                if nh < 0 or H <= nh or nw < 0 or W <= nw:
                    continue
                a, b = A[h][w], A[nh][nw]
                if a > b:
                    a, b = b, a
                ans.append([a, b])
    ans.sort()
    for a, b in ans:
        print(a, b)


if __name__ == "__main__":
    main()
