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
    N, K, X = NMI()
    S = [SI() for _ in range(N)]
    T = []
    now = []

    def dfs(idx):
        if idx == K:
            T.append("".join(now))
            return
        for s in S:
            now.append(s)
            dfs(idx + 1)
            now.pop()

    dfs(0)
    T.sort()
    print(T[X - 1])


if __name__ == "__main__":
    main()
