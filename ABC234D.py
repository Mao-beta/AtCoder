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
        1-index
        sum -> i番目までの和
        add -> i番目にxを足す
        :param n:
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.each = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum_range(self, l, r):
        # [l, r) (1-index)
        return self.sum(r-1) - self.sum(l-1)

    def add(self, i, x):
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def __repr__(self):
        return str(self.each)


def main():
    N, K = NMI()
    P = NLI()
    tree = BIT(N)
    for i, p in enumerate(P, start=1):
        tree.add(p, 1)
        if i >= K:
            t = i - K + 1
            ok = N+1
            ng = 0
            while abs(ok-ng) > 1:
                X = (ok + ng) // 2
                # print(X, tree.sum(X), t, tree)
                if tree.sum(X) >= t:
                    ok = X
                else:
                    ng = X
            print(ok)


if __name__ == "__main__":
    main()
