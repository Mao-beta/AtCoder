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


def main():
    A, B = NMI()
    if B == 0:
        print(0)
        return

    P = prime_fact(A)

    if B % 2 == 0:
        num = B // 2
        for p, k in P.items():
            num = num * (B*k+1) % MOD99
        print(num)

    else:
        odd = False
        target = 1
        for p, k in P.items():
            if k % 2:
                odd = True
                target = p
                break

        # print(P, target)

        if odd:
            num = (B * P[target] + 1) // 2
            num = num * B % MOD99
            for p, k in P.items():
                if p == target:
                    continue
                num = num * (B * k + 1) % MOD99
            print(num)

        else:
            num = B // 2
            Ks = list(P.values())
            n = len(Ks)

            base = 1
            for i in range(n):
                num += B * B % MOD99 * (Ks[i]//2) % MOD99 * base % MOD99
                num %= MOD99
                base = base * (B * Ks[i] + 1) % MOD99

            print(num)



if __name__ == "__main__":
    main()
