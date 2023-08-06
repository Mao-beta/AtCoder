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
    N = NI()
    A = NLI()


    def max_subarray_difference_sum(A):
        """
        Aを連続部分列に分割したとき、各部分列のMax-Minの合計の最大値
        https://atcoder.jp/contests/codequeen2023-final-open/tasks/codequeen2023_final_e
        https://stackoverflow.com/questions/66454201/maximize-the-sum-of-absolute-difference-between-max-and-min-elements-of-all-non
        """
        dp = [[0, 0, 0] for _ in range(len(A))]

        for i in range(1, len(A)):
            if A[i] >= A[i - 1]:
                dp[i][0] = A[i] - A[i - 1] + max(dp[i - 1][0], dp[i - 1][2])
                dp[i][1] = 0

            if A[i] <= A[i - 1]:
                dp[i][0] = 0
                dp[i][1] = A[i - 1] - A[i] + max(dp[i - 1][1], dp[i - 1][2])

            dp[i][2] = max(dp[i - 1])

        return max(dp[-1])

    print(max_subarray_difference_sum(A))


if __name__ == "__main__":
    main()
