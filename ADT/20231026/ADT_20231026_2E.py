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
    N = NI()
    T = dict()
    D = set()
    for i in range(N):
        s, t = SMI()
        t = int(t)
        if s in D:
            continue
        else:
            D.add(s)
            T[s] = (i, t)

    idx = 0
    now = -1
    for s, (i, t) in T.items():
        if t > now:
            now = t
            idx = i
        elif t == now:
            idx = min(idx, i)

    print(idx + 1)


if __name__ == "__main__":
    main()
