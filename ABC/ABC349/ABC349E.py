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


def main():
    A = NLI() + NLI() + NLI()
    INF = 10**15
    X = [0] * 9

    def check(default):
        L = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]
        for i, j, k in L:
            s = X[i] + X[j] + X[k]
            if s == 3:
                return INF
            elif s == -3:
                return -INF
        return default


    def rec(now: int):
        turn = now.bit_count()

        if turn == 9:
            res = 0
            for ta, a in zip(X, A):
                res += ta * a
            return res

        if turn % 2 == 0:
            # takahashi
            res = -INF
            for i in range(9):
                if (now >> i) & 1:
                    continue

                X[i] = 1
                c = check(-INF)
                if c == INF:
                    X[i] = 0
                    return INF
                r = rec(now | (1<<i))
                res = max(res, r)
                X[i] = 0

        else:
            # aoki
            res = INF
            for i in range(9):
                if (now >> i) & 1:
                    continue

                X[i] = -1
                c = check(INF)
                if c == -INF:
                    X[i] = 0
                    return -INF
                r = rec(now | (1<<i))
                res = min(res, r)
                X[i] = 0

        # print(turn, bin(now), res)
        return res

    r = rec(0)
    if r > 0:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
