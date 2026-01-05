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
    N, M = NMI()
    RC = EI(M)
    ans = 0
    S = set()
    DR = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    DC = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for r, c in RC:
        if (r, c) in S:
            continue
        ans += 1
        for dr, dc in zip(DR, DC):
            S.add((r+dr, c+dc))
    print(ans)


if __name__ == "__main__":
    main()
