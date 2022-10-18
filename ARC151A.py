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
    S = SI()
    T = SI()

    Z = ["0"] * N

    hs, ht = 0, 0
    for x, s, t in zip(Z, S, T):
        if x != s:
            hs += 1
        if x != t:
            ht += 1

    h = hs - ht
    if h % 2:
        print(-1)
        exit()

    for i in range(N-1, -1, -1):
        if h < 0 and S[i] == "0" and T[i] == "1":
            Z[i] = "1"
            h += 2
        elif h > 0 and T[i] == "0" and S[i] == "1":
            Z[i] = "1"
            h -= 2

    print("".join(Z))


if __name__ == "__main__":
    main()
