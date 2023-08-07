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


def main():
    N = NI()
    X = SI()
    S = [SI() for _ in range(N)]

    def make_hand(X, S):
        CX = Counter(X)
        CS = Counter(S)
        res_c = ""
        res_n = 0
        for x in X:
            nx = CX[x]
            ns = CS[x]
            n = min(nx, 3) + min(ns, 2)
            if n < res_n:
                continue
            if n == res_n and x > res_c:
                continue
            res_n = n
            res_c = x
        for x in S:
            nx = CX[x]
            ns = CS[x]
            n = min(nx, 3) + min(ns, 2)
            if n < res_n:
                continue
            if n == res_n and x > res_c:
                continue
            res_n = n
            res_c = x

        return res_c, res_n

    hands = []
    for i, s in enumerate(S, start=1):
        c, n = make_hand(X, s)
        hands.append([-n, ord(c), i])

    hands.sort()
    print(hands[0][2])


if __name__ == "__main__":
    main()
