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
    P = [N] + [x-1 for x in NLI()]
    G = [[] for _ in range(N)]
    for i, p in enumerate(P):
        if i == 0:
            continue
        G[p].append(i)
    S = SLI()

    def dfs(now):
        s = S[now]
        if s not in ["+", "x"]:
            return int(s)

        res = []
        for g in G[now]:
            res.append(dfs(g))
        if s == "+":
            return (res[0] + res[1]) % MOD99
        else:
            return (res[0] * res[1]) % MOD99

    print(dfs(0))


if __name__ == "__main__":
    main()
