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
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            self.data[p - 1] %= MOD99
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        return (self.sum0(r) - self.sum0(l)) % MOD99

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
            s %= MOD99
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    N = NI()
    A = NLI()
    B = NLI()
    AI = [[a, i] for i, a in enumerate(A)]
    AI.sort()
    A = [A[i] for a, i in AI]
    B = [B[i] for a, i in AI]

    # dp[j][i]: 総和がjで最後に使ったのがAi(1-index)
    dp = [BIT(5002) for _ in range(5002)]
    dp[0].add(0, 1)

    for i in range(1, N+1):
        b = B[i-1]
        for j in range(b, 5001):
            s = dp[j-b].sum(0, i)
            dp[j].add(i, s)

    ans = 0
    il = 1
    for j in range(5001):
        while il < N+1 and j > A[il-1]:
            il += 1
        ans += dp[j].sum(il, N+1)
        ans %= MOD99

    print(ans)


if __name__ == "__main__":
    main()
