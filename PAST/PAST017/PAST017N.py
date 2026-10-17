import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N = NI()
    T = NLI()
    T.sort()
    S = sum(T)
    B = 1 << N
    INF = 10**20
    # dp[case]: すでにみた集合がcaseのときの期待値の最小値
    dp = [INF] * B
    dp[0] = 0
    for case in range(B):
        k = case.bit_count() + 1
        l = 0
        for i in range(N):
            if (case >> i) & 1:
                l += T[i]
        # 遷移
        for i in range(N):
            if (case >> i) & 1 == 0:
                r = l + T[i]
                fl = N * l / (k-0.5)
                fr = N * r / (k-0.5)
                if fr <= S:
                    e = S * (r - l) - (fr + fl) * (r - l) / 2
                elif S <= fl:
                    e = (fr + fl) * (r - l) / 2 - S * (r - l)
                else:
                    m = S * (k-0.5) / N
                    e = S * (m - l) - (S + fl) * (m - l) / 2
                    e += (fr + S) * (r - m) / 2 - S * (r - m)
                dp[case|(1<<i)] = min(dp[case|(1<<i)], dp[case] + e)

    print(dp[-1]/S)


if __name__ == "__main__":
    main()
