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
EI = lambda m: [NLI() for _ in range(m)]


class Node:
    def __init__(self):
        self.child: list[None|"Node"] = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        now = self.root
        for s in word:
            si: int = ord(s) - ord("a")
            if now.child[si] is None:
                now.child[si] = Node()
            now = now.child[si]
        now.is_end = True
        return

    def search(self, word: str) -> bool:
        now = self.root
        for s in word:
            si: int = ord(s) - ord("a")
            if now.child[si] is None:
                return False
            now = now.child[si]
        return now.is_end


def main():
    N, M = NMI()
    trie = Trie()
    for _ in range(N):
        trie.insert(SI())
    for _ in range(M):
        if trie.search(SI()):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
