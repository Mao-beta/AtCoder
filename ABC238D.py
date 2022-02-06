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
    T = NI()
    for _ in range(T):
        A, S = NMI()
        dp = [[0]*2 for _ in range(61)]
        dp[0][0] = 1

        for i in range(60):
            a = (A >> i) & 1
            s = (S >> i) & 1
            for j in range(2):
                if j == 0 and a == 1 and s == 0:
                    nj = 1
                elif j == 1 and a == 1 and s == 1:
                    nj = 1
                elif j == 0 and a == 0 and s == 0:
                    nj = 0
                elif j == 0 and a == 0 and s == 1:
                    nj = 0
                elif j == 1 and a == 0 and s == 0:
                    nj = 1
                elif j == 1 and a == 0 and s == 1:
                    nj = 0
                else:
                    continue

                dp[i+1][nj] |= dp[i][j]

        print("Yes" if dp[-1][0] else "No")



if __name__ == "__main__":
    main()
