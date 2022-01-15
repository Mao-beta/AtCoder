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


class BinaryTrie:
    def __init__(self, max_query=5 * 10 ** 5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    def size(self):
        return self.cnt[0]

    # xの個数
    def count(self, x):
        pt = 0
        for i in range(self.bitlen - 1, -1, -1):
            y = x >> i & 1
            if self.nodes[2 * pt + y] == -1:
                return 0
            pt = self.nodes[2 * pt + y]
        return self.cnt[pt]

    # xの挿入
    def insert(self, x):
        pt = 0
        for i in range(self.bitlen - 1, -1, -1):
            y = x >> i & 1
            if self.nodes[2 * pt + y] == -1:
                self.id += 1
                self.nodes[2 * pt + y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2 * pt + y]
        self.cnt[pt] += 1

    # xの削除
    # xが存在しないときは何もしない
    def erase(self, x):
        if self.count(x) == 0:
            return
        pt = 0
        for i in range(self.bitlen - 1, -1, -1):
            y = x >> i & 1
            self.cnt[pt] -= 1
            pt = self.nodes[2 * pt + y]
        self.cnt[pt] -= 1

    # 昇順x番目の値(1-indexed)
    def kth_elm(self, x):
        assert 1 <= x <= self.size()
        pt, ans = 0, 0
        for i in range(self.bitlen - 1, -1, -1):
            ans <<= 1
            if self.nodes[2 * pt] != -1 and self.cnt[self.nodes[2 * pt]] > 0:
                if self.cnt[self.nodes[2 * pt]] >= x:
                    pt = self.nodes[2 * pt]
                else:
                    x -= self.cnt[self.nodes[2 * pt]]
                    pt = self.nodes[2 * pt + 1]
                    ans += 1
            else:
                pt = self.nodes[2 * pt + 1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か(1-indexed)
    # x以上の要素がない時はsize+1を返す
    def lower_bound(self, x):
        pt, ans = 0, 1
        for i in range(self.bitlen - 1, -1, -1):
            if pt == -1: break
            if x >> i & 1 and self.nodes[2 * pt] != -1:
                ans += self.cnt[self.nodes[2 * pt]]
            pt = self.nodes[2 * pt + (x >> i & 1)]
        return ans


def main():
    """ABC234D"""
    bt = BinaryTrie()
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    for i in range(K - 1):
        bt.insert(P[i])

    for i in range(K - 1, N):
        bt.insert(P[i])
        print(bt.kth_elm(i + 2 - K))


if __name__ == "__main__":
    main()
