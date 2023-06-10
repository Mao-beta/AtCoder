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


def small(N, M, S):
    ans = 0
    for X in product("ab", repeat=N):
        X = "".join(X)
        ok = True
        for si in S:
            if si in X:
                ok = False
        if ok:
            ans += 1
    return ans % MOD99


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


def large(N, M, S):
    B = 1<<6
    A = [[0]*B for _ in range(B)]
    res = [0] * B
    is_ok = [True] * B
    
    for i, X in enumerate(product("ab", repeat=6)):
        X = "".join(X)
        ok = True
        for si in S:
            if si in X:
                ok = False
        is_ok[i] = ok
        if ok:
            res[i] = 1
        
    for b in range(B):
        if not is_ok[b]:
            continue

        nb = b * 2 % B
        if is_ok[nb]:
            A[nb][b] += 1
        if is_ok[nb+1]:
            A[nb+1][b] += 1
    
    M = pow_matrix(A, N-6, MOD99)
    ans = [0] * B

    for i in range(B):
        for j in range(B):
            ans[i] += M[i][j] * res[j] % MOD99

    return sum(ans) % MOD99


def main():
    N, M = NMI()
    S = [SI() for _ in range(M)]
    if N <= 6:
        ans = small(N, M, S)
    else:
        ans = large(N, M, S)
    print(ans)


if __name__ == "__main__":
    main()
