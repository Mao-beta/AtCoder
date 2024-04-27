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
    N, M = NMI()
    AB = EI(M)
    AB.sort()
    ans = []
    for i in range(1, N+1):
        for j in range(M):
            ans.append([i, (i+j-1)%N+1])

    H = list(range(N+1))
    W = list(range(N+1))
    usedH = set()
    usedW = set()
    h = 1
    w = 1
    for a, b in AB:
        # 見ているマスの現在のh, w
        ha, wb = H[a], W[b]
        if ha not in usedH:
            # 行先マスと現在マスを交換
            H[a] = h
            H[h] = ha
            W[b] = w
            W[w] = wb
            w += 1
        elif wb not in usedW:
            pass

        else:
            pass

    for x, y in ans:
        print(x, y)


if __name__ == "__main__":
    main()
