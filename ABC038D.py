import sys
import math
from collections import defaultdict
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    WH = [NLI() for _ in range(N)]
    WH.sort(key=lambda x: (x[0], -x[1]))

    INF = 10**6
    dp = [INF] * (N+1)
    dp[0] = 0
    for w, h in WH:
        idx = bisect.bisect_left(dp, h)
        dp[idx] = h

    print(bisect.bisect_left(dp, INF) - 1)


if __name__ == "__main__":
    main()
