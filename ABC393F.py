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
    N, Q = NMI()
    A = NLI()
    RX = EI(Q)
    R2XI = [[] for _ in range(N+1)]
    for i, (r, x) in enumerate(RX):
        R2XI[r].append([x, i])

    INF = 1 << 60
    n = len(A)
    # dp[i]は長さがiとなるLISの末尾の最小値
    dp = [INF] * (n + 1)
    dp[0] = -INF
    ans = [0] * Q
    for i, a in enumerate(A):
        # print(R2XI[i+1])
        idx = bisect.bisect_left(dp, a)
        dp[idx] = a
        # print(dp)
        for r, (x, qi) in enumerate(R2XI[i+1]):
            y = bisect.bisect_right(dp, x)-1
            # print(r, x, qi, y)
            ans[qi] = y
    # print(dp)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
