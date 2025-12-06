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


MOD = 998244353
_IMAG = 911660635
_IIMAG = 86583718
_rate2 = (
    0,
    911660635,
    509520358,
    369330050,
    332049552,
    983190778,
    123842337,
    238493703,
    975955924,
    603855026,
    856644456,
    131300601,
    842657263,
    730768835,
    942482514,
    806263778,
    151565301,
    510815449,
    503497456,
    743006876,
    741047443,
    56250497,
    867605899,
    0,
)
_irate2 = (
    0,
    86583718,
    372528824,
    373294451,
    645684063,
    112220581,
    692852209,
    155456985,
    797128860,
    90816748,
    860285882,
    927414960,
    354738543,
    109331171,
    293255632,
    535113200,
    308540755,
    121186627,
    608385704,
    438932459,
    359477183,
    824071951,
    103369235,
    0,
)
_rate3 = (
    0,
    372528824,
    337190230,
    454590761,
    816400692,
    578227951,
    180142363,
    83780245,
    6597683,
    70046822,
    623238099,
    183021267,
    402682409,
    631680428,
    344509872,
    689220186,
    365017329,
    774342554,
    729444058,
    102986190,
    128751033,
    395565204,
    0,
)
_irate3 = (
    0,
    509520358,
    929031873,
    170256584,
    839780419,
    282974284,
    395914482,
    444904435,
    72135471,
    638914820,
    66769500,
    771127074,
    985925487,
    262319669,
    262341272,
    625870173,
    768022760,
    859816005,
    914661783,
    430819711,
    272774365,
    530924681,
    0,
)


def _fft(a):
    n = len(a)
    h = (n - 1).bit_length()
    le = 0
    for le in range(0, h - 1, 2):
        p = 1 << (h - le - 2)
        rot = 1
        for s in range(1 << le):
            rot2 = rot * rot % MOD
            rot3 = rot2 * rot % MOD
            offset = s << (h - le)
            for i in range(p):
                a0 = a[i + offset]
                a1 = a[i + offset + p] * rot
                a2 = a[i + offset + p * 2] * rot2
                a3 = a[i + offset + p * 3] * rot3
                a1na3imag = (a1 - a3) % MOD * _IMAG
                a[i + offset] = (a0 + a2 + a1 + a3) % MOD
                a[i + offset + p] = (a0 + a2 - a1 - a3) % MOD
                a[i + offset + p * 2] = (a0 - a2 + a1na3imag) % MOD
                a[i + offset + p * 3] = (a0 - a2 - a1na3imag) % MOD
            rot = rot * _rate3[(~s & -~s).bit_length()] % MOD
    if h - le & 1:
        rot = 1
        for s in range(1 << (h - 1)):
            offset = s << 1
            l = a[offset]
            r = a[offset + 1] * rot
            a[offset] = (l + r) % MOD
            a[offset + 1] = (l - r) % MOD
            rot = rot * _rate2[(~s & -~s).bit_length()] % MOD


def _ifft(a):
    n = len(a)
    h = (n - 1).bit_length()
    le = h
    for le in range(h, 1, -2):
        p = 1 << (h - le)
        irot = 1
        for s in range(1 << (le - 2)):
            irot2 = irot * irot % MOD
            irot3 = irot2 * irot % MOD
            offset = s << (h - le + 2)
            for i in range(p):
                a0 = a[i + offset]
                a1 = a[i + offset + p]
                a2 = a[i + offset + p * 2]
                a3 = a[i + offset + p * 3]
                a2na3iimag = (a2 - a3) * _IIMAG % MOD
                a[i + offset] = (a0 + a1 + a2 + a3) % MOD
                a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % MOD
                a[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % MOD
                a[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % MOD
            irot = irot * _irate3[(~s & -~s).bit_length()] % MOD
    if le & 1:
        p = 1 << (h - 1)
        for i in range(p):
            l = a[i]
            r = a[i + p]
            a[i] = l + r if l + r < MOD else l + r - MOD
            a[i + p] = l - r if l - r >= 0 else l - r + MOD


def ntt(a) -> None:
    if len(a) <= 1:
        return
    _fft(a)


def intt(a) -> None:
    if len(a) <= 1:
        return
    _ifft(a)
    iv = pow(len(a), MOD - 2, MOD)
    for i, x in enumerate(a):
        a[i] = x * iv % MOD


def multiply(s: list, t: list) -> list:
    n, m = len(s), len(t)
    l = n + m - 1
    if min(n, m) <= 60:
        a = [0] * l
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                a[i + j] += x * y
        return [x % MOD for x in a]
    z = 1 << (l - 1).bit_length()
    a = s + [0] * (z - n)
    b = t + [0] * (z - m)
    _fft(a)
    _fft(b)
    for i, x in enumerate(b):
        a[i] = a[i] * x % MOD
    _ifft(a)
    a[l:] = []
    iz = pow(z, MOD - 2, MOD)
    return [x * iz % MOD for x in a]


def pow2(a: list) -> list:
    l = (len(a) << 1) - 1
    if len(a) <= 60:
        s = [0] * l
        for i, x in enumerate(a):
            for j, y in enumerate(a):
                s[i + j] += x * y
        return [x % MOD for x in s]
    k = 2
    M = 4
    while M < l:
        M <<= 1
        k += 1
    s = a + [0] * (M - len(a))
    _fft(s, k)
    s = [x * x % MOD for x in s]
    _ifft(s, k)
    s[l:] = []
    invm = pow(M, MOD - 2, MOD)
    return [x * invm % MOD for x in s]


def ntt_doubling(a: list) -> None:
    M = len(a)
    intt(a)
    r = 1
    zeta = pow(3, (MOD - 1) // (M << 1), MOD)
    for i, x in enumerate(a):
        a[i] = x * r % MOD
        r = r * zeta % MOD
    ntt(a)

class FPS:
    """
    高速数列演算(Fast Polynomial Series, FPS)を実装したクラス。

    このクラスでは、多項式の加減乗除、対数、指数、冪乗、積分、微分などの
    演算を効率的に行うための関数群を提供します。
    また、数列の縮約や特定のスカラーとの演算もサポートします。

    主な機能：
    - 多項式の加算・減算・乗算・除算
    - 多項式のスカラー加算・減算・乗算
    - 多項式の微分・積分
    - 多項式の対数・指数
    - 特定の値での多項式の評価
    - 逆数列の計算
    - 商と余りの計算

    注意：
    全ての演算は特定の法 (MOD = 998244353) における有限体上で行われます。

    メソッドの説明：
    - shrink(a): 与えられた数列 a の末尾にあるゼロを削除します。
    - add(a, b): 2つの数列 a, b の和を計算します。
    - add_scalar(a, k): 数列 a の定数項にスカラー k を加算します。
    - sub(a, b): 2つの数列 a, b の差を計算します。
    - sub_scalar(a, k): 数列 a の定数項からスカラー k を減算します。
    - neg(a): 数列 a の全ての要素を負数にします。
    - mul_scalar(a, k): 数列 a の全ての要素をスカラー k で乗算します。
    - matmul(a, b): (未検証) 要素ごとの積を計算します。
    - div(a, b): 数列 a を数列 b で割った結果を計算します。
    - mod(a, b): 数列 a を数列 b で割った余りを計算します。
    - divmod(a, b): 数列 a を数列 b で割った商と余りをタプルで返します。
    - eval(a, x): 数列 a を特定の値 x で評価した結果を返します。
    - inv(a, deg): 数列 a の逆数列を指定した次数まで計算します。
    - pow(a, k, deg): 数列 a の k 乗を指定した次数まで計算します。
    - exp(a, deg): 数列 a の指数関数を指定した次数まで計算します。
    - log(a, deg): 数列 a の対数を指定した次数まで計算します。
    - integral(a): 数列 a の積分を計算します。
    - fps_diff(a): 数列 a の微分を計算します。

    使用例：
    ```
    MOD = 998244353
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = FPS.add(a, b)  # [5, 7, 9]
    ```
    """
    @staticmethod
    def shrink(a: list) -> None:
        while a and not a[-1]:
            a.pop()

    @staticmethod
    def add(a: list, b: list) -> list:
        if len(a) < len(b):
            res = b[::]
            for i, x in enumerate(a):
                res[i] += x
        else:
            res = a[::]
            for i, x in enumerate(b):
                res[i] += x
        return [x % MOD for x in res]

    @staticmethod
    def add_scalar(a: list, k: int) -> list:
        res = a[:]
        res[0] = (res[0] + k) % MOD
        return res

    @classmethod
    def sub(cls, a: list, b: list) -> list:
        if len(a) < len(b):
            res = b[::]
            for i, x in enumerate(a):
                res[i] -= x
            res = cls.neg(res)
        else:
            res = a[::]
            for i, x in enumerate(b):
                res[i] -= x
        return [x % MOD for x in res]

    @classmethod
    def sub_scalar(cls, a: list, k: int) -> list:
        return cls.add_scalar(a, -k)

    @staticmethod
    def neg(a: list) -> list:
        return [MOD - x if x else 0 for x in a]

    @staticmethod
    def mul_scalar(a: list, k: int) -> list:
        return [x * k % MOD for x in a]

    @staticmethod
    def matmul(a: list, b: list) -> list:
        "not verified"
        return [x * b[i] % MOD for i, x in enumerate(a)]

    @classmethod
    def div(cls, a: list, b: list) -> list:
        if len(a) < len(b):
            return []
        n = len(a) - len(b) + 1
        cnt = 0
        if len(b) > 64:
            return multiply(a[::-1][:n], cls.inv(b[::-1], n))[:n][::-1]
        f, g = a[::], b[::]
        while g and not g[-1]:
            g.pop()
            cnt += 1
        coef = pow(g[-1], MOD - 2, MOD)
        g = cls.mul_scalar(g, coef)
        deg = len(f) - len(g) + 1
        gs = len(g)
        quo = [0] * deg
        for i in range(deg)[::-1]:
            quo[i] = x = f[i + gs - 1] % MOD
            for j, y in enumerate(g):
                f[i + j] -= x * y
        return cls.mul_scalar(quo, coef) + [0] * cnt

    @classmethod
    def mod(cls, a: list, b: list) -> list:
        res = cls.sub(a, multiply(cls.div(a, b), b))
        while res and not res[-1]:
            res.pop()
        return res

    @classmethod
    def divmod(cls, a: list, b: list):
        q = cls.div(a, b)
        r = cls.sub(a, multiply(q, b))
        while r and not r[-1]:
            r.pop()
        return q, r

    @staticmethod
    def eval(a: list, x: int) -> int:
        r = 0
        w = 1
        for v in a:
            r += w * v % MOD
            w = w * x % MOD
        return r % MOD

    @staticmethod
    def inv(a: list, deg: int = -1) -> list:
        # assert(self[0] != 0)
        if deg == -1:
            deg = len(a)
        res = [0] * deg
        res[0] = pow(a[0], MOD - 2, MOD)
        d = 1
        while d < deg:
            f = [0] * (d << 1)
            tmp = min(len(a), d << 1)
            f[:tmp] = a[:tmp]
            g = [0] * (d << 1)
            g[:d] = res[:d]
            ntt(f)
            ntt(g)
            for i, x in enumerate(g):
                f[i] = f[i] * x % MOD
            intt(f)
            f[:d] = [0] * d
            ntt(f)
            for i, x in enumerate(g):
                f[i] = f[i] * x % MOD
            intt(f)
            for j in range(d, min(d << 1, deg)):
                if f[j]:
                    res[j] = MOD - f[j]
                else:
                    res[j] = 0
            d <<= 1
        return res

    @classmethod
    def pow(cls, a: list, k: int, deg=-1) -> list:
        n = len(a)
        if deg == -1:
            deg = n
        if k == 0:
            if not deg:
                return []
            ret = [0] * deg
            ret[0] = 1
            return ret
        for i, x in enumerate(a):
            if x:
                rev = pow(x, MOD - 2, MOD)
                ret = cls.mul_scalar(
                    cls.exp(
                        cls.mul_scalar(cls.log(cls.mul_scalar(a, rev)[i:], deg), k), deg
                    ),
                    pow(x, k, MOD),
                )
                ret[:0] = [0] * (i * k)
                if len(ret) < deg:
                    ret[len(ret) :] = [0] * (deg - len(ret))
                    return ret
                return ret[:deg]
            if (i + 1) * k >= deg:
                break
        return [0] * deg

    @staticmethod
    def exp(a: list, deg=-1) -> list:
        # assert(not self or self[0] == 0)
        if deg == -1:
            deg = len(a)
        inv = [0, 1]

        def inplace_integral(F: list) -> list:
            n = len(F)
            while len(inv) <= n:
                j, k = divmod(MOD, len(inv))
                inv.append((-inv[k] * j) % MOD)
            return [0] + [x * inv[i + 1] % MOD for i, x in enumerate(F)]

        def inplace_diff(F: list) -> list:
            return [x * i % MOD for i, x in enumerate(F) if i]

        b = [1, (a[1] if 1 < len(a) else 0)]
        c = [1]
        z1 = []
        z2 = [1, 1]
        m = 2
        while m < deg:
            y = b + [0] * m
            ntt(y)
            z1 = z2
            z = [y[i] * p % MOD for i, p in enumerate(z1)]
            intt(z)
            z[: m >> 1] = [0] * (m >> 1)
            ntt(z)
            for i, p in enumerate(z1):
                z[i] = z[i] * (-p) % MOD
            intt(z)
            c[m >> 1 :] = z[m >> 1 :]
            z2 = c + [0] * m
            ntt(z2)
            tmp = min(len(a), m)
            x = a[:tmp] + [0] * (m - tmp)
            x = inplace_diff(x)
            x.append(0)
            ntt(x)
            for i, p in enumerate(x):
                x[i] = y[i] * p % MOD
            intt(x)
            for i, p in enumerate(b):
                if not i:
                    continue
                x[i - 1] -= p * i % MOD
            x += [0] * m
            for i in range(m - 1):
                x[m + i], x[i] = x[i], 0
            ntt(x)
            for i, p in enumerate(z2):
                x[i] = x[i] * p % MOD
            intt(x)
            x.pop()
            x = inplace_integral(x)
            x[:m] = [0] * m
            for i in range(m, min(len(a), m << 1)):
                x[i] += a[i]
            ntt(x)
            for i, p in enumerate(y):
                x[i] = x[i] * p % MOD
            intt(x)
            b[m:] = x[m:]
            m <<= 1
        return b[:deg]

    @classmethod
    def log(cls, a: list, deg=-1) -> list:
        # assert(a[0] == 1)
        if deg == -1:
            deg = len(a)
        return cls.integral(multiply(cls.fps_diff(a), cls.inv(a, deg))[: deg - 1])

    @staticmethod
    def integral(a: list) -> list:
        n = len(a)
        res = [0] * (n + 1)
        if n:
            res[1] = 1
        for i in range(2, n + 1):
            j, k = divmod(MOD, i)
            res[i] = (-res[k] * j) % MOD
        for i, x in enumerate(a):
            res[i + 1] = res[i + 1] * x % MOD
        return res

    @staticmethod
    def fps_diff(a: list) -> list:
        return [i * x % MOD for i, x in enumerate(a) if i]


def main():
    N, M, L = NMI()
    A = NLI()
    B = set(NLI())
    F = [0] * (2*N)
    F[0] = 1
    G = [0] * (2*N)
    for a in A:
        G[a] = pow(M, -1, MOD99)

    def dc_fft(l, r):
        # 分割統治FFT
        # 終了条件
        if r-l <= 0:
            return
        if r-l == 1:
            if l in B:
                F[l] = 0
            return

        m = (l+r) // 2
        # 左の区間について再帰
        dc_fft(l, m)

        # [l,m) -> [m,r) のdp遷移
        if l < N:
            f = F[l:min(N,m)]
            g = G[:r-l]
            h = multiply(f, g)
            for i in range(m, r):
                F[i] += h[i-l]
                F[i] %= MOD99

        # 右の区間について再帰
        dc_fft(m, r)

    dc_fft(0, 2*N)
    # print(F)
    print(sum(F[N:2*N]) % MOD99)


if __name__ == "__main__":
    main()
