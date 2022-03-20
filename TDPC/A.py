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
    def __init__(self, n, mod=998244353, A=None):
        """nは最高次の次数"""
        self.n = n
        self.A = [0] * (self.n+1)
        self.mod = mod

        if A is not None:
            for i, a in enumerate(A):
                self.A[i] = a

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


def main():
    N = NI()
    P = NLI()
    fps = FPS(10000)
    fps.add_a(1, 0)
    for p in P:
        fps.mul_base(1, 1, p)
    print(10001 - fps.A.count(0))


if __name__ == "__main__":
    main()
