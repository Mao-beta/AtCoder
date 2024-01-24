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
    N, K = NMI()
    X = []
    Y = []
    for _ in range(N):
        x, y = NMI()
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()

    def mergesort(A, B):
        ai, bi = 0, 0
        res = []
        while ai < N and bi < N:
            a, b = A[ai], B[bi]
            if a > b:
                res.append(b)
                bi += 1
            else:
                res.append(a)
                ai += 1
        return res + A[ai:] + B[bi:]

    def calc(A, t, gap):
        res = 0
        for a in A:
            if a < t-gap:
                res += t-gap - a
            elif a > t:
                res += a - t
        return res


    def judge(mid):
        """
        幅をmid以下にできるか？
        Xと、Xを右にmidずらしたものをマージソートし、
        N番目のときがそのmidにおける最小
        Yでもやって、操作回数がK以下ならOK
        """
        Xm = [x+mid for x in X]
        Ym = [y+mid for y in Y]
        Xs = mergesort(X, Xm)
        Ys = mergesort(Y, Ym)
        tx, ty = Xs[N-1], Ys[N-1]
        res = calc(X, tx, mid) + calc(Y, ty, mid)
        return res <= K

    ok = 10**9
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if judge(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
