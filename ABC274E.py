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
    XY = [NLI() for _ in range(N)]
    PQ = [NLI() for _ in range(M)]
    XYPQ = XY + PQ

    D = [[0.]*(N+M) for _ in range(N+M)]
    for i in range(N+M):
        xi, yi = XYPQ[i]
        for j in range(N+M):
            xj, yj = XYPQ[j]
            D[i][j] = math.sqrt((xi-xj)**2 + (yi-yj)**2)

    INF = 10**15
    # boost, now, state
    dp = [[[INF]*(1<<(N+M)) for _ in range(N+M)] for _ in range(6)]
    mask = (1<<N) - 1

    for i in range(N+M):
        state = 1 << i
        now = i
        boost = 0 if i < N else 1
        x, y = XYPQ[i]
        time = math.sqrt(x**2 + y**2)
        dp[boost][now][state] = min(dp[boost][now][state], time)


    ans = INF

    for state in range(1<<(N+M)):
        for now in range(N+M):
            for boost in range(6):
                speed = 1 << boost
                time = dp[boost][now][state]
                if time == INF:
                    continue

                if (state & mask) == mask:
                    x, y = XYPQ[now]
                    t = math.sqrt(x**2 + y**2) / speed
                    ans = min(ans, time + t)
                    continue

                for goto in range(N+M):
                    if (state >> goto) & 1:
                        continue

                    state_g = state | (1<<goto)
                    time_g = time + D[now][goto] / speed
                    if goto >= N:
                        boost_g = boost + 1
                    else:
                        boost_g = boost

                    dp[boost_g][goto][state_g] = min(dp[boost_g][goto][state_g], time_g)

    print(ans)


if __name__ == "__main__":
    main()
