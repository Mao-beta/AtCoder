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
    N = NI()

    # あとi回振れるときの期待値
    dp = [0] * (N+1)

    for i in range(1, N+1):
        e = dp[i-1]
        # eより大きい目が出たら確定
        for k in range(1, 7):
            if k > e:
                dp[i] += k / 6
            else:
                dp[i] += e * 1/6

    print(dp[N])


if __name__ == "__main__":
    main()
