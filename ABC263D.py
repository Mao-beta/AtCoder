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
    N, L, R = NMI()
    A = NLI()

    INF = 10**20

    # 左からi個見て、最後が元々/Lだったときのmin
    dpl = [[INF] * 2 for _ in range(N+1)]
    dpr = [[INF] * 2 for _ in range(N+1)]

    dpl[0][0] = 0
    dpl[0][1] = 0
    for i, a in enumerate(A):
        dpl[i + 1][0] = min(dpl[i][0] + a, dpl[i][1] + a, dpl[i + 1][0])
        dpl[i + 1][1] = min(dpl[i][1] + L, dpl[i + 1][1])

    dpr[0][0] = 0
    dpr[0][1] = 0
    for i, a in enumerate(reversed(A)):
        dpr[i + 1][0] = min(dpr[i][0] + a, dpr[i][1] + a, dpr[i + 1][0])
        dpr[i + 1][1] = min(dpr[i][1] + R, dpr[i + 1][1])

    ans = INF
    for i in range(N+1):
        tmp = min(dpl[i]) + min(dpr[N-i])
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
