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
        self.B = 32
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
    N = NI()
    A = NLI()
    A = [x-1 for x in A]

    L = [0] * N
    for i in range(N):
        if L[i]:
            continue
        S = set()
        S.add(i)
        a = i
        while True:
            a = A[a]
            if a in S:
                break
            S.add(a)
        x = len(S)
        for s in S:
            L[s] = x
    R = [pow(10, 100, L[i]) for i in range(N)]
    D = Doubling(A)
    for a in A:
        a = D.query(a, N)
        if R[a] > 0:
            x = D.query(a, R[a])
        else:
            x = a
        print(x+1, end=" ")


if __name__ == "__main__":
    main()
