import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    P = NI()
    # 上からi桁決めて、3を含まずmod3でjの数の個数
    dp = [[0]*3 for _ in range(P+1)]
    dp[0][0] = 1
    for i in range(P):
        for j in range(3):
            for x in range(10):
                if x == 3:
                    continue
                dp[i+1][(j+x)%3] += dp[i][j]
    # 3の倍数(all_0) + 3含む(in_all) - 両方(in_0)
    ex_0 = dp[P][0] - 1
    all_0 = 10**P // 3
    in_0 = all_0 - ex_0
    in_all = 10**P - sum(dp[P])
    # print(all_0, in_all, in_0, ex_0)
    print(all_0 + in_all - in_0)


if __name__ == "__main__":
    main()
