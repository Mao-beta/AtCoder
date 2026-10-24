"""逆元・CRT・floor_sum・離散対数・mod平方根。

出典: _ACL_math.py, ABC270G, LC_Inv_of_Polynomials.py。
PyPy向け。Codonでは乗算やCRTの法の積を64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    pow_mod(2, 10, 1000), inv_gcd(6, 15), inv_mod(3, 7)  # => (24, (3, 3), 5)
    crt([2, 3], [3, 5])  # x=2 mod3、x=3 mod5 -> x=8 mod15
    # => (8, 15)
    crt([0, 1], [2, 2])  # 矛盾
    # => (0, 0)
    floor_sum(4, 3, 2, 1)  # => 4
    discrete_log(2, 8, 13), sqrt_mod(4, 7)  # => (3, 2)
"""

from math import gcd, isqrt


def pow_mod(x, n, m):
    """ACL形式。x**n mod m。n>=0、m>=1。
    xは整数の底、nは非負整数の指数、mは正整数の法。時間O(1+log(n+1))回の法乗算、追加空間O(1)個の整数。
    """
    if n < 0 or m < 1:
        raise ValueError("n>=0 and m>=1 required")
    return pow(x, n, m)


def inv_gcd(a, b):
    """(gcd(a,b), x)。b>0、a*x≡gcd(a,b) (mod b)、0<=x<b/gcd(a,b)。
    aは整数、bは正整数の法。時間O(log(b+1))回の除算、追加空間O(1)個の整数。
    """
    if b <= 0:
        raise ValueError("b must be positive")
    a %= b
    s, t, x, y = b, a, 0, 1
    while t:
        q = s // t
        s, t = t, s - q * t
        x, y = y, x - q * y
    return s, x % (b // s)


def inv_mod(x, m):
    """x*y≡1 (mod m)となる逆元y（0<=y<m）を返す。m>0。
    xとmが互いに素でなければValueError。素数でないmにも対応。O(log m)。
    xは整数、mは正整数の法。追加空間O(1)個の整数。
    """
    g, x = inv_gcd(x, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x


def crt(r, m):
    """O(k log M)。x≡r_i(mod m_i)。最小非負解と周期。解なしは(0,0)。
    rは剰余の整数列、mは同じ長さの正の法の整数列。k=len(r)、Mは途中で合成される法の最大値。追加空間O(1)個の整数（整数のbit長はMに依存）。
    """
    if len(r) != len(m):
        raise ValueError("length mismatch")
    r0, m0 = 0, 1
    for value, mod in zip(r, m):
        if mod <= 0:
            raise ValueError("m must be positive")
        value %= mod
        g, inverse = inv_gcd(m0, mod)
        if (value - r0) % g:
            return 0, 0
        step = (value - r0) // g * inverse % (mod // g)
        r0 += m0 * step
        m0 *= mod // g
        r0 %= m0
    return r0, m0


def floor_sum(n, m, a, b):
    """sum((a*i+b)//m for i in range(n))。a,bは負でもよい。O(log m)。
    nは項数の非負整数、mは正整数の除数、a/bは整数の一次式の係数/定数項。追加空間O(1)個の整数。
    """
    if n < 0 or m <= 0:
        raise ValueError("n>=0 and m>0 required")
    answer = 0
    while True:
        qa, a = divmod(a, m)
        qb, b = divmod(b, m)
        answer += qa * (n * (n - 1) // 2) + qb * n
        top = a * n + b
        if top < m:
            return answer
        n, b = divmod(top, m)
        m, a = a, m


def discrete_log(a, b, mod):
    """最小x>=0でa^x≡b(mod mod)。解なし-1。互いに素でなくても可。O(sqrt(mod))。
    a/bは整数の底/目標値、modは正整数の法。追加空間O(sqrt(mod))個の整数。
    """
    if mod <= 0:
        raise ValueError("mod must be positive")
    a %= mod
    b %= mod
    offset, factor = 0, 1
    while True:
        if b == factor % mod:
            return offset
        g = gcd(a, mod)
        if g == 1:
            break
        if b % g:
            return -1
        b //= g
        mod //= g
        factor = factor * (a // g) % mod
        offset += 1
    target = b * inv_mod(factor, mod) % mod
    step = isqrt(mod) + 1
    table = {}
    value = 1
    for j in range(step):
        if value not in table:
            table[value] = j
        value = value * a % mod
    backward = inv_mod(pow(a, step, mod), mod)
    value = target
    for i in range(step + 1):
        if value in table:
            return offset + i * step + table[value]
        value = value * backward % mod
    return -1


def sqrt_mod(a, prime):
    """Tonelli–Shanks。primeは素数。小さい方の平方根、存在しなければ-1。
    aは平方根を求める整数、primeは素数の法。時間O(log² prime)程度の法乗算（非平方剰余の探索は別）、追加空間O(1)個の整数。
    """
    if prime < 2:
        raise ValueError("prime must be >=2")
    a %= prime
    if a == 0 or prime == 2:
        return a
    if pow(a, (prime - 1) // 2, prime) != 1:
        return -1
    q, s = prime - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (prime - 1) // 2, prime) != prime - 1:
        z += 1
    c, x, t = pow(z, q, prime), pow(a, (q + 1) // 2, prime), pow(a, q, prime)
    while t != 1:
        i, power = 0, t
        while power != 1:
            power = power * power % prime
            i += 1
        b = pow(c, 1 << (s - i - 1), prime)
        x = x * b % prime
        c = b * b % prime
        t = t * c % prime
        s = i
    return min(x, prime - x)
