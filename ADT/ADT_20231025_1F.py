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
    WS = [[w, int(s)] for w, s in zip(W, S)]
    WS.sort()
    WS.append([10**10, 2])
    adult = S.count("1")
    ans = max(adult, N-adult)
    now = adult
    for i in range(N):
        w, s = WS[i]
        if s == 0:
            now += 1
        else:
            now -= 1
        if w == WS[i+1][0]:
            continue
        ans = max(ans, now)
    print(ans)


if __name__ == "__main__":
    main()
