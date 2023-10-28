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
    N, X, Y = NMI()
    A = NLI()
    Xs = A[1::2]
    Ys = A[::2]

    def split_and_list(A):
        """
        半分全列挙して前半と後半の部分和を返す
        O(2^(N//2))
        """
        N = len(A)
        former, latter = A[:N // 2], A[N // 2:]
        fn, ln = len(former), len(latter)
        F = []
        FI = []
        for k in range(fn + 1):
            for c in combinations(range(fn), k):
                F.append(sum([former[i] for i in c])*2)
                FI.append(c)
        L = []
        LI = []
        for k in range(ln + 1):
            for c in combinations(range(ln), k):
                L.append(sum([latter[i] for i in c])*2)
                LI.append(c)
        return F, FI, L, LI


    def solve(X, Xs):
        F, FI, L, LI = split_and_list(Xs)
        gap = X + sum(Xs)

        def get_plus_idx(F, FI, L, LI, gap):
            FS = set(F)
            LS = set(L)

            for f, fis in zip(F, FI):
                if gap - f not in LS:
                    continue
                lis = LI[L.index(gap-f)]
                lis = [i+len(Xs)//2 for i in lis]
                return list(fis) + lis

            return None

        return get_plus_idx(F, FI, L, LI, gap)

    X_plus = solve(X, Xs)
    Y_plus = solve(Y, Ys)

    if X_plus is None or Y_plus is None:
        print("No")
        return

    X_plus = set(2 * i + 1 for i in X_plus)
    Y_plus = set(2 * i for i in Y_plus)
    now = "xp"
    ans = []
    for i in range(N):
        if i % 2 == 0:
            # Y
            if i in Y_plus:
                if now == "xp":
                    ans.append("L")
                    now = "yp"
                else:
                    ans.append("R")
                    now = "yp"
            else:
                if now != "xp":
                    ans.append("L")
                    now = "ym"
                else:
                    ans.append("R")
                    now = "ym"

        else:
            # X
            if i in X_plus:
                if now == "yp":
                    ans.append("R")
                    now = "xp"
                else:
                    ans.append("L")
                    now = "xp"
            else:
                if now != "yp":
                    ans.append("R")
                    now = "xm"
                else:
                    ans.append("L")
                    now = "xm"

    print("Yes")
    print("".join(ans))


if __name__ == "__main__":
    main()
