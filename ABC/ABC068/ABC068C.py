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


#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N, M = NMI()
    ships = [NLI() for _ in range(M)]
    graph = make_adjlist_nond(N, ships)

    if set(graph[1]) & set(graph[N]):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
