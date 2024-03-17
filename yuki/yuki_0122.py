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
    X = EI(7)

    ge_W = [0] * 20002
    lt_W = [0] * 20002
    for i in range(20001):
        ge = 1
        lt = 1
        for j, (m, M) in enumerate(X):
            if j % 2 == 0:
                if i < m:
                    ge *= M-m+1
                elif i > M:
                    ge *= 0
                else:
                    ge *= M-i+1
            else:
                if i < m:
                    lt *= 0
                elif i > M:
                    lt *= M-m+1
                else:
                    lt *= i-m
        ge_W[i] = ge
        lt_W[i] = lt

    ge_M = [0] * 20002
    lt_M = [0] * 20002
    for i in range(20001):
        ge = 1
        lt = 1
        for j, (m, M) in enumerate(X):
            if j % 2 == 1:
                if i < m:
                    ge *= M - m + 1
                elif i > M:
                    ge *= 0
                else:
                    ge *= M - i + 1
            else:
                if i < m:
                    lt *= 0
                elif i > M:
                    lt *= M - m + 1
                else:
                    lt *= i - m
        ge_M[i] = ge
        lt_M[i] = lt

    ans = 0
    for i in range(20001):
        if i < 15:
            print(i, ge_W[i] - ge_W[i+1], lt_W[i])
            print(i, ge_M[i] - ge_M[i+1], lt_M[i])
        ans += (ge_W[i] - ge_W[i+1]) * lt_W[i]
        ans += (ge_M[i] - ge_M[i+1]) * lt_M[i]
        ans %= MOD

    print(ge_M[:15])
    print(lt_M[:15])

    print(ans)


if __name__ == "__main__":
    main()
