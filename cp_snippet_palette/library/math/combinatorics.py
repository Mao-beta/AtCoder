"""組合せ・篩・試し割り。出典: _Fractions.py。
PyPy向け。Combは素数modかつ前計算上限n<modを要求。
Codonでは掛け算・総和を64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    c = Comb(10)
    c.combination(5, 2), c.permutation(5, 2), c.homogeneous(3, 2)  # => (10, 20, 6)
    combination_small_k(100, 2)  # => 4950
    smallest_prime_factors(6), primes_up_to(10)  # => ([0, 1, 2, 3, 2, 5, 2], [2, 3, 5, 7])
    factorize_trial(12), divisors(12)  # => ({2: 2, 3: 1}, [1, 2, 3, 4, 6, 12])
"""

from math import isqrt


class Comb:
    """0..nまでの階乗・逆階乗を前計算し、組合せを素数modで求める。
    0<=n<modが必要。素数判定は行わない。構築O(n)、各問い合わせO(1)。
    fact[i]=i!、ifact[i]=1/i!。問い合わせのnが前計算上限を超えるとValueError。
    入力: nは前計算する最大の非負整数、modはnより大きい素数。構築O(n+log mod)時間・O(n)空間。各問い合わせのn/kは選ぶ元の個数/選ぶ個数で整数。
    """
    def __init__(self, n, mod=998244353):
        """入力: nは前計算する最大の非負整数、modはnより大きい素数。構築O(n+log mod)時間・O(n)空間。各問い合わせのn/kは選ぶ元の個数/選ぶ個数で整数。
        """
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
        """n個からk個選ぶ組合せnCk mod mod。n<0またはkが0..n外なら0。
        時間・追加空間O(1)。
        """
        if k < 0 or k > n or n < 0:
            return 0
        if n >= len(self.fact):
            raise ValueError("n exceeds precomputation")
        return self.fact[n] * self.ifact[k] % self.mod * self.ifact[n - k] % self.mod

    def permutation(self, n, k):
        """n個からk個を順に選ぶ順列nPk mod mod。n<0またはkが0..n外なら0。
        時間・追加空間O(1)。
        """
        if k < 0 or k > n or n < 0:
            return 0
        if n >= len(self.fact):
            raise ValueError("n exceeds precomputation")
        return self.fact[n] * self.ifact[n - k] % self.mod

    def homogeneous(self, n, k):
        """n種類から重複を許してk個選ぶ個数。n>0なら(n+k-1)Ck。
        前計算上限はn+k-1以上必要。n=0はk=0のとき1、他は0。
        時間・追加空間O(1)。
        """
        if n < 0 or k < 0:
            return 0
        if n == 0:
            return int(k == 0)
        return self.combination(n + k - 1, k)


def combination_small_k(n, k, prime=998244353):
    """O(min(k,n-k))。nが大きい場合向け。min(k,n-k)<primeが必要。
    n/kは元の個数/選ぶ個数の整数、primeは素数の法。K=min(k,n-k)として時間O(K+log prime)、追加空間O(1)。
    """
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
    """0..nの最小素因数を長さn+1のlistで返す。n>=0。
    spf[x]でxの最小素因数を引ける。例: spf[12]=2。spf[1]=1、spf[0]=0。
    O(n log log n)時間・O(n)空間。
    nは前計算する最大の非負整数。
    """
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
    """2以上n以下の素数を昇順listで返す。n>=0、O(n log log n)時間・O(n)空間。
    nは前計算する最大の非負整数。
    """
    spf = smallest_prime_factors(n)
    return [p for p in range(2, n + 1) if spf[p] == p]


def factorize_trial(n):
    """O(sqrt(n))。{素数:指数}。n>=1。大きな整数はfactorize64を使う。
    nは分解する正整数。作業空間O(log(n+1))以内。
    """
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
    """正整数nの正の約数を昇順listで返す。n<1はValueError。O(√n)。
    出力空間O(τ(n))。τ(n)はnの正の約数の個数。
    """
    if n < 1:
        raise ValueError("n must be positive")
    small, large = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]
