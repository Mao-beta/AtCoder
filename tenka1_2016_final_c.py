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
EI = lambda m: [NLI() for _ in range(m)]



class Node:
    def __init__(self, w=0):
        self.child = [-1] * 26
        self.weight = w

class Trie:
    def __init__(self):
        self.D = [Node()]

    def s2i(self, s):
        return ord(s) - ord("a")

    def add(self, word, weight):
        now = 0
        for i, w in enumerate(word):
            wi = self.s2i(w)
            if self.D[now].child[wi] == -1:
                self.D[now].child[wi] = len(self.D)
                self.D.append(Node())
            now = self.D[now].child[wi]
        self.D[now].weight = weight

    def find(self, word):
        now = 0
        for i, w in enumerate(word):
            wi = self.s2i(w)
            if self.D[now].child[wi] == -1:
                return 0
            now = self.D[now].child[wi]
        return self.D[now].weight

    def find_all(self, word):
        res = [0] * (len(word)+1)
        now = 0
        for i, w in enumerate(word, start=1):
            wi = self.s2i(w)
            if self.D[now].child[wi] == -1:
                break
            now = self.D[now].child[wi]
            res[i] = self.D[now].weight
        return res


def main():
    S = SI()
    M = NI()
    P = [SI() for _ in range(M)]
    W = [NI() for _ in range(M)]
    trie = Trie()
    for p, w in zip(P, W):
        trie.add(p, w)

    dp = [0] * (len(S)+1)
    for l in range(len(S)):
        T = S[l:min(l+200, len(S))]
        res = trie.find_all(T)
        for d, w in enumerate(res):
            dp[l+d] = max(dp[l+d], dp[l] + w)

    print(dp[-1])


if __name__ == "__main__":
    main()
