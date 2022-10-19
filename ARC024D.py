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
    N = NI()
    XY = [tuple(NMI()) for _ in range(N)]
    XY.sort()
    P = set(XY)

    ans = []

    def rec(l, r):
        if r - l < 2:
            return
        m = (l + r) // 2
        mx, my = XY[m]
        S = set()
        for i in range(l, r):
            x, y = XY[i]
            S.add(y)
        S.discard(my)
        for y in S:
            ans.append((mx, y))
        rec(l, m)
        rec(m+1, r)

    rec(0, N)

    ans = set(ans) - P
    print(len(ans))
    for xy in ans:
        print(*xy)


if __name__ == "__main__":
    main()
