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
    N, M, S = NMI()
    A = NLI()
    XY = EI(M)
    XY = [[x-1, y-1] for x, y in XY]
    NG = [[0]*N for _ in range(N)]
    for x, y in XY:
        NG[x][y] = 1
        NG[y][x] = 1
    # 使った集合がcaseのときの最小グループ数
    dp = [0] * (1<<N)


if __name__ == "__main__":
    main()
