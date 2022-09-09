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


def main(N, LR):
    D = defaultdict(list)
    kouho = set()
    for l, r in LR:
        kouho.add(l)
        kouho.add(r)
        D[l].append((r, "l"))
        D[r].append((l, "r"))

    kouho = sorted(list(kouho))

    def f(c):
        X = []
        for ll, rr in LR:
            if c < ll:
                X.append(ll)
            elif rr < c:
                X.append(rr)
            else:
                X.append(c)

        return calc(X)


    # 三分探索
    l = 0
    r = len(kouho)

    while r - l > 3:
        c1 = l + (r-l) // 3
        c2 = r - (r-l) // 3
        if f(kouho[c1]) < f(kouho[c2]):
            r = c2
        else:
            l = c1

    ans = 10**20
    for i in range(l, r):
        ans = min(ans, f(kouho[i]))
    print(ans)


def calc(X):
    n = len(X)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            res += abs(X[i] - X[j])
    return res


def guchoku(N, LR):
    P = []
    for l, r in LR:
        P.append(list(range(l, r+1)))

    for X in product(*P):
        print(X, calc(X))



if __name__ == "__main__":
    N = NI()
    LR = [NLI() for _ in range(N)]
    main(N, LR)

    # guchoku(N, LR)
