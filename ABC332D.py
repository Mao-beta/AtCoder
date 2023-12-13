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


def main():
    H, W = NMI()
    A = EI(H)
    B = EI(H)

    def compress(S):
        """ 座標圧縮 """

        S = set(S)
        zipped, unzipped = {}, {}
        for i, a in enumerate(sorted(S), start=1):
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
        Z, _ = compress(A)
        tree = BIT(N)
        res = 0
        for a in A:
            za = Z[a]
            res += tree.sum(za)
            tree.add(za, 1)
        return N * (N - 1) // 2 - res


    def check(Ph, Pw):
        for h in range(H):
            for w in range(W):
                if A[Ph[h]][Pw[w]] != B[h][w]:
                    return False
        return True


    ans = 100000
    for Ph in permutations(range(H)):
        inv_h = inversion_num(Ph)
        for Pw in permutations(range(W)):
            inv_w = inversion_num(Pw)
            if check(Ph, Pw):
                ans = min(ans, inv_h + inv_w)

    if ans >= 100000:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
