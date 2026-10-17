import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


class FPS:
    def __init__(self, A, mod=998244353):
        """nは最高次の次数"""
        self.n = len(A) - 1
        self.A = A.copy()
        self.mod = mod

    def __repr__(self):
        return str(self.A)

    def add_a(self, a, k):
        """x^kの係数にaを足す"""
        self.A[k] += a
        self.A[k] %= self.mod

    def mul_base(self, a, b, k):
        """(a + b x^k)倍"""
        for i in range(self.n, -1, -1):
            self.A[i] *= a
            if i-k >= 0:
                self.A[i] += self.A[i-k] * b
            self.A[i] %= self.mod

    def mul(self, other, lim=False):
        """
        P -> PとQの畳み込みにする, self.n次より上は無視
        愚直にやるのでO(d^2)
        """
        if lim:
            res = [0] * (self.n+1)
            for s in range(self.n+1):
                for i in range(self.n+1):
                    j = s - i
                    if j > other.n or j < 0: continue
                    res[s] += self.A[i] * other.A[j]
                    res[s] %= self.mod
            self.A = res

        else:
            res = [0] * (self.n + other.n + 1)
            for i in range(self.n+1):
                for j in range(other.n+1):
                    res[i+j] += self.A[i] * other.A[j]
                    res[i+j] %= self.mod
            self.A = res


def main():
    N, M, K = NMI()
    f = [0] * (K+1)
    f[0] = 1
    f = FPS(f)
    g = [1] * (M + 1)
    g[0] = 0
    g = FPS(g)
    for _ in range(N):
        f.mul(g, lim=True)
        # print(f.A)
    print(sum(f.A[:K+1]) % MOD99)


if __name__ == "__main__":
    main()
