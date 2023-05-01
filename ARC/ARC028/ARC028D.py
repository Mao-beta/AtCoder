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
    N, M, Q = NMI()
    A = NLI()
    KX = EI(Q)
    base = [0] * (M+1)
    base[0] = 1
    f = base.copy()


    def mul_sparse(f: list, a, b, k):
        """(a + b * x^k)倍"""
        res = f.copy()
        for i in range(M+1):
            res[i] += f[i] * (a-1)
            if i+k <= M:
                res[i+k] += f[i] * b
            res[i] %= MOD
        return res

    def div_sparse_one(f: list, k):
        """(1-x^k)で割る"""
        res = f.copy()
        for i in range(M+1):
            if i+k <= M:
                res[i+k] += res[i]
                res[i+k] %= MOD
        return res

    def xk_of_mul(k, f, g):
        """f * g の x^k をもとめる(O(k))"""
        res = 0
        fn = len(f)
        gn = len(g)
        for fi in range(k+1):
            gi = k - fi
            if 0 <= fi < fn and 0 <= gi < gn:
                res += f[fi] * g[gi]
                res %= MOD
        return res


    for a in A:
        f = list(accumulate(mul_sparse(f, 1, -1, a+1)))


    ans = [0] * Q
    K2X = defaultdict(list)
    for i, (k, x) in enumerate(KX):
        K2X[k].append([i, x])

    for k, IX in K2X.items():
        g = div_sparse_one(f, A[k-1]+1)
        g = mul_sparse(g, 1, -1, 1)

        for i, x in IX:
            ans[i] = g[M - x] % MOD

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
