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
    N, M = NMI()
    A = EI(M)
    ans = [[0]*N for _ in range(N)]
    for j in range(M):
        for i in range(N-1):
            x, y = A[j][i], A[j][i+1]
            ans[x-1][y-1] += 1
            ans[y-1][x-1] += 1

    res = 0
    for x in range(N):
        for y in range(x+1, N):
            if ans[x][y] == 0:
                res += 1

    print(res)


if __name__ == "__main__":
    main()
