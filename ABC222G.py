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
    T = NI()
    for _ in range(T):
        K = NI()

        if 2 % K == 0:
            print(1)
            continue

        if K % 5 == 0 or K % 4 == 0:
            print(-1)
            continue

        if K % 2 == 0:
            A = [[10, 1],
                 [0, 1]]
            K //= 2
            a0 = 1
        else:
            A = [[10, 2],
                 [0, 1]]
            a0 = 2

        inv = pow(10, -1, K)
        sq = int(K**0.5)+1
        Asq = pow_matrix(A, sq, K)

        # f^(√K)(x)は行列累乗で求まる
        def fsq(x):
            p, q = Asq[0][0], Asq[0][1]
            return (p * x + q) % K

        def finv(x):
            return (x - A[0][1]) * inv % K

        # Baby step: fy[q] = f^(-q)(0) modK
        fy = [0]
        fy_rev = dict()
        for i in range(sq+2):
            res = finv(fy[-1])
            fy.append(res)

        for i in range(len(fy)-1, -1, -1):
            fy_rev[fy[i]] = i

        # Giant step: fsqx[p] = f^(√K * p)(a0) modK
        fsqx = [a0]
        for i in range(sq+2):
            fsqx.append(fsq(fsqx[-1]))

        # f^(√K*p)(a0) = f^(-q)(0) のとき、√K*p+q が答え(最後に1-indexにする)
        for p, x in enumerate(fsqx):
            if x in fy_rev:
                q = fy_rev[x]
                print(p*sq + q + 1)
                break


if __name__ == "__main__":
    main()
