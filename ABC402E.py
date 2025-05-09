import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
from math import isclose

sys.set_int_max_str_digits(10**6)
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
    N, X = NMI()
    SCP = EI(N)
    # 今の集合がiで残りj円使える
    dp = [[0.0] * (X+1) for _ in range(1<<N)]
    for i in range((1<<N)-1, -1, -1):
        for j in range(1, X+1):
            for x in range(N):
                if (i>>x) & 1:
                    continue
                # print(f"{i=} {j=} {x=}")
                s, c, p = SCP[x]
                if j >= c:
                    e = dp[i][j-c] * (100-p)/100 + (dp[i^(1<<x)][j-c]+s) * p/100
                    dp[i][j] = max(dp[i][j], e)
    # print(*dp, sep="\n")
    print(dp[0][X])


if __name__ == "__main__":
    main()
