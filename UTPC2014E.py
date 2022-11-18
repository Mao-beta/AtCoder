import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


class Node:
    def __init__(self, par, val):
        self.par = par
        self.val = val
        self.C = [-1] * 10

        self.submax = 0

    def __str__(self):
        return f"par={self.par} val={self.val} C={self.C}"

    def __repr__(self):
        return f"par={self.par} val={self.val} C={self.C}"


class Trie:
    def __init__(self):
        self.tree = [Node(-1, 0)]
        self.new_idx = 1

    def add(self, key, val):
        now = 0
        for s in key:
            si = int(s)

            par_node = self.tree[now]

            if par_node.C[si] != -1:
                now = par_node.C[si]
                continue

            par_node.C[si] = self.new_idx

            node = Node(par=now, val=0)
            now = self.new_idx
            self.tree.append(node)
            self.new_idx += 1

        leaf = self.tree[now]
        leaf.val += val

        while now > 0:
            now_node = self.tree[now]
            par = now_node.par
            par_node = self.tree[par]

            par_node.submax = max(par_node.submax,
                                  now_node.submax + now_node.val)

            now = par

    def query(self):
        return self.tree[0].submax


def main():
    N = NI()
    AB = [SLI() for _ in range(N)]
    # print(AB)
    trie = Trie()

    for a, b in AB:
        a = a[::-1]
        b = int(b)
        trie.add(a, b)
        print(trie.query())

    # print(*trie.tree, sep="\n")


if __name__ == "__main__":
    main()
