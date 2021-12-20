import sys
import math
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, B, K = NMI()
    C = NLI()

    # dp[i] 2^i回ぶんの遷移後のベクトル
    dp = [[0]*B for _ in range(61)]

    P10 = [1]
    for i in range(62):
        P10.append(P10[-1] * 10 % B)


    for c in C:
        dp[0][c%B] += 1

    for i in range(1, 61):
        #print(i)
        p10 = pow(10, i, B)
        for j in range(B):
            for k in range(B):
                nj = (j * p10 + k) % B
                dp[i][nj] += dp[i-1][j] % MOD * dp[i-1][k] % MOD
                dp[i][nj] %= MOD


    def step(va):
        res = [0] * B

        vb = dp[0]
        for i in range(B):
            for j in range(B):
                idx = (i * 10 + j) % B
                res[idx] += va[i] * vb[j]
                res[idx] %= MOD

        return res


    def double(va, n):
        res = [0] * B

        vb = va[:]
        p10 = pow(10, n, B)

        for i in range(B):
            for j in range(B):
                idx = (i * p10 + j) % B
                res[idx] += va[i] * vb[j]
                res[idx] %= MOD

        return res


    @lru_cache(maxsize=None)
    def rec(n):
        if n == 1:
            return dp[0][:]

        if n % 2:
            res = step(rec(n-1))

        else:
            va = rec(n//2)
            res = double(va, n//2)

        return res


    print(rec(N)[0])


if __name__ == "__main__":
    main()
