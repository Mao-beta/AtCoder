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

prime_table = make_prime_table(1000002)
# 素数列挙
primes = [p for i, p in enumerate(prime_table) if i == p]

# 約数の個数　上のprime_tableと組み合わせて使う
def div_num(n):
    result = 1
    while n != 1:
        p = prime_table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result *= e+1
    return result


def main():
    N, p = SMI()
    N = int(N)
    p = float(p)
    ans = 0
    for n in range(2, N+1):
        d = div_num(n)
        ans += pow(1-p, d-2)
    print(ans)


if __name__ == "__main__":
    main()
