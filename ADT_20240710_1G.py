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
    ABXY = EI(M)
    ABXY = [[x-1, y-1, w, z] for x, y, w, z in ABXY]
    G = [[] for _ in range(N)]
    for a, b, x, y in ABXY:
        G[a].append([b, x, y])
        G[b].append([a, -x, -y])

    que = deque()
    que.append([0, 0, 0])

    ans = [[] for _ in range(N)]
    ans[0] = [0, 0]
    while que:
        u, x, y = que.popleft()
        for v, dx, dy in G[u]:
            if len(ans[v]):
                continue
            ans[v] = [x+dx, y+dy]
            que.append([v, *ans[v]])
    for a in ans:
        if len(a):
            print(*a)
        else:
            print("undecidable")


if __name__ == "__main__":
    main()
