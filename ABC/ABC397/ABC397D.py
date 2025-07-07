import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def gcd(a, b):
    while a:
        a, b = b%a, a
    return b


def is_prime(n):
    if n == 2:
        return 1
    if n == 1 or n%2 == 0:
        return 0

    m = n - 1
    lsb = m & -m
    s = lsb.bit_length()-1
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:
            continue
        x = pow(a,d,n)
        r = 0
        if x == 1:
            continue
        while x != m:
            x = pow(x,2,n)
            r += 1
            if x == 1 or r == s:
                return 0
    return 1


def find_prime_factor(n):
    if n%2 == 0:
        return 2

    m = int(n**0.125)+1

    for c in range(1,n):
        f = lambda a: (pow(a,2,n)+c)%n
        y = 0
        g = q = r = 1
        k = 0
        while g == 1:
            x = y
            while k < 3*r//4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = f(y)
                    q = q*abs(x-y)%n
                g = gcd(q,n)
                k += m
            k = r
            r *= 2
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x-y),n)
        if g == n:
            continue
        if is_prime(g):
            return g
        elif is_prime(n//g):
            return n//g
        else:
            return find_prime_factor(g)


def factorize(n):
    # expected O(N^(1/4))
    res = {}
    while not is_prime(n) and n > 1:  # nが合成数である間nの素因数の探索を繰り返す
        p = find_prime_factor(n)
        s = 0
        while n%p == 0:  # nが素因数pで割れる間割り続け、出力に追加
            n //= p
            s += 1
        res[p] = s
    if n > 1:  # n>1であればnは素数なので出力に追加
        res[n] = 1
    return res


def divisors_from_prime_factors(prime_factors, need_sort=True):
    """
    素因数分解から約数リストを生成します。(1とその数自身を含む)

    Parameters
    ---
    prime_factors
        素因数分解を表現した、タプルのリスト。
        p1^a1 * p2^a2 であれば、 [(p1,a1),(p2,a2)] 。
    need_sort
        Trueの場合、約数リストをソートして返します。
    """
    # 既知の約数リスト
    div = [1]
    for p, a in prime_factors:
        # 既知の約数それぞれに対して、
        # p^1倍, p^2倍, ... p^a倍 したものを計算して約数リストに追加する
        m = len(div)
        for i in range(m):
            for j in range(1, a + 1):
                div.append(div[i] * p ** j)
    if need_sort:
        div.sort()
    return div


def main():
    N = NI()
    D = factorize(N)
    D = [(p, k) for p, k in D.items()]
    div = divisors_from_prime_factors(D)
    for k in div:
        m = N // k
        l = 12*m - k**2*3
        # print(k, l)
        if l <= 0:
            continue
        r = math.isqrt(l)
        # print(l, r)
        if r ** 2 != l:
            continue
        p = r - 3*k
        # print(k, p)
        if p <= 0 or p % 6:
            continue
        y  = p // 6
        x = y + k
        # print(x, y)
        if x**3 - y**3 == N:
            print(x, y)
            return
    print(-1)


if __name__ == "__main__":
    main()
