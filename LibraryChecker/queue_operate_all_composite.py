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


class Matrix:
    def __init__(self, mat, mod=998244353):
        self.mat = mat
        self.mod = mod
        self.nrow = len(mat)
        self.ncol = len(mat[0])

    def inv(self):
        a, b = self.mat[0]
        c, d = self.mat[1]
        det = abs(a*d-b*c)
        invdet = pow(det, -1, self.mod)
        a2, d2 = d * invdet % self.mod, a * invdet % self.mod
        b2, c2 = -b * invdet % self.mod, -c * invdet % self.mod
        return Matrix([[a2, b2], [c2, d2]], self.mod)

    def __matmul__(self, other):
        a1, b1 = self.mat[0]
        c1, d1 = self.mat[1]
        a2, b2 = other.mat[0]
        c2, d2 = other.mat[1]
        mat = [[(a1*a2+b1*c2) % self.mod, (a1*b2+b1*d2) % self.mod],
               [(c1*a2+d1*c2) % self.mod, (c1*b2+d1*d2) % self.mod]]
        return Matrix(mat, self.mod)

def main():
    Q = NI()
    F = deque()
    A = Matrix([[1, 0],[0, 1]], MOD99)
    # y = (a b) x
    # 1   (0 1) 1
    # (y 1) = Fn Fn-1 ... F1 (x 1)
    for i in range(Q):
        q, *X = NMI()
        if q == 0:
            a, b = X
            Fi = Matrix([[a, b], [0, 1]], MOD99)
            F.append(Fi)
            A = Fi @ A
        elif q == 1:
            Fi = F.popleft()
            A = A @ Fi.inv()
        else:
            x = X[0]
            a, b = A.mat[0]
            print((a*x+b) % MOD99)


if __name__ == "__main__":
    main()
