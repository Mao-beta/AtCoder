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
EI = lambda m: [NLI() for _ in range(m)]


class SqrtDecomposition:
    def __init__(self, A: list):
        self.A = A[:]
        self.N = len(A)
        self.sz = int(self.N ** 0.5 + 1)
        self.B = [A[l:l+self.sz] for l in range(0, self.N, self.sz)]
        self.state = [None for _ in range(len(self.B))]

    def reflect(self, bi):
        # B[bi]に更新を反映
        if self.state[bi]:
            l = bi * self.sz
            r = min(l + self.sz, self.N)
            self.sort(l, r)
            self.state[bi] = 0
        return

    def swap(self, i):
        # i番目とi+1番目をswap
        bi, ri = divmod(i, self.sz)
        bj, rj = divmod(i+1, self.sz)
        self.reflect(bi)
        self.reflect(bj)
        self.B[bi][ri], self.B[bj][rj] = self.B[bj][rj], self.B[bi][ri]
        return

    def sort(self, l, r):
        # A[l:r]を昇順にsort
        # 集計
        for bi in range(len(self.B)):
            bl = bi * self.sz
            br = min(bl + self.sz, self.N)
            ll = max(l, bl)
            rr = min(r, br)
            print(l, r, bl, br, ll, rr)
            if ll == bl and rr == br:
                self.state[bi] = 1
            else:
                print(ll, rr, self.B[bi][ll - bl:rr - bl])
                self.B[bi][ll - bl:rr - bl] = sorted(self.B[bi][ll - bl:rr - bl])

        for bi in range(len(self.B)):
            bl = bi * self.sz
            br = min(bl + self.sz, self.N)
            ll = max(l, bl)
            rr = min(r, br)
            print(l, r, bl, br, ll, rr)
            if ll == bl and rr == br:
                self.state[bi] = 1
            else:
                print(ll, rr, self.B[bi][ll-bl:rr-bl])
                self.B[bi][ll-bl:rr-bl] = sorted(self.B[bi][ll-bl:rr-bl])
        return


    def get_A(self):
        for bi in range(len(self.B)):
            self.reflect(bi)
        res = []
        for b in self.B:
            res += b
        return res

    def __repr__(self):
        return str(self.B)


def main():
    N, Q = NMI()
    TXY = EI(Q)
    A = [i+1 for i in range(N)]
    S = SqrtDecomposition(A)
    for t, x, y in TXY:
        x -= 1
        if t == 1:
            S.swap(x)
        else:
            S.sort(x, y)
        print(S.B, S.state)

    ans = S.get_A()
    print(*ans)


if __name__ == "__main__":
    main()
