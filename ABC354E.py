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
    N = NI()
    AB = EI(N)
    match = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if AB[i][0] == AB[j][0] or AB[i][1] == AB[j][1]:
                match[i][j] = 1
                match[j][i] = 1
    # 状態iからはじめて勝てるか
    dp = [0] * (1<<N)
    for case in range((1<<N)-1, -1, -1):
        for i in range(N):
            if (case >> i) & 1:
                continue
            for j in range(i+1, N):
                if (case >> j) & 1:
                    continue
                if not match[i][j]:
                    continue
                nc = case | (1<<i) | (1<<j)
                if dp[nc] == 0:
                    dp[case] = 1
    if dp[0]:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
