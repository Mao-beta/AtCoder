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
    M = NI()
    B = NLI()
    X = NI()
    
    # i段目に到達可能
    dp = [0] * (X+1)
    for b in B:
        dp[b] = -1
    dp[0] = 1
    for i in range(X):
        if dp[i] <= 0:
            continue
        for a in A:
            if i+a <= X and dp[i+a] != -1:
                dp[i+a] = 1

    if dp[X]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
