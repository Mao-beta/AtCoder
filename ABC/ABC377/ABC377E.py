import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


from typing import List

class Doubling:
    """
    ダブリング
    1回目の遷移先をもったリストを入力としてダブリング遷移を構築
    DB.query(x, k): xのk回後の遷移先を返す

    firsts = [2, 1, 3, 0]
    DB = Doubling(firsts)
    print(DB.query(2, 1)) # 3
    print(DB.query(2, 2)) # 0
    print(DB.query(2, 3)) # 2
    """
    def __init__(self, firsts: List[int]):
        self.firsts = firsts
        self.n = len(firsts)
        self.B = 62
        self.maxk = (1 << self.B) - 1
        self.D = [[0]*self.n for _ in range(self.B+1)]

        self._build()

    def _build(self):
        for i in range(self.n):
            self.D[0][i] = self.firsts[i]

        for b in range(self.B):
            for i in range(self.n):
                m = self.D[b][i]
                x = self.D[b][m]
                self.D[b+1][i] = x

    def query(self, x, k):
        assert 0 <= x < self.n
        assert 1 <= k <= self.maxk

        res = x
        for b in range(self.B+1):
            if (k >> b) & 1:
                res = self.D[b][res]
        return res


def main():
    N, K = NMI()
    P = NLI()
    P = [x-1 for x in P]
    seen = [0] * N
    ans = [0] * N
    for si in range(N):
        if seen[si]:
            continue
        L = []
        L.append(si)
        seen[si] = 1
        i = si
        while True:
            j = P[i]
            if seen[j]:
                break
            seen[j] = 1
            L.append(j)
            i = j

        # print(si, L)
        amari = pow(2, K, len(L))
        for r, l in enumerate(L):
            ans[l] = L[(r+amari)%len(L)] + 1
    print(*ans)


if __name__ == "__main__":
    main()
