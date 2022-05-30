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
    N, M = NMI()

    K = len(bin(M)[2:])

    if N > K:
        print(0)
        exit()

    # 2進法でi+1桁かつM以下の整数の数
    Z = [0] * K
    for i in range(K-1):
        Z[i] = pow(2, i, MOD99)

    Z[-1] = (M - sum(Z)) % MOD99

    # K個中からN個を選ぶときの総積の和
    # [x^N] Π(1+Z[i]x)
    P = [0] * (N+1)
    P[0] = 1

    for z in Z:
        Q = [0] * (N+1)
        for i in range(N+1):
            Q[i] += P[i]
            Q[i] %= MOD99
        for i in range(N):
            Q[i+1] += P[i] * z
            Q[i+1] %= MOD99
        P = Q

    # print(P)
    print(P[N])


if __name__ == "__main__":
    main()
