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


class BIT():
    def __init__(self, n):
        """
        0-index
        sum -> i番目までの和
        add -> i番目にxを足す
        :param n:
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.each = [0] * (n + 1)

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def __repr__(self):
        return str(self.each)


def main():
    N, M, K = NMI()

    if K == 0:
        print(pow(M, N, MOD99))
        exit()

    dp = [[0]*(M+1) for _ in range(N+1)]

    B = BIT(M+1)

    for j in range(1, M+1):
        dp[1][j] = 1
        B.add(j, 1)

    S = [0] * (N+1)
    S[1] = M

    # print(B)

    for i in range(2, N+1):
        B2 = BIT(M+1)
        S = B.sum(M) % MOD99
        for j in range(1, M+1):
            l = max(j - K + 1, 1)
            r = min(j + K - 1, M)
            # print(l, r)
            B2.add(j, (S - B.sum(r) + B.sum(l-1)) % MOD99)
        B, B2 = B2, B
        # print(B2)

    print(B.sum(M) % MOD99)


if __name__ == "__main__":
    main()
