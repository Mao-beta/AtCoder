import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a - 1, b - 1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, M = NMI()
    UV = [NLI() for _ in range(M)]
    graph = adjlist_nond_1to0(N, UV)
    UV = [[x-1, y-1] for x, y in UV]

    INF = 10**10
    dp = [[INF]*(1<<N) for _ in range(N)]
    for i in range(N):
        dp[i][0] = 0
        dp[i][1<<i] = 1

    for start in range(N):
        que = deque()
        que.append((start, 1<<start))

        # print(graph)

        while que:
            now, state = que.popleft()
            step = dp[now][state]
            # print(now, step, state)

            for goto in graph[now]:
                ns = state ^ (1 << goto)

                if dp[goto][ns] <= step + 1:
                    continue

                dp[goto][ns] = step + 1
                que.append((goto, ns))

    # print(*dp, sep="\n")
    ans = 0
    for i in range(1<<N):
        tmp = INF
        for j in range(N):
            tmp = min(tmp, dp[j][i])
        ans += tmp
    print(ans)


if __name__ == "__main__":
    main()
