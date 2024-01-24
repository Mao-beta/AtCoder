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


def solve(N, S, T):
    ans = 0
    aa, bb, toa, tob = 0, 0, 0, 0
    for i, (s, t) in enumerate(zip(S, T)):
        if s == "A" and t == "A":
            aa += 1
        elif s == "A" and t == "B":
            tob += 1
            if toa > 0:
                toa -= 1
                tob -= 1
                ans += 1
                aa += 1
                bb += 1
            elif aa > 0:
                tob -= 1
                ans += 1
                bb += 1
            else:
                print(-1)
                return
        elif s == "B" and t == "A":
            toa += 1
        if s == "B" and t == "B":
            bb += 1

    if toa > 0:
        for i, (s, t) in enumerate(zip(S[::-1], T[::-1])):
            if s == "B" and t == "B":
                ans += toa
                break
            if s == "A" and t == "B":
                ans += toa
                break
            if s == "B" and t == "A":
                print(-1)
                return

    print(ans)


def main():
    N = NI()
    S = SI()
    T = SI()
    solve(N, S, T)


if __name__ == "__main__":
    main()
