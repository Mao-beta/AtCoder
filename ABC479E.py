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
    AB = EI(N-1)
    G = [[] for _ in range(N)]
    for i, (a, b) in enumerate(AB, start=1):
        G[a-1].append((b-1, i))
        G[b-1].append((a-1, i))

    C = [0] * N
    SZ = [1] * N

    def dfs(now, par, v):
        sz = 1
        for g, i in G[now]:
            if g == par:
                continue
            sz += dfs(g, now, i)
        if sz > N-sz:
            C[now] += v
        else:
            C[now] -= v
            C[0] += v
        SZ[now] = sz
        return sz

    dfs(0, N, 0)

    ans = [0] * N

    def dfs2(now, par, v):
        v += C[now]
        ans[now] = v
        for g, i in G[now]:
            if g == par:
                continue
            dfs2(g, now, v)

    dfs2(0, N, 0)
    print(*ans)


if __name__ == "__main__":
    main()
