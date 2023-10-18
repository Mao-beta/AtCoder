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
    res = [0] * 840
    for s in range(840):
        now = s + X
        for p, t in PT:
            now = (now + p-1) // p * p + t
        now += Y
        res[s] = now - s
    for q in querys:
        print(q + res[q % 840])


if __name__ == "__main__":
    main()
