import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    P = [4, 9, 5, 7, 11, 13, 17, 19, 23]
    C = list(accumulate([0]+P))
    print(sum(P), flush=True)
    A = []
    now = 0
    for p in P:
        for a in range(now+1, now+p):
            A.append(a+1)
        A.append(now+1)
        now += p

    # A = [1, 0, 3, 4, 2]
    # P = [2, 3]
    # C = list(accumulate([0] + P))
    print(*A, flush=True)
    # print(C)

    B = NLI()
    rems = []
    for i in range(len(P)):
        # print(i, C[i])
        idx = C[i]
        rem = B[idx]-1 - C[i]
        rems.append(rem)

    r0, m0 = crt(rems, P)
    print(r0, flush=True)


if __name__ == "__main__":
    main()
