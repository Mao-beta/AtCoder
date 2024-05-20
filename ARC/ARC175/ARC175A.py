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


def guchoku(N, P, S):
    ans = 0
    for pro in product("LR", repeat=N):
        ok = True
        for i in range(N):
            if S[i] == "?":
                continue
            if S[i] != pro[i]:
                ok = False
        if not ok:
            continue
        X = [0] * N
        for p in P:
            s = pro[p]
            if X[p] == X[(p+1)%N] == 1:
                ok = False
                break

            if X[p]:
                X[(p+1)%N] = 1
            elif X[(p+1)%N]:
                X[p] = 1
            else:
                if s == "L":
                    X[p] = 1
                else:
                    X[(p+1)%N] = 1
        if ok:
            ans += 1
    return ans % MOD99


def main(N, P, S):
    ans = 0
    if S[P[0]] != "L":
        # R start
        X = [0] * N
        tmp = 1
        for i, p in enumerate(P):
            X[p] = 1
            if i > 0:
                if X[(p-1) % N]:
                    if S[p] == "?":
                        tmp = tmp * 2 % MOD99
                else:
                    if S[p] == "L":
                        tmp *= 0
        # print(tmp)
        ans += tmp

    if S[P[0]] != "R":
        # L start
        X = [0] * N
        tmp = 1
        for i, p in enumerate(P):
            X[p] = 1
            if i > 0:
                if X[(p+1) % N]:
                    if S[p] == "?":
                        tmp = tmp * 2 % MOD99
                else:
                    if S[p] == "R":
                        tmp *= 0
        # print(tmp)
        ans += tmp

    return ans % MOD99


if __name__ == "__main__":
    N = NI()
    P = NLI()
    P = [x-1 for x in P]
    S = SI()
    print(main(N, P, S))

    # N = 5
    # for P in permutations(range(N), N):
    #     for S in product("LR?", repeat=N):
    #         ans = main(N, P, S)
    #         gu = guchoku(N, P, S)
    #         assert ans == gu, (N, P, S, ans, gu)
