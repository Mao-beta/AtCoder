import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    INF = N+100
    dp = [INF] * (N+1)
    dp[1] = 1
    que = deque()
    que.append(1)
    while que:
        x = que.popleft()
        g = bin(x).count("1")
        if 1 <= x-g <= N and dp[x-g] >= INF:
            dp[x-g] = dp[x] + 1
            que.append(x-g)
        if 1 <= x+g <= N and dp[x+g] >= INF:
            dp[x+g] = dp[x] + 1
            que.append(x+g)
    ans = dp[N]
    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
