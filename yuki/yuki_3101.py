import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


# 高速エラストテネス　sieve[n]はnにおけるn未満の最大の約数
def make_prime_table(n):
    sieve = [1] * (n + 1)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, n + 1):
        for j in range(i*2, n + 1, i):
            sieve[j] = i
    return sieve

prime_table = make_prime_table(1000001)
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


class BIT():
    """
    BIT 0-index  ACL for python
    add(p, x): p番目にxを加算
    get(p): p番目を取得
    sum0(r): [0:r)の和を取得
    sum(l, r): [l:r)の和を取得
    """

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    Q = NI()
    LR = EI(Q)
    R2LI = [[] for _ in range(10**6+1)]
    for i, (l, r) in enumerate(LR):
        R2LI[r].append([l, i])
    ans = [0] * Q
    bit = BIT(10**6+1)
    for r in range(1, 10**6+1):
        bit.add(prime_table[r], 1)
        for l, i in R2LI[r]:
            ans[i] = r-l+1 - bit.sum(l, 10**6+1)
            # print(bit.debug()[:21])
            # print(l, r, i, ans[i])
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
