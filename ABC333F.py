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
    # P[i][j]: 列にi人、自分より前にj人いて、最後まで残る確率
    P = [[0]*N for _ in range(N+1)]
    P[1][0] = 1

    inv2 = pow(2, MOD99 - 2, MOD99)
    for i in range(2, N+1):
        p = 0
        for j in range(i):
            p += pow(2, j+1, MOD99) * P[i-1][j] % MOD99
            p %= MOD99
        # (2^i - 1)でわる
        x = pow(2, i, MOD99) - 1
        p = p * pow(x, MOD99-2, MOD99) % MOD99
        P[i][i-1] = p

        for j in range(i-1):
            p = P[i][(j-1)%i] * inv2 % MOD99
            if j > 0:
                p += P[i-1][(j-1)%i] * inv2 % MOD99
            p %= MOD99
            P[i][j] = p

    print(*P[N])


if __name__ == "__main__":
    main()
