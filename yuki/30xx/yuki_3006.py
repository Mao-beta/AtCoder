import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    X1, Y1, N = NMI()

    if X1 % MOD99 == Y1 % MOD99 == 0:
        print(X1%MOD99, Y1%MOD99)
        return

    if X1 % MOD99 == 1 and Y1 % MOD99 == 0:
        print(N%MOD99, 0)
        return

    A = [[X1, -5*Y1],
         [Y1, X1]]
    # (XN, YN)T = A^(N-1) * (X1, Y1)T
    # A^(N-1)+...+A^0 = (A^N - E) * (A-E)^-1
    X = pow_matrix(A, N, MOD99)
    XE = [[X[0][0]-1, X[0][1]],
          [X[1][0], X[1][1]-1]]
    AE = [[X1-1, -5*Y1],
          [Y1, X1-1]]
    d = AE[0][0]*AE[1][1]-AE[0][1]*AE[1][0]
    dinv = pow(d, MOD99-2, MOD99)
    AEinv = [[AE[1][1]*dinv, -AE[0][1]*dinv],
             [-AE[1][0]*dinv, AE[0][0]*dinv]]
    X = mul_matrix(XE, AEinv, MOD99)
    x = X[0][0] * X1 + X[0][1] * Y1
    y = X[1][0] * X1 + X[1][1] * Y1
    print(x%MOD99, y%MOD99)


if __name__ == "__main__":
    main()
