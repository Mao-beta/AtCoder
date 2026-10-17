"""逆元・CRT・floor_sum・離散対数・mod平方根。
出典: _ACL_math.py, ABC270G, LC_Inv_of_Polynomials.py。
PyPy向け。Codonでは乗算やCRTの法の積を64bit以内にする。
"""

from math import gcd, isqrt


def pow_mod(x, n, m):
    """ACL形式。x**n mod m。n>=0、m>=1。"""
    if n < 0 or m < 1:
        raise ValueError("n>=0 and m>=1 required")
    return pow(x, n, m)


def inv_gcd(a, mod):
    """(gcd(a,mod), x)。a*x≡gcd (mod mod)、0<=x<mod/gcd。"""
    if mod <= 0:
        raise ValueError("mod must be positive")
    a %= mod
    s, t, x, y = mod, a, 0, 1
    while t:
        q = s // t
        s, t = t, s - q * t
        x, y = y, x - q * y
    return s, x % (mod // s)


def inv_mod(a, mod):
    g, x = inv_gcd(a, mod)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x


def crt(remainders, moduli):
    """O(k log M)。x≡r_i(mod m_i)。最小非負解と周期。解なしは(0,0)。"""
    if len(remainders) != len(moduli):
        raise ValueError("length mismatch")
    r, m = 0, 1
    for value, mod in zip(remainders, moduli):
        if mod <= 0:
            raise ValueError("moduli must be positive")
        value %= mod
        g, inverse = inv_gcd(m, mod)
        if (value - r) % g:
            return 0, 0
        step = (value - r) // g * inverse % (mod // g)
        r += m * step
        m *= mod // g
        r %= m
    return r, m


def floor_sum(n, mod, a, b):
    """sum((a*i+b)//mod for i in range(n))。a,bは負でもよい。O(log mod)。"""
    if n < 0 or mod <= 0:
        raise ValueError("n>=0 and mod>0 required")
    answer = 0
    while True:
        qa, a = divmod(a, mod)
        qb, b = divmod(b, mod)
        answer += qa * (n * (n - 1) // 2) + qb * n
        top = a * n + b
        if top < mod:
            return answer
        n, b = divmod(top, mod)
        mod, a = a, mod


def discrete_log(a, b, mod):
    """最小x>=0でa^x≡b(mod mod)。解なし-1。互いに素でなくても可。O(sqrt(mod))。"""
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
    """Tonelli–Shanks。primeは素数。小さい方の平方根、存在しなければ-1。"""
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
