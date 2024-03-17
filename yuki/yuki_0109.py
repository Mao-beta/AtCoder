import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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

# 約数列挙（単体）
def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    T = NI()
    for _ in range(T):
        N, M = NMI()
        if M == 1:
            print(0)
            continue

        if N >= M:
            print(0)
            continue

        if M <= 10**5 or N <= 10**5:
            ans = 1
            for i in range(1, N+1):
                ans = ans * i % M
            print(ans)

        else:
            P = prime_fact(M)
            r = []
            m = []
            for p, k in P.items():
                mod = p**k
                m.append(mod)
                if N >= mod or k >= 2:
                    r.append(0)
                else:
                    # (p-1)!=-1
                    # p-1, p-2, ..., N+1で割っていく
                    x = p-1
                    for i in range(p-1, N, -1):
                        x = x * pow(i, p-2, p) % p
                    r.append(x)

            r0, m0 = crt(r, m)
            print(r0)


if __name__ == "__main__":
    main()
