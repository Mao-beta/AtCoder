import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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






class BinaryTrie:
    def __init__(self, max_b=62):
        self.MAX_B = max_b
        self.ROOT = 0
        self.ch = [[-1, -1]]
        self.cnts = [0]

    def _new_node(self):
        # 新ノードを追加し、そのindexを返す
        self.ch.append([-1, -1])
        self.cnts.append(0)
        assert len(self.ch) == len(self.cnts)
        return len(self.ch) - 1

    def _ensure_node(self, v, lr):
        nv = self.ch[v][lr]
        if nv == -1:
            nv = self._new_node()
        return nv

    def add(self, x, k=1):
        # xをk個追加(負も含む)
        v = self.ROOT
        self.cnts[v] += k
        for bit in range(self.MAX_B, -1, -1):
            lr = (x >> bit) & 1
            nv = self._ensure_node(v, lr)
            self.ch[v][lr] = nv
            self.cnts[nv] += k
            v = nv

    def discard(self, x, k=1):
        self.add(x, -k)

    def xor_min(self, x):
        # 含まれる数の中で、最小のx^yを返す
        assert self.cnts[self.ROOT] > 0
        v = self.ROOT
        res = 0
        for bit in range(self.MAX_B, -1, -1):
            assert self.cnts[v] > 0
            lr = (x >> bit) & 1
            to = self.ch[v][lr]
            if to != -1 and self.cnts[to] > 0:
                v = to
            else:
                v = self.ch[v][lr^1]
                res |= 1 << bit
        return res


def main():
    Q = NI()
    BT = BinaryTrie()
    S = set()
    for _ in range(Q):
        q, x = NMI()
        if q == 0:
            if x in S:
                continue
            BT.add(x)
            S.add(x)
        elif q == 1:
            if x not in S:
                continue
            BT.discard(x)
            S.discard(x)
        else:
            ans = BT.xor_min(x)
            print(ans)
        # print(BT.ch)
        # print(BT.cnts)


if __name__ == "__main__":
    main()
