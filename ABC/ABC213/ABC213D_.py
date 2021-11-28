import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
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
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, edges)

    def euler_tour(start, n):
        stack = deque()
        stack.append(start)

        seen = [0] * n
        seen[start] = 1
        res = []

        while stack:
            now = stack.pop()

            # 行きがけ
            if now >= 0:
                res.append(now)
                for goto in sorted(graph[now], reverse=True):
                    if seen[goto]: continue
                    seen[goto] = 1
                    stack.append(~now) # ここ大事
                    stack.append(goto)

            # 帰りがけ
            else:
                res.append(~now)

        return res

    for v in euler_tour(0, N):
        print(v+1, end=" ")


if __name__ == "__main__":
    main()
