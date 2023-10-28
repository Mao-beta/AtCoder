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


def solve(S, K):
    N = len(S)
    # [l, r)における答え
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for l in range(N, -1, -1):
        for r in range(l + 1, N + 1):
            # 初期値
            dp[l][r] = r-l
            # とくにof関係ないとき
            for m in range(l + 1, r):
                dp[l][r] = min(dp[l][r], dp[l][m] + dp[m][r])
            # 左端がo, 途中にfがあれば除ける
            # fの位置を全探索
            if S[l] == "o":
                for m in range(l + 1, r):
                    if S[m] != "f":
                        continue
                    # oからfまで全部取れないと無理
                    if dp[l + 1][m] > 0:
                        continue
                    # fより後ろからK個まで追加で除ける
                    dp[l][r] = min(dp[l][r], max(0, dp[m+1][r] - K))

    print(dp[0][N])

def main():
    S = SI()
    K = NI()
    solve(S, K)


if __name__ == "__main__":
    main()
