import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, W = NMI()
    XY = EI(N)
    Q = NI()
    TA = EI(Q)
    W2B = [[] for _ in range(W)]
    for i, (x, y) in enumerate(XY):
        W2B[x-1].append([y-1, i])
    for x in range(W):
        W2B[x].sort(reverse=True)
        if len(W2B[x]) == 0:
            for i in range(Q):
                print("Yes")
            return
    # print(W2B)
    INF = 10**18
    lasts = [INF] * N
    end = False
    while not end:
        IDX = []
        t = 0
        for w in range(W):
            y, i = W2B[w].pop()
            if len(W2B[w]) == 0:
                end = True
            t = max(t, y)
            IDX.append(i)
        for i in IDX:
            lasts[i] = t
    for t, a in TA:
        if lasts[a-1] >= t:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
