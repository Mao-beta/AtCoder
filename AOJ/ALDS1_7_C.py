import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    N = NI()
    graph = [[] for i in range(N)]
    parents = [-1] * N
    for i in range(N):
        u, l, r = NMI()
        graph[u].append(l)
        graph[u].append(r)
        if l != -1:
            parents[l] = u
        if r != -1:
            parents[r] = u

    root = parents.index(-1)

    Pre = []
    In = []
    Post = []

    def rec(now):
        if now == -1:
            return

        Pre.append(now)
        for i, goto in enumerate(graph[now]):
            rec(goto)
            if i == 0:
                In.append(now)
        Post.append(now)

    rec(root)
    print("Preorder")
    print(" " + " ".join(map(str, Pre)))
    print("Inorder")
    print(" " + " ".join(map(str, In)))
    print("Postorder")
    print(" " + " ".join(map(str, Post)))


if __name__ == "__main__":
    main()
