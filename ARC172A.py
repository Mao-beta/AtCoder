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
    H, W, N = NMI()
    A = NLI()
    A.sort(reverse=True)
    A = [1<<a for a in A]

    if H > W:
        H, W = W, H

    P = [[H, W]]

    for a in A:
        if len(P) == 0:
            print("No")
            return
        h, w = P.pop()
        if h < a:
            print("No")
            return
        if h > a:
            P.append([h-a, a])
        if w > a:
            P.append(sorted([h, w-a]))
        # print(P)
        if P:
            P.sort()

    print("Yes")


if __name__ == "__main__":
    main()
