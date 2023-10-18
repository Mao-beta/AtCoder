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


from sortedcontainers import SortedSet


M = 10 ** 6
def f(a, b):
    return a * M + b

def g(x):
    return divmod(x, M)

def main():
    N = NI()
    A = NLI()
    Q = NI()
    TSX = EI(Q)

    A = [x-1 for x in A]
    R = [0] * N
    for i, a in enumerate(A):
        R[a] = i

    # S2i[s]: クエリのsが表す数列のindex
    S = list(range(Q+1))
    set_idx = SortedSet(f(i, A[i]) for i in range(N))
    set_val = SortedSet(f(A[i], i) for i in range(N))
    INF = 10**6
    ans = [[set_idx, set_val]]

    # print(*ans, sep="\n")

    for i, (t, s, x) in enumerate(TSX):
        # print(t, s, x)
        sidx, sval = ans[S[s]]
        n = len(sidx)

        if t == 1:
            nsidx = SortedSet()
            nsval = SortedSet()

            if x > n // 2:
                while len(sidx) > x:
                    k, v = g(sidx.pop())
                    sval.discard(f(v, k))
                    nsidx.add(f(k, v))
                    nsval.add(f(v, k))
            else:
                for _ in range(x):
                    k, v = g(sidx.pop(0))
                    sval.discard(f(v, k))
                    nsidx.add(f(k, v))
                    nsval.add(f(v, k))
                S[s], S[i+1] = S[i+1], S[s]

            ans.append([nsidx, nsval])

        else:
            x -= 1
            nsidx = SortedSet()
            nsval = SortedSet()
            former = sval.bisect_left(f(x, INF-1))
            # print("#former", (x, INF), former)

            if former > n // 2:
                while len(sval) > former:
                    v, k = g(sval.pop())
                    sidx.discard(f(k, v))
                    nsidx.add(f(k, v))
                    nsval.add(f(v, k))
            else:
                for _ in range(former):
                    v, k = g(sval.pop(0))
                    sidx.discard(f(k, v))
                    nsidx.add(f(k, v))
                    nsval.add(f(v, k))
                S[s], S[i + 1] = S[i + 1], S[s]

            ans.append([nsidx, nsval])

        print(len(ans[S[i+1]][0]))
        # print(*ans, sep="\n")




class DynamicFenwickTree:
    """
    Binary Indexed Tree(BIT)は区間和と一点加算が配列長をnとして時間計算量O(logn)で出来るが、
    空間計算量がO(n)になるためnがメモリサイズより大きいときに使用できない。
    そこで、配列の代わりに連想配列を利用することで空間計算量を(クエリ数をqとして)O(qlogn)で抑えたものが動的Binary Indexed Treeである。
    https://nyaannyaan.github.io/library/data-structure/dynamic-binary-indexed-tree.hpp.html
    """
    def __init__(self, size=None):
        self.N = size + 1 if size is not None else None
        self.data = {}

    def add(self, k, x):
        k += 1
        while k < self.N:
            self.data[k] = self.data.get(k, 0) + x
            k += k & -k

    def sum(self, k):
        if k < 0:
            return 0
        ret = 0
        while k > 0:
            ret += self.data.get(k, 0)
            k -= k & -k
        return ret

    def range_sum(self, a, b):
        return self.sum(b) - self.sum(a)

    def __getitem__(self, k):
        return self.sum(k + 1) - self.sum(k)

    def lower_bound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = 1
        while (k << 1) < self.N:
            k <<= 1
        while k:
            if x + k <= self.N - 1 and self.data.get(x + k, 0) < w:
                w -= self.data.get(x + k, 0)
                x += k
            k >>= 1
        return x

    def __repr__(self):
        return str(self.data)


class DynamicFenwickTree2D:
    def __init__(self, n=None, m=None):
        self.N = n + 1 if n is not None else None
        self.M = m
        self.bit = [DynamicFenwickTree(self.M) for _ in range(self.N)] if self.N is not None else []

    def add(self, i, j, x):
        i += 1
        while i < self.N:
            self.bit[i].add(j, x)
            i += i & -i

    def sum(self, n, m):
        if n < 0 or m < 0:
            return 0
        ret = 0
        while n > 0:
            ret += self.bit[n].sum(m)
            n -= n & -n
        return ret

    def range_sum(self, nl, ml, nr, mr):
        ret = 0
        while nl != nr:
            if nl < nr:
                ret += self.bit[nr].range_sum(ml, mr)
                nr -= nr & -nr
            else:
                ret -= self.bit[nl].range_sum(ml, mr)
                nl -= nl & -nl
        return ret




def main2():
    N = NI()
    A = NLI()
    Q = NI()
    TSX = EI(Q)

    A = [x-1 for x in A]
    seg = DynamicFenwickTree2D(N, N)
    for i, a in enumerate(A):
        seg.add(i, a, 1)

    XL = [0] * (Q+1)
    XR = [0] * (Q+1)
    YL = [0] * (Q+1)
    YR = [0] * (Q+1)

    XR[0] = N
    YR[0] = N

    for i, (t, s, x) in enumerate(TSX):
        xl, xr, yl, yr = XL[s], XR[s], YL[s], YR[s]
        XL[i + 1], XR[i + 1], YL[i + 1], YR[i + 1] = xl, xr, yl, yr

        if t == 1:
            def judge(X):
                return seg.range_sum(xl, yl, X, yr) >= x

            ok = xr
            ng = xl-1
            while abs(ok - ng) > 1:
                X = (ok + ng) // 2
                if judge(X):
                    ok = X
                else:
                    ng = X

            XL[i+1] = ok
            XR[s] = ok

        else:
            x -= 1
            if yl <= x+1 < yr:
                YL[i+1] = x+1
                YR[s] = x+1
            elif x+1 < yl:
                YR[s] = yl
            else:
                YL[i+1] = yr

        xl, xr, yl, yr = XL[i+1], XR[i+1], YL[i+1], YR[i+1]
        # print(t, s, x, B[-1])
        print(seg.range_sum(xl, yl, xr, yr))


if __name__ == "__main__":
    main2()
