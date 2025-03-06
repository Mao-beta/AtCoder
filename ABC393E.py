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
    N, K = NMI()
    A = NLI()
    INF = 10**6
    C = [0] * (INF+1)
    for a in A:
        C[a] += 1
    ans = [0] * (INF+1)
    for g in range(INF, 0, -1):
        now = 0
        use = []
        for x in range(g, INF+1, g):
            now += C[x]
            if ans[x] == 0:
                use.append(x)
        if now >= K:
            for u in use:
                ans[u] = g
    print(*[ans[a] for a in A], sep="\n")


if __name__ == "__main__":
    main()
