"""Miller–RabinとPollard rho。符号なし64bit範囲。多倍長乗算を使うためPyPy専用。

抽出元: LibraryChecker/LC_factorize.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    bool(is_probable_prime(97)), bool(is_probable_prime(91))  # => (True, False)
    dict(prime_fact(360))  # => {2: 3, 3: 2, 5: 1}
    find_prime_factor(15) in (3, 5)  # => True
    sorted(divisors(12)), totient(12), lcm(6, 8)  # => ([1, 2, 3, 4, 6, 12], 4, 24)
"""

from math import gcd
from collections import Counter


def is_probable_prime(n):
    """nが素数ならTrue、そうでなければFalse。n<2は偽。
    n<2**64の整数専用。上限以上はValueError。条件式if is_probable_prime(n)で使う。
    時間O(log(n+1))回の法乗算、補助空間O(log(n+1))bit。多倍長整数の乗算コストは別。
    """
    if n < 2:
        return False
    if n >= 1 << 64:
        raise ValueError("only n < 2**64 is supported")
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    m = n - 1
    lsb = m & -m
    s = lsb.bit_length() - 1
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:
            continue
        x = pow(a, d, n)
        r = 0
        if x == 1:
            continue
        while x != m:
            x = pow(x, 2, n)
            r += 1
            if x == 1 or r == s:
                return False
    return True


def find_prime_factor(n):
    """合成数nの素因数を1つ返すPollard rhoの補助関数。最小素因数とは限らない。
    前提は合成数かつ2<=n<2**64。通常は入力判定も行うprime_fact(n)を使う。
    Pollard rhoの目安は小さい素因子pに対しO(sqrt(p))回程度の法演算。定数を変えて再試行するため最悪時間の保証ではない。再帰の深さはO(log n)以内。
    """
    if n % 2 == 0:
        return 2

    m = int(n**0.125) + 1

    for c in range(1, n):
        f = lambda a: (pow(a, 2, n) + c) % n
        y = 0
        g = q = r = 1
        k = 0
        while g == 1:
            x = y
            while k < 3 * r // 4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            k = r
            r *= 2
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x - y), n)
        if g == n:
            continue
        if is_probable_prime(g):
            return g
        elif is_probable_prime(n // g):
            return n // g
        else:
            return find_prime_factor(g)


def prime_fact(N):
    """1<=n<2**64を素因数分解しCounter({素数:指数})を返す。1なら空のCounter。
    辞書のキー順は保証しない。昇順の素数列が必要ならsorted(result)。
    任意精度の中間乗算を使うのでPyPy向け。
    入力Nは正整数。時間は素数判定とPollard rhoの試行回数に依存し、一般にO(N^(1/4))程度が目安だが最悪保証なし。補助空間O(log N)個の整数以内。
    """
    n = N
    if not 1 <= n < 1 << 64:
        raise ValueError("1 <= n < 2**64 required")
    res = Counter()
    while (
        not is_probable_prime(n) and n > 1
    ):  # nが合成数である間nの素因数の探索を繰り返す
        p = find_prime_factor(n)
        s = 0
        while n % p == 0:  # nが素因数pで割れる間割り続け、出力に追加
            n //= p
            s += 1
        res[p] = s
    if n > 1:  # n>1であればnは素数なので出力に追加
        res[n] = 1
    return res


def divisors(N):
    """正整数Nの全約数をlistで返す。順序は未指定。整列にはsorted(divisors(N))。
    1<=N<2**64。素因数分解と約数列挙の計算量。
    τを約数個数、Tをprime_fact(N)の時間とするとO(T+τ)時間・O(τ)空間。Nは正整数。
    """
    result = [1]
    for p, e in prime_fact(N).items():
        base = result[:]
        power = 1
        for _ in range(e):
            power *= p
            result.extend(d * power for d in base)
    return result


def totient(N):
    """1..NでNと互いに素な整数の個数。1<=N<2**64、totient(1)=1。
    Nは正整数。prime_fact(N)の時間Tに対してO(T+log N)時間、補助空間O(log N)以内。
    """
    result = N
    for p in prime_fact(N):
        result -= result // p
    return result


def lcm(x, y):
    """非負整数x,yの最小公倍数。片方が0なら0。O(log min(x,y))。
    追加空間O(1)個の整数。
    """
    return x // gcd(x, y) * y if x and y else 0
