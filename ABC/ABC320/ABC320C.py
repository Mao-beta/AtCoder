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
    M = NI()
    S = [SI()*3 for _ in range(3)]
    ans = 10**10
    for x in range(10):
        dp = [[0] * 8 for _ in range(3*M+1)]
        dp[0][0] = 1
        sx = str(x)
        for t in range(3*M):
            for c in range(8):
                if dp[t][c] == 0:
                    continue
                for k in range(3):
                    s = S[k][t]
                    dp[t+1][c] = dp[t][c]
                    if s == sx:
                        nc = c | (1<<k)
                        dp[t+1][nc] = 1

        for t in range(3*M+1):
            if dp[t][7]:
                ans = min(ans, t-1)
                break

    if ans == 10**10:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
