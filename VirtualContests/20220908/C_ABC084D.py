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

prime_table = make_prime_table(100010)
# 素数列挙
primes = set(p for i, p in enumerate(prime_table) if i == p)


def main():
    Q = NI()
    A = [0] * 100010
    for n in range(1, 10**5, 2):
        if n in primes and ((n+1) // 2) in primes:
            A[n] = 1

    C = list(accumulate(A))
    for _ in range(Q):
        l, r = NMI()
        l -= 1
        print(C[r] - C[l])


if __name__ == "__main__":
    main()
