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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        edges = [NLI() for _ in range(N-1)]
        graph = adjlist_nond_1to0(N, edges)
        seen = [0] * N

        def rec(now):
            g = 0
            seen[now] = 1
            for goto in graph[now]:
                if seen[goto]:
                    continue
                g ^= rec(goto) + 1
            return g

        print("Alice" if rec(0) else "Bob")




if __name__ == "__main__":
    main()
