import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


MOD = 998244353

sum_e = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 0, 0, 0, 0, 0, 0, 0, 0, 0)
sum_ie = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 0, 0, 0, 0, 0, 0, 0, 0, 0)

def butterfly(arr):
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p] * now
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (l - r) % MOD
            now *= sum_e[(~s & -~s).bit_length() - 1]
            now %= MOD

def butterfly_inv(arr):
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1)[::-1]:
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p]
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (MOD + l - r) * inow % MOD
            inow *= sum_ie[(~s & -~s).bit_length() - 1]
            inow %= MOD
    inv = pow(n, MOD - 2, MOD)
    for i in range(n):
        arr[i] *= inv
        arr[i] %= MOD

def build_exp(n, b):
    exp = [0] * (n + 1)
    exp[0] = 1
    for i in range(n):
        exp[i + 1] = exp[i] * b % MOD
    return exp

def build_factorial(n):
    fct = [0] * (n + 1)
    inv = [0] * (n + 1)
    fct[0] = inv[0] = 1
    for i in range(n):
        fct[i + 1] = fct[i] * (i + 1) % MOD
    inv[n] = pow(fct[n], MOD - 2, MOD)
    for i in range(n)[::-1]:
        inv[i] = inv[i + 1] * (i + 1) % MOD
    return fct, inv

def sqrt_mod(n):
    if n == 0: return 0
    if n == 1: return 1
    h = (MOD - 1) // 2
    if pow(n, h, MOD) != 1: return -1
    q, s = MOD - 1, 0
    while not q & 1:
        q >>= 1
        s += 1
    z = 1
    while pow(z, h, MOD) != MOD - 1:
        z += 1
    m, c, t, r = s, pow(z, q, MOD), pow(n, q, MOD), pow(n, (q + 1) // 2, MOD)
    while t != 1:
        k = 1
        while pow(t, 1 << k, MOD) != 1:
            k += 1
        x = pow(c, pow(2, m - k - 1, MOD - 1), MOD)
        m = k
        c = (x * x) % MOD
        t = (t * c) % MOD
        r = (r * x) % MOD
    if r * r % MOD != n: return -1
    return r

class FormalPowerSeries():
    def __init__(self, arr=None):
        if arr is None: arr = []
        self.arr = [v % MOD for v in arr]

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return FormalPowerSeries(self.arr[key])
        else:
            assert key >= 0
            if key >= len(self):
                return 0
            else:
                return self.arr[key]

    def __setitem__(self, key, val):
        assert key >= 0
        if key >= len(self):
            self.arr += [0] * (key - len(self) + 1)
        self.arr[key] = val % MOD

    def __str__(self):
        return ' '.join(map(str, self.arr))

    def resize(self, sz):
        assert sz >= 0
        if len(self) >= sz:
            return self[:sz]
        else:
            return FormalPowerSeries(self.arr + [0] * (sz - len(self)))

    def shrink(self):
        while self.arr and not self.arr[-1]:
            self.arr.pop()

    def times(self, k):
        return FormalPowerSeries([v * k for v in self.arr])

    def __pos__(self):
        return self

    def __neg__(self):
        return self.times(-1)

    def __add__(self, other):
        if other.__class__ == FormalPowerSeries:
            n = len(self)
            m = len(other)
            arr = [self[i] + other[i] for i in range(min(n, m))]
            if n >= m:
                arr += self.arr[m:]
            else:
                arr += other.arr[n:]
            return FormalPowerSeries(arr)
        else:
            return self + FormalPowerSeries([other])

    def __iadd__(self, other):
        if other.__class__ == FormalPowerSeries:
            n = len(self)
            m = len(other)
            for i in range(min(n, m)):
                self.arr[i] += other[i]
                self.arr[i] %= MOD
            if n < m:
                self.arr += other.arr[n:]
        else:
            self.arr[0] += other
            self.arr[0] %= MOD
        return self

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __isub__(self, other):
        self += -other
        return self

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if other.__class__ == FormalPowerSeries:
            f = self.arr.copy()
            g = other.arr.copy()
            n = len(f)
            m = len(g)
            if not n or not m: return FormalPowerSeries()
            if min(n, m) <= 100:
                if n < m: f, n, g, m = g, m, f, n
                arr = [0] * (n + m - 1)
                for i in range(n):
                    for j in range(m):
                        arr[i + j] += f[i] * g[j]
                        arr[i + j] %= MOD
                return FormalPowerSeries(arr)
            z = 1 << (n + m - 2).bit_length()
            f += [0] * (z - n)
            g += [0] * (z - m)
            butterfly(f)
            butterfly(g)
            for i in range(z):
                f[i] *= g[i]
                f[i] %= MOD
            butterfly_inv(f)
            f = f[:n + m - 1]
            return FormalPowerSeries(f)
        else:
            return self.times(other)

    def __matmul__(self, other):
        assert other.__class__ == FormalPowerSeries
        n = max(len(self), len(other))
        res = (self * other).resize(n)
        return res

    def __imul__(self, other):
        if other.__class__ == FormalPowerSeries:
            f = self.arr.copy()
            g = other.arr.copy()
            n = len(f)
            m = len(g)
            if not n or not m: return FormalPowerSeries()
            if min(n, m) <= 100:
                if n < m: f, n, g, m = g, m, f, n
                arr = [0] * (n + m - 1)
                for i in range(n):
                    for j in range(m):
                        arr[i + j] += f[i] * g[j]
                        arr[i + j] %= MOD
                self.arr = arr
                return self
            z = 1 << (n + m - 2).bit_length()
            f += [0] * (z - n)
            g += [0] * (z - m)
            butterfly(f)
            butterfly(g)
            for i in range(z):
                f[i] *= g[i]
                f[i] %= MOD
            butterfly_inv(f)
            self.arr = f[:n + m - 1]
            return self
        else:
            n = len(self)
            for i in range(n):
                self.arr[i] *= other
                self.arr[i] %= MOD
            return self

    def __rmul__(self, other):
        return self.times(other)

    def __pow__(self, k): #exp書いたら修正
        n = len(self)
        tmp = FormalPowerSeries(self.arr)
        res = FormalPowerSeries([1])
        while k:
            if k & 1:
                res *= tmp
                res = res.resize(n)
            tmp *= tmp
            tmp = tmp.resize(n)
            k >>= 1
        return res

    def square(self):
        f = self.arr.copy()
        n = len(f)
        if not n: return FormalPowerSeries()
        if n <= 100:
            arr = [0] * (2 * n - 1)
            for i in range(n):
                for j in range(n):
                    arr[i + j] += f[i] * f[j]
                    arr[i + j] %= MOD
            return FormalPowerSeries(arr)
        z = 1 << (2 * n - 2).bit_length()
        f += [0] * (z - n)
        butterfly(f)
        for i in range(z):
            f[i] *= f[i]
            f[i] %= MOD
        butterfly_inv(f)
        f = f[:2 * n - 1]
        return FormalPowerSeries(f)

    def __lshift__(self, key):
        assert key >= 0
        return FormalPowerSeries([0] * key + self.arr)

    def __rshift__(self, key):
        assert key >= 0
        return self[key:]

    def __invert__(self):
        assert self[0] != 0
        n = len(self)
        r = pow(self[0], MOD - 2, MOD)
        m = 1
        res = FormalPowerSeries([r])
        while m < n:
            f = [0] * (2 * m)
            g = [0] * (2 * m)
            for i in range(2 * m):
                f[i] = self[i]
            for i in range(m):
                g[i] = res[i]
            butterfly(f)
            butterfly(g)
            for i in range(2 * m):
                f[i] *= g[i]
                f[i] %= MOD
            butterfly_inv(f)
            for i in range(m):
                f[i] = 0
            butterfly(f)
            for i in range(2 * m):
                f[i] *= g[i]
                f[i] %= MOD
            butterfly_inv(f)
            for i in range(m, 2 * m):
                res[i] -= f[i]
            m <<= 1
        return res.resize(n)

    def __truediv__(self, other):
        if other.__class__ == FormalPowerSeries:
            return self * ~other
        else:
            return self * pow(other, MOD - 2, MOD)

    def __rtruediv__(self, other):
        return other * ~self

    def differentiate(self):
        n = len(self)
        arr = [0] * n
        for i in range(1, n):
            arr[i - 1] = self[i] * i % MOD
        return FormalPowerSeries(arr)

    def integrate(self):
        n = len(self)
        arr = [0] * n
        for i in range(n - 1):
            arr[i + 1] = self[i] * pow(i + 1, MOD - 2, MOD) % MOD
        return FormalPowerSeries(arr)

    def log(self):
        assert self[0] == 1
        n = len(self)
        return (self.differentiate() / self).integrate().resize(n)

    def __floordiv__(self, other):
        if other.__class__ == FormalPowerSeries:
            n = len(self)
            m = len(other)
            if n < m: return FormalPowerSeries()
            l = n - m + 1
            if m <= 100:
                arr = [0] * l
                inv = pow(other[m - 1], MOD - 2, MOD)
                tmp = self[::-1]
                for i in range(l):
                    arr[i] = tmp[i] * inv % MOD
                    for j in range(m):
                        tmp[i + j] -= other[m - j - 1] * arr[i]
                        tmp[i + j] %= MOD
                return FormalPowerSeries(arr[::-1])
            res = (self[~l:][::-1] * ~(other[::-1].resize(l))).resize(l)[::-1]
            return res
        else:
            return self * pow(other, MOD - 2, MOD)

    def __rfloordiv__(self, other):
        return other * ~self

    def __mod__(self, other):
        n = len(self)
        m = len(other)
        if n < m: return FormalPowerSeries(self.arr)
        res = self[:m - 1] - ((self // other) * other)[:m - 1]
        return res

    def multipoint_evaluation(self, xs):
        n = len(xs)
        sz = 1 << (n - 1).bit_length()
        g = [FormalPowerSeries([1]) for _ in range(2 * sz)]
        for i in range(n):
            g[i + sz] = FormalPowerSeries([-xs[i], 1])
        for i in range(1, sz)[::-1]:
            g[i] = g[2 * i] * g[2 * i + 1]
        g[1] = self % g[1]
        for i in range(2, 2 * sz):
            g[i] = g[i >> 1] % g[i]
        res = [g[i + sz][0] for i in range(n)]
        return res

def polynomial_interpolation(xs, ys):
    assert len(xs) == len(ys)
    n = len(xs)
    sz = 1 << (n - 1).bit_length()
    f = [FormalPowerSeries([1]) for _ in range(2 * sz)]
    for i in range(n):
        f[i + sz] = FormalPowerSeries([-xs[i], 1])
    for i in range(1, sz)[::-1]:
        f[i] = f[2 * i] * f[2 * i + 1]
    g = [FormalPowerSeries([0])] * (2 * sz)
    g[1] = f[1].differentiate() % f[1]
    for i in range(2, n + sz):
        g[i] = g[i >> 1] % f[i]
    for i in range(n):
        g[i + sz] = FormalPowerSeries([ys[i] * pow(g[i + sz][0], MOD - 2, MOD) % MOD])
    for i in range(1, sz)[::-1]:
        g[i] = g[2 * i] * f[2 * i + 1] + g[2 * i + 1] * f[2 * i]
    return g[1][:n]

def berlekamp_massey(arr):
    if arr.__class__ == FormalPowerSeries:
        arr = arr.arr
    n = len(arr)
    b = [1]
    c = [1]
    l, m, p = 0, 0, 1
    for i in range(n):
        m += 1
        d = arr[i]
        for j in range(1, l + 1):
            d += c[j] * arr[i - j]
            d %= MOD
        if d == 0: continue
        t = c.copy()
        q = d * pow(p, MOD - 2, MOD) % MOD
        if len(c) < len(b) + m:
            c += [0] * (len(b) + m - len(c))
        for j in range(len(b)):
            c[j + m] -= q * b[j]
            c[j + m] %= MOD
        if 2 * l <= i:
            b = t
            l, m, p = i + 1 - l, 0, d
    return c

def linear_recurrence(arr, coeff, k):
    if arr.__class__ == FormalPowerSeries:
        arr = arr.arr
    d = len(arr)
    f = FormalPowerSeries(arr)
    q = FormalPowerSeries(coeff)
    p = (f * q).resize(d)
    while k:
        r = [-q[i] if i & 1 else q[i] for i in range(len(q))] + [0] * (d + 1 - len(q))
        r = FormalPowerSeries(r)
        p *= r
        q *= r
        p = p[(k & 1)::2]
        q = q[::2]
        k >>= 1
    return p[0] % MOD


def main():
    N, M = NMI()
    C = NLI()
    P = NLI()

    F = FormalPowerSeries(C) # 多項式定義
    res = F.multipoint_evaluation(P) # 多点取得
    print(*res)


if __name__ == "__main__":
    main()
