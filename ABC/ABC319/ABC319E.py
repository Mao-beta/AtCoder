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
    N, X, Y = NMI()
    PT = EI(N-1)
    Q = NI()
    querys = [NI() for _ in range(Q)]

    ans = [0] * 1680
    r2idx = dict()
    for s in range(1680):
        R = []
        for i in range(5, 9):
            R.append(s % i)
        R = tuple(R)
        r2idx[R] = s

        now = s + X
        for p, t in PT:
            c = (now + p-1) // p * p
            r = c - now
            now += r + t
        now += Y
        ans[s] = now - s

    for q in querys:
        R = []
        for i in range(5, 9):
            R.append(q % i)
        R = tuple(R)
        idx = r2idx[R]
        print(q + ans[idx])


if __name__ == "__main__":
    main()
