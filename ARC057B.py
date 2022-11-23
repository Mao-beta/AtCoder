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
    A = [NI() for _ in range(N)]
    INF = 10**15
    C = list(accumulate([0]+A))

    if C[-1] == K:
        print(1)
        exit()

    # dp[i][j] i日終わってj回機嫌が良いときの最小勝利回数
    dp = [[INF]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        a = A[i]
        c = C[i]
        for j in range(N+1):
            d = dp[i][j]
            if d == INF:
                continue

            dp[i+1][j] = min(dp[i+1][j], d)

            if c == 0:
                x = 1
            else:
                # d/ci < d+x/ci+a なる最小のx
                x = a * d // c + 1

            dp[i+1][j+1] = min(dp[i+1][j+1], d + x)


    ans = 0
    for j in range(N+1):
        if dp[-1][j] <= K:
            ans = j

    # print(*dp, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
