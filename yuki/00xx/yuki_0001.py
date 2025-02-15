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


def main():
    N = NI()
    C = NI()
    V = NI()
    S = NLI()
    T = NLI()
    Y = NLI()
    M = NLI()
    INF = 10**18
    dp = [[INF]*(C+1) for _ in range(N)]
    dp[0][C] = 0
    E = [[s-1, t-1, y, m] for s, t, y, m in zip(S, T, Y, M)]
    E.sort()
    for s, t, y, m in E:
        for c in range(C+1):
            if dp[s][c] >= INF:
                continue
            if c - y < 0:
                continue
            dp[t][c-y] = min(dp[t][c-y], dp[s][c] + m)
    ans = min(dp[-1])
    if ans < INF:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
