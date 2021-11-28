import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = adjlist_nond_1to0(N, edges)

    seen = [0] * N

    def dfs(start):
        stack = deque()
        stack.append(start)
        seen[start] = 1
        E = 0
        V = 0

        while stack:
            now = stack.pop()
            V += 1
            E += len(graph[now])

            for goto in graph[now]:
                if seen[goto]:
                    continue
                stack.append(goto)
                seen[goto] = 1

        E //= 2
        if V != E:
            print(0)
            exit()

        return

    ans = 1

    for start in range(N):
        if seen[start] != 0:
            continue

        dfs(start)
        ans = ans * 2 % MOD

    print(ans)


if __name__ == "__main__":
    main()
