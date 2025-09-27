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
    T = NI()
    for _ in range(T):
        N = NI()
        S = "0" + SI()
        dp = [0] * (1<<N)
        dp[0] = 1
        for i in range(1<<N):
            if dp[i] == 0:
                continue
            for j in range(N):
                ni = i ^ (1<<j)
                if ni > i and S[ni] == "0":
                    dp[ni] = 1
        # print(dp)
        if dp[-1]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
