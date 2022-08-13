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
    P = NLI()
    I = NLI()
    P = [x-1 for x in P]
    I = [x-1 for x in I]

    if P[0] != 0:
        print(-1)
        exit()

    ans = [[0, 0] for _ in range(N)]
    I_inv = {x: i for i, x in enumerate(I)}
    now = [0]

    def rec(l, r):
        if l >= r:
            return -1

        if now[0] >= N:
            print(-1)
            exit()

        root = P[now[0]]
        now[0] += 1
        idx = I_inv[root]
        lc = rec(l, idx)
        rc = rec(idx+1, r)
        ans[root][0] = lc + 1
        ans[root][1] = rc + 1
        return root

    rec(0, N)

    cnt = 0
    for l, r in ans:
        if l > 0:
            cnt += 1
        if r > 0:
            cnt += 1

    if cnt != N-1:
        print(-1)

    else:
        for l, r in ans:
            print(l, r)


if __name__ == "__main__":
    main()
