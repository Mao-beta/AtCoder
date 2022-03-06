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


def compress(S):
    """ 座標圧縮 """

    zipped, unzipped = {}, {}
    for i, a in enumerate(S, start=1):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


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

    def add(self, i, x):
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def __repr__(self):
        return str(self.each)


def inversion_num(A):
    """
    リストAの転倒数を座標圧縮ありで求める。要BIT, compress
    """
    N = len(A)
    tree = BIT(N)
    res = 0
    for a in A:
        res += tree.sum(a)
        tree.add(a, 1)
    return N * (N - 1) // 2 - res


def main():
    N = NI()
    A = NLI()
    B = NLI()

    if Counter(A) != Counter(B):
        print("No")
        exit()

    for k in Counter(A).values():
        if k >= 2:
            print("Yes")
            exit()

    Z, UZ = compress(A)
    B = [Z[b] for b in B]

    if inversion_num(B) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
