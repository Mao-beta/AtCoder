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


def inv_gcd(a, b):
    a = a % b
    if a == 0:
        return b, 0
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0:
        m0 += b // s
    return s, m0


def inv_mod(x, m):
    assert 1 <= m
    z = inv_gcd(x, m)
    assert z[0] == 1
    return z[1]


def crt(r,m):
    # r: 余りのlist
    # m: modのlist
    assert len(r) == len(m)
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return 0, 0
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g:
            return 0, 0
        x = (r1-r0) // g % u1 * im % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return r0,m0


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


def _main():
    T, M = NMI()
    P = factorize(M)
    # P2X[p][i]: pでi!を何回割れるか
    P2X = defaultdict(lambda: [0]*5001)
    # P2R[pk][i]: i!でpk以外の部分のmod
    P2R = defaultdict(lambda: [1]*5001)
    for p, k in P.items():
        pk = p**k
        for i in range(1, 5001):
            x = 0
            t = i
            while t > 0:
                x += t // p
                t //= p
            P2X[p][i] = x
            while i % p == 0:
                i //= p
            P2R[pk][i] = P2R[pk][i-1] * i % pk

    print(P2X)
    print(P2R)

    for _ in range(T):
        N = NI()
        C = NLI()
        Cs = sum(C)
        Rs = []
        Ms = []
        print(P)

        for p, k in P.items():
            pk = p**k
            Ms.append(pk)
            r = P2R[pk][Cs]
            x = P2X[p][Cs]
            print(r, x)
            for c in C:
                print(f"{p=}, {c=}, {P2X[p][c]=}")
                x -= P2X[p][c]
                r = r * inv_mod(P2R[pk][c], pk) % pk
            if x >= k:
                Rs.append(0)
            else:
                print(r, p, x)
                Rs.append(r * p**x % pk)

        r0, m0 = crt(Rs, Ms)
        print(r0, m0, Rs, Ms)

    print(crt([2, 1], [512, 3125]))


def main():
    T, M = NMI()
    X = [[1]*5001 for _ in range(5001)]
    for i in range(2, 5001):
        for j in range(1, i):
            X[i][j] = (X[i-1][j-1] + X[i-1][j]) % M

    for _ in range(T):
        N = NI()
        C = NLI()
        S = sum(C)
        ans = 1
        for c in C:
            ans = ans * X[S][c] % M
            S -= c
        print(ans)


if __name__ == "__main__":
    main()
