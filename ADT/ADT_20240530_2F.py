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
    N = NI()
    S = [SI() for _ in range(N)]
    T = [SI() for _ in range(N)]

    S = [[i, j] for i in range(N) for j in range(N) if S[i][j] == "#"]
    T = [[i, j] for i in range(N) for j in range(N) if T[i][j] == "#"]

    def rot(P):
        res = []
        for x, y in P:
            res.append([-y, x])
        return res

    def normalize(P):
        xmin = min(x for x, y in P)
        ymin = min(y for x, y in P)
        return sorted([[x-xmin, y-ymin] for x, y in P])

    S = normalize(S)
    T = normalize(T)
    for _ in range(4):
        S = normalize(rot(S))
        if S == T:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
