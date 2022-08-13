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
    ans = [[0]*N for _ in range(N)]

    x = 1
    h = 0
    w = 0
    while x <= N**2:
        ans[h][w] = x
        if w % N == N-1:
            w = 0
            h += 2
        else:
            w += 1

        if h >= N:
            h %= N

        if ans[h][w] != 0:
            h += 1
            h %= N

        x += 1

    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
