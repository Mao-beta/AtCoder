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


import cmath
class Vector:
    EPS = 1e-11

    def __init__(self, x, y):
        self.z = complex(x, y)

    def __add__(self, other):
        nz = self.z + other.z
        return Vector(nz.real, nz.imag)

    def __sub__(self, other):
        nz = self.z - other.z
        return Vector(nz.real, nz.imag)

    def __mul__(self, a):
        nz = self.z * a
        return Vector(nz.real, nz.imag)

    def __rmul__(self, a):
        return self * a

    def __truediv__(self, a):
        nz = self.z / a
        return Vector(nz.real, nz.imag)

    def __abs__(self):
        return abs(self.z)

    def __eq__(self, other):
        g = self - other
        return abs(g.real()) < self.EPS and abs(g.imag()) < self.EPS

    def real(self):
        return self.z.real

    def imag(self):
        return self.z.imag

    def norm(self):
        return self.real() ** 2 + self.imag() ** 2

    def dot(self, other):
        return (self.z * other.z.conjugate()).real

    def cross(self, other):
        a, b = self.real(), self.imag()
        c, d = other.real(), other.imag()
        return a * d - b * c

    def phase(self, degree=False):
        res = cmath.phase(self.z)
        if degree:
            res = math.degrees(res)
        return res

    def is_parallel(self, other):
        return abs(self.cross(other)) < self.EPS

    def is_orthogonal(self, other):
        return abs(self.dot(other)) < self.EPS

    def __repr__(self):
        return f"Vector({self.real()}, {self.imag()})"


class Line:
    def __init__(self, P: Vector, Q: Vector, is_segment: bool=False):
        self.D = Q - P
        if self.D.real() < 0:
            self.D *= -1
        self.P = P
        self.Q = None
        if is_segment:
            self.Q = Q
        self.is_segment = is_segment

    def projection(self, V: Vector):
        """点Vから直線への射影"""
        va = self.D
        vb = V - self.P
        return va.dot(vb) * va / va.norm() + self.P

    def reflection(self, V: Vector):
        """直線について点Vと対称な点"""
        proj = self.projection(V)
        return proj * 2 - V

    def is_on(self, V: Vector):
        proj = self.projection(V)
        return proj == V

    def __repr__(self):
        return f"Line({self.P}, {self.D})"


def main():
    A = NLI()
    B = NLI()
    C = NLI()

    A = Vector(*A)
    B = Vector(*B)
    C = Vector(*C)
    L = Line(B, C)
    M = L.projection(A)
    x = math.sqrt((M-A).norm())
    ab = math.sqrt((B-A).norm())
    ac = math.sqrt((C-A).norm())
    if (M-B).dot(M-C) < 0:
        print(x)
    else:
        print(min(ab, ac))



if __name__ == "__main__":
    main()
