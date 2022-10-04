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
    if n == 1:
        size = len(A)
        E = [[0] * size for _ in range(size)]
        for i in range(size):
            E[i][i] = 1
        return mul_matrix(A, E, mod)

    if n % 2 == 0:
        tA = pow_matrix(A, n//2, mod)
        return mul_matrix(tA, tA, mod)
    else:
        tA = pow_matrix(A, n-1, mod)
        return mul_matrix(tA, A, mod)


def main():
    N, X, Y = NMI()
    C = SI()
    C = [int(c == "A") for c in C]
    
    # T/Aが失敗/成功する確率のmod
    P = [[0, 0], [0, 0]]
    inv100 = pow(100, MOD99-2, MOD99)
    P[0][0] = (100 - X) * inv100 % MOD99
    P[0][1] = X * inv100 % MOD99
    P[1][0] = (100 - Y) * inv100 % MOD99
    P[1][1] = Y * inv100 % MOD99
    
    H = 24
    # A[i][j] i時直前から始めてj-1時にアクセスする確率
    A = [[0]*H for _ in range(H)]
    
    # 1周分失敗したときの確率
    Z = 1
    for c in C:
        Z = Z * P[c][0] % MOD99

    assert Z != 1
    bunbo = pow(1-Z, MOD99-2, MOD99)
    
    for i in range(H):
        now = 1
        for g in range(1, H+1):
            # jはi+1～i+24
            j = i + g
            # j-1時に成功
            access = now * P[C[(j-1)%H]][1] % MOD99 * bunbo % MOD99
            A[i][j%H] = access
            # j-1時では失敗
            now = now * P[C[(j-1)%H]][0] % MOD99

            if g == H:
                assert now == Z

    Q = pow_matrix(A, N, MOD99)

    ans = 0
    for i in range(H):
        if C[i]:
            ans += Q[0][(i+1)%H]
            ans %= MOD99

    print(ans % MOD99)

    # print(*A, sep="\n")
    # print()
    # print(*Q, sep="\n")


if __name__ == "__main__":
    main()
