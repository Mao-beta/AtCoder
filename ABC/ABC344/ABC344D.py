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
    T = SI()
    N = NI()
    S = []
    for _ in range(N):
        a, *s = SMI()
        S.append(s)
    INF = 10**10
    dp = [[INF]*(len(T)+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        SS = S[i]
        for s in SS:
            for j in range(len(T)+1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                if j + len(s) > len(T):
                    continue
                t = T[j:j + len(s)]
                if s != t:
                    continue
                nj = j+len(s)
                dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + 1)

    ans = dp[-1][-1]
    print(-1 if ans >= INF else ans)


if __name__ == "__main__":
    main()
