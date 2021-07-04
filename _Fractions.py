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


class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )


def zeta(n, dp):
    """
    高速ゼータ変換　和集合のリストから積集合のリストへ変換など
    """
    dp = dp.copy()
    for j in range(n):
        bit = 1<<j
        for i in range(1<<n):
            if i & bit == 0:
                dp[i] += dp[i | bit]
    return dp


def mobius(n, dp):
    """
    高速メビウス変換　積集合のリストから和集合のリストへ変換など
    """
    dp = dp.copy()
    for j in range(n):
        bit = 1<<j
        for i in range(1<<n):
            if i & bit == 0:
                dp[i] -= dp[i | bit]
    return dp



class Combinations:
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.inv[i - 1] * pow(i, self.mod - 2, self.mod) % self.mod

    def cmb(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] * self.inv[n - r] % MOD

    def perm(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % MOD


# nCr 要math
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


def combination_mod_initialize(n, MOD=10**9+7):
    fac = [1]*(n+1)
    inv = [1]*(n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = inv[i-1] * pow(i, MOD-2, MOD) % MOD
    return fac, inv

# 二項係数　高速
def combination_mod(n, r, fac, inv, mod=10**9+7):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * inv[r] * inv[n-r]


class Eratosthenes:
    """
    エラトステネスの篩、メビウス関数
    素因数分解、約数列挙、互いに素の個数
    """
    def __init__(self, n):
        self.n = n
        self.is_prime = [1] * (self.n + 1)
        self.min_factor = [-1] * (self.n + 1)
        self.mobius = [1] * (self.n + 1)

        self.is_prime[0] = 0
        self.is_prime[1] = 0
        self.min_factor[1] = 0

        for p in range(2, self.n + 1):
            if not self.is_prime[p]: continue

            self.min_factor[p] = p
            self.mobius[p] = -1

            for q in range(2*p, self.n + 1, p):
                self.is_prime[q] = 0

                if self.min_factor[q] == -1:
                    self.min_factor[q] = p
                if (q//p) % p == 0:
                    self.mobius[q] = 0
                else:
                    self.mobius[q] = -self.mobius[q]

    def factorize(self, x):
        """
        :param x:
        :return: 整数xの素因数分解、{素数p: 個数k}の辞書
        """
        res = {}
        while x > 1:
            p = self.min_factor[x]
            k = 0

            while self.min_factor[x] == p:
                x //= p
                k += 1

            res[p] = k

        return res

    def divisors(self, x):
        """
        約数列挙
        :param x:
        :return:
        """

        res = {1}
        facs = self.factorize(x)

        for p, k in facs.items():
            R = res.copy()
            for d in R:
                for _ in range(k):
                    d *= p
                    res.add(d)

        return res

    def euler(self, x):
        """
        1以上x以下の整数のうち、xと互いに素なものの個数
        """
        facs = self.factorize(x)
        res = x
        for p, k in facs.items():
            res *= p-1
            res //= p
        return res




# 高速エラストテネス　sieve[n]はnの最小の素因数
def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    return sieve

prime_table = make_prime_table(1000)

# 素因数分解　上のprime_tableと組み合わせて使う
def prime_factorize(n):
    result = []
    while n != 1:
        p = prime_table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result.append((p, e))
    return result


# Nの素因数分解を辞書で返す(単体)
def prime_fact(n):
    root = int(n**0.5) + 1
    prime_dict = {}
    for i in range(2, root):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    pass


if __name__ == "__main__":
    main()