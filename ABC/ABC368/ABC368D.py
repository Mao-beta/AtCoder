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
    AB = EI(N-1)
    AB = [[x-1, y-1] for x, y in AB]
    V = NLI()
    V = [x-1 for x in V]
    V = set(V)

    D = [0] * N
    G = [[] for _ in range(N)]
    for a, b in AB:
        D[a] += 1
        D[b] += 1
        G[a].append(b)
        G[b].append(a)

    start = V.pop()
    V.add(start)

    ans = [0]

    def dfs(now, par):
        res = now in V
        for goto in G[now]:
            if par == goto:
                continue
            need = dfs(goto, now)
            res |= need
        if res:
            ans[0] += 1
        # print(now+1, par+1, res)
        return res

    dfs(start, N)
    print(ans[0])


if __name__ == "__main__":
    main()
