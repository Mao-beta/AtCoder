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
    # Dをi個見て直前がSj
    N, M = NMI()
    S = NLI()
    RS = {s:i for i, s in enumerate(S)}
    D = NLI()
    dp = [0] * N
    for i, d in enumerate(D):
        m = max(dp)
        dp2 = [m] * N
        for j, s in enumerate(S):
            l, u = s-d, s+d
            for x in [l, u]:
                if x not in RS:
                    continue
                # print(f"{i=} {s=}->{j=} {x=}, {d=} {dp2[RS[x]]=}, {dp[j]+1=}")
                nj = RS[x]
                dp2[nj] = max(dp2[nj], dp[j]+1)
        dp, dp2 = dp2, dp
        # print(dp)
    print(max(dp))


if __name__ == "__main__":
    main()
