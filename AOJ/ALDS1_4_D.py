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
    N, K = NMI()
    W = [NI() for _ in range(N)]
    Wmax = max(W)

    ok = 10**10
    ng = Wmax - 1
    while abs(ok-ng) > 1:
        X = (ok+ng) // 2
        T = []
        now = 0
        for w in W:
            if now + w > X:
                T.append(now)
                now = 0
            now += w
        if now > 0:
            T.append(now)

        if len(T) <= K:
            ok = X
        else:
            ng = X
    print(ok)


if __name__ == "__main__":
    main()
