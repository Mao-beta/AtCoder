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
    Nw = NI()
    W = NLI()
    Nb = NI()
    B = NLI()
    Wc = [0] * 21
    Bc = [0] * 21
    for w in W:
        Wc[w] = 1
    for b in B:
        Bc[b] = 1

    ans = 0
    tmp = 0
    c = 0
    for i in range(20, 0, -1):
        if c == 0:
            if Wc[i]:
                tmp += 1
                c ^= 1
        else:
            if Bc[i]:
                tmp += 1
                c ^= 1
    ans = max(ans, tmp)

    tmp = 0
    c = 1
    for i in range(20, 0, -1):
        if c == 0:
            if Wc[i]:
                tmp += 1
                c ^= 1
        else:
            if Bc[i]:
                tmp += 1
                c ^= 1
    ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
