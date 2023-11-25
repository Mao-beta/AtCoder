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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    Q, K = NMI()
    querys = [SLI() for _ in range(Q)]
    M = 10001
    F = [0] * M
    F[0] = 1

    def mul(d):
        # (1-t^d)をかける
        for i in range(M-1, d-1, -1):
            F[i] -= F[i-d]
            F[i] %= MOD99

    def div(d):
        # (1-t^d)で割る
        for i in range(d, M):
            F[i] += F[i-d]
            F[i] %= MOD99


    for op, x in querys:
        x = int(x)

        if op == "+":
            # (1+t^x)=(1-t^2x)/(1-t^x)をかける
            mul(2*x)
            div(x)
        else:
            # 1/(1+t^x)=(1-t^x)/(1-t^2x)をかける
            mul(x)
            div(2*x)

        print(F[K])


if __name__ == "__main__":
    main()
