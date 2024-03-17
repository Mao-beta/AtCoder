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


def d2(xa, ya, xb, yb):
    return (xa-xb)**2 + (ya-yb)**2

def main():
    x1, y1, x2, y2, x3, y3 = NMI()
    for x4 in range(-200, 201):
        for y4 in range(-200, 201):
            E = []
            for (xa, ya), (xb, yb) in combinations([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], 2):
                E.append(d2(xa, ya, xb, yb))
            E.sort()
            if E[0]*2 == E[1]*2 == E[2]*2 == E[3]*2 == E[4] == E[5]:
                print(x4, y4)
                return
    print(-1)


if __name__ == "__main__":
    main()
