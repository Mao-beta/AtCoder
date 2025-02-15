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


# 行列積（任意サイズ）
def mul_matrix(A, B, mod=998244353):
    Ah = len(A)
    Aw = len(A[0])
    Bh = len(B)
    Bw = len(B[0])
    assert Aw == Bh
    C = [[0] * Bw for _ in range(Ah)]
    for h in range(Ah):
        Arow = A[h]
        Crow = C[h]
        for i in range(Aw):
            a = Arow[i]
            Brow = B[i]
            for w in range(Bw):
                Crow[w] = (Crow[w] + a * Brow[w]) % mod
    return C

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=998244353):
    assert len(A) == len(A[0])
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
    N, K = NMI()
    A = NLI()

    if K <= 10**6:
        S = sum(A)
        for i in range(K-N):
            A.append(S % MOD)
            S = S - A[i] + A[i+N]
        print(A[-1], sum(A) % MOD)

    else:
        B = [[0]*(N+1) for _ in range(N+1)]
        B[0] = [1] * (N+1)
        B[0][-1] = 0
        for i in range(N-1):
            B[i+1][i] = 1
        B[-1] = [1] * (N+1)
        C = pow_matrix(B, K-N, MOD)
        A = A[::-1]
        A.append(sum(A))

        f, s = 0, 0
        for j in range(N+1):
            f += C[0][j] * A[j] % MOD
            f %= MOD

        for j in range(N+1):
            s += C[-1][j] * A[j] % MOD
            s %= MOD

        print(f, s)


if __name__ == "__main__":
    main()
