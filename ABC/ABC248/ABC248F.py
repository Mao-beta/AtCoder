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
    N, P = NMI()
    if N == 2:
        print(4)
        exit()

    # i個コの字をつけ、直前の状態がj(非連結0, 連結1)、削ったのがk本
    dp0 = [[0] * (N+3) for _ in range(N)]
    dp1 = [[0] * (N+3) for _ in range(N)]
    dp0[0][1] = 1
    dp1[0][0] = 1

    for i in range(N-1):
        ni = i + 1
        for k in range(N):
            dp0[ni][k + 1] += dp0[i][k]
            dp1[ni][k + 0] += dp0[i][k]
            dp0[ni][k + 2] += dp1[i][k] * 2
            dp1[ni][k + 1] += dp1[i][k] * 3
            dp1[ni][k + 0] += dp1[i][k]

            dp0[ni][k + 1] %= P
            dp1[ni][k + 0] %= P
            dp0[ni][k + 2] %= P
            dp1[ni][k + 1] %= P
            dp1[ni][k + 0] %= P

    ans = []
    for k in range(1, N):
        ans.append(dp1[-1][k])

    print(*ans)


if __name__ == "__main__":
    main()
