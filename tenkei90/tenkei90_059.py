import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_d_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
    return res


def main():
    N, M, Q = NMI()
    edges = [NLI() for _ in range(M)]
    querys = [NLI() for _ in range(Q)]
    graph = adjlist_d_1to0(N, edges)

    dp = [1]
    for _ in range(N-1):
        dp.append(dp[-1]<<1)

    for i, gotos in enumerate(graph):
        for j in gotos:
            dp[j] |= dp[i]

    for a, b in querys:
        a, b = a-1, b-1
        if (dp[b] >> a) & 1:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
