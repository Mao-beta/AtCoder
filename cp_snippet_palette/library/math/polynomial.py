"""FFT・FPS・多項式GCD/逆元・特殊数列。係数は低次から。
FFT/FPSのAPIはshakayami/ACL-for-pythonに合わせる。単体で貼り付け可能。
FFTは素数MODを指定、FPSとlist形式の補助関数は998244353固定。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    fft = FFT(998244353)
    fft.convolution([1, 2], [3, 4])  # => [3, 10, 8]
    f = FPS([1, 2, 1])
    f.Func, f.diff().Func  # => ([1, 2, 1], [2, 2])
    FPS([1, -1]).inv(5).Func  # => [1, 1, 1, 1, 1]
    FPS([1, 1]).powfps(3, 4).Func  # => [1, 3, 3, 1]
    f.log(5).exp(5).Func  # => [1, 2, 1, 0, 0]
    f.sqrt(3).Func  # => [1, 1, 0]
    f.multipoint_evaluation([0, 1, 2]), f.taylor_shift(1).Func  # => ([1, 4, 9], [4, 4, 1])
    polynomial_interpolation([0, 1, 2], [1, 4, 9]).Func  # => [1, 2, 1]
inv(d)、log/exp/sqrt/powfpsのdegは係数数。5ならx^0..x^4。-1は入力の係数数。
sqrtは解なしならFPS([])。ゼロ級数の平方根も偽になるため、boolだけで解の有無を判定しない。

list形式の独自拡張（sizeも係数数）。sqrtだけは解なしをNoneで返す。
    fps_inverse([1, -1], 5)  # => [1, 1, 1, 1, 1]
    fps_exp(fps_log([1, 2, 3], 3), 3)  # => [1, 2, 3]
    fps_power([1, 1], 3, 4)  # => [1, 3, 3, 1]
    fps_sqrt([1, 2, 1], 3)  # => [1, 1, 0]
    bostan_mori([1], [1, -1, -1], 5)  # => 8
    polynomial_gcd([-1, 0, 1], [-1, 1])  # => [998244352, 1]
    polynomial_inverse([1, 1], [0, 0, 1])  # => [1, 998244352]
    polynomial_divmod([1, 2, 1], [1, 1])  # => ([1, 1], [])
    linear_recurrence_ntt([0, 1], [1, 1], 10)  # => 55
    subset_sum([1, 2, 2], 5), partition_function(4)  # => ([1, 1, 2, 2, 1, 1], [1, 1, 2, 3, 5])
    bernoulli_number(1), stirling_first(3), stirling_second(3)  # => ([1, 499122176], [0, 2, 998244350, 1], [0, 1, 3, 1])
入力と計算量の共通規約: 係数は整数で、listの添字iがx^iの係数。法は998244353。M(D)=O(D log(D+1))はD係数の多項式積の計算量。
 入力長のコピー・検査にも線形時間がかかる。法を固定した整数演算回数で表す。
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
    """内部用の順NTT。長さ2^k（1以上2^23以下）のlist Aをその場で変換し、戻り値なし。
    通常はconvolutionを使う。逆変換後は長さの逆元を掛ける必要がある。
    Aは剰余係数の可変list。N=len(A)として時間O(N log(N+1))、入力以外の空間O(log N)以内。
    """
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
    """内部用の逆NTT。長さ2^kのlist Aをその場で変換する。戻り値なし。
    butterflyの結果に適用すると元配列のlen(A)倍となる。正規化は呼び出し側で行う。
    Aは剰余係数の可変list。N=len(A)として時間O(N log(N+1))、入力以外の空間O(log N)以内。
    """
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


def _convolution998(_A, _B):
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


def _polynomial_square(_A):
    """旧名。係数list _Aの二乗の畳み込みを返す（_convolution998(_A,_A)相当）。
    相関ではなく通常の多項式の二乗。入力非破壊、空なら[]。
    """
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


class _FormalPowerSeries:
    """mod=998244353の係数を低次から保持する旧FPSクラス。poly属性は係数list。
    f=_FormalPowerSeries([a0,a1,...])。f[i]は係数、範囲外の非負添字は0。
    f[i]=vで必要な長さまで拡張、f[l:r]は新しいFPS。+,-,*,//,%を利用可能。
    //と%は多項式の商・余り。除数の末尾0はshrink()で除去する。
    メソッドのdegは最大次数（結果の係数数は原則deg+1）、省略時はlen(f)-1。
    新規コードは係数数sizeを指定するfps_inverse/log/exp/power/sqrtを推奨する。
    """

    def __init__(self, poly=()):
        self.poly = [p % FPS_MOD for p in poly]

    def __getitem__(self, key):
        if isinstance(key, slice):
            res = self.poly[key]
            return _FormalPowerSeries(res)
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
        """係数数をsizeに切り詰める、または0埋めした新しいFPSを返す。元のselfは変更しない。"""
        if size < 0:
            raise ValueError("negative size")
        if len(self) >= size:
            return self[:size]
        else:
            return _FormalPowerSeries(self.poly + [0] * (size - len(self)))

    def shrink(self):
        """末尾の0係数をその場で削除する。零多項式はpoly=[]。戻り値はNone。"""
        while self.poly and self.poly[-1] == 0:
            self.poly.pop()

    def times(self, n):
        """全係数に整数nを掛けた新しいFPS。f*nと同じ。剰余を取る。"""
        n %= FPS_MOD
        res = [p * n for p in self.poly]
        return _FormalPowerSeries(res)

    def __pos__(self):
        return self

    def __neg__(self):
        return self.times(-1)

    def __add__(self, other):
        if other.__class__ == _FormalPowerSeries:
            s = len(self)
            t = len(other)
            n = min(s, t)
            res = [self[i] + other[i] for i in range(n)]
            if s >= t:
                res += self.poly[t:]
            else:
                res += other.poly[s:]
            return _FormalPowerSeries(res)
        else:
            return self + _FormalPowerSeries([other])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if other.__class__ == _FormalPowerSeries:
            res = _convolution998(self.poly, other.poly)
            return _FormalPowerSeries(res)
        else:
            return self.times(other)

    def __rmul__(self, other):
        return self.times(other)

    def __lshift__(self, other):
        return _FormalPowerSeries(([0] * other) + self.poly)

    def __rshift__(self, other):
        return self[other:]

    def square(self):
        """self*selfを新しいFPSとして返す。係数数は通常2*len(self)-1。"""
        res = _polynomial_square(self.poly)
        return _FormalPowerSeries(res)

    def inv(self, deg=-1):
        """1/fをx^(deg+1)未満で打ち切ったFPS。f[0]!=0が必要。
        deg=-1はlen(f)-1。新規コードはfps_inverse(a,size)を使う。
        """
        assert self[0]
        if deg == -1:
            deg = len(self) - 1
        r = _fps_inv_mod(self[0])
        m = 1
        T = [0] * (deg + 1)
        T[0] = r
        res = _FormalPowerSeries(T)
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
        if other.__class__ == _FormalPowerSeries:
            return self * other.inv()
        else:
            return self * _fps_inv_mod(other)

    def __rtruediv__(self, other):
        return other * self.inv()

    # P,Qを多項式として見たときのPをQで割った商を求める
    def __floordiv__(self, other):
        if other.__class__ == _FormalPowerSeries:
            if len(self) < len(other):
                return _FormalPowerSeries()
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
        """形式微分f'(x)を新しいFPSで返す。係数i*a[i]をi-1次へ移す。"""
        res = [k * p for k, p in enumerate(self.poly[1:], 1)]
        return _FormalPowerSeries(res)

    def integrate(self):
        """定数項0の形式積分を新しいFPSで返す。係数a[i]/(i+1)をi+1次へ移す。"""
        res = [0] + [_fps_integer_inverse(k) * p for k, p in enumerate(self.poly, 1)]
        return _FormalPowerSeries(res)

    def log(self, deg=-1):
        """log(f)を最大deg次まで計算しFPSで返す。f[0]==1が必要。
        deg=-1はlen(f)-1。新規コードはfps_log(a,size)。
        """
        if self[0] != 1:
            raise ValueError("FPS log requires constant coefficient 1")
        if deg == -1:
            deg = len(self) - 1
        if deg == 0:
            return _FormalPowerSeries([0])
        return (self.differentiate() * self.inv(deg - 1))[:deg].integrate()

    def exp(self, deg=-1):
        """exp(f)を最大deg次まで計算しFPSで返す。f[0]==0が必要。
        deg=-1はlen(f)-1。新規コードはfps_exp(a,size)。
        """
        if self[0] != 0:
            raise ValueError("FPS exp requires constant coefficient 0")
        if deg == -1:
            deg = len(self) - 1
        res = _FormalPowerSeries([1])
        G = _FormalPowerSeries([1])
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
            return _FormalPowerSeries()
        if n == 0:
            return _FormalPowerSeries([1] + [0] * (size - 1))
        if n < 0:
            return self.inv(deg).__pow__(-n, deg)
        for d, p in enumerate(self.poly):
            if p:
                break
        else:
            return _FormalPowerSeries([0] * size)
        shift = d * n
        if shift >= size:
            return _FormalPowerSeries([0] * size)
        G = (self[d:] * _fps_inv_mod(p)).resize(size - shift)
        G = (G.log(size - shift - 1) * n).exp(size - shift - 1) * pow(p, n, FPS_MOD)
        return _FormalPowerSeries([0] * shift + G.poly).resize(size)

    def sqrt(self, deg=-1):
        """fの形式平方根を最大deg次まで求める。存在しなければ整数-1。
        成功時はFPSだが0係数部分で短くなる場合がある。係数数が必要ならresizeする。
        新規コードは長さsizeのlistまたはNoneを返すfps_sqrtを使う。
        """
        if deg == -1:
            deg = len(self) - 1
        if len(self) == 0:
            return _FormalPowerSeries()
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
            return _FormalPowerSeries()

        sqr = _fps_sqrt_mod(self[0])
        if sqr == -1:
            return -1
        T = [0] * (deg + 1)
        T[0] = sqr
        res = _FormalPowerSeries(T)
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
        """数値列Pに対する[f(P[0]),f(P[1]),...]を剰余のlistで返す。入力非破壊。"""
        m = len(P)
        size = 1 << (m - 1).bit_length()
        G = [_FormalPowerSeries([1]) for _ in range(2 * size)]
        for i in range(m):
            G[size + i] = _FormalPowerSeries([-P[i], 1])
        for i in range(size - 1, 0, -1):
            G[i] = G[2 * i] * G[2 * i + 1]
        G[1] = self % G[1]
        for i in range(2, size + m):
            G[i] = G[i >> 1] % G[i]
        res = [G[i][0] for i in range(size, size + m)]
        return res

    # f(x+a)
    def taylor_shift(self, a):
        """f(x+a)の係数を新しいFPSとして返す。aは整数、計算は剰余。"""
        a %= FPS_MOD
        n = len(self)
        t = 1
        F = self[:]
        G = _FormalPowerSeries([0] * n)
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
        """f(P(x))を最大deg次まで計算する。PもFPSを渡す。
        P[0]==0、または外側fの次数<=degで使う（高次係数の省略に注意）。
        deg省略時はlen(f)-1。戻り値はFPS。
        """
        if deg == -1:
            deg = len(self) - 1
        k = int(deg**0.5 + 1)
        d = (deg + k) // k
        X = [_FormalPowerSeries([1])]
        for i in range(k):
            X.append((X[i] * P)[: deg + 1])
        Y = [_FormalPowerSeries([0] * (deg + 1)) for _ in range(k)]
        for i in range(k):
            for j in range(d):
                if i * d + j > deg:
                    break
                for t in range(deg + 1):
                    if t >= len(X[j]):
                        break
                    Y[i][t] += X[j][t] * self[i * d + j]
        res = _FormalPowerSeries([0] * (deg + 1))
        Z = _FormalPowerSeries([1])
        for i in range(k):
            Y[i] = (Y[i] * Z)[: deg + 1]
            for j in range(len(Y[i])):
                res[j] += Y[i][j]
            Z = (Z * X[d])[: deg + 1]
        return res


def _poly_coef(Q, P, n):
    """旧FPS形式の係数取得。[x^n]P(x)/Q(x)を整数で返す。Q,PはFPS。
    引数順は分母Q、分子P、次数n。Q[0]!=0,n>=0。新規コードはbostan_mori。
    """
    if n < 0 or Q[0] == 0:
        raise ValueError("nonnegative index and nonzero denominator constant required")
    while n:
        R = [0] * len(Q.poly)
        for i, q in enumerate(Q.poly):
            if i & 1:
                R[i] = -q
            else:
                R[i] = q
        R = _FormalPowerSeries(R)
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
    """非負整数列Aから各要素を高々一度選ぶ部分集合和の個数を剰余で返す。
    戻り値の長さlimit+1、result[s]は和sを作る選び方の数。空集合も含む。
    同値の要素は別物、0の要素も選ぶ/選ばないを数える。limit>=0。
    N=len(A)、D=limit+1。時間O(N+D log(D+1)+M(D) log(D+1))以内、空間O(D)。M(D)=O(D log(D+1))は畳み込みの時間。
    """
    if limit < 0 or any(a < 0 for a in A):
        raise ValueError("nonnegative weights and limit required")
    C = [0] * (limit + 1)
    for a in A:
        if a <= limit:
            C[a] += 1
    res = _FormalPowerSeries([0] * (limit + 1))
    for i in range(1, limit + 1):
        for k in range(1, limit // i + 1):
            j = i * k
            res[j] += ((k & 1) * 2 - 1) * C[i] * _fps_integer_inverse(k)
    factor = pow(2, C[0], FPS_MOD)
    return [x * factor % FPS_MOD for x in res.exp(limit).poly]


def partition_function(n):
    """0..nの整数分割数を剰余のlistで返す。順序を区別しない正整数への分割。
    p[0]=1。例: p[4]=5。n>=0。
    nは求める最大添字の非負整数でn<998244353。D=n+1として時間O(D log²(D+1))以内、空間O(D log(D+1))以内。
    法を固定し、畳み込み・FPS演算の安全側の上界で表す。
    """
    res = _FormalPowerSeries([0] * (n + 1))
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
    """B_0..B_nをmod 998244353で返す。生成関数x/(exp(x)-1)。
    B_0=1、B_1=-1/2という符号規約。n>=0。
    nは求める最大添字の非負整数でn<998244353。D=n+1として時間O(D log²(D+1))以内、空間O(D log(D+1))以内。
    法を固定し、畳み込み・FPS演算の安全側の上界で表す。
    """
    n += 1
    Q = _FormalPowerSeries([_fps_factorial_inverse(i + 1) for i in range(n)]).inv(n - 1)
    res = [v * _fps_factorial(i) % FPS_MOD for i, v in enumerate(Q.poly)]
    return res


def stirling_first(n):
    """符号付き第一種Stirling数s(n,k)をk=0..nのlistで返す。
    x(x-1)...(x-n+1)の係数。負値はmodで正規化される。n>=0。
    nは求める最大添字の非負整数でn<998244353。D=n+1として時間O(D log²(D+1))以内、空間O(D log(D+1))以内。
    法を固定し、畳み込み・FPS演算の安全側の上界で表す。
    """
    P = []
    a = n
    while a:
        if a & 1:
            P.append(1)
        P.append(0)
        a >>= 1
    res = _FormalPowerSeries([1])
    t = 0
    for x in P[::-1]:
        if x:
            res *= _FormalPowerSeries([-t, 1])
            t += 1
        else:
            res *= res.taylor_shift(-t)
            t *= 2
    return res.poly


def stirling_second(n):
    """第二種Stirling数S(n,k)をk=0..nのlistで返す。
    n個の区別する要素をk個の空でない無順序集合に分割する数。n>=0。
    nは求める最大添字の非負整数でn<998244353。D=n+1として時間O(D log²(D+1))以内、空間O(D log(D+1))以内。
    法を固定し、畳み込み・FPS演算の安全側の上界で表す。
    """
    F = _FormalPowerSeries([0] * (n + 1))
    G = _FormalPowerSeries([0] * (n + 1))
    for i in range(n + 1):
        F[i] = pow(i, n, FPS_MOD) * _fps_factorial_inverse(i)
        G[i] = (1 - (i & 1) * 2) * _fps_factorial_inverse(i)
    return (F * G)[: n + 1].poly


def _polynomial_interpolation(X, Y):
    """f(X[i])=Y[i]を満たす次数len(X)未満の多項式をFPSで返す。
    X,Yは等長、Xはmod上で全て異なる必要がある。係数listは戻り値.poly。
    空なら空FPS。計算はmod 998244353。
    """
    if len(X) != len(Y) or len(set(x % FPS_MOD for x in X)) != len(X):
        raise ValueError("distinct interpolation points and matching lengths required")
    n = len(X)
    if n == 0:
        return _FormalPowerSeries()
    size = 1 << (n - 1).bit_length()
    M = [_FormalPowerSeries([1]) for _ in range(2 * size)]
    G = [0] * (2 * size)
    for i in range(n):
        M[size + i] = _FormalPowerSeries([-X[i], 1])
    for i in range(size - 1, 0, -1):
        M[i] = M[2 * i] * M[2 * i + 1]
    G[1] = M[1].differentiate() % M[1]
    for i in range(2, size + n):
        G[i] = G[i >> 1] % M[i]
    for i in range(n):
        G[size + i] = _FormalPowerSeries([Y[i] * _fps_inv_mod(G[size + i][0])])
    for i in range(size - 1, 0, -1):
        G[i] = G[2 * i] * M[2 * i + 1] + G[2 * i + 1] * M[2 * i]
    return G[1][:n]


class _PolyMat2:
    """多項式GCD内部用の2×2行列。各成分a00,a01,a10,a11はFPS。
    省略時は単位行列。M*Nで行列積、M*(f,g)でFPSの組への作用。
    通常の数値行列はbasic/matrix.pyを使う。デフォルト成分を直接変更しないこと。
    """

    def __init__(
        self,
        a00=_FormalPowerSeries([1]),
        a01=_FormalPowerSeries(),
        a10=_FormalPowerSeries(),
        a11=_FormalPowerSeries([1]),
    ):
        self.a00 = a00
        self.a01 = a01
        self.a10 = a10
        self.a11 = a11

    def __mul__(self, other):
        if type(other) == _PolyMat2:
            A00 = self.a00 * other.a00 + self.a01 * other.a10
            A01 = self.a00 * other.a01 + self.a01 * other.a11
            A10 = self.a10 * other.a00 + self.a11 * other.a10
            A11 = self.a10 * other.a01 + self.a11 * other.a11
            A00.shrink()
            A01.shrink()
            A10.shrink()
            A11.shrink()
            return _PolyMat2(A00, A01, A10, A11)
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
        return _PolyMat2()
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

    res = _PolyMat2()
    while 1:
        m1 = _inner_half_gcd(p)
        p = m1 * p
        if len(p[1]) == 0:
            return m1 * res
        p = _inner_naive_gcd(m1, p)
        if len(p[1]) == 0:
            return m1 * res
        res = m1 * res


def _poly_gcd(a, b):
    """旧FPS形式のGCD。a,bはFPS、戻り値もFPSで最高次係数を1にする。
    新規コードはlistを受け取るpolynomial_gcd(a,b)を使う。入力非破壊。
    """
    a, b = a[:], b[:]
    p = (a, b)
    m = _inner_poly_gcd(a, b)
    p = m * p
    if len(p[0]):
        coef = _fps_inv_mod(p[0].poly[-1])
        return p[0] * coef
    return p[0]


def _poly_inv(f, g):
    """旧FPS形式。f*gの逆ではなく、fの多項式gを法とする逆元をFPSで返す。
    gの次数は1以上。逆元なしは整数-1。新規コードはpolynomial_inverseを使う。
    """
    f, g = f[:], g[:]
    g.shrink()
    if len(g) <= 1:
        raise ValueError("modulus polynomial must have positive degree")
    p = (f, g)
    m = _inner_poly_gcd(f, g)
    _gcd = (m * p)[0]
    if len(_gcd) != 1:
        return -1
    x = (_FormalPowerSeries([1]), g)
    res = ((m * x)[0] % g) * _fps_inv_mod(_gcd[0])
    res.shrink()
    return res


# 統一API: sizeは係数の個数（x**size未満）、返り値はlist。
def fps_inverse(a, size):
    """係数列aの1/aをx^size未満で打ち切った長さsizeのlist。
    size>=0、size>0ならa[0]!=0 mod 998244353。入力非破壊。
    aは低次からの整数係数list、sizeは必要な係数数Dの非負整数（次数D未満）。
    時間O(len(a)+D log²(D+1))以内、空間O(len(a)+D log(D+1))以内。法を固定した上界。
    """
    if size < 0:
        raise ValueError("negative size")
    if size == 0:
        return []
    if not a or a[0] % FPS_MOD == 0:
        raise ValueError("nonzero constant coefficient required")
    return _FormalPowerSeries(a).inv(size - 1).resize(size).poly


def fps_log(a, size):
    """log(a)の先頭size係数をlistで返す。size>=0、size>0ならa[0]==1 mod MOD。
    係数は低次から。入力非破壊。
    aは低次からの整数係数list、sizeは必要な係数数Dの非負整数（次数D未満）。
    時間O(len(a)+D log²(D+1))以内、空間O(len(a)+D log(D+1))以内。法を固定した上界。
    """
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    return _FormalPowerSeries(a).log(size - 1).resize(size).poly


def fps_exp(a, size):
    """exp(a)の先頭size係数をlistで返す。size>=0、size>0ならa[0]==0 mod MOD。
    空のaは零級数。入力非破壊。
    aは低次からの整数係数list、sizeは必要な係数数Dの非負整数（次数D未満）。
    時間O(len(a)+D log²(D+1))以内、空間O(len(a)+D log(D+1))以内。法を固定した上界。
    """
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    return _FormalPowerSeries(a).exp(size - 1).resize(size).poly


def fps_power(a, exponent, size):
    """a^exponentの先頭size係数をlistで返す。size>=0。0乗は1。
    負のexponentはa[0]!=0が必要。入力非破壊、法は998244353。
    aは低次からの整数係数list、sizeは必要な係数数Dの非負整数（次数D未満）。
    時間O(len(a)+D log²(D+1))以内、空間O(len(a)+D log(D+1))以内。法を固定した上界。
    exponentは整数の指数。上の時間に定数項の累乗O(log(abs(exponent)+1))回の法乗算を加える。
    """
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    return _FormalPowerSeries(a).__pow__(exponent, size - 1).resize(size).poly


def fps_sqrt(a, size):
    """aの形式平方根を長さsizeの係数listで返す。存在しなければNone。
    size>=0。二つの根のどちらを返すかは未指定。入力非破壊。
    aは低次からの整数係数list、sizeは必要な係数数Dの非負整数（次数D未満）。
    時間O(len(a)+D log²(D+1))以内、空間O(len(a)+D log(D+1))以内。法を固定した上界。
    """
    if size < 0:
        raise ValueError("negative size")
    if not size:
        return []
    result = _FormalPowerSeries(a).sqrt(size - 1)
    return None if result == -1 else result.resize(size).poly


def bostan_mori(numerator, denominator, n):
    """[x**n] P(x)/Q(x)。O(M(d)log n)、Q[0]!=0。
    numerator/denominatorはP/Qの低次からの整数係数list、nは求める係数の非負整数添字。Q[0]は非零、d=max(len(P),len(Q))。
    M(d)=O(d log(d+1))、空間O(d)。
    """
    return _poly_coef(_FormalPowerSeries(denominator), _FormalPowerSeries(numerator), n)


def polynomial_gcd(a, b):
    """モニックGCD。入力を変更しない。gcd(0,0)=[]。
    入力は低次からの整数係数list。Nは二つの入力の係数数の最大値、M(N)=O(N log(N+1))は畳み込み時間。空間はO(N log(N+1))以内。
    a/bは対象多項式。時間O(M(N) log(N+1))。
    """
    result = _poly_gcd(_FormalPowerSeries(a), _FormalPowerSeries(b))
    result.shrink()
    return result.poly


def polynomial_inverse(a, modulus):
    """aの多項式modulusによる逆元を係数listで返す。存在しなければNone。
    係数は低次から、法998244353。非零定数を法とすると[]、零多項式の法は不可。
    Half-GCDを利用しO(M(N)log N)。入力非破壊。
    入力は低次からの整数係数list。Nは二つの入力の係数数の最大値、M(N)=O(N log(N+1))は畳み込み時間。空間はO(N log(N+1))以内。
    aは逆元を求める多項式、modulusは法とする非零多項式。
    """
    g = _FormalPowerSeries(modulus)
    g.shrink()
    if not len(g):
        raise ValueError("zero modulus polynomial")
    if len(g) == 1:
        return []
    result = _poly_inv(_FormalPowerSeries(a), g)
    return None if result == -1 else result.poly


def polynomial_divmod(a, b):
    """多項式aをbで割った(商list,余りlist)。低次から、法998244353。
    末尾0は除き、零多項式は[]。b=0はZeroDivisionError。入力非破壊、O(M(N))。
    例: polynomial_divmod([1,2,1],[1,1])は([1,1],[])。
    入力は低次からの整数係数list。Nは二つの入力の係数数の最大値、M(N)=O(N log(N+1))は畳み込み時間。空間はO(N log(N+1))以内。
    """
    f, g = _FormalPowerSeries(a), _FormalPowerSeries(b)
    f.shrink()
    g.shrink()
    if not len(g):
        raise ZeroDivisionError("zero divisor polynomial")
    q = f // g
    r = f - q * g
    q.shrink()
    r.shrink()
    return q.poly, r.poly


def linear_recurrence_ntt(initial, coefficients, n):
    """k次漸化式のa[n]をBostan–Moriで返す。O(M(k)log n)、法998244353固定。
    initialは先頭k項。a[t]=sum(coefficients[j]*a[t-j-1])、n>=0。
    空の漸化式は零列。小さなkや別の素数ではlinear_recurrence.pyも選べる。
    例: linear_recurrence_ntt([0,1],[1,1],10)は55。
    initial/coefficientsは整数列、k=len(coefficients)=len(initial)、nは求める項の0-indexed添字。
    M(k)=O(k log(k+1))、追加空間O(k)。
    """
    k = len(coefficients)
    if n < 0 or len(initial) != k:
        raise ValueError("invalid recurrence parameters")
    if not k:
        return 0
    if n < k:
        return initial[n] % FPS_MOD
    q = [1] + [-x % FPS_MOD for x in coefficients]
    p = _convolution998(initial, q)[:k]
    return bostan_mori(p, q, n)


# https://github.com/shakayami/ACL-for-python/blob/master/convolution.py
class FFT:
    """FFT(MOD)。素数MODで係数列を畳み込む。係数は低次から。
    convolution(a,b)は入力非破壊で長さlen(a)+len(b)-1のlistを返す。
    NTT長zはMOD-1の約数である2冪に限る。998244353ならz<=2**23。
    短い片方（40以下）は直接計算。通常O(z log z)、メモリO(z)。
    入力: MODはNTT用の素数。既知の998244353等なら構築O(log MOD)時間・空間。
    一般の素数ではprimitive_root_constexprによる因数分解・原始根探索も行うので、そのコストが加わる。
    """

    def primitive_root_constexpr(self, m):
        """素数mの原始根を返す内部補助。mが素数であることは呼び出し側で保証する。
        mは素数の法。m-1の異なる素因子数D、試す原始根候補数Cに対しO(sqrt(m)+C*D*log m)時間が目安。既知の法はO(1)で返す。空間O(log m)以内。
        """
        if m == 2:
            return 1
        if m == 167772161:
            return 3
        if m == 469762049:
            return 3
        if m == 754974721:
            return 11
        if m == 998244353:
            return 3
        divs = [0] * 20
        divs[0] = 2
        cnt = 1
        x = (m - 1) // 2
        while x % 2 == 0:
            x //= 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                divs[cnt] = i
                cnt += 1
                while x % i == 0:
                    x //= i
            i += 2
        if x > 1:
            divs[cnt] = x
            cnt += 1
        g = 2
        while 1:
            ok = True
            for i in range(cnt):
                if pow(g, (m - 1) // divs[i], m) == 1:
                    ok = False
                    break
            if ok:
                return g
            g += 1

    def bsf(self, x):
        """正整数xの末尾0ビット数を返す。
        xは正の整数。末尾の連続0bit数を返す。時間O(log(x+1))以内、追加空間O(1)。
        """
        assert x > 0
        res = 0
        while x % 2 == 0:
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
        """入力: MODはNTT用の素数。既知の998244353等なら構築O(log MOD)時間・空間。
        一般の素数ではprimitive_root_constexprによる因数分解・原始根探索も行うので、そのコストが加わる。
        """
        assert MOD >= 2
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
        prod = 1
        iprod = 1
        for i in range(self.rank2 - 1):
            self.rate2[i] = (self.root[i + 2] * prod) % self.mod
            self.irate2[i] = (self.iroot[i + 2] * iprod) % self.mod
            prod = (prod * self.iroot[i + 2]) % self.mod
            iprod = (iprod * self.root[i + 2]) % self.mod
        prod = 1
        iprod = 1
        for i in range(self.rank2 - 2):
            self.rate3[i] = (self.root[i + 3] * prod) % self.mod
            self.irate3[i] = (self.iroot[i + 3] * iprod) % self.mod
            prod = (prod * self.iroot[i + 3]) % self.mod
            iprod = (iprod * self.root[i + 3]) % self.mod

    def butterfly(self, a):
        """list aを順NTTで上書き。長さは対応する2冪。戻り値なし。
        aは整数係数の可変list。N=len(a)。時間O(N log(N+1))、追加空間O(1)個の整数。
        """
        n = len(a)
        assert n > 0 and n & (n - 1) == 0 and (self.mod - 1) % n == 0
        h = (n - 1).bit_length()

        LEN = 0
        while LEN < h:
            if h - LEN == 1:
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
        """list aを逆NTTで上書き。復元には長さの逆元を掛ける。戻り値なし。
        aは整数係数の可変list。N=len(a)。時間O(N log(N+1))、追加空間O(1)個の整数。
        """
        n = len(a)
        assert n > 0 and n & (n - 1) == 0 and (self.mod - 1) % n == 0
        h = (n - 1).bit_length()
        LEN = h
        while LEN:
            if LEN == 1:
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
                        a[i + offset + 3 * p] = (
                            (a0 - a1 - a2na3iimag) * irot3 % self.mod
                        )
                    irot *= self.irate3[(~s & -~s).bit_length() - 1]
                    irot %= self.mod
                LEN -= 2

    def convolution(self, a, b):
        """a,bの多項式積の係数listをMODで返す。空入力なら[]。入力非破壊。
        a/bは低次からの整数係数list。N=len(a)、K=len(b)、ZはN+K-1以上の最小2冪。通常O(Z log Z)時間・O(Z)空間。
        min(N,K)<=40ではO(NK)時間の直接計算。
        """
        n = len(a)
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
        if (self.mod - 1) % z:
            raise ValueError("NTT length must divide MOD-1")
        a = a + [0] * (z - n)
        b = b + [0] * (z - m)
        self.butterfly(a)
        self.butterfly(b)
        c = [(a[i] * b[i]) % self.mod for i in range(z)]
        self.butterfly_inv(c)
        iz = pow(z, self.mod - 2, self.mod)
        for i in range(n + m - 1):
            c[i] = (c[i] * iz) % self.mod
        return c[: n + m - 1]


class FPS:
    """FPS(L)。998244353での形式的冪級数。係数listはFunc属性、低次から。
    shakayami/ACL-for-pythonと同じinv(d)/log(deg)/exp(deg)/sqrt(deg)/powfps(k,deg)。
    d・degは結果の係数数。-1はlen(Func)。各演算は新しいFPSを返す。
    +=などの複合代入とreduce()だけは自身を変更する。
    独自拡張multipoint_evaluation/taylor_shiftは元ライブラリの機能を維持する。
    入力: Lは低次からの整数係数列（空も可）。N=len(L)、構築O(N)時間・空間。以下のNは現在のlen(Func)。Dは指定した出力係数数で、d/deg=-1ならN。
    法は固定。
    """

    mod = FPS_MOD

    def __init__(self, L):
        """入力: Lは低次からの整数係数列（空も可）。N=len(L)、構築O(N)時間・空間。以下のNは現在のlen(Func)。Dは指定した出力係数数で、d/deg=-1ならN。
        法は固定。
        """
        self.Func = [x % self.mod for x in L]

    def __mul__(self, other):
        if isinstance(other, int):
            return FPS([x * other for x in self.Func])
        return FPS(_convolution998(self.Func, other.Func))

    def __add__(self, other):
        a, b = self.Func, other.Func
        return FPS(
            [
                (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                for i in range(max(len(a), len(b)))
            ]
        )

    def __sub__(self, other):
        return self + other * (-1)

    def __truediv__(self, other):
        if isinstance(other, int):
            return self * pow(other, -1, self.mod)
        return self * other.inv()

    def __floordiv__(self, other):
        if isinstance(other, int):
            return self / other
        return FPS(polynomial_divmod(self.Func, other.Func)[0])

    def __mod__(self, other):
        return FPS(polynomial_divmod(self.Func, other.Func)[1])

    def __imul__(self, other):
        self.Func = (self * other).Func
        return self

    def __iadd__(self, other):
        self.Func = (self + other).Func
        return self

    def __isub__(self, other):
        self.Func = (self - other).Func
        return self

    def __itruediv__(self, other):
        self.Func = (self / other).Func
        return self

    def __lshift__(self, d):
        return FPS([0] * d + self.Func)

    def __rshift__(self, d):
        return FPS(self.Func[d:] + [0] * min(len(self.Func), d))

    def __ilshift__(self, d):
        self.Func = (self << d).Func
        return self

    def __irshift__(self, d):
        self.Func = (self >> d).Func
        return self

    def __bool__(self):
        return any(self.Func)

    def __eq__(self, other):
        return isinstance(other, FPS) and self.Func == other.Func

    def __lt__(self, other):
        return (len(self.Func), self.Func) < (len(other.Func), other.Func)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other <= self

    def __repr__(self):
        return f"FPS({self.Func})"

    __str__ = __repr__

    def butterfly(self, a):
        """aを順NTTで上書きし、同じlistを返す。長さは2冪、2**23以下。
        aは整数係数の可変list。K=len(a)としてO(K log(K+1))時間、入力以外の空間O(log K)以内。
        """
        butterfly(a)
        return a

    def butterfly_inv(self, a):
        """aを逆NTTで上書きし、同じlistを返す。復元時は長さの逆元を掛ける。
        aは整数係数の可変list。K=len(a)としてO(K log(K+1))時間、入力以外の空間O(log K)以内。
        """
        butterfly_inv(a)
        return a

    def reduce(self):
        """末尾の0係数をその場で除く。零多項式はFunc=[]。戻り値なし。
        引数なし。時間O(N)、追加空間O(1)。N=len(Func)（処理前）。
        """
        while self.Func and self.Func[-1] == 0:
            self.Func.pop()

    def resize(self, deg):
        """係数数degへ0埋め・切り詰めした新しいFPS。元のselfは変更しない。
        degは非負整数の出力係数数D。時間・出力空間O(D)。
        """
        assert deg >= 0
        return FPS(self.Func[:deg] + [0] * max(0, deg - len(self.Func)))

    def inv(self, d=-1):
        """1/f mod x**d。定数項!=0。d=-1はlen(Func)、結果はd係数。
        d/degは非負整数の出力係数数D（省略時N=len(Func)）。時間O(N+D log²(D+1))以内、作業空間O(N+D log(D+1))以内。
        """
        return FPS(fps_inverse(self.Func, len(self.Func) if d == -1 else d))

    def diff(self):
        """形式微分した新しいFPS。O(N)。"""
        return FPS([i * self.Func[i] for i in range(1, len(self.Func))])

    def integral(self):
        """定数項0で形式積分した新しいFPS。係数数はN+1、N<mod。
        引数なし。N=len(Func)として時間・出力空間O(N+1)（逆数表を必要な長さまで延長するコストを含む）。
        """
        return FPS(
            [0] + [x * _fps_integer_inverse(i + 1) for i, x in enumerate(self.Func)]
        )

    def log(self, deg=-1):
        """log(f) mod x**deg。定数項==1。deg=-1はlen(Func)。
        d/degは非負整数の出力係数数D（省略時N=len(Func)）。時間O(N+D log²(D+1))以内、作業空間O(N+D log(D+1))以内。
        """
        return FPS(fps_log(self.Func, len(self.Func) if deg == -1 else deg))

    def exp(self, deg=-1):
        """exp(f) mod x**deg。定数項==0。deg=-1はlen(Func)。
        d/degは非負整数の出力係数数D（省略時N=len(Func)）。時間O(N+D log²(D+1))以内、作業空間O(N+D log(D+1))以内。
        """
        return FPS(fps_exp(self.Func, len(self.Func) if deg == -1 else deg))

    def mod_sqrt(self, a):
        """aのmod 998244353の平方根。存在しなければ-1。
        aは整数。p=998244353としてO(log² p)程度の法乗算、空間O(1)個の整数。
        """
        return _fps_sqrt_mod(a % self.mod)

    def sqrt(self, deg=-1):
        """平方根 mod x**deg。存在しなければFPS([])。deg=-1はlen(Func)。
        d/degは非負整数の出力係数数D（省略時N=len(Func)）。時間O(N+D log²(D+1))以内、作業空間O(N+D log(D+1))以内。
        """
        result = fps_sqrt(self.Func, len(self.Func) if deg == -1 else deg)
        return FPS([] if result is None else result)

    def powfps(self, k, deg=-1):
        """f**k mod x**deg。k>=0、deg=-1はlen(Func)。k=0も対応。
        d/degは非負整数の出力係数数D（省略時N=len(Func)）。時間O(N+D log²(D+1))以内、作業空間O(N+D log(D+1))以内。
        kは非負整数の指数。定数項の累乗にO(log(k+1))回の法乗算が加わる。
        """
        return FPS(fps_power(self.Func, k, len(self.Func) if deg == -1 else deg))

    def multipoint_evaluation(self, P):
        """独自拡張: [f(P[0]),f(P[1]),...]をlistで返す。
        Pは評価点の整数list。D=max(len(Func),len(P))。時間O(D log²(D+1))、空間O(D log(D+1))以内。
        """
        return _FormalPowerSeries(self.Func).multipoint_evaluation(P)

    def taylor_shift(self, c):
        """独自拡張: f(x+c)を新しいFPSで返す。
        cはxに足す整数。N=len(Func)。時間O(N log(N+1))、追加空間O(N)。
        """
        return FPS(_FormalPowerSeries(self.Func).taylor_shift(c).poly)


def polynomial_interpolation(X, Y):
    """相異なるXと同長のYからf(X[i])=Y[i]を満たす次数<len(X)のFPSを返す。
    係数は戻り値.Func。998244353固定。独自拡張。
    Xは評価点、Yは各点での値を同じ順に並べた整数list。Xは法の下でも相異なる。N=len(X)=len(Y)。
    時間O(N log²(N+1))、空間O(N log(N+1))以内。
    """
    return FPS(_polynomial_interpolation(X, Y).poly)
