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


# 正方行列の積 mod
def mul_matrix(A, B, mod=10**9+7):
    size = len(A)
    ans = [[0] * size for _ in range(size)]
    for h in range(size):
        for w in range(size):
            for i in range(size):
                ans[h][w] += A[h][i] * B[i][w] % mod
                ans[h][w] %= mod
    return ans

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=10**9+7):
    bitn = len(bin(n)) - 2
    pows = []
    size = len(A)
    E = [[0] * size for _ in range(size)]
    for i in range(size):
        E[i][i] = 1

    pows.append(A)
    ans = E

    for i in range(bitn):
        if (n >> i) & 1:
            ans = mul_matrix(pows[-1], ans, mod)
        pows.append(mul_matrix(pows[-1], pows[-1], mod))

    return ans


def main():
    H, R = NMI()
    G = EI(R)
    B = 1 << R

    dps = []

    order = list(range(B))
    order.sort(key=lambda x: bin(x).count("1"))

    for r in range(R):
        # dp[now][b]: 通った部屋の状態がbでいまnowにいる
        dp = [[0] * B for _ in range(R)]
        dp[r][1<<r] = 1
        for b in order:
            for now in range(R):
                if dp[now][b] == 0:
                    continue
                for g in range(R):
                    if (b >> g) & 1:
                        continue
                    if G[now][g] == 0:
                        continue
                    dp[g][b | (1<<g)] += dp[now][b]
                    dp[g][b | (1<<g)] %= MOD

        dps.append([sum(d) % MOD for d in dp])

    A = pow_matrix(dps, H)
    print(A[0][0])


if __name__ == "__main__":
    main()
