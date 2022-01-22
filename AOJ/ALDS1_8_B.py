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


class Node:
    __slots__ = ["left", "right", "par"]
    def __init__(self, left=None, right=None, par=None):
        self.left = left
        self.right = right
        self.par = par


class BinarySearchTree:
    def __init__(self):
        self.V = {}
        self.root = None

    def insert(self, key):
        # 初期化
        self.V[key] = Node()

        # 最初のノードならrootにして終了
        if self.root is None:
            self.root = key
            return

        # 木を潜る
        now = self.root
        par = None
        while now:
            par = now
            if key <= now:
                now = self.V[now].left
            else:
                now = self.V[now].right

        # keyのノードの親を定める
        self.V[key].par = par
        # parのノードのどちらの子かを定める
        if key <= par:
            self.V[par].left = key
        else:
            self.V[par].right = key

    def find(self, key):
        return key in self.V

    def preorder(self):
        res = self._preorder_rec(self.root)
        return res

    def _preorder_rec(self, now):
        v = self.V[now]
        res = [now]
        res += [] if v.left is None else self._preorder_rec(v.left)
        res += [] if v.right is None else self._preorder_rec(v.right)
        return res

    def inorder(self):
        res = self._inorder_rec(self.root)
        return res

    def _inorder_rec(self, now):
        v = self.V[now]
        res = [] if v.left is None else self._inorder_rec(v.left)
        res += [now]
        res += [] if v.right is None else self._inorder_rec(v.right)
        return res


def main():
    M = NI()
    T = BinarySearchTree()
    for _ in range(M):
        query = SI()
        if query == "print":
            ino = T.inorder()
            preo = T.preorder()
            print(" ", end="")
            print(*ino)
            print(" ", end="")
            print(*preo)

        else:
            q, k = query.split()
            k = int(k)

            if q == "find":
                print("yes" if T.find(k) else "no")
            else:
                T.insert(k)


if __name__ == "__main__":
    main()
