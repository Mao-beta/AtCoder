import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def bostan_mori(A: FPS, Q: FPS, N: int):
    """数列A、d次の特性方程式QからN番目の項を計算する"""
    A = FPS(A.A)
    Q = FPS(Q.A)
    N -= 1

    while N > 0:
        # print(N)
        Q1 = FPS([q * (-1)**(i%2) for i, q in enumerate(Q.A)])
        A.mul(Q1)
        Q.mul(Q1)

        if N % 2 == 0:
            A = FPS(A.A[::2])
        else:
            A = FPS(A.A[1::2])
        Q = FPS(Q.A[::2])

        N >>= 1
        # print(A)

    return A.A[0]


def main():
    """ ABC159F, ABC169Fなど """
    A = FPS([0, 1, 1])
    Q = FPS([1, -1, -1])
    for i in range(10):
        res = bostan_mori(A, Q, i)
        print(res)


if __name__ == "__main__":
    main()
