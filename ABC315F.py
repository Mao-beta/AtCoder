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
    N = NI()
    XY = EI(N)
    INF = 10**20
    # dp[i][j]: いま点i(0-index)にいて、それまでにj点とばしている
    dp = [[INF]*33 for _ in range(N)]
    dp[0][0] = 0.0

    D = [[0.0] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, min(N, i+33)):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            D[i].append(math.sqrt((x1-x2)**2 + (y1-y2)**2))

    for i in range(N-1):
        for j in range(33):
            for skip in range(33):
                ni = i + 1 + skip
                nj = j + skip
                if ni >= N or nj >= 33:
                    continue
                try:
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + D[i][ni-i])
                except:
                    pass

    # print(D)

    ans = INF
    for i, a in enumerate(dp[N-1]):
        if i > 0:
            p = pow(2, i-1)
        else:
            p = 0
        ans = min(ans, a + p)

    print(ans)


if __name__ == "__main__":
    main()
