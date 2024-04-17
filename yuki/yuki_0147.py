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
    N = NI()
    CD = EI(N)
    # z  1 1  y
    # y  1 0  x
    A = [[1, 1], [1, 0]]
    x = [2, 1]
    ans = 1
    for c, d in CD:
        F = pow_matrix(A, c-1, MOD)
        t = (F[0][0] * x[0] + F[0][1] * x[1]) % MOD
        if t == 0:
            print(0)
            return
        ans = ans * pow(t, d%(MOD-1), MOD) % MOD
    print(ans)


if __name__ == "__main__":
    main()
