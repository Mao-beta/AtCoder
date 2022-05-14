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


def main():
    N, K = NMI()
    A = NLI()
    B = NLI()
    dp = [[0]*2 for _ in range(N+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(N-1):

        for j in range(2):
            if dp[i][j] == 0:
                continue

            # print(i, j)
            if j == 0 and abs(A[i] - A[i+1]) <= K:
                dp[i+1][0] = 1
            if j == 0 and abs(A[i] - B[i+1]) <= K:
                dp[i+1][1] = 1
            if j == 1 and abs(B[i] - A[i+1]) <= K:
                dp[i+1][0] = 1
            if j == 1 and abs(B[i] - B[i+1]) <= K:
                dp[i+1][1] = 1

    if dp[N-1][0] == 1 or dp[N-1][1] == 1:
        print("Yes")
    else:
        print("No")

    # print(dp)


if __name__ == "__main__":
    main()
