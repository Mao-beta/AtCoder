import sys
import math
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


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

prime_table = make_prime_table(1000001)
prime_table = [p for i, p in enumerate(prime_table) if i == p]


def main():
    N, K = NMI()

    D = defaultdict(int)

    for i in range(N, N-K, -1):
        D[i] = i

    ans = 1
    for p in prime_table:
        k = 0
        tmpN = N
        while tmpN > 1:
            k += tmpN // p
            tmpN //= p

        tmpK = K
        while tmpK > 1:
            k -= tmpK // p
            tmpK //= p

        tmpR = N-K
        while tmpR > 1:
            k -= tmpR // p
            tmpR //= p

        ans = ans * (k+1) % MOD

        for i in range(N//p * p, N-K, -p):
            while D[i] % p == 0:
                D[i] //= p

    for p in D.values():
        if p != 1:
            ans = ans * 2 % MOD

    print(ans)


if __name__ == "__main__":
    main()
