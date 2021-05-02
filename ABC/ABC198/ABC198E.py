import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N = NI()
    C = [-1] + NLI()
    edges = [NLI() for _ in range(N-1)]
    graph = make_adjlist_nond(N, edges)

    hold = set()
    seen = [0]*(N+1)
    C_cnt = [0]*(max(C)+2)
    ans = []

    def rec(now):
        if C_cnt[C[now]] == 0:
            ans.append(now)
        C_cnt[C[now]] += 1
        seen[now] = 1

        #print(now, C_cnt)

        for goto in graph[now]:
            if seen[goto]:
                continue
            rec(goto)

        C_cnt[C[now]] -= 1

    rec(1)
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
