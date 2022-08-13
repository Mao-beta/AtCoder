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
            s %= MOD99
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            self.data[i] %= MOD99
            i += i & -i

    def get(self, i):
        i += 1
        return self.each[i] % MOD99

    def set(self, i, x):
        b = self.get(i)
        self.add(i, -b)
        self.add(i, x)

    def __repr__(self):
        return str(self.each)


def main():
    N, Q = NMI()
    A = [0] + NLI()
    querys = [NLI() for _ in range(Q)]

    tree = BIT(N+1)
    itree = BIT(N+1)
    i2tree = BIT(N+1)

    for i, a in enumerate(A):
        tree.set(i, a)
        itree.set(i, a*i % MOD99)
        i2tree.set(i, a*i*i % MOD99)


    for query in querys:
        if query[0] == 1:
            _, x, v = query
            tree.set(x, v)
            itree.set(x, v*x % MOD99)
            i2tree.set(x, v*x*x % MOD99)

        else:
            x = query[1]
            # print("x", x)
            # print(tree)
            # print(itree)
            # print(i2tree)
            ans = i2tree.sum(x) - (2*x+3) * itree.sum(x) % MOD99 + (x+1) * (x+2) % MOD99 * tree.sum(x) % MOD99
            ans = ans * pow(2, MOD99-2, MOD99) % MOD99
            print(ans)


if __name__ == "__main__":
    main()
