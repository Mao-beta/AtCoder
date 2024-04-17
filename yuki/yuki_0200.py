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
    N = NI()
    A = NI()
    B = NLI()
    C = NI()
    D = NLI()
    B.sort()
    D.sort(reverse=True)
    ans = 0
    XB = B[:]
    XD = D[:]
    for t in range(N):
        ha, hc = -1, -1
        for i, b in enumerate(XB):
            for j, d in enumerate(XD):
                if b > d:
                    ha = i
                    hc = j
                    break
            if ha >= 0:
                break
        if ha >= 0:
            ans += 1
            XB.pop(ha)
            XD.pop(hc)
        else:
            XB.pop(0)
            XD.pop(0)

        if len(XB) == 0:
            XB = B[:]
        if len(XD) == 0:
            XD = D[:]
    print(ans)


if __name__ == "__main__":
    main()
