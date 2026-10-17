"""組合せ・篩・試し割り。出典: _Fractions.py。
PyPy向け。Combは素数modかつ前計算上限n<modを要求。
Codonでは掛け算・総和を64bit以内にする。
"""

from math import isqrt


class Comb:
    def __init__(self, n, mod=998244353):
        if not 0 <= n < mod or mod < 2:
            raise ValueError("0<=n<prime mod required")
        self.mod = mod
        self.fact = [1] * (n + 1)
        self.ifact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.ifact[n] = pow(self.fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.ifact[i - 1] = self.ifact[i] * i % mod

    def combination(self, n, k):
        if k < 0 or k > n or n < 0:
            return 0
        if n >= len(self.fact):
            raise ValueError("n exceeds precomputation")
        return self.fact[n] * self.ifact[k] % self.mod * self.ifact[n - k] % self.mod

    def permutation(self, n, k):
        if k < 0 or k > n or n < 0:
            return 0
        if n >= len(self.fact):
            raise ValueError("n exceeds precomputation")
        return self.fact[n] * self.ifact[n - k] % self.mod

    def homogeneous(self, n, k):
        if n < 0 or k < 0:
            return 0
        if n == 0:
            return int(k == 0)
        return self.combination(n + k - 1, k)


def combination_small_k(n, k, prime=998244353):
    """O(min(k,n-k))。nが大きい場合向け。min(k,n-k)<primeが必要。"""
    if k < 0 or k > n or n < 0:
        return 0
    k = min(k, n - k)
    if prime < 2 or k >= prime:
        raise ValueError("k must be smaller than prime")
    numerator, denominator = 1, 1
    for i in range(1, k + 1):
        numerator = numerator * ((n - k + i) % prime) % prime
        denominator = denominator * i % prime
    return numerator * pow(denominator, prime - 2, prime) % prime


def smallest_prime_factors(n):
    """O(n log log n)時間・O(n)空間。spf[1]=1、spf[0]=0。"""
    if n < 0:
        raise ValueError("negative limit")
    spf = list(range(n + 1))
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for x in range(p * p, n + 1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def primes_up_to(n):
    spf = smallest_prime_factors(n)
    return [p for p in range(2, n + 1) if spf[p] == p]


def factorize_trial(n):
    """O(sqrt(n))。{素数:指数}。n>=1。大きな整数はfactorize64を使う。"""
    if n < 1:
        raise ValueError("n must be positive")
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def divisors(n):
    if n < 1:
        raise ValueError("n must be positive")
    small, large = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]
