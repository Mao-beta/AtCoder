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
    AB = [NLI() for _ in range(M)]
    graph = adjlist_nond_1to0(N, AB)
    
    def is_bipartite(N, graph):
        colors = [-1] * N

        def dfs_paint_01_color(start):
            if colors[start] != -1:
                return True

            stack = deque()
            stack.append(start)

            colors[start] = 0

            while stack:
                now = stack.pop()
                c = colors[now]

                for goto in graph[now]:
                    if colors[goto] == 1 - c:
                        continue
                    elif colors[goto] == c:
                        return False
                    stack.append(goto)
                    colors[goto] = 1 - c

            return True

        res = True
        for s in range(N):
            res &= dfs_paint_01_color(s)

        return res

    if is_bipartite(N, graph):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
