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


class BinaryTrie:

    def __init__(self, bit_depth):
        self.root = [None, None, 0]  # [0-child, 1-child, count]
        self.bit_start = 1 << (bit_depth - 1)
        self.xor_mask = 0

    def insert(self, x):
        """xを格納"""
        b = self.bit_start
        node = self.root
        node[2] += 1
        while b:
            i = bool(x & b)
            if node[i] is None:
                node[i] = [None, None, 1]
            else:
                node[i][2] += 1
            node = node[i]
            b >>= 1

    def search(self, x):
        b = self.bit_start
        node = self.root
        res = 0
        while b:
            i = bool(x & b)
            # print(x, b, i)
            # print(node[i], node[i^1])
            if node[i^1] is not None:
                res |= b
            node = node[i]
            b >>= 1
        return res

    def pop_min(self):
        """xor_mask適用後の最小値を、適用前の値で取得し、木からは削除"""
        b = self.bit_start
        node = self.root
        m = self.xor_mask
        ret = 0
        node[2] -= 1
        while b:
            i = bool(m & b)
            if node[i] is None:
                i ^= 1
            ret = (ret << 1) + i

            if node[i][2] > 1:
                node[i][2] -= 1
                node = node[i]
            else:
                tmp = node[i]
                node[i] = None
                node = tmp
            b >>= 1
        return ret



def main():
    N = NI()
    A = NLI()

    T = BinaryTrie(31)
    for a in A:
        T.insert(a)

    ans = 1<<32
    for a in A:
        tmp = T.search(a)
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
