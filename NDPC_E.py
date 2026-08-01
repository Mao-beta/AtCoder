import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    # 区間スケジューリングを複数クエリでやるdp
    N, M, Q = NMI()
    AB = EI(M)
    LR = EI(Q)
    AB = [[x-1, y] for x, y in AB]
    LR = [[x-1, y] for x, y in LR]
    # jから2^i個飛んだときの右端の最小値
    dp = [[N+1]*(N+2) for _ in range(20)]
    AB.sort()
    i = N-1
    x = N+1
    for a, b in AB[::-1]:
        while a < i:
            dp[0][i] = x
            i -= 1
        x = min(x, b)
        # print(a, b, i)
        dp[0][i] = min(dp[0][i], x)
    for i in range(1, 20):
        for j in range(N):
            dp[i][j] = dp[i-1][dp[i-1][j]]
    # print(*dp, sep="\n")

    for l, r in LR:
        ans = 0
        now = l
        for i in range(19, -1, -1):
            if dp[i][now] <= r:
                ans |= 1 << i
                now = dp[i][now]
        print(ans)


if __name__ == "__main__":
    main()
