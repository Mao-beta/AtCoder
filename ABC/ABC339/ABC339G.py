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


def compress(S):
    """ 座標圧縮 """

    S = sorted(list(set(S)))
    zipped, unzipped = {}, {}
    for i, a in enumerate(S):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped, S


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
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    N = NI()
    A = NLI()
    Z, UZ, SA = compress(A)
    ZN = len(Z)
    Q = NI()
    ans = [0]
    B = 2000
    BITs = []
    for i in range(0, N, B):
        if i+B <= N:
            r = i+B
            bit = BIT(ZN)
        else:
            r = N
            bit = BIT(ZN)
        for idx in range(i, r):
            a = A[idx]
            bit.add(Z[a], a)
        BITs.append(bit)

    for _ in range(Q):
        a, b, c = NMI()
        l = a ^ ans[-1]
        r = b ^ ans[-1]
        x = c ^ ans[-1]
        l -= 1

        bl = (l + B-1) // B
        br = r // B
        res = 0

        if bl > br:
            for idx in range(l, r):
                if A[idx] <= x:
                    res += A[idx]
            ans.append(res)
            continue

        bx = bisect.bisect_right(SA, x)

        for idx in range(l, bl*B):
            if A[idx] <= x:
                res += A[idx]
        for idx in range(br*B, r):
            if A[idx] <= x:
                res += A[idx]

        for bi in range(bl, br):
            res += BITs[bi].sum0(bx)

        ans.append(res)

    print("\n".join(map(str, ans[1:])))


if __name__ == "__main__":
    main()
