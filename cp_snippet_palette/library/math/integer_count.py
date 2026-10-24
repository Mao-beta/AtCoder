"""整数除算の商ごとの区間・合同方程式・φ/μの一括前計算。
floor_sum(n,m,a,b)とは別に、分母が変わるsum(N//i)を扱う。
標準Pythonのみ。整数演算のオーバーフローがないPyPyを基準とする。

使い方（このファイル全体を貼り付けてから実行）
    list(floor_quotient_ranges(5))  # => [(1, 2, 5), (2, 3, 2), (3, 6, 1)]
    sum_floor_quotients(5)  # => 10
    linear_congruence(6, 4, 10)  # => (4, 5)
    totient_sieve(6)  # => [0, 1, 1, 2, 2, 4, 2]
    mobius_sieve(6)  # => [0, 1, -1, -1, 0, -1, 1]
"""

from math import gcd


def floor_quotient_ranges(n):
    """n//iが一定の半開区間(l,r,商)をiの昇順にyield。1<=i<=n、n>=0。
    O(sqrt(n))個、追加空間O(1)。n=0なら何も返さない。
    nは非負整数の被除数。
    """
    assert n >= 0
    l = 1
    while l <= n:
        q = n // l
        r = n // q + 1
        yield l, r, q
        l = r


def sum_floor_quotients(n):
    """sum(n//i for i in range(1,n+1))。O(sqrt(n))時間・O(1)空間。
    nは非負整数の被除数。
    """
    return sum((r - l) * q for l, r, q in floor_quotient_ranges(n))


def linear_congruence(a, b, mod):
    """a*x≡b (mod mod)の全解を(x0,周期)で返す。解なしNone、mod>0。
    全解はx=x0+k*周期、0<=x0<周期。全整数が解なら(0,1)。O(log mod)。
    a/bは整数の係数/右辺、modは正整数の法。追加空間O(1)個の整数。
    """
    assert mod > 0
    g = gcd(a, mod)
    if b % g:
        return None
    period = mod // g
    if period == 1:
        return 0, 1
    return (b // g * pow(a // g, -1, period)) % period, period


def totient_sieve(limit):
    """phi[0..limit]。phi[n]は1..nでnと互いに素の個数。phi[0]=0、phi[1]=1。
    O(limit log log limit)時間・O(limit)空間。
    limitは前計算する最大の非負整数。返り値は長さlimit+1のlist。
    """
    assert limit >= 0
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for x in range(p, limit + 1, p):
                phi[x] -= phi[x] // p
    return phi


def mobius_sieve(limit):
    """メビウス関数mu[0..limit]。mu[0]=0、mu[1]=1。平方因子あり0、異なるk素因子なら(-1)^k。
    線形篩、O(limit)時間・空間。約数ごとの包除に使う。
    limitは前計算する最大の非負整数。返り値は長さlimit+1のlist。
    """
    assert limit >= 0
    mu, composite, primes = [0] * (limit + 1), bytearray(limit + 1), []
    if limit:
        mu[1] = 1
    for x in range(2, limit + 1):
        if not composite[x]:
            primes.append(x)
            mu[x] = -1
        for p in primes:
            y = x * p
            if y > limit:
                break
            composite[y] = 1
            if x % p == 0:
                break
            mu[y] = -mu[x]
    return mu
