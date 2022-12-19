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


class BIT():
    """
    BIT 0-index  ACL for python
    add(p, x): p番目にxを加算
    get(p): p番目を取得
    sum0(r): [0:r)の和を取得
    sum(l, r): [l:r)の和を取得
    """
    def __init__(self,N):
        self.n=N
        self.data=[0 for i in range(N)]

    def add(self,p,x):
        assert 0<=p<self.n,"0<=p<n,p={0},n={1}".format(p,self.n)
        p+=1
        while(p<=self.n):
            self.data[p-1]+=x
            p+=p& -p

    def get(self, p):
        return self.sum(p, p+1)

    def sum(self,l,r):
        assert (0<=l and l<=r and r<=self.n),"0<=l<=r<=n,l={0},r={1},n={2}".format(l,r,self.n)
        return self.sum0(r)-self.sum0(l)

    def sum0(self,r):
        s=0
        while(r>0):
            s+=self.data[r-1]
            r-=r&-r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, K = NMI()
    A = NLI()
    Z, UZ = compress(A)
    A = [Z[a] for a in A]
    # print(A)

    # L[r]: [l:r)での交換回数がK以下となる極大な区間のl
    # 尺取りでrごとにもとめる
    L = [0] * (N+1)
    bit = BIT(N)
    l = 0
    k = 0
    for r, ar in enumerate(A, start=1):
        k += bit.sum(ar+1, N)
        bit.add(ar, 1)

        # print(bit.debug())
        # print(k)

        while l < r and k > K:
            k -= bit.sum(0, A[l])
            bit.add(A[l], -1)
            # print(bit.debug(), k)
            l += 1

        # print(bit.debug())
        # print(k)
        L[r] = l
        # print("lr", l, r)

    # print("L", L)

    #     l                 i
    # xxx | (L[i])oooo(i-1) | (i)
    # dp[i]: i個まで分割し終わっているときの場合の数をBITでもつ
    # dp[i] = dp[L[i]]~dp[i-1]までの総和 = dp.sum(l, i)
    dp = BIT(N+1)
    dp.add(0, 1)
    for i in range(1, N+1):
        dp.add(i, dp.sum(L[i], i) % MOD)

    # print(dp.debug())
    print(dp.get(N) % MOD)


if __name__ == "__main__":
    main()
