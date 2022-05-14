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
    N, M = NMI()
    T = NLI()
    A = NLI()
    B = NLI()
    P = []
    for a in A:
        P.append([a, 0])
    for b in B:
        P.append([b, 1])
    P.sort()
    now = 0
    place = 0
    ans = 0
    for p, ab in P:
        if now > p:
            continue
        elif place == ab:
            now = p + T[place]
            if place:
                ans += 1
            place = 1 - place
    print(ans)


if __name__ == "__main__":
    main()
