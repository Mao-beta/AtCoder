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


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N = NI()
    UV = EI(N-1)
    G = adjlist(N, UV)
    D = [0] * N
    for u, v in UV:
        D[u-1] += 1
        D[v-1] += 1

    seen = [0] * N
    ans = 0
    for s, d in enumerate(D):
        if d != 3:
            continue
        if seen[s]:
            continue
        que = deque()
        que.append(s)
        num = 0
        while que:
            now = que.popleft()
            seen[now] = 1
            for goto in G[now]:
                if seen[goto]:
                    continue
                if D[goto] == 2:
                    num += 1
                    continue
                if D[goto] != 3:
                    continue
                que.append(goto)
        ans += num * (num-1) // 2
        # print(s+1, num, ans)
    print(ans)



if __name__ == "__main__":
    main()
