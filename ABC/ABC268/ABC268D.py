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


def main():
    N, M = NMI()
    S = [SI() for _ in range(N)]
    TT = [SI() for _ in range(M)]
    T = set()

    for tt in TT:
        X = tt.split("_")
        ok = True
        for x in X:
            if x == "":
                continue
            if x not in S:
                ok = False
        if ok:
            T.add(tt)


    # あと何文字使えるか
    rem = 16 - (sum([len(s) for s in S]))

    UU = []
    U = []

    def rec(i):
        now = sum(U)
        if now > rem:
            return

        if i >= N - 1:
            UU.append(U[:])
            return

        for u in range(1, rem + 1):
            U.append(u)
            rec(i + 1)
            U.pop()

    rec(0)

    for SP in permutations(S, N):
        for U in UU:
            X = ""
            for xi in range(N - 1):
                X += SP[xi]
                X += "_" * U[xi]
            X += SP[-1]
            if 3 <= len(X) <= 16 and X not in T:
                print(X)
                exit()

    print(-1)


if __name__ == "__main__":
    main()
