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
    N, M = NMI()

    seen = set()

    def dfs(now, par):
        seen.add(now)

        j = SI()

        if j == "OK":
            exit()
        elif j == "-1":
            exit()

        k, *V = map(int, j.split())
        for v in V:
            if v in seen:
                continue
            print(v, flush=True)
            dfs(v, now)

        if par != -1:
            print(par, flush=True)
            j = SI()

    dfs(1, -1)


if __name__ == "__main__":
    main()
