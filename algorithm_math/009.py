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
    N, S = NMI()
    A = NLI()
    dp = [[0]*20001 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a = A[i]
        for j in range(S+1):
            dp[i+1][j] |= dp[i][j]
            dp[i+1][j+a] |= dp[i][j]
    print("Yes" if dp[N][S] else "No")


if __name__ == "__main__":
    main()
