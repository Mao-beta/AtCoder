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
    XY = [NLI() for _ in range(M)]
    XY = [[x-1, y-1] for x, y in XY]

    # 自分に指している点
    P = [[] for _ in range(N)]
    for x, y in XY:
        P[y].append(x)

    dp = [0] * (1<<N)
    dp[0] = 1

    for case in range(1<<N):
        now = dp[case]
        for i in range(N):
            if (case >> i) & 1:
                continue

            now_P = P[i]
            now_P = [(case >> p) & 1 for p in now_P]
            if not all(now_P):
                continue

            goto = case | (1 << i)
            dp[goto] += now

    print(dp[-1])


if __name__ == "__main__":
    main()
