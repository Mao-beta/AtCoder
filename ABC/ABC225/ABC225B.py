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
    AB = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, AB)
    for adj in graph:
        if len(adj) == N-1:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
