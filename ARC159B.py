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



def main(A, B):

    # A = 10**9+7
    # B = A + 30

    if A > B:
        A, B = B, A

    G = B - A
    if G == 0:
        return 1

    P = prime_fact(G)

    big = -1
    for p in P:
        if p > 10**6:
            big = p

    ans = 0
    while A > 0:
        g = math.gcd(A, B)
        # print(A, B, g, G)

        if g > 1:
            A //= g
            B //= g
            A -= 1
            B -= 1
            ans += 1
            G //= g

            PG = prime_fact(g)
            for p, k in PG.items():
                P[p] -= k
                if P[p] == 0:
                    del P[p]

        elif G == big:
            if A > G:
                k = A % G
                ans += k
                B -= k
                A -= k
            elif A == G:
                ans += 1
                break
            else:
                ans += A
                B -= A
                A -= A

        elif G == 1:
            ans += A
            break
        else:
            nums = []
            for p in P:
                nums.append([A % p, p])

            nums.sort()
            k, p = nums[0]

            ans += k
            A -= k
            B -= k

    return ans


def guchoku(A, B):
    ans = 0
    while A >= 1 and B >= 1:
        g = math.gcd(A, B)
        A -= g
        B -= g
        ans += 1
    return ans


if __name__ == "__main__":
    A, B = NMI()
    ans = main(A, B)
    print(ans)
    exit()

    from random import randint

    for i in range(100):
        m = 10**4
        M = 10**8
        A = randint(m, M)
        B = randint(A, M)
        print(A, B)
        ans = main(A, B)
        gu = guchoku(A, B)

        assert ans == gu, f"{A}, {B}, {ans}, {gu}"
