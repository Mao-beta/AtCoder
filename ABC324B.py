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
# 素数列挙
primes = [p for i, p in enumerate(prime_table) if i == p]

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

# 約数列挙（単体）
def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


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
    N = NI()
    P = factorize(N)
    P = set(P.keys())
    P.discard(2)
    P.discard(3)
    if len(P) > 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
