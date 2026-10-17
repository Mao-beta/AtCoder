"""998244353固定のNTT・FPS・多項式GCD/逆元・特殊数列。係数は低次から。
抽出元: LibraryChecker/LC_Inv_of_Polynomials.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。
"""

FPS_MOD = 998244353


_FPS_SUM_E = (
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
)


_FPS_SUM_IE = (
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
)


def _fps_sqrt_mod(a):
    a %= FPS_MOD
    if a < 2:
        return a
    k = (FPS_MOD - 1) // 2
    if pow(a, k, FPS_MOD) != 1:
        return -1
    b = 1
    while pow(b, k, FPS_MOD) == 1:
        b += 1
    m, e = FPS_MOD - 1, 0
    while m % 2 == 0:
        m >>= 1
        e += 1
    x = pow(a, (m - 1) // 2, FPS_MOD)
    y = a * x * x % FPS_MOD
    x *= a
    x %= FPS_MOD
    z = pow(b, m, FPS_MOD)
    while y != 1:
        j, t = 0, y
        while t != 1:
            j += 1
            t *= t
            t %= FPS_MOD
        z = pow(z, 1 << (e - j - 1), FPS_MOD)
        x *= z
        x %= FPS_MOD
        z *= z
        z %= FPS_MOD
        y *= z
        y %= FPS_MOD
        e = j
    return x


def _fps_inv_mod(a):
    a %= FPS_MOD
    if a == 0:
        raise ZeroDivisionError("inverse of zero")
    s, t = FPS_MOD, a
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0:
        m0 += FPS_MOD // s
    return m0


_fps_fac = [1, 1]


_fps_finv = [1, 1]


_fps_inv = [1, 1]


def _fps_factorial(i):
    while i >= len(_fps_fac):
        _fps_fac.append(_fps_fac[-1] * len(_fps_fac) % FPS_MOD)
    return _fps_fac[i]


def _fps_factorial_inverse(i):
    while i >= len(_fps_inv):
        _fps_inv.append(
            (-_fps_inv[FPS_MOD % len(_fps_inv)]) * (FPS_MOD // len(_fps_inv)) % FPS_MOD
        )
    while i >= len(_fps_finv):
        _fps_finv.append(_fps_finv[-1] * _fps_inv[len(_fps_finv)] % FPS_MOD)
    return _fps_finv[i]


def _fps_integer_inverse(i):
    while i >= len(_fps_inv):
        _fps_inv.append(
            (-_fps_inv[FPS_MOD % len(_fps_inv)]) * (FPS_MOD // len(_fps_inv)) % FPS_MOD
        )
    return _fps_inv[i]


def butterfly(A):
    n = len(A)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = A[i + offset]
                r = A[i + offset + p] * now
                A[i + offset] = (l + r) % FPS_MOD
                A[i + offset + p] = (l - r) % FPS_MOD
            now *= _FPS_SUM_E[(~s & -~s).bit_length() - 1]
            now %= FPS_MOD


def butterfly_inv(A):
    n = len(A)
    h = (n - 1).bit_length()
    for ph in range(h, 0, -1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = A[i + offset]
                r = A[i + offset + p]
                A[i + offset] = (l + r) % FPS_MOD
                A[i + offset + p] = (FPS_MOD + l - r) * inow % FPS_MOD
            inow *= _FPS_SUM_IE[(~s & -~s).bit_length() - 1]
            inow %= FPS_MOD


def convolution(mod, a, b=None):
    """ACL Python版の convolution(mod, a, b)。mod=998244353専用。

    旧 convolution(a, b) は998244353として保持する。
    任意modの畳み込み・整数畳み込みには対応しない。
    """
    if b is None:
        _A, _B = mod, a
    else:
        if mod != FPS_MOD:
            raise ValueError("only modulus 998244353 is supported")
        _A, _B = a, b
    A = [x % FPS_MOD for x in _A]
    B = [x % FPS_MOD for x in _B]
    n = len(A)
    m = len(B)
    if not n or not m:
        return []
    if min(n, m) <= 60:
        if n < m:
            n, m = m, n
            A, B = B, A
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += A[i] * B[j]
                res[i + j] %= FPS_MOD
        return res
    z = 1 << (n + m - 2).bit_length()
    if z > 1 << 23:
        raise ValueError("NTT length exceeds 2**23")
    A += [0] * (z - n)
    B += [0] * (z - m)
    butterfly(A)
    butterfly(B)
    for i in range(z):
        A[i] *= B[i]
        A[i] %= FPS_MOD
    butterfly_inv(A)
    A = A[: n + m - 1]
    iz = _fps_inv_mod(z)
    for i in range(n + m - 1):
        A[i] *= iz
        A[i] %= FPS_MOD
    return A


def autocorrelation(_A):
    A = _A.copy()
    n = len(A)
    if not n:
        return []
    if n <= 60:
        res = [0] * (n + n - 1)
        for i in range(n):
            for j in range(n):
                res[i + j] += A[i] * A[j]
                res[i + j] %= FPS_MOD
        return res
    z = 1 << (n + n - 2).bit_length()
    A += [0] * (z - n)
    butterfly(A)
    for i in range(z):
        A[i] *= A[i]
        A[i] %= FPS_MOD
    butterfly_inv(A)
    A = A[: n + n - 1]
    iz = _fps_inv_mod(z)
    for i in range(n + n - 1):
        A[i] *= iz
        A[i] %= FPS_MOD
    return A


class FormalPowerSeries:
    def __init__(self, poly=()):
        self.poly = [p % FPS_MOD for p in poly]

    def __getitem__(self, key):
        if isinstance(key, slice):
            res = self.poly[key]
            return FormalPowerSeries(res)
        else:
            if key < 0:
                raise IndexError("list index out of range")
            if key >= len(self.poly):
                return 0
            else:
                return self.poly[key]

    def __setitem__(self, key, value):
        if key < 0:
            raise IndexError("list index out of range")
        if key >= len(self.poly):
            self.poly += [0] * (key - len(self.poly) + 1)
        self.poly[key] = value % FPS_MOD

    def __len__(self):
        return len(self.poly)

    def resize(self, size):
        if size < 0:
            raise ValueError("negative size")
        if len(self) >= size:
            return self[:size]
        else:
            return FormalPowerSeries(self.poly + [0] * (size - len(self)))

    def shrink(self):
        while self.poly and self.poly[-1] == 0:
            self.poly.pop()

    def times(self, n):
        n %= FPS_MOD
        res = [p * n for p in self.poly]
        return FormalPowerSeries(res)

    def __pos__(self):
        return self

    def __neg__(self):
        return self.times(-1)

    def __add__(self, other):
        if other.__class__ == FormalPowerSeries:
            s = len(self)
            t = len(other)
            n = min(s, t)
            res = [self[i] + other[i] for i in range(n)]
            if s >= t:
                res += self.poly[t:]
            else:
                res += other.poly[s:]
            return FormalPowerSeries(res)
        else:
            return self + FormalPowerSeries([other])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if other.__class__ == FormalPowerSeries:
            res = convolution(self.poly, other.poly)
            return FormalPowerSeries(res)
        else:
            return self.times(other)

    def __rmul__(self, other):
        return self.times(other)

    def __lshift__(self, other):
        return FormalPowerSeries(([0] * other) + self.poly)

    def __rshift__(self, other):
        return self[other:]

    def square(self):
        res = autocorrelation(self.poly)
        return FormalPowerSeries(res)

    def inv(self, deg=-1):
        assert self[0]
        if deg == -1:
            deg = len(self) - 1
        r = _fps_inv_mod(self[0])
        m = 1
        T = [0] * (deg + 1)
        T[0] = r
        res = FormalPowerSeries(T)
        t = 748683265
        iz = 1
        while m <= deg:
            F = [0] * (2 * m)
            G = [0] * (2 * m)
            for j in range(min(len(self), 2 * m)):
                F[j] = self[j]
            for j in range(m):
                G[j] = res[j]
            butterfly(F)
            butterfly(G)
            for j in range(2 * m):
                F[j] *= G[j]
                F[j] %= FPS_MOD
            butterfly_inv(F)
            for j in range(m):
                F[j] = 0
            butterfly(F)
            for j in range(2 * m):
                F[j] *= G[j]
                F[j] %= FPS_MOD
            butterfly_inv(F)
            iz *= t
            iz %= FPS_MOD
            for j in range(m, min(2 * m, deg + 1)):
                res[j] = -F[j] * iz
            m <<= 1
        return res

    # P/Q
    def __truediv__(self, other):
        if other.__class__ == FormalPowerSeries:
            return self * other.inv()
        else:
            return self * _fps_inv_mod(other)

    def __rtruediv__(self, other):
        return other * self.inv()

    # P,Qを多項式として見たときのPをQで割った商を求める
    def __floordiv__(self, other):
        if other.__class__ == FormalPowerSeries:
            if len(self) < len(other):
                return FormalPowerSeries()
            else:
                m = len(self) - len(other) + 1
                res = (self[-1 : -m - 1 : -1] * other[::-1].inv(m))[m - 1 :: -1]
                return res
        else:
            return self * _fps_inv_mod(other)

    def __rfloordiv__(self, other):
        return other * self.inv()

    def __mod__(self, other):
        if len(self) < len(other):
            return self[:]
        else:
            res = self[: len(other) - 1] - ((self // other) * other)[: len(other) - 1]
            return res

    def differentiate(self):
        res = [k * p for k, p in enumerate(self.poly[1:], 1)]
        return FormalPowerSeries(res)

    def integrate(self):
        res = [0] + [_fps_integer_inverse(k) * p for k, p in enumerate(self.poly, 1)]
        return FormalPowerSeries(res)

    def log(self, deg=-1):
        if self[0] != 1:
            raise ValueError("FPS log requires constant coefficient 1")
        if deg == -1:
            deg = len(self) - 1
        if deg == 0:
            return FormalPowerSeries([0])
        return (self.differentiate() * self.inv(deg - 1))[:deg].integrate()

    def exp(self, deg=-1):
        if self[0] != 0:
            raise ValueError("FPS exp requires constant coefficient 0")
        if deg == -1:
            deg = len(self) - 1
        res = FormalPowerSeries([1])
        G = FormalPowerSeries([1])
        df = self.differentiate()
        m = 1
        while m <= deg:
            G = G * 2 - (res * G.square())[:m]
            m <<= 1
            dft = df[:m]
            W = dft + (G * (res.differentiate() - (res * dft)[:m]))[:m]
            res += (res * (self[:m] - W.integrate()[:m]))[:m]
        return res[: deg + 1]

    def __pow__(self, n, deg=-1):
        if deg == -1:
            deg = len(self) - 1
        size = deg + 1
        if size <= 0:
            return FormalPowerSeries()
        if n == 0:
            return FormalPowerSeries([1] + [0] * (size - 1))
        if n < 0:
            return self.inv(deg).__pow__(-n, deg)
        for d, p in enumerate(self.poly):
            if p:
                break
        else:
            return FormalPowerSeries([0] * size)
        shift = d * n
        if shift >= size:
            return FormalPowerSeries([0] * size)
        G = (self[d:] * _fps_inv_mod(p)).resize(size - shift)
        G = (G.log(size - shift - 1) * n).exp(size - shift - 1) * pow(p, n, FPS_MOD)
        return FormalPowerSeries([0] * shift + G.poly).resize(size)

    def sqrt(self, deg=-1):
        if deg == -1:
            deg = len(self) - 1
        if len(self) == 0:
            return FormalPowerSeries()
        if self[0] == 0:
            for d in range(1, len(self)):
                if self[d]:
                    if d & 1:
                        return -1
                    if deg < d // 2:
                        break
                    res = self[d:].sqrt(deg - d // 2)
                    if res == -1:
                        return -1
                    res = res << (d // 2)
                    return res
            return FormalPowerSeries()

        sqr = _fps_sqrt_mod(self[0])
        if sqr == -1:
            return -1
        T = [0] * (deg + 1)
        T[0] = sqr
        res = FormalPowerSeries(T)
        two_inv = (FPS_MOD + 1) // 2
        m = 1
        while m <= deg:
            m <<= 1
            k = min(m, deg + 1)
            res += (res.inv(m - 1) * self[:m])[:k]
            res *= two_inv
        return res

    # 各p_i(0<=i<m)についてf(p_i)を求める
    def multipoint_evaluation(self, P):
        m = len(P)
        size = 1 << (m - 1).bit_length()
        G = [FormalPowerSeries([1]) for _ in range(2 * size)]
        for i in range(m):
            G[size + i] = FormalPowerSeries([-P[i], 1])
        for i in range(size - 1, 0, -1):
            G[i] = G[2 * i] * G[2 * i + 1]
        G[1] = self % G[1]
        for i in range(2, size + m):
            G[i] = G[i >> 1] % G[i]
        res = [G[i][0] for i in range(size, size + m)]
        return res

    # f(x+a)
    def taylor_shift(self, a):
        a %= FPS_MOD
        n = len(self)
        t = 1
        F = self[:]
        G = FormalPowerSeries([0] * n)
        for i in range(n):
            F[i] *= _fps_factorial(i)
        for i in range(n):
            G[i] = t * _fps_factorial_inverse(i)
            t = t * a % FPS_MOD
        res = (F * G[::-1])[n - 1 :]
        for i in range(n):
            res[i] *= _fps_factorial_inverse(i)
        return res

    # Q(P)
    def composition(self, P, deg=-1):
        if deg == -1:
            deg = len(self) - 1
        k = int(deg**0.5 + 1)
        d = (deg + k) // k
        X = [FormalPowerSeries([1])]
        for i in range(k):
            X.append((X[i] * P)[: deg + 1])
        Y = [FormalPowerSeries([0] * (deg + 1)) for _ in range(k)]
        for i in range(k):
            for j in range(d):
                if i * d + j > deg:
                    break
                for t in range(deg + 1):
                    if t >= len(X[j]):
                        break
                    Y[i][t] += X[j][t] * self[i * d + j]
        res = FormalPowerSeries([0] * (deg + 1))
        Z = FormalPowerSeries([1])
        for i in range(k):
            Y[i] = (Y[i] * Z)[: deg + 1]
            for j in range(len(Y[i])):
                res[j] += Y[i][j]
            Z = (Z * X[d])[: deg + 1]
        return res


def poly_coef(Q, P, n):
    if n < 0 or Q[0] == 0:
        raise ValueError("nonnegative index and nonzero denominator constant required")
    while n:
        R = [0] * len(Q.poly)
        for i, q in enumerate(Q.poly):
            if i & 1:
                R[i] = -q
            else:
                R[i] = q
        R = FormalPowerSeries(R)
        P = P * R
        Q = Q * R
        if n & 1:
            P = P[1::2]
        else:
            P = P[::2]
        Q = Q[::2]
        n >>= 1
    return P[0] * _fps_inv_mod(Q[0]) % FPS_MOD


def subset_sum(A, limit):
    if limit < 0 or any(a < 0 for a in A):
        raise ValueError("nonnegative weights and limit required")
    C = [0] * (limit + 1)
    for a in A:
        if a <= limit:
            C[a] += 1
    res = FormalPowerSeries([0] * (limit + 1))
    for i in range(1, limit + 1):
        for k in range(1, limit // i + 1):
            j = i * k
            res[j] += ((k & 1) * 2 - 1) * C[i] * _fps_integer_inverse(k)
    factor = pow(2, C[0], FPS_MOD)
    return [x * factor % FPS_MOD for x in res.exp(limit).poly]


def partition_function(n):
    res = FormalPowerSeries([0] * (n + 1))
    res[0] = 1
    for k in range(1, n + 1):
        k1 = k * (3 * k + 1) // 2
        k2 = k * (3 * k - 1) // 2
        if k2 > n:
            break
        if k1 <= n:
            res[k1] += 1 - (k & 1) * 2
        if k2 <= n:
            res[k2] += 1 - (k & 1) * 2
    return res.inv().poly


def bernoulli_number(n):
    n += 1
    Q = FormalPowerSeries([_fps_factorial_inverse(i + 1) for i in range(n)]).inv(n - 1)
    res = [v * _fps_factorial(i) % FPS_MOD for i, v in enumerate(Q.poly)]
    return res


def stirling_first(n):
    P = []
    a = n
    while a:
        if a & 1:
            P.append(1)
        P.append(0)
        a >>= 1
    res = FormalPowerSeries([1])
    t = 0
    for x in P[::-1]:
        if x:
            res *= FormalPowerSeries([-t, 1])
            t += 1
        else:
            res *= res.taylor_shift(-t)
            t *= 2
    return res.poly


def stirling_second(n):
    F = FormalPowerSeries([0] * (n + 1))
    G = FormalPowerSeries([0] * (n + 1))
    for i in range(n + 1):
        F[i] = pow(i, n, FPS_MOD) * _fps_factorial_inverse(i)
        G[i] = (1 - (i & 1) * 2) * _fps_factorial_inverse(i)
    return (F * G)[: n + 1].poly


def polynomial_interpolation(X, Y):
    if len(X) != len(Y) or len(set(x % FPS_MOD for x in X)) != len(X):
        raise ValueError("distinct interpolation points and matching lengths required")
    n = len(X)
    if n == 0:
        return FormalPowerSeries()
    size = 1 << (n - 1).bit_length()
    M = [FormalPowerSeries([1]) for _ in range(2 * size)]
    G = [0] * (2 * size)
    for i in range(n):
        M[size + i] = FormalPowerSeries([-X[i], 1])
    for i in range(size - 1, 0, -1):
        M[i] = M[2 * i] * M[2 * i + 1]
    G[1] = M[1].differentiate() % M[1]
    for i in range(2, size + n):
        G[i] = G[i >> 1] % M[i]
    for i in range(n):
        G[size + i] = FormalPowerSeries([Y[i] * _fps_inv_mod(G[size + i][0])])
    for i in range(size - 1, 0, -1):
        G[i] = G[2 * i] * M[2 * i + 1] + G[2 * i + 1] * M[2 * i]
    return G[1][:n]


class Mat2:
    def __init__(
        self,
        a00=FormalPowerSeries([1]),
        a01=FormalPowerSeries(),
        a10=FormalPowerSeries(),
        a11=FormalPowerSeries([1]),
    ):
        self.a00 = a00
        self.a01 = a01
        self.a10 = a10
        self.a11 = a11

    def __mul__(self, other):
        if type(other) == Mat2:
            A00 = self.a00 * other.a00 + self.a01 * other.a10
            A01 = self.a00 * other.a01 + self.a01 * other.a11
            A10 = self.a10 * other.a00 + self.a11 * other.a10
            A11 = self.a10 * other.a01 + self.a11 * other.a11
            A00.shrink()
            A01.shrink()
            A10.shrink()
            A11.shrink()
            return Mat2(A00, A01, A10, A11)
        else:
            b0 = self.a00 * other[0] + self.a01 * other[1]
            b1 = self.a10 * other[0] + self.a11 * other[1]
            b0.shrink()
            b1.shrink()
            return (b0, b1)

    def __imul__(self, other):
        A00 = self.a00 * other.a00 + self.a01 * other.a10
        A01 = self.a00 * other.a01 + self.a01 * other.a11
        A10 = self.a10 * other.a00 + self.a11 * other.a10
        A11 = self.a10 * other.a01 + self.a11 * other.a11
        A00.shrink()
        A01.shrink()
        A10.shrink()
        A11.shrink()
        self.a00 = A00
        self.a01 = A01
        self.a10 = A10
        self.a11 = A11
        return self


def _inner_naive_gcd(m, p):
    quo = p[0] // p[1]
    rem = p[0] - p[1] * quo
    b10 = m.a00 - m.a10 * quo
    b11 = m.a01 - m.a11 * quo
    rem.shrink()
    b10.shrink()
    b11.shrink()
    b10, m.a10 = m.a10, b10
    b11, m.a11 = m.a11, b11
    b10, m.a00 = m.a00, b10
    b11, m.a01 = m.a01, b11
    return (p[1], rem)


def _inner_half_gcd(p):
    n, m = len(p[0]), len(p[1])
    k = (n + 1) // 2
    if m <= k:
        return Mat2()
    m1 = _inner_half_gcd((p[0] >> k, p[1] >> k))
    p = m1 * p
    if len(p[1]) <= k:
        return m1
    p = _inner_naive_gcd(m1, p)
    if len(p[1]) <= k:
        return m1
    l = len(p[0]) - 1
    j = 2 * k - l - 1
    p = (p[0] >> j, p[1] >> j)
    return _inner_half_gcd(p) * m1


def _inner_poly_gcd(a, b):
    p = (a, b)
    p[0].shrink()
    p[1].shrink()
    n, m = len(p[0]), len(p[1])
    if n < m:
        mat = _inner_poly_gcd(p[1], p[0])
        mat.a00, mat.a01 = mat.a01, mat.a00
        mat.a10, mat.a11 = mat.a11, mat.a10
        return mat

    res = Mat2()
    while 1:
        m1 = _inner_half_gcd(p)
        p = m1 * p
        if len(p[1]) == 0:
            return m1 * res
        p = _inner_naive_gcd(m1, p)
        if len(p[1]) == 0:
            return m1 * res
        res = m1 * res


def poly_gcd(a, b):
    a, b = a[:], b[:]
    p = (a, b)
    m = _inner_poly_gcd(a, b)
    p = m * p
    if len(p[0]):
        coef = _fps_inv_mod(p[0].poly[-1])
        return p[0] * coef
    return p[0]


def poly_inv(f, g):
    f, g = f[:], g[:]
    g.shrink()
    if len(g) <= 1:
        raise ValueError("modulus polynomial must have positive degree")
    p = (f, g)
    m = _inner_poly_gcd(f, g)
    _gcd = (m * p)[0]
    if len(_gcd) != 1:
        return -1
    x = (FormalPowerSeries([1]), g)
    res = ((m * x)[0] % g) * _fps_inv_mod(_gcd[0])
    res.shrink()
    return res


# 統一API: sizeは係数の個数（x**size未満）、返り値はlist。
def fps_inverse(a, size):
    if size < 0:
        raise ValueError("negative size")
    if size == 0:
        return []
    if not a or a[0] % FPS_MOD == 0:
        raise ValueError("nonzero constant coefficient required")
    return FormalPowerSeries(a).inv(size - 1).resize(size).poly


def fps_log(a, size):
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    return FormalPowerSeries(a).log(size - 1).resize(size).poly


def fps_exp(a, size):
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    return FormalPowerSeries(a).exp(size - 1).resize(size).poly


def fps_power(a, exponent, size):
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    return FormalPowerSeries(a).__pow__(exponent, size - 1).resize(size).poly


def fps_sqrt(a, size):
    """平方根がなければNone。二つの根のどちらを返すかは未指定。"""
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    result = FormalPowerSeries(a).sqrt(size - 1)
    return None if result == -1 else result.resize(size).poly


def bostan_mori(numerator, denominator, n):
    """[x**n] P(x)/Q(x)。O(M(d)log n)、Q[0]!=0。"""
    return poly_coef(FormalPowerSeries(denominator), FormalPowerSeries(numerator), n)


def polynomial_gcd(a, b):
    """モニックGCD。入力を変更しない。gcd(0,0)=[]。"""
    result = poly_gcd(FormalPowerSeries(a), FormalPowerSeries(b))
    result.shrink()
    return result.poly


def polynomial_inverse(a, modulus):
    """aの多項式modulusによる逆元。存在しなければNone。"""
    result = poly_inv(FormalPowerSeries(a), FormalPowerSeries(modulus))
    return None if result == -1 else result.poly
