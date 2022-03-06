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
    N, K = NMI()
    Win_P = NLI()
    T = SI()
    hand = {"r": 0, "s": 1, "p": 2}

    # dp[i][j]はi回じゃんけんして最後に出した手がj
    dp = [[0]*3 for _ in range(N+1)]
    for i in range(N):
        hm = hand[T[i]]
        for j in range(3):
            is_win = (j - hm) % 3 == 2
            for bj in range(1, 3):
                bj = (bj + j) % 3
                if i+1-K > 0:
                    dp[i+1][j] = max(dp[i+1][j], dp[i+1-K][bj] + Win_P[j] * is_win)
                else:
                    dp[i+1][j] = Win_P[j] * is_win

    ans = 0
    for d in dp[-K:]:
        ans += max(d)
    print(ans)


if __name__ == "__main__":
    main()
