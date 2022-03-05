import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


class Knapsack:
    def __init__(self, N, WV):
        self.N = N
        self.WV = WV
        self.sumW = 0
        self.sumV = 0
        for w, v in WV:
            self.sumW += w
            self.sumV += v

    def solve_limW(self, limW):
        dp = [[0]*(limW + 1) for _ in range(self.N + 1)]

        for i in range(self.N):
            w, v = self.WV[i]
            for j in range(limW + 1):
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                if j+w <= limW:
                    dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)

        return max(dp[-1])


def main():
    N, W = NMI()
    WV = [NLI() for _ in range(N)]
    print(Knapsack(N, WV).solve_limW(W))


if __name__ == "__main__":
    main()
