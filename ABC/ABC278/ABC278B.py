import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    H, M = NMI()

    for t in range(H*60+M, 24*60*2):
        h, m = divmod(t, 60)
        if h >= 24:
            h -= 24
        h_miss = h // 10 * 10 + m // 10
        m_miss = h % 10 * 10 + m % 10
        if 0 <= h_miss < 24 and 0 <= m_miss < 60:
            print(h, m)
            exit()


if __name__ == "__main__":
    main()
