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
            self.sibling = -1

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
        u, l, r = NMI()
        if l != -1:
            tree.add(u, l)
            tree.V[l].sibling = r
        if r != -1:
            tree.add(u, r)
            tree.V[r].sibling = l

    root = tree.roots()[0]
    D = [-1] * N
    D[root] = 0
    H = [-1] * N

    def rec(now):
        node = tree.V[now]
        h = 0
        for goto in node.children:
            D[goto] = D[now] + 1
            h = max(h, rec(goto)+1)

        H[now] = h
        return h

    rec(root)

    for i, node in enumerate(tree.V):
        status = "internal node"
        if i == root:
            status = "root"
        elif not node.children:
            status = "leaf"

        print(f"node {i}: parent = {node.par}, sibling = {node.sibling}, "
              f"degree = {len(node.children)}, depth = {D[i]}, height = {H[i]}, {status}")


if __name__ == "__main__":
    main()
