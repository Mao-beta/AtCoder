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
    N = NI()
    S = SI()
    W = NLI()
    WS = []
    ad = S.count("1")
    ch = N - ad
    for s, w in zip(S, W):
        WS.append([w, int(s)])
    WS.sort()
    ans = max(ad, ch)
    f = ad
    prev = -1
    for w, s in WS:
        if prev != w:
            ans = max(ans, f)

        if s == 0:
            f += 1
        else:
            f -= 1

        prev = w

    print(ans)


if __name__ == "__main__":
    main()
