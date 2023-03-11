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



# ACL for python
class FFT():
    def primitive_root_constexpr(self, m):
        if m == 2: return 1
        if m == 167772161: return 3
        if m == 469762049: return 3
        if m == 754974721: return 11
        if m == 998244353: return 3
        divs = [0] * 20
        divs[0] = 2
        cnt = 1
        x = (m - 1) // 2
        while (x % 2 == 0): x //= 2
        i = 3
        while (i * i <= x):
            if (x % i == 0):
                divs[cnt] = i
                cnt += 1
                while (x % i == 0):
                    x //= i
            i += 2
        if x > 1:
            divs[cnt] = x
            cnt += 1
        g = 2
        while (1):
            ok = True
            for i in range(cnt):
                if pow(g, (m - 1) // divs[i], m) == 1:
                    ok = False
                    break
            if ok:
                return g
            g += 1

    def bsf(self, x):
        res = 0
        while (x % 2 == 0):
            res += 1
            x //= 2
        return res

    rank2 = 0
    root = []
    iroot = []
    rate2 = []
    irate2 = []
    rate3 = []
    irate3 = []

    def __init__(self, MOD):
        self.mod = MOD
        self.g = self.primitive_root_constexpr(self.mod)
        self.rank2 = self.bsf(self.mod - 1)
        self.root = [0 for i in range(self.rank2 + 1)]
        self.iroot = [0 for i in range(self.rank2 + 1)]
        self.rate2 = [0 for i in range(self.rank2)]
        self.irate2 = [0 for i in range(self.rank2)]
        self.rate3 = [0 for i in range(self.rank2 - 1)]
        self.irate3 = [0 for i in range(self.rank2 - 1)]
        self.root[self.rank2] = pow(self.g, (self.mod - 1) >> self.rank2, self.mod)
        self.iroot[self.rank2] = pow(self.root[self.rank2], self.mod - 2, self.mod)
        for i in range(self.rank2 - 1, -1, -1):
            self.root[i] = (self.root[i + 1] ** 2) % self.mod
            self.iroot[i] = (self.iroot[i + 1] ** 2) % self.mod
        prod = 1;
        iprod = 1
        for i in range(self.rank2 - 1):
            self.rate2[i] = (self.root[i + 2] * prod) % self.mod
            self.irate2[i] = (self.iroot[i + 2] * iprod) % self.mod
            prod = (prod * self.iroot[i + 2]) % self.mod
            iprod = (iprod * self.root[i + 2]) % self.mod
        prod = 1;
        iprod = 1
        for i in range(self.rank2 - 2):
            self.rate3[i] = (self.root[i + 3] * prod) % self.mod
            self.irate3[i] = (self.iroot[i + 3] * iprod) % self.mod
            prod = (prod * self.iroot[i + 3]) % self.mod
            iprod = (iprod * self.root[i + 3]) % self.mod

    def butterfly(self, a):
        n = len(a)
        h = (n - 1).bit_length()

        LEN = 0
        while (LEN < h):
            if (h - LEN == 1):
                p = 1 << (h - LEN - 1)
                rot = 1
                for s in range(1 << LEN):
                    offset = s << (h - LEN)
                    for i in range(p):
                        l = a[i + offset]
                        r = a[i + offset + p] * rot
                        a[i + offset] = (l + r) % self.mod
                        a[i + offset + p] = (l - r) % self.mod
                    rot *= self.rate2[(~s & -~s).bit_length() - 1]
                    rot %= self.mod
                LEN += 1
            else:
                p = 1 << (h - LEN - 2)
                rot = 1
                imag = self.root[2]
                for s in range(1 << LEN):
                    rot2 = (rot * rot) % self.mod
                    rot3 = (rot2 * rot) % self.mod
                    offset = s << (h - LEN)
                    for i in range(p):
                        a0 = a[i + offset]
                        a1 = a[i + offset + p] * rot
                        a2 = a[i + offset + 2 * p] * rot2
                        a3 = a[i + offset + 3 * p] * rot3
                        a1na3imag = (a1 - a3) % self.mod * imag
                        a[i + offset] = (a0 + a2 + a1 + a3) % self.mod
                        a[i + offset + p] = (a0 + a2 - a1 - a3) % self.mod
                        a[i + offset + 2 * p] = (a0 - a2 + a1na3imag) % self.mod
                        a[i + offset + 3 * p] = (a0 - a2 - a1na3imag) % self.mod
                    rot *= self.rate3[(~s & -~s).bit_length() - 1]
                    rot %= self.mod
                LEN += 2

    def butterfly_inv(self, a):
        n = len(a)
        h = (n - 1).bit_length()
        LEN = h
        while (LEN):
            if (LEN == 1):
                p = 1 << (h - LEN)
                irot = 1
                for s in range(1 << (LEN - 1)):
                    offset = s << (h - LEN + 1)
                    for i in range(p):
                        l = a[i + offset]
                        r = a[i + offset + p]
                        a[i + offset] = (l + r) % self.mod
                        a[i + offset + p] = (l - r) * irot % self.mod
                    irot *= self.irate2[(~s & -~s).bit_length() - 1]
                    irot %= self.mod
                LEN -= 1
            else:
                p = 1 << (h - LEN)
                irot = 1
                iimag = self.iroot[2]
                for s in range(1 << (LEN - 2)):
                    irot2 = (irot * irot) % self.mod
                    irot3 = (irot * irot2) % self.mod
                    offset = s << (h - LEN + 2)
                    for i in range(p):
                        a0 = a[i + offset]
                        a1 = a[i + offset + p]
                        a2 = a[i + offset + 2 * p]
                        a3 = a[i + offset + 3 * p]
                        a2na3iimag = (a2 - a3) * iimag % self.mod
                        a[i + offset] = (a0 + a1 + a2 + a3) % self.mod
                        a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % self.mod
                        a[i + offset + 2 * p] = (a0 + a1 - a2 - a3) * irot2 % self.mod
                        a[i + offset + 3 * p] = (a0 - a1 - a2na3iimag) * irot3 % self.mod
                    irot *= self.irate3[(~s & -~s).bit_length() - 1]
                    irot %= self.mod
                LEN -= 2

    def convolution(self, a, b):
        n = len(a);
        m = len(b)
        if not (a) or not (b):
            return []
        if min(n, m) <= 40:
            res = [0] * (n + m - 1)
            for i in range(n):
                for j in range(m):
                    res[i + j] += a[i] * b[j]
                    res[i + j] %= self.mod
            return res
        z = 1 << ((n + m - 2).bit_length())
        a = a + [0] * (z - n)
        b = b + [0] * (z - m)
        self.butterfly(a)
        self.butterfly(b)
        c = [(a[i] * b[i]) % self.mod for i in range(z)]
        self.butterfly_inv(c)
        iz = pow(z, self.mod - 2, self.mod)
        for i in range(n + m - 1):
            c[i] = (c[i] * iz) % self.mod
        return c[:n + m - 1]


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


def _bostan_mori(A: FPS, Q: FPS, N: int):
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


M = 5

def mul_sparse(f: list, a, b, k, M):
    """(a + b * x^k)倍  x^Mまで"""
    res = f.copy()
    for i in range(M+1):
        res[i] += f[i] * (a-1)
        if i+k <= M:
            res[i+k] += f[i] * b
        res[i] %= MOD
    return res

def div_sparse_one(f: list, k, M):
    """(1-x^k)で割る x^Mまで"""
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


def mul(f, g, mod=998244353):
    """愚直畳み込み"""
    fn = len(f)
    gn = len(g)
    res = [0] * (fn + gn - 1)
    for fi in range(fn):
        for gi in range(gn):
            res[fi+gi] += f[fi] * g[gi] % mod
            res[fi+gi] %= mod
    return res





# def bostan_mori(A: list, Q: list, n: int, mod=998244353):
#     """
#     d+1項間線形漸化式Qをもつ数列Aの第n項 modをもとめる
#     O(M(d)logN) M(d)はd次多項式同士の積の計算量(現在はO(d^2 logN))
#     http://q.c.titech.ac.jp/docs/progs/polynomial_division.html
#
#     :param A: 数列のd項まで
#     :param Q: 母関数の分母をあらわすd+1項のlist
#         (フィボナッチなら An - An-1 - An-2 = 0 なので [1, -1, -1])
#     :param n: 求めたい第n項(0-index)
#     :return: A[n]
#     """
#     assert len(A) == len(Q) - 1
#
#     while n > 0:
#         Qm = [-q if i % 2 else q for i, q in enumerate(Q)]
#         V = mul(Q, Qm, mod)
#         Q = [v for i, v in enumerate(V) if i % 2 == 0]
#         AQm = mul(A, Qm, mod)
#         if n % 2 == 0:
#             A = AQm[::2]
#             n >>= 1
#         else:
#             A = AQm[1::2]
#             n -= 1
#             n >>= 1
#         # print(n, AQm, V, A)
#
#     return A[0]



# 要FFT
def mul_fft(f, g, fft):
    """FFT畳み込み"""
    # fft = FFT(mod)
    res = fft.convolution(f, g)
    return res

fft = FFT(MOD99)

def bostan_mori_fft(P: list, Q: list, fft: FFT, n: int):
    """
    d+1項間線形漸化式Qをもつ数列の第n項 modをもとめる
    A = P / Q
    O(M(d)logN) M(d)はd次多項式同士の積の計算量(O(dlogd logN))
    d <= 15000くらいは2秒以内で計算できそう
    http://q.c.titech.ac.jp/docs/progs/polynomial_division.html

    :param P: 母関数の分子を表すd項以下のlist
    :param Q: 母関数の分母をあらわすd+1項のlist
        (フィボナッチなら An - An-1 - An-2 = 0 なので Q=[1, -1, -1])
    :param n: 求めたい第n項(0-index)
    :return: A[n]
    """

    while n > 0:
        Qm = [-q if i % 2 else q for i, q in enumerate(Q)]
        V = mul_fft(Q, Qm, fft)
        Q = V[::2]
        PQm = mul_fft(P, Qm, fft)
        if n % 2 == 0:
            P = PQm[::2]
            n >>= 1
        else:
            P = PQm[1::2]
            n >>= 1

    return P[0]


def main():
    """ ABC159F, ABC169Fなど """

    # フィボナッチの母関数は 1 / (1-x-x^2)
    P = [1]
    Q = [1, -1, -1]

    for i in range(5):
        res = bostan_mori_fft(P, Q, fft, i)
        print(i, res)


if __name__ == "__main__":
    main()
