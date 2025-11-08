import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    T = NI()
    for _ in range(T):
        N, W = NMI()
        XY = EI(N)
        X2Y = [[] for _ in range(60)]
        for x, y in XY:
            X2Y[x].append(y)
        ans = 0
        L = []
        for x in range(60):
            L += X2Y[x]
            L.sort()
            # print(x, L)
            if (W >> x) & 1 and L:
                ans += L[-1]
                L.pop()
            L2 = []
            while len(L) >= 2:
                w1 = L.pop()
                w2 = L.pop()
                L2.append(w1 + w2)
            L2 += L[:]
            L = L2
        print(ans)


if __name__ == "__main__":
    main()
