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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


class SqrtDecomposition:
    def __init__(self, A: list, Z: dict):
        self.A = [Z[a] for a in A]
        self.Z = Z
        self.N = len(A)
        self.sz = int(self.N ** 0.5 + 1)
        self.B = [self.A[l:l+self.sz] for l in range(0, self.N, self.sz)]
        # 全体で何が何個あるか
        self.state = [0] * len(self.Z)
        # 更新の遅延
        self.lazy = [0] * len(self.B)


    def apply(self, l, r, x):
        for bi in range(len(self.B)):
            bl = bi * self.sz
            br = min(bl + self.sz, self.N)
            ll = max(l, bl)
            rr = min(r, br)
            if ll == bl and rr == br:
                # bucket丸々
                if self.lazy[bi] > 0:
                    self.state[self.lazy[bi]] -= br - bl
                else:
                    for a in self.B[bi]:
                        self.state[a] -= 1
                self.lazy[bi] = x
                self.state[x] += br - bl
            else:
                # 端の愚直処理
                # まず遅延を解除
                if self.lazy[bi] > 0:
                    for a in self.B[bi]:
                        self.state[a] -= 1
                    self.state[self.lazy[bi]] += len(self.B[bi])
                    self.lazy[bi] = 0
                # 該当部分を更新
                for i in range(bl-ll, br-ll):
                    self.state[self.B[bi][i]] -= 1
                    self.state[x] += 1
                    self.B[bi][i] = x


    def prod(self, l, r):

        for bi in range(len(self.B)):
            bl = bi * self.sz
            br = min(bl + self.sz, self.N)
            ll = max(l, bl)
            rr = min(r, br)
            if ll == bl and rr == br:
                # bucket丸々
                # あとでreflect
                pass
            else:
                # 端の愚直処理
                pass


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
    N = NI()
    A = NLI()
    Q = NI()
    LRX = EI(Q)
    Z, UZ = compress(A + [x for l, r, x in LRX])
    sq = SqrtDecomposition(A)


if __name__ == "__main__":
    main()
