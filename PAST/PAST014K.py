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
    N, t, p = NMI()
    A = NLI()

    # 入れる→100％で a*(100-t)/100 を得る
    # 入れない→p%で a*(100-t)/100 を得る、次0
    # 　　　　→(100-p)%で a 得る

    # dp[i]: iラウンド後から始めたときの期待値
    dp = [0]*(N+2)
    for i in range(N-1, -1, -1):
        a = A[i]
        reward = a - a*t//100
        E_in = dp[i+1] + reward
        E_out = (dp[i+2] + reward) * p/100 \
                + (dp[i+1] + a) * (100-p)/100

        dp[i] = max(E_in, E_out)
    print(dp[0])
    # print(dp)


if __name__ == "__main__":
    main()
