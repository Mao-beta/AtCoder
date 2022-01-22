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

    class Node:
        def __init__(self):
            self.par = -1
            self.children = []

        def __repr__(self):
            return f"par={self.par} children={self.children}"

    class Tree:
        def __init__(self, n):
            self.n = n
            self.V = [Node() for _ in range(n)]

        def add(self, u, v):
            self.V[u].children.append(v)
            self.V[v].par = u

        def roots(self):
            return [i for i, node in enumerate(self.V) if node.par == -1]


    tree = Tree(N)

    for i in range(N):
        u, k, *C = NMI()
        for v in C:
            tree.add(u, v)

    root = tree.roots()[0]
    D = [-1] * N
    D[root] = 0

    def rec(now):
        node = tree.V[now]
        for goto in node.children:
            D[goto] = D[now] + 1
            rec(goto)

    rec(root)

    for i, node in enumerate(tree.V):
        status = "internal node"
        if i == root:
            status = "root"
        elif not node.children:
            status = "leaf"

        print(f"node {i}: parent = {node.par}, depth = {D[i]}, {status}, {node.children}")


if __name__ == "__main__":
    main()
