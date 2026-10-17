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
    X = NI()

    def rec(d):
        D.add(int("".join(map(str, now))))
        nd = now[-1] + d
        if nd < 0 or nd >= 10:
            return
        now.append(nd)
        rec(d)
        now.pop()

    D = set()

    for s in range(1, 10):
        for d in range(-9, 10):
            if d == 0:
                continue
            now = [s]
            rec(d)

    for s in range(1, 10):
        for k in range(1, 19):
            D.add(int(str(s)*k))

    D = sorted(list(D))
    idx = bisect.bisect_left(D, X)
    print(D[idx])


if __name__ == "__main__":
    main()
