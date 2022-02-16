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
    L = []
    A = 0
    for i in range(N):
        a, b = NMI()
        L.append([a+b, a])
        A += a
    L.sort(key=lambda x: -(x[0]+x[1]))

    B = 0
    ans = 0
    for t, a in L:
        ans += 1
        B += t
        A -= a
        if B > A:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
