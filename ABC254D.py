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


class Eratosthenes:
    """
    エラトステネスの篩、メビウス関数
    素因数分解、約数列挙、互いに素の個数
    """
    def __init__(self, n):
        self.n = n
        self.is_prime = [1] * (self.n + 1)
        self.min_factor = [-1] * (self.n + 1)
        self.mobius = [1] * (self.n + 1)

        self.is_prime[0] = 0
        self.is_prime[1] = 0
        self.min_factor[1] = 0

        for p in range(2, self.n + 1):
            if not self.is_prime[p]: continue

            self.min_factor[p] = p
            self.mobius[p] = -1

            for q in range(2*p, self.n + 1, p):
                self.is_prime[q] = 0

                if self.min_factor[q] == -1:
                    self.min_factor[q] = p
                if (q//p) % p == 0:
                    self.mobius[q] = 0
                else:
                    self.mobius[q] = -self.mobius[q]

    def factorize(self, x):
        """
        :param x:
        :return: 整数xの素因数分解、{素数p: 個数k}の辞書
        """
        res = {}
        while x > 1:
            p = self.min_factor[x]
            k = 0

            while self.min_factor[x] == p:
                x //= p
                k += 1

            res[p] = k

        return res

    def divisors(self, x):
        """
        約数列挙
        :param x:
        :return:
        """

        res = {1}
        facs = self.factorize(x)

        for p, k in facs.items():
            R = res.copy()
            for d in R:
                for _ in range(k):
                    d *= p
                    res.add(d)

        return res

    def euler(self, x):
        """
        1以上x以下の整数のうち、xと互いに素なものの個数
        """
        facs = self.factorize(x)
        res = x
        for p, k in facs.items():
            res *= p-1
            res //= p
        return res


def main():
    N = NI()
    E = Eratosthenes(N+1)
    S = [i**2 for i in range(1, int(N**0.5) + 10)]

    ans = 0
    for x in range(1, N+1):
        P = E.factorize(x)
        y = 1
        for p, k in P.items():
            if k % 2:
                y *= p

        # print(x, y, N//y, bisect.bisect_right(S, N//y))
        ans += bisect.bisect_right(S, N//y)

    print(ans)


if __name__ == "__main__":
    main()
