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
    C = NI()
    N = NI()
    A = NLI()
    B = []
    for a in A:
        for t in range(20):
            if a * (1<<t) <= C:
                B.append([a*(1<<t), (1<<t)])
    # print(B)
    N = len(B)
    INF = 10**18
    # i個見たときでfの値がjのときの個数
    dp = [INF]*(C+1)
    dp2 = [INF]*(C+1)
    dp[0] = 0
    for i in range(N):
        b, t = B[i]
        for j in range(C+1):
            dp2[j] = min(dp2[j], dp[j])
            if j+b <= C:
                dp2[j+b] = min(dp2[j+b], dp[j] + t)
        dp, dp2 = dp2, dp
    ans = dp[C]
    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
