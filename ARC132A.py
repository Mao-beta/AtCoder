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
    N = NI()
    R = NLI()
    C = NLI()
    Q = NI()
    querys = [NLI() for _ in range(Q)]

    R = [x-1 for x in R]
    C = [x-1 for x in C]
    querys = [[x-1, y-1] for x, y in querys]

    Rv = [0] * N
    Cv = [0] * N
    for i, r in enumerate(R):
        Rv[r] = i
    for i, c in enumerate(C):
        Cv[c] = i

    Rq = [set() for _ in range(N)]
    Cq = [set() for _ in range(N)]
    for i, (r, c) in enumerate(querys):
        Rq[r].add(i)
        Cq[c].add(i)

    # print(Rv)
    # print(Cv)
    # print(Rq)
    # print(Cq)

    ans = [""] * Q
    M = N-1
    m = 0
    for i in range(N):
        if i % 2 == 0:
            r, c = Rv[M], Cv[M]
            qi = Rq[r] | Cq[c]
            for q in qi:
                if not ans[q]:
                    ans[q] = "#"
            M -= 1

        else:
            r, c = Rv[m], Cv[m]
            qi = Rq[r] | Cq[c]
            for q in qi:
                if not ans[q]:
                    ans[q] = "."
            m += 1

    print("".join(ans))


if __name__ == "__main__":
    main()
