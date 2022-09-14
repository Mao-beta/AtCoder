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
    A = NLI()
    INF = 10**20

    # 左からi個みたときのN個の総和の最大
    L = [0] * (3*N+1)
    # 右からi個みたときのN個の総和の最小
    R = [INF] * (3*N+1)

    now = 0
    hq = []
    heapify(hq)
    for i in range(3*N):
        a = A[i]
        heappush(hq, a)

        now += a

        while len(hq) > N:
            x = heappop(hq)
            now -= x

        L[i+1] = now

    now = 0
    hq = []
    heapify(hq)
    for i in range(3*N):
        a = A[3*N-1-i]
        heappush(hq, -a)

        now += a

        while len(hq) > N:
            x = heappop(hq) * (-1)
            now -= x

        R[i+1] = now

    ans = -INF
    for i in range(N, 2*N+1):
        ans = max(ans, L[i] - R[3*N-i])
    print(ans)


if __name__ == "__main__":
    main()
