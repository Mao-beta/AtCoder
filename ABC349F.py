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


def main():
    # 10**16以下の約数の個数は最大で40000くらい、素因数の種類は11くらい、素因数は22個くらい
    N, M = NMI()
    PM = list(factorize(M).items())
    A = NLI()
    # Mの約数のみに絞る
    A = [a for a in A if M % a == 0]
    N = len(A)

    L = len(PM)
    D = [0] * N

    for i, a in enumerate(A):
        print(i, a)
        for pi, (p, k) in enumerate(PM):
            ac = 0
            while a % p == 0:
                a //= p
                ac += 1
            if ac == k:
                D[i] ^= 1 << pi

    print(D)
    C = [0] * (1<<L)
    for i, d in enumerate(D):
        C[d] += 1

    def subset_zeta_transform(A, N, mod):
        res = A[:]
        for i in range(N):
            for j in range((1 << N)):
                if j & (1 << i) == 0:
                    nj = j ^ (1 << i)
                    res[nj] += res[j]
                    res[nj] %= mod
        return res

    print(C)
    C = subset_zeta_transform(C, L, MOD99)
    print(C)

    ans = 0
    for case in range(1<<L):
        # caseで1のbitは制約違反となる素因数, 0は自由
        bit = case.bit_count()
        x = N - C[case]
        print(bin(case), x)
        ans += pow(2, x, MOD99) * (-1) ** bit

    print(ans % MOD99)


if __name__ == "__main__":
    main()
