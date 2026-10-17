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
    N, M = NMI()
    SC = [SMI() for _ in range(M)]
    INF = 10**15
    dp = [[INF]*(1<<N) for _ in range(M+1)]
    dp[0][0] = 0

    for i in range(M):
        sb = 0
        S, c = SC[i]
        c = int(c)
        for si, s in enumerate(S):
            sb |= (1<<si) * (s == "Y")

        for case in range(1<<N):
            if dp[i][case] == INF: continue

            dp[i+1][case] = min(dp[i+1][case], dp[i][case])

            if case | sb == case:
                continue

            ncase = case | sb
            dp[i+1][ncase] = min(dp[i+1][ncase], dp[i][case] + c)

    ans = dp[-1][-1]
    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
